from django.shortcuts import render, redirect,HttpResponse
from .forms import AssistanceRequestForm
from .models import AssistanceRequest
from django.contrib.auth.decorators import login_required


def home(request):
    return HttpResponse("<h1>Welcome to Breakdown Assistance</h1><p><a href='/request/'>Request Help</a><p>")

@login_required
def request_assistance(request):
    if request.method == 'POST':
        form = AssistanceRequestForm(request.POST)
        if form.is_valid():
            assistance = form.save(commit=False)
            assistance.user = request.user
            assistance.save()
            return redirect('my_requests')
    else:
        form = AssistanceRequestForm()
    return render(request, 'core/request_assistance.html', {'form': form})

@login_required
def my_requests(request):
    requests = AssistanceRequest.objects.filter(user=request.user)
    return render(request, 'core/my_requests.html', {'requests': requests})

@login_required
def all_requests(request):
    if not request.user.is_staff:
        return redirect('my_requests')
    requests = AssistanceRequest.objects.all()
    return render(request, 'core/all_requests.html', {'requests': requests})