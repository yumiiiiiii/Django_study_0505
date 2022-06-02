from django.contrib.auth.forms import UserCreationForm
from.models import CustomUser

class UserForm(UserCreationForm):
    class Meta:
        model=CustomUser
        fields=['username','password1','password2','age']