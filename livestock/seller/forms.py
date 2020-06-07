from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms

# class UserCreateForm(UserCreationForm):
#
#     class Meta:
#         fields = ('username','phone','email','password1','password2')
#         model = get_user_model()
#
#     def __init__(self,*args,**kwargs):
#         super().__init__(*args,**kwargs)
        # self.fields['username'].label = 'Seller Name'
        # self.fields['phone'].label = "Contact Number"
    # def __init__(self, *args, **kwargs):
    #     user = kwargs.pop("user", None)
    #     super().__init__(*args, **kwargs)
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username',  'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username' ,'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image','phone','address','city','state','pincode']
