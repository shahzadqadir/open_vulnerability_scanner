from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    fields = ["username", ]