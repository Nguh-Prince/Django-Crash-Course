from django import forms

from .models import *

class CustomerFeedbackForm(forms.ModelForm):
    template_name = "ecommerce/contact-form-snippet.html"
    class Meta:
        model = CustomerFeedback
        fields = ["name", "email", "message"]