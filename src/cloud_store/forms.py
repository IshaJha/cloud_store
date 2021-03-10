from django import forms

class contactForm(forms.Form):
    fullname = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Name", "name":"fullname"}))
    subject = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Subject", "name":"subject"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control", "placeholder":"Email", "name":"fullname"}))
    message = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control", "placeholder":"Your contant", "name":"message"}))