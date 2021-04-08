import json
import stripe

from django.conf import settings
from django.db.models import Q
from django.http import JsonResponse

from .models import Job
import stripe 
from django.conf import settings



def api_search(request):
    jobslist = []
    data = json.loads(request.body)
    query = data['query']
    employee_type = data['employee_type']

    jobs = Job.objects.filter(status=Job.ACTIVE).filter(Q(title__icontains=query) | Q(description__icontains=query) | Q(wage_min__icontains=query) | Q(wage_max__icontains=query) | Q(job_country__icontains=query))

    if employee_type:
        jobs = jobs.filter(employee_type=employee_type)

    
    for job in jobs:
        obj = {
            'id': job.id,
            'title': job.title,
            'description': job.description,
            'wage_min': job.wage_min,
            'wage_max': job.wage_max,
 
            'job_country': job.job_country,

            'preffered_gender': job.preffered_gender,

            'url': '/jobs/%s/' % job.id
        }
        jobslist.append(obj)
    
    return JsonResponse({'jobs': jobslist})