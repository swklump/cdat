from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

intersections = [('mill plain blvd / se 164th', 'Mill Plain Blvd / SE 164th Ave'),
('4th plain blvd  / ne stapleton rd','4th Plain Blvd / NE Stapleton'),
('ne andresen rd / ne burton rd','NE Andresen Rd / NE Burton Rd')]

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username','email','password1','password2']

#class IntersectionForm(forms.Form):
#    intersections = forms.ModelChoiceField(queryset=Intersection.objects.all(), widget=forms.Select(attrs={"onChange":'refresh()'}))

class PostForm(forms.Form):

    select_your_state = forms.ChoiceField(choices=[('alaska','Alaska'),('nebraska','Nebraska'),('nevada','Nevada'),('newyork','New York'),
    	('washington','Washington')])
    # choose_your_crash_file = forms.FileField(attrs={"onChange":'refresh()'})
    choose_your_crash_file = forms.FileField()
    select_how_many_diagrams_to_create = forms.IntegerField()
    select_your_intersection = forms.ChoiceField(choices=intersections)
    sort_by = forms.ChoiceField(choices=[('total crashes','Total Crashes'),('fatal crashes','Fatal Crashes (K)'),
    	('fatal and serious injury crashes','Fatal and Serious Injury Crashes (K+A)'),
    	('fatal and all injury crashes','Fatal and All Injury Crashes (K+A+B+C)')])
    ped_bike_filter = forms.ChoiceField(choices=[('no filter','No Filter'),
        ('pedestrian and bicyclist crashes only','Pedestrian and Bicyclist Crashes Only')])


# I think I see what I have to do. I have to run the program and add the available intersections to the

#some parsing function