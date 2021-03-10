from django import forms

class login_form(forms.Form):
    Username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Name", "name":"fullname"}))
    Password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control", "placeholder":"Password", "name":"password"}))

# password = forms.CharField(max_length=32, widget=forms.PasswordInput)
# password = forms.CharField(widget=forms.PasswordInput())


