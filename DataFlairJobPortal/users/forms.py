from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("email","first_name","surname","user_type","location","date_of_birth")


class RecruiterCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("email","first_name","surname","user_type","location","date_of_birth")


class SeekerCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("email","first_name","surname","user_type","location","date_of_birth")



class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("email","first_name","surname","user_type","location","date_of_birth")