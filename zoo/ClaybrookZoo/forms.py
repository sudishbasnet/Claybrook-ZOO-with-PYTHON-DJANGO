from django import forms
from django.forms import ModelForm
from ClaybrookZoo import models
from django.contrib.auth.forms import UserCreationForm


class UpdateForm(forms.ModelForm):
    class Meta:
        model = models.Update
        fields =('heading','description')




class VisitorSponsorForm(forms.ModelForm):
    class Meta:
        model = models.Sponsor
        fields =('name','existing_customer','official_id','primary_contact','secondary_contact','address','web_address','animal','sponsor_band','total_fee','agreement_period','signage_area_percent','signage_photo','note')
        widgets = {
                'total_fee': forms.TextInput(attrs={'readonly':'readonly'}),
            }

class AdminSponsorForm(forms.ModelForm):
    class Meta:
        model = models.Sponsor
        fields =('name','existing_customer','sponsored_user','official_id','primary_contact','secondary_contact','address','web_address','animal','sponsor_band','total_fee','agreement_period','signage_area_percent','signage_photo','note','payment_detail','payment_received','review_date')
        widgets = {
                'total_fee': forms.TextInput(attrs={'readonly':'readonly'}),
            }

class Booking(forms.ModelForm):
    class Meta:
        model = models.Booking
        fields =('entry_date','no_of_entries','total_cost')
        widgets = {
                'total_cost': forms.TextInput(attrs={'readonly':'readonly'}),
            }

class Feedback(forms.ModelForm):
    class Meta:
        model = models.Feedback
        fields =('description',)


class OfficialBooking(forms.ModelForm):
    class Meta:
        model = models.Booking
        fields =('name','entry_date','no_of_entries','total_cost','payment')
        widgets = {
                'total_cost': forms.TextInput(attrs={'readonly':'readonly'}),
            }


class Reptile(forms.ModelForm):
    class Meta:
        model = models.Reptile
        fields = ('reproduction_type','offspring_number','clutch_size')
    
class Mammal(forms.ModelForm):
    class Meta:
        model = models.Mammal
        fields = ('gestational_period','mammal_category','average_temperature')


class Bird(forms.ModelForm):
    class Meta:
        model = models.Bird
        fields = ('nest_construction','clutch_size','wing_span','fly_ability')

    
class Fish(forms.ModelForm):
    class Meta:
        model = models.Fish
        fields = ('average_temperature','water_type')



class AnimalForm(forms.ModelForm):
    class Meta:
        model = models.Animal
        fields =('species','name','gender','dob','date_joined','location','born_place','population_distribution','average_dimension','average_life_span','dietary_requirement','natural_habitat','colour_variants')


class Watchlist(forms.ModelForm):
    class Meta:
        model = models.WatchList
        fields = ('animal','condition','location','observation_date')

class SignUpForm(UserCreationForm):
    class Meta:
        model = models.User
        unique_together = ('email',)
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2' )


class SignUpFormUpdate(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ('username', 'first_name', 'last_name','email' )
        widgets = {
                'username': forms.TextInput(attrs={'readonly':'readonly'}),
                'email': forms.TextInput(attrs={'readonly':'readonly'}),
            }


class StaffSignUpForm(UserCreationForm):
    class Meta:
        model = models.User
        fields = ('username', 'first_name', 'last_name','email','role','password1', 'password2' )
        

class StaffSignUpFormUpdate(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ('username', 'first_name', 'last_name','email','role' )