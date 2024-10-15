from django.urls import path

from . import views

app_name = "empower360"

urlpatterns = [

    path("", views.index, name="index"),
    path("<int:questionnaire_id>/", views.questionnaire, name="questionnaire"),
    path("<int:questionnaire_id>/sumbit/", views.submit, name="submit"),

]