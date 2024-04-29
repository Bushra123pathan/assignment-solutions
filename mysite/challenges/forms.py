from django import forms
from .models import ServiceRequest

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['request_type', 'details', 'attachment']

# In views.py
from .forms import ServiceRequestForm

def submit_service_request(request):
    form = ServiceRequestForm(request.POST, request.FILES)
    if form.is_valid():
        # Save the form data
    # Render the form
    return render(request, 'submit_request.html', {'form': form})