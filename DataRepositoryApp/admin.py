from django.contrib import admin
from django import forms
from django.core.exceptions import ValidationError
from django.contrib import admin
from .models import Alumni
import re

EMAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"


class StateAlumniForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'size': '50'}), required=True)
    session = forms.CharField(widget=forms.TextInput(attrs={'size': '50'}),max_length=7, required=True, help_text="Example: 2014-15")
    address = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 50}), required=False)
    current_position = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 50}), required=False)
    contact_no = forms.CharField(widget=forms.TextInput(attrs={'size': '50'}), min_length=11, max_length=14,
                                 required=False)
    email = forms.CharField(widget=forms.TextInput(attrs={'size': '50'}), required=False)

    def clean(self):
        error_dict = {}
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        session = cleaned_data.get('session')
        substr = str(session).split('-')
        try:
            float(substr[0])
            float(substr[1])
        except Exception as e:
            print(e)
            error_dict['session'] = ValidationError("Invalid Session Format (" + session + ")")

        if len(substr[0]) != 4 or len(substr[1]) != 2:
            error_dict['session'] = ValidationError("Invalid Session Format ("+session+")")
        if email and not re.match(EMAIL_REGEX, email):
            error_dict['email'] = ValidationError("Invalid Email Format ("+email+")")
        if error_dict:
            raise ValidationError(error_dict)


class StateAlumni(admin.ModelAdmin):
    form = StateAlumniForm
    sortable_by = ('session', 'created_at')
    search_fields = ('name', 'session', 'current_position', 'contact_no', 'email')
    list_display = ('name', 'session', 'current_position', 'contact_no', 'created_at')


admin.site.register(Alumni, StateAlumni)
