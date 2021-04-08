from django.contrib.auth.models import User
from django.db import models
#from PIL import Image


class Job(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField()
    #image = models.ImageField(default='placeholder.jpg', upload_to='jobworkstation_pics')
    phone_number = models.CharField(max_length=35, blank=True, null=True)
    job_country = models.CharField(max_length=300, blank=True, null=True)
    job_adress = models.CharField(max_length=300, blank=True, null=True)
    job_zipcode = models.CharField(max_length=300, blank=True, null=True)

    CASH = 'cash_1'
    CLICK = 'click_2'
    PAYME = 'payme_3'
    OSON = 'oson_4'
    VISA = 'visa_5'
    CRYPTOCURRENCY = 'cryptocurrency_6'
    EWALLET = 'ewallet_7'
    CHOICES_PAYMET = (
        (CASH, 'cash'),
        (CLICK, 'click'),
        (PAYME, 'payme'),
        (OSON, 'oson'),
        (VISA, 'visa'),
        (CRYPTOCURRENCY, 'cryptocurrency'),
        (EWALLET, 'ewallet'),
    )
    payment_type = models.CharField(max_length=20, choices=CHOICES_PAYMET, default=CASH)
    FIXED = 'fixed_1'
    HOURLY = 'hourly_1'
    BY_PROJECT = 'by_project_1'
    CHOICES_SALARY = (
        (FIXED, 'fixed'),
        (HOURLY, 'hourly'),
        (BY_PROJECT, 'by_project'),
    )
    salary_type = models.CharField(max_length=100, choices=CHOICES_SALARY, default=FIXED)

    wage_min = models.CharField(max_length=100)
    wage_max = models.CharField(max_length=100)

    UZS = 'uzs_1'
    USD = 'usd_2'
    EUR = 'eur_3'
    RUBL = 'rubl_4'
    CHOICES_CURRENCY = (
        (UZS, 'uzs'),
        (USD, 'usd'),
        (EUR, 'eur'),
        (RUBL, 'rubl'),
    )
    currency = models.CharField(max_length=100, choices=CHOICES_CURRENCY, default=UZS)

    ONLINE = 'online_1'
    OFFLINE = 'offline_2'
    CHOICES_EMPLOYEE = (
        (ONLINE, 'online'),
        (OFFLINE, 'offline'),
    )
    employee_type = models.CharField(max_length=100, choices=CHOICES_EMPLOYEE, default=OFFLINE)


    MALE = 'male_1'
    FEMALE = 'female_2'
    ANY = 'any_3'
    CHOICES_GENDER = (
        (MALE, 'male'),
        (FEMALE, 'female'),
        (ANY, 'any'),
    )
    preffered_gender = models.CharField(max_length=100, choices=CHOICES_GENDER, default=MALE)

    ACTIVE = 'active'
    EMPLOYED = 'employed'
    ARCHIVED = 'archived'

    CHOICES_STATUS = (
        (ACTIVE, 'Active'),
        (EMPLOYED, 'Employed'),
        (ARCHIVED, 'Archived'),
    )


    created_by = models.ForeignKey(User, related_name='jobs', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, choices=CHOICES_STATUS, default=ACTIVE)

    def __str__(self):
        return self.title
    
class Application(models.Model):
    job = models.ForeignKey(Job, related_name='applications', on_delete=models.CASCADE)
    content = models.TextField()
    experience = models.TextField()

    created_by = models.ForeignKey(User, related_name='applications', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    




# Create your models here.

