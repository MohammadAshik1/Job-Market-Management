from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm,SetPasswordForm, PasswordChangeForm
from django.contrib.auth.models import User
from .models import Post,Category,Cv

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'block bg-[#18debb] bg-opacity-20 w-96 rounded-xl px-3 py-2 focus:outline-none placeholder:text-gray-400'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'block bg-[#18debb] bg-opacity-20 w-96 rounded-xl px-3 py-2 focus:outline-none placeholder:text-gray-400'
    }))

class SendEmail(PasswordResetForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email address',
        'class': 'block bg-[#18debb] bg-opacity-20 w-96 rounded-xl px-3 py-2 focus:outline-none placeholder:text-gray-400'
    }))

class ConfirmPassword(SetPasswordForm):
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'block bg-[#18debb] bg-opacity-20 w-96 rounded-xl px-3 py-2 focus:outline-none placeholder:text-gray-400'
    }))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat password',
        'class': 'block bg-[#18debb] bg-opacity-20 w-96 rounded-xl px-3 py-2 focus:outline-none placeholder:text-gray-400'
    }))

class PasswordChange(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={
    'placeholder': 'Old Password',
    'class': 'block bg-[#18debb] bg-opacity-20 w-96 rounded-xl px-3 py-2 focus:outline-none placeholder:text-gray-400'
    }))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'block bg-[#18debb] bg-opacity-20 w-96 rounded-xl px-3 py-2 focus:outline-none placeholder:text-gray-400'
    }))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat password',
        'class': 'block bg-[#18debb] bg-opacity-20 w-96 rounded-xl px-3 py-2 focus:outline-none placeholder:text-gray-400'
    }))


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'block bg-[#18debb] bg-opacity-20 w-96 rounded-xl px-3 py-2 focus:outline-none placeholder:text-gray-400'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email address',
        'class': 'block bg-[#18debb] bg-opacity-20 w-96 rounded-xl px-3 py-2 focus:outline-none placeholder:text-gray-400'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'block bg-[#18debb] bg-opacity-20 w-96 rounded-xl px-3 py-2 focus:outline-none placeholder:text-gray-400'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat password',
        'class': 'block bg-[#18debb] bg-opacity-20 w-96 rounded-xl px-3 py-2 focus:outline-none placeholder:text-gray-400'
    }))


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['category', 'name', 'description', 'salary', 'image']
    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Job name',
        'class': 'bg-transparent w-full px-3 py-2 border-[1px] border-gray-300 focus:outline-none focus:border-[#397f77]'
    }))
    description = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'bg-transparent w-full px-3 py-2 border-[1px] border-gray-300 focus:outline-none focus:border-[#397f77]'
    }))

    salary = forms.FloatField(widget=forms.NumberInput(attrs={
        'class': 'bg-transparent w-full px-3 py-2 border-[1px] border-gray-300 focus:outline-none focus:border-[#397f77]'
    }))

    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={
        'class': 'px-10 py-2 bg-[#397f77] text-white text-lg font-semibold rounded-lg my-5 hover:bg-[#18debb] duration-300'
    }))

    category = forms.ModelChoiceField(queryset=Category.objects.all(),widget=forms.Select(attrs={
        'class' : 'block appearance-none w-full bg-gray-200 border border-gray-200 text-gray-700 py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500" id="grid-state'
    }))

class PostSearchForm(forms.Form):
    search_query = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Searc...',
        'class': 'px-3 py-1 bg-gray-50 w-full border-0  border-r-gray-300 border-r-2 focus:border-transparent focus:border-r-gray-300 focus:ring-0 outline-transparent placeholder:text-[#397f77]'
    }))

class PostFilterForm(forms.Form):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='All Categories', required=False,widget=forms.Select(attrs={
        'class' : ' bg-gray-200 border border-gray-200 text-gray-700 py-3 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500" '
    }))

class CvForm(forms.ModelForm):
    class Meta:
        model = Cv
        fields = ('cv', 'job')



    