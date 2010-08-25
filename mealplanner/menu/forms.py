from django import forms

class MenuItemForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=1000)
    diet = forms.ChoiceField(required=True,widget=forms.RadioSelect(),choices=[("v*","V* (vegan)"),("v","V (vegetarian)"),("m","M (meat eater)")])
    glutenfree = forms.BooleanField(required=False)
    nonuts = forms.BooleanField(required=False)
    nopeanuts = forms.BooleanField(required=False)

