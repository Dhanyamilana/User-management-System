from django import forms
from combon.models import Emp,Dhan


class LoginForm(forms.ModelForm):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(max_length=128, widget=forms.PasswordInput, required=False)
    class Meta:
        model = Dhan
        fields= ["phoneno","dob","address"]
        widgets = {
            # 'username' : forms.TextInput(attrs={'class': 'form-control'}),
            'phoneno' : forms.TextInput(attrs={'class': 'form-control'}),
            'dob' : forms.DateInput(attrs={'class': 'form-control'}),
            'address' : forms.TextInput(attrs={'class': 'form-control'}),
            # 'password' : forms.TextInput(attrs={'class': 'form-control'}),
        }

    def _init_(self, *args, **kwargs):
        user_instance = kwargs.pop('user_instance', None)
        super(LoginForm, self)._init_(*args, **kwargs)
        if user_instance:
            self.user_instance = user_instance
            self.fields['username'] .initial = user_instance.username
            self.fields['password'].widget.attrs['placeholder'] = 'Enter new password'

class EmpForm(forms.ModelForm):  
    class Meta:  
        model = Emp 
        fields = '__all__'
        widgets = {
            'empid' : forms.TextInput(attrs={'class': 'form-control'}), 
            'name' : forms.TextInput(attrs={'class': 'form-control'}), 
            'email' : forms.EmailInput(attrs={'class': 'form-control'}),
            'contact' : forms.TextInput(attrs={'class': 'form-control'}),
        }

