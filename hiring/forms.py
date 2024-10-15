from django import forms
from .models import HiringForm


class NewHiringForm(forms.ModelForm):
    JOB_TYPE = [
        ('Full Time - دوام كامل', 'Full Time - دوام كامل'),
        ('Part Time - دوام جزئي', 'Part Time - دوام جزئي'),
    ]
    job_type = forms.ChoiceField(choices=JOB_TYPE, label='Job Type - نوع الوظيفة', widget=forms.RadioSelect())

    RESASON = [
        ('Promotion - ترقية', 'Promotion - ترقية'),
        ('New Hire - تعيين جديد', 'New Hire - تعيين جديد'),
        ('Replacement - بديل', 'Replacement - بديل'),
    ]
    reason_for = forms.ChoiceField(choices=RESASON, label='Reason For Hiring - سبب التوظيف',
                                    widget=forms.RadioSelect())

    GENDER = [
        ('Male - ذكر', 'Male - ذكر'),
        ('Female - انثي', 'Female - انثي'),
        ('No Preference - لا يوجد تفضيل', 'No Preference - لا يوجد تفضيل'),
    ]
    gender = forms.ChoiceField(choices=GENDER, label='Gender Preference - تفضيل النوع', widget=forms.RadioSelect())

    CAREER = [
        ('Student (Undergraduate) - طالب', 'Student (Undergraduate) - طالب'),
        ('Entry Level (Fresh Grad - Junior Level) - مستوي مبتدأ',
         'Entry Level (Fresh Grad - Junior Level) - مستوي مبتدأ'),
        ('Experienced (Non-Manager) - خبير', 'Experienced (Non-Manager) - خبير'),
        ('Managerial Level - مدير', 'Managerial Level - مدير'),
        ('Senior Management - اعلي من مدير', 'Senior Management - اعلي من مدير'),
    ]
    career_level = forms.ChoiceField(choices=CAREER, label='Career Level - المستوي الوظيفي', widget=forms.RadioSelect())

    EDU_LEVEL = [
        ('School - مدرسة', 'School - مدرسة'),
        ('Middle Institute - معهد متوسط', 'Middle Institute - معهد متوسط'),
        ('High Institute - معهد عالي', 'High Institute - معهد عالي'),
        ('Bachelor Degree - بكالريوس', 'Bachelor Degree - بكالريوس'),
        ('Master Degree - ماجيستير', 'Master Degree - ماجيستير'),
        ('Doctoral Degree - دكتوراه', 'Doctoral Degree - دكتوراه'),
        ('No Preference - لا يوجد تفضيل', 'No Preference - لا يوجد تفضيل'),
    ]
    edu_level = forms.ChoiceField(choices=EDU_LEVEL, label='Educational Level', widget=forms.RadioSelect())

    ENG_LEVEL = [
        ('Beginner (A1) - مبتدأ', 'Beginner (A1) - مبتدأ'),
        ('Elementary (A2) - مقبول', 'Elementary (A2) - مقبول'),
        ('Intermediate (B1) - متوسط', 'Intermediate (B1) - متوسط'),
        ('Upper Intermediate (B2) - فوق المتوسط', 'Upper Intermediate (B2) - فوق المتوسط'),
        ('Advanced (C1) - طليق', 'Advanced (C1) - طليق'),
        ('No Preference - لا يوجد تفضيلات', 'No Preference - لا يوجد تفضيلات'),
    ]
    eng_level = forms.ChoiceField(choices=ENG_LEVEL, label='English Level', widget=forms.RadioSelect())

    MIC_LEVEL = [
        ('Fair - مقبول', 'Fair - مقبول'),
        ('Good - جيد', 'Good - جيد'),
        ('Very Good - جيد جدا', 'Very Good - جيد جدا'),
        ('Excellent - ممتاز', 'Excellent - ممتاز'),
        ('Advanced - متقدم', 'Advanced - متقدم'),
        ('No Preference - لا يوجد تفضيلات', 'No Preference - لا يوجد تفضيلات'),
    ]
    microsoft_level = forms.ChoiceField(choices=MIC_LEVEL, label='Microsoft Office Level', widget=forms.RadioSelect())

    class Meta:
        model = HiringForm
        fields = ['hiring_position', 'job_type', 'reporting_to', 'num_of_vac', 'reason_for', 'gender', 'career_level',
                  'year_of_ex', 'edu_level', 'edu_major', 'required_cert', 'eng_level', 'microsoft_level']

        labels = {'hiring_position': "The Required Hiring Position/Title - المنصب/ المسمي الوظيفي المطلوب تعيينه",
                  'reporting_to': 'Reporting To - يتبع اداريا و فنيا ل',
                  'num_of_vac': 'Number Of Vacancies Required - عدد الموظفين المطلوبين للوظيفة',
                  'year_of_ex': 'Years Of Experience',
                  'edu_major': 'Educational Major',
                  'required_cert': 'Required Certificates',
                  }
