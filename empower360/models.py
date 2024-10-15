from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from .validators import validate_email_domain


class Employee(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    emp_name = models.CharField(max_length=50, db_column='employee_name')
    emp_id = models.IntegerField(db_column='employee_id')
    email = models.CharField(max_length=100, db_column='email')

    def __str__(self):
        return f"{self.emp_name} : {self.emp_id}"

    class Meta:
        db_table = "CR_Employee"
        managed = False


class Questionnaire(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    name = models.CharField(max_length=50, db_column='name')
    status = models.IntegerField(db_column='status')
    # create a related name to replace Questionnaire_set
    emp_questioned = models.ForeignKey(Employee, on_delete=models.DO_NOTHING, db_column='emp_questioned',
                                       related_name='questionnaire_questioned')
    emp_targeted = models.ForeignKey(Employee, on_delete=models.DO_NOTHING, db_column='emp_targeted',
                                     related_name='questionnaire_targeted')
    connection = models.CharField(max_length=50, db_column='connection')
    due_date = models.DateTimeField(db_column='due_date')
    start_date= models.DateTimeField(db_column='start_date', null=True)
    end_date = models.DateTimeField(db_column='end_date', null=True)
    # emp_questioned = models.IntegerField(db_column='emp_questioned')
    # emp_targted = models.IntegerField(db_column='emp_targeted')

    def __str__(self):
        return f"Questionnaire_name:{self.name}"

    class Meta:
        db_table = "CR_Questionnaire"
        managed = False
        unique_together = ("emp_questioned", "emp_targeted")


class Question(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    title = models.CharField(max_length=150, db_column='title')
    title_ar = models.CharField(max_length=150, db_column='title_ar')
    body = models.CharField(max_length=250, db_column='body')
    body_ar = models.CharField(max_length=250, db_column='body_ar', blank=True, null=True)
    type = models.IntegerField(db_column='type')

    def __str__(self):
        return f"{self.title}"

    class Meta:
        db_table = "CR_Question"
        managed = False


class QuestionLink(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.DO_NOTHING, db_column='questionnaire_id')
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING, db_column='question_id')
    answer = models.CharField(max_length=2000, db_column='answer')

    def __str__(self):
        return f"{self.questionnaire.name} -- {self.question.title}"

    class Meta:
        db_table = "CR_Question_Link"
        managed = False


class Choice(models.Model):
    id = models.AutoField(primary_key=True, db_column='id')
    text = models.CharField(max_length=300, db_column='text')
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING, db_column='question_id')
    score = models.IntegerField(db_column='score')

    def __str__(self):
        return f"{self.question.title} -> {self.text}"

    class Meta:
        db_table = "CR_Choice"
        managed = False


