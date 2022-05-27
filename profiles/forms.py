
from django import forms
from . models import Profile
from users.models import CustomUser


class ProfileForm(forms.ModelForm):

    city = forms.CharField(label="City", widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    phone = forms.CharField(label="Phone", widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    zipcode = forms.CharField(label="Zipcode", widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    state = forms.CharField(label="State", widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    address = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': '2'}))
    photo = forms.FileField(label='Photo', widget=forms.FileInput(
        attrs={'class': 'form-control',}))


    class Meta:
        model = Profile
        fields = ['phone', 'city', 'state',
                  'zipcode', 'photo', 'address', ]


class CustomUserForm(forms.ModelForm):
    first_name = forms.CharField(label="First Name", widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    last_name = forms.CharField(label="Last Name", widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    username = forms.CharField(label="Username", widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    email = forms.CharField(label="Email", widget=forms.EmailInput(
        attrs={'class': 'form-control', 'readonly': 'readonly'}))

    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name",'username', "email")
