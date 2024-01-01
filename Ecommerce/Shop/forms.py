from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm


class RegisterForm(UserCreationForm):
    # fields we want to include and customize in our form
    first_name = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'نام',
                                                            'class': 'form-control',
                                                            }))
    last_name = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'نام خانوادگی',
                                                            'class': 'form-control',
                                                            }))
    username = forms.CharField(max_length=100,
                            required=True,
                            widget=forms.TextInput(attrs={'placeholder': 'نام کاربری',
                                                            'class': 'form-control',
                                                            }))
    email = forms.EmailField(required=True,
                            widget=forms.TextInput(attrs={'placeholder': 'پست الکترونیک',
                                                        'class': 'form-control',
                                                        }))
    password1 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'کلمه عبور',
                                                                'class': 'form-control',
                                                                'data-toggle': 'password',
                                                                'id': 'password',
                                                                }))
    password2 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'رمز عبور را تایید کنید',
                                                                'class': 'form-control',
                                                                'data-toggle': 'password',
                                                                'id': 'password',
                                                                }))
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100,
                            required=True,
                            widget=forms.TextInput(attrs={'placeholder': 'نام کاربری',
                                                            'class': 'form-control',
                                                            }))
    password = forms.CharField(max_length=50,
                            required=True,
                            widget=forms.PasswordInput(attrs={'placeholder': 'کلمه عبور',
                                                                'class': 'form-control',
                                                                'data-toggle': 'password',
                                                                'id': 'password',
                                                                'name': 'password',
                                                                }))
    remember_me = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']

class CommentForm(forms.Form):
    name = forms.CharField(max_length=100,required=True,)
    email = forms.CharField(max_length=50,required=True,)
    massage = forms.CharField(max_length=10000,required=True,)
                            # widget=forms.TextInput(attrs={'placeholder': 'Name Full',
                            #             'class': 'form-control me-2',
                            #             'aria-label': 'Username',
                            #             'aria-describedby': 'basic-addon1'})
    # widget=forms.TextInput(attrs={'placeholder': 'Email',
    #                                         'class': 'form-control me-2',
    #                                         'aria-label': 'Email',
    #                                         'aria-describedby': 'basic-addon2'})
    # widget=forms.Textarea(attrs={'placeholder': 'Your Comment...',
    #                                         'class': 'form-control',
    #                                         'rows': '7',
    # 
    #                                         'aria-label': 'text'})
    
class CommentReplyForm(forms.Form):
    name_reply = forms.CharField(max_length=100, required=True,)
    email_reply = forms.CharField(max_length=50, required=True,)
    massage_reply= forms.CharField(max_length=10000, required=True,)