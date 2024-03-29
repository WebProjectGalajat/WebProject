from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from webspotify.models import Favourite_Song


class CustomUserCreationForm(UserCreationForm):
	class Meta(UserCreationForm.Meta):
		fields = UserCreationForm.Meta.fields + ("email", "first_name", "last_name")

