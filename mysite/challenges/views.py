from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ServiceRequest, CustomerAccount

@login_required
def submit_service_request(request):
    if request.method == 'POST':
        # Handle form submission and save the service request
    else:
        # Render the form to submit service request
        return render(request, 'submit_request.html')

@login_required
def track_service_request(request):
    # Retrieve and display service requests for the logged-in customer
    return render(request, 'track_request.html', context)

@login_required
def view_account_info(request):
    # Retrieve and display account information for the logged-in customer
    return render(request, 'account_info.html', context)