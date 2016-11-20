from django import forms
from .models import Mainapp ,CreateRoom


class MainappForm(forms.ModelForm):
	class Meta:
		model = Mainapp
		fields = ['email']

	# Nov 19 - can filter out, if the user exist within the cisco spark app
	def clean_email(self):

		email = self.cleaned_data.get('email')
		if False:
			raise forms.ValidationError("If you have make safe can print this out betters")

		return email


class CreateRoomForm(forms.ModelForm):
	class Meta:
		model = CreateRoom
		fields = ['room_name']
		widgets = {'room_name': forms.TextInput(attrs={'background-color': 'gray'}),}

	# Nov 19 - can filter out, if the user exist within the cisco spark app
	def clean_room_name(self):

		room_name = self.cleaned_data.get('room_name')
		if False:
			raise forms.ValidationError("If you have make safe can print this out betters")

		return room_name










# ------- END OF CODE ---------
