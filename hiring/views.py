from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import HiringForm
from .forms import NewHiringForm
from django.utils import timezone


from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    if request.user.is_authenticated:
        forms = HiringForm.objects.filter(created_by = request.user).exclude(status=3).order_by('-created_at')
        print()
        return render(request, 'hiring/index.html', {"forms": forms})

def new_request(request):
    if request.method == 'POST':
        form = NewHiringForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.created_by = request.user
            form.save()
            return redirect('hiring:index')
    else:
        form = NewHiringForm()
    return render(request, 'hiring/new_request.html', {"form": form})

def request_approval(request):
    forms = HiringForm.get_approval_requests(emp_id= request.user.company_id)
    return render(request, 'hiring/request_approval.html',{'forms': forms})

def approval_form_action(request, form_id):
    if request.method == 'POST':
        form = get_object_or_404(HiringForm, id=form_id)
        authorized_forms = HiringForm.get_approval_requests(emp_id=request.user.company_id)
        if form in authorized_forms:
            if int(request.POST['request_type']) == 1:
                form.status = 1
                form.approved_at = timezone.now()
            elif int(request.POST['request_type']) == 2:
                form.status = 2
            manager_note = request.POST['manager_note']   
            if manager_note:
                form.manager_note = manager_note   
            form.save()
        else:
            return render(request, 'unauthorized.html')
    return redirect('hiring:request_approval')


def hr_screen(request):
    if request.method == 'POST':
        form_id = request.POST.get('form_id')
        request_type = int(request.POST.get('request_type', 0))
        hr_note = request.POST.get('hr_note')
        if form_id:
            form = get_object_or_404(HiringForm, id=form_id)
            if request_type == 2:
                form.status = 2
            elif request_type == 3:
                form.status = 3
            if hr_note:
                form.hr_note = hr_note
            form.save()
    forms = HiringForm.objects.filter(status=1).order_by('-created_at')
    return render(request, 'hiring/hr_screen.html', {"forms": forms})



# def reject_form(request, form_id):
#     form = get_object_or_404(Form, id=form_id)
#     form.status = 2
#     form.save()
#     return redirect('home')
#
#
# def end(request, form_id):
#     form = get_object_or_404(Form, id=form_id)
#     form.end = 1
#     form.save()
#     return redirect('hr')