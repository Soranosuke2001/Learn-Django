from django import forms
from django.core import validators

# Creating your own validators
# Note: The function name must start with the word `check`
def check_for_z(value: str):
  if value[0].lower() != 'z':
    raise forms.ValidationError("NAME MUST START WITH A Z")


class FormName(forms.Form):
  name = forms.CharField()
  email = forms.EmailField()
  verify_email = forms.EmailField(label="Enter your email again: ")
  text = forms.CharField(widget=forms.Textarea)
  botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

  # Note: This is the old way of doing things. Django has its own built in functions to help
  # def clean_botcatcher(self):
  #   botcatcher = self.cleaned_data['botcatcher']

  #   if len(botcatcher) > 0:
  #     raise forms.ValidationError("GOTCHA BOT!")

  #   return botcatcher


  # Note: In order to validate the entire form at once, create the `clean` method
  def clean(self):
    all_clean_data = super().clean()

    email = all_clean_data['email']
    vmail = all_clean_data['verify_mail']

    if email != vmail:
      raise forms.ValidationError("MAKE SURE EMAILS MATCH!")
  