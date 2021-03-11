from django.contrib.auth.models import User
from django import forms
from .models import MovieBulkUpload

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class MovieBulkUploadModelForm(forms.ModelForm):
    class Meta:
        model = MovieBulkUpload
        fields = ('csv_file',)
