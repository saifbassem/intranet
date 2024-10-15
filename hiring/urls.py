from django.urls import path

from . import views

app_name = "hiring"

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new_request/', views.new_request, name='new_request'),
    path('request_approval/', views.request_approval, name='request_approval'),
    path('approval_form_action/<int:form_id>', views.approval_form_action, name='approval_form_action'),
    path('hr_screen/', views.hr_screen, name='hr_screen'),

    # path('form/hr/', views.hr, name='hr'),
    # # path('form/data/<int:form_id>/', views.data_of_req, name='data_of_req'),
    # path('form/approve/<int:form_id>/', views.approve_form, name='approve_form'),
    # path('form/reject/<int:form_id>/', views.reject_form, name='reject_form'),
    # path('form/end/<int:form_id>/', views.end, name='end'),

]