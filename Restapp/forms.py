from django import forms
from .models import User, Student



class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password',]

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'department': forms.Select(attrs={'class': 'form-control'}),
            'courses': forms.Select(attrs={'class': 'form-control'}),
        
        }
        


    