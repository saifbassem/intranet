from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from login import models as login_model

# Create your models here.
class HiringForm(models.Model):
    hiring_position = models.CharField(max_length=150)
    job_type = models.CharField(max_length=150)
    reporting_to = models.CharField(max_length=150,default="")
    num_of_vac = models.IntegerField(default=0)
    reason_for = models.CharField(max_length=150,default="")
    gender = models.CharField(max_length=150,default="")
    career_level = models.CharField(max_length=150,default="")
    year_of_ex = models.CharField(max_length=150,default="")
    edu_level = models.CharField(max_length=150,default="")
    edu_major = models.CharField(max_length=150,default="")
    required_cert = models.CharField(max_length=150,default="")
    eng_level = models.CharField(max_length=150,default="")
    microsoft_level = models.CharField(max_length=150,default="")
    status = models.IntegerField(default=0)
    created_by = models.ForeignKey(login_model.CustomUser, related_name='hiring_form', on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(default=timezone.now)
    approved_at = models.DateTimeField(default=None)
    manager = models.IntegerField(default=0)
    hr_note = models.CharField(max_length=4000,default="")
    manager_note= models.CharField(max_length=4000,default="")

    def __str__(self) :
        return self.hiring_position

    class Meta:
        db_table = "HR_HiringForm"
    @staticmethod
    def get_approval_requests(emp_id):
        approval_requests = HiringForm.objects.filter(manager=emp_id, status=0).order_by('-created_at')
        return approval_requests if approval_requests is not None else 0




