from django import forms
from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm as BaseUserChangeForm

User = get_user_model()


class UserChangeForm(BaseUserChangeForm):
    class Meta(BaseUserChangeForm.Meta):
        model = User
        fields = ["username", "email", "mobile","role"]  


class UserCreationForm(admin_forms.UserCreationForm):
    class Meta(admin_forms.UserCreationForm.Meta):
        model = User
        fields = ["username", "email", "mobile","role"]  

    error_messages = {
        "duplicate_username": "A user with that username already exists.",
        "duplicate_email": "A user with that email already exists.",
        "duplicate_mobile": "A user with that mobile number already exists.",
    }

    def clean_email(self) -> str:
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(self.error_messages["duplicate_email"])
        return email

    def clean_username(self) -> str:
        username = self.cleaned_data["username"]
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(self.error_messages["duplicate_username"])
        return username

    def clean_mobile(self) -> str:
        mobile = self.cleaned_data["mobile"]
        if User.objects.filter(mobile=mobile).exists():
            raise forms.ValidationError(self.error_messages["duplicate_mobile"])
        return mobile
