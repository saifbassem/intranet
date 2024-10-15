from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.http import Http404
from django.urls import reverse
from django.utils import timezone
from django.core.exceptions import PermissionDenied

from .models import Questionnaire, QuestionLink, Employee
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout as django_logout



# helper function to get employee data
def get_employee(email):
    employee = get_object_or_404(Employee, email=email)
    return employee

@login_required
def index(request):
    now = timezone.now()
    context={}
    # Filter return a list , get returns a single record
    if request.user.is_authenticated:
        employee = get_employee(request.user.email)
        questionnaire_list = Questionnaire.objects.filter(emp_questioned=employee.id, status=0, due_date__gt=now).order_by("id")
        outdated_questionnaires = Questionnaire.objects.filter(emp_questioned=employee.id, status=0, due_date__lt=now).order_by("id")
        context = {"questionnaire_list": questionnaire_list, "employee": employee, "outdated_questionnaires": outdated_questionnaires}
    return render(request, "empower360/index.html", context)

@login_required
def questionnaire(request, questionnaire_id):
    now = timezone.now()
    questionnaire = get_object_or_404(Questionnaire, pk=questionnaire_id)

    employee = get_employee(request.user.email)
    # Check if employee trying to open the questionnaire is the targeted employee
    if questionnaire.emp_questioned.id == employee.id:
        # Check the date of the questionnaire
        if questionnaire.due_date > now:
            questionnaire.start_date = now
            questionnaire.save()
            return render(request, "empower360/questionnaire.html", {"questionnaire": questionnaire})

    return redirect('empower360:unauthorized')

@login_required
def submit(request, questionnaire_id):
    now = timezone.now()

    result = request.POST.copy()
    del result['csrfmiddlewaretoken']

    for key, value in result.items():
        link_id = key
        link = QuestionLink.objects.get(pk=link_id)
        link.answer = value
        link.save()

    questionnaire = Questionnaire.objects.get(pk=questionnaire_id)
    questionnaire.status = 1
    questionnaire.end_date = now
    questionnaire.save()

    # page_load_time = request.POST.get('page_load_time', None)
    # print(f"Now: {now} - Load time: {page_load_time}")

    # print(f"Key:{key} - Value: {value}")
    return HttpResponseRedirect(reverse("empower360:index"))


