import datetime

from django import forms

from utils import getWeekdayStr


class LateSubmitForm(forms.Form):
    name = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=200)
    message = forms.CharField(max_length=500,required=False)

    type = forms.ChoiceField(required=True,widget=forms.RadioSelect(),choices=[("all","no matter when dinner is served."),("early","only if dinner will be served before 7pm")])
    schedule = forms.ChoiceField(required=True,widget=forms.RadioSelect(),choices=[("today","today only."),("weekday","every week on "+getWeekdayStr(datetime.datetime.now())+"s")])
    diet = forms.ChoiceField(required=True,widget=forms.RadioSelect(),choices=[("v*","V* (vegan)"),("v","V (vegetarian)"),("m","M (meat eater)")])

    glutenfree = forms.BooleanField(required=False)
    nonuts = forms.BooleanField(required=False)
    nopeanuts = forms.BooleanField(required=False)

