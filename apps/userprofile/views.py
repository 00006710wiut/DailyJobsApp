from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from apps.job.models import Job, Application 
from .models import ConversationMessage
from apps.notification.utilities import create_notification
from .forms import UserUpdateForm, UserprofileUpdateForm



@login_required
def dashboard(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = UserprofileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.userprofile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('dashboard')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = UserprofileUpdateForm(instance=request.user.userprofile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'userprofile/dashboard.html', context)

@login_required
def view_application(request, application_id):

    if request.user.userprofile.is_employer:
        application = get_object_or_404(Application, pk=application_id, job__created_by=request.user)
    else:   
        application = get_object_or_404(Application, pk=application_id, created_by=request.user)

    if request.method == 'POST':
        content = request.POST.get('content')

        if content:
            conversationmessage = ConversationMessage.objects.create(application=application, content=content, created_by=request.user)
            
            create_notification(request, application.created_by, 'message', extra_id=application.id)



            return redirect('view_application', application_id=application_id)


    return render(request, 'userprofile/view_application.html', {'application': application})

@login_required
def view_dashboard_job(request, job_id):
    job = get_object_or_404(Job, pk=job_id, created_by=request.user)

    return render(request, 'userprofile/view_dashboard_job.html', {'job': job})


