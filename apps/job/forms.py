from django import forms

from .models import Job, Application


class AddJobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description', 'phone_number', 
        'job_country', 'job_adress', 
        'job_zipcode', 'payment_type', 
        'salary_type', 'wage_min', 
        'wage_max', 'currency', 
        'employee_type', 'preffered_gender']

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['content', 'experience']

    
