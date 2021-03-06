# Imports
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Project, Comment, Profile

# Form for regsitering a new user
class RegisterForm(UserCreationForm):
    
    # Sign up form fields
    email = forms.EmailField(max_length=200, required=True)
    username = forms.CharField(max_length=50, required=True)
    password1 = forms.CharField(max_length=50, required=True)
    password2 = forms.CharField(max_length=50, required=True)
    
    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2', )

# Form for creating a new project
class CreateProjectForm(forms.ModelForm):
    rating = forms.IntegerField(required=False)
    code_link = forms.CharField(required=False)

    class Meta:
        model = Project
        fields =  ('name', 'description', 'project_image', 'rating', 'code_link', )
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

# Form for commenting on a project
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text', )

# Form for edit user profile
class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'bio', 'profile_image')

class EditProfileForm(forms.ModelForm):
    username = forms.CharField(required=True)
    class Meta:
        model = User
        fields = ('username', 'email')