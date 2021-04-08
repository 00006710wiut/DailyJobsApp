from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Job
from apps.notification.utilities import create_notification
from .forms import AddJobForm, ApplicationForm


from django.http import JsonResponse
import stripe
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
import razorpay

def search(request):
    return render(request, 'job/search.html')
    
def job_detail(request, job_id, **kwargs):
    job = Job.objects.get(pk=job_id)   

    if request.method == 'POST':
        amount = 50000
        client = razorpay.Client(
            auth=('rzp_test_ExeUGieMdyvqvk', 'caoGVPn9zvnCVFY72aqCnv1e'))
        payment = client.order.create({'amount': amount, 'currency': 'INR', 'payment_capture': '1'})

    # OPTIONALclient.order.create(amount=order_amount, currency=order_currency, receipt=order_receipt, notes=notes)
    return render(request, 'job/job_detail.html', {'job': job})


@csrf_exempt       
def success(request):
    return render(request, 'job/success.html')


@login_required
def apply_for_job(request, job_id):
    job = Job.objects.get(pk=job_id)

    if request.method == 'POST':
        form = ApplicationForm(request.POST)

        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.created_by = request.user
            application.save()

            create_notification(request, job.created_by, 'application', extra_id=application.id)

            return redirect('dashboard')
    else:
        form = ApplicationForm()
    
    return render(request, 'job/apply_for_job.html', {'form': form, 'job': job})





@login_required
def add_job(request):
    if request.method == 'POST':
        form = AddJobForm(request.POST)

        if form.is_valid():
            job = form.save(commit=False)
            job.created_by = request.user
            job.save()


            return redirect('dashboard')
    else:
        form = AddJobForm()
    
    return render(request, 'job/add_job.html', {'form': form})


@login_required
def edit_job(request, job_id):
    job = get_object_or_404(Job, pk=job_id, created_by=request.user)

    if request.method == 'POST':
        form = AddJobForm(request.POST, instance=job)

        if form.is_valid():
            job = form.save(commit=False)
            job.status = request.POST.get('status')
            job.save()

            return redirect('dashboard')
    else:
        form = AddJobForm(instance=job)
    
    return render(request, 'job/edit_job.html', {'form': form, 'job': job})


