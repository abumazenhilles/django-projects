from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(label="User Name")
    password = forms.CharField(label="password", widget=forms.PasswordInput)


class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=30, min_length=5, required=True, widget=forms.TextInput(
        attrs={
            "placeholder": "Username",
            "class": "form-control"
        }), label="your Name")
    first_name = forms.CharField(
        max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(
        max_length=30, required=False, help_text='Optional.')
    password = forms.CharField(max_length=30, min_length=8, required=True,
                               widget=forms.PasswordInput(
                                   attrs={
                                       "placeholder": "Password",
                                       "class": "form-control"
                                   }), label="password")
    confirm = forms.CharField(max_length=30, min_length=8, required=True,
                              widget=forms.PasswordInput(
                                  attrs={
                                      "placeholder": "Confirm Password",
                                      "class": "form-control"
                                  }
                              ), label="Password Confirm")
    email = forms.EmailField(max_length=254, widget=forms.EmailInput(
        attrs={
            "placeholder": "Email",
            "class": "form-control"
        }), help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    # def clean(self):
    #     user = super(RegisterForm, self).save(commit=False)
    #     user.username = self.cleaned_data.get("username")
    #     user.password = self.cleaned_data.get("password")
    #     user.confirm = self.cleaned_data.get("confirm")
    #     user.first_name = self.cleaned_data.get("first_name")
    #     user.last_name = self.cleaned_data.get("last_name")
    #     user.email = self.cleaned_data.get("email")
    #     user.save()

    #     if password and confirm and password != confirm:
    #         raise forms.ValidationError("Password Does Not Match")

    #     values = {
    #         "username": username,
    #         "password": password
    #     }
    #     return values
