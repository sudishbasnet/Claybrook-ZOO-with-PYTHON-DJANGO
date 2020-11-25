from django.test import TestCase
from ClaybrookZoo import forms,models

class SignupformTest(TestCase):
    def test_signup_form1(self):
        dat = {
            "username": "user",
            "first_name": "user",
            "last_name" : "seventy",
            "email":"user@test.com",
            "password1": "blabit2539",
            "password2": "blabit2539"
            }

        self.form(dat)  

    def test_signup_form2(self):
        dat = {
            "username": "user",
            "first_name": "",
            "last_name" : "seventy",
            "email":"user@test.com",
            "password1": "blabit2539",
            "password2": "blabit2539"
        }
        self.form(dat) 

    def test_signup_form3(Self):
        dat = {
            "username": "user",
            "first_name": "sudish",
            "last_name" : "",
            "email":"user@test.com",
            "password1": "blabit2539",
            "password2": "blabit2539"
        }
        self.form(dat)  

    def test_signup_form4(Self):
        dat = {
            "username": "user",
            "first_name": "user",
            "last_name" : "seventy",
            "email":"",
            "password1": "blabit2539",
            "password2": "blabit2539"
        }

        self.form(dat)

    def test_signup_form5(Self):
        dat = {
            "username": "user",
            "first_name": "user",
            "last_name" : "seventy",
            "email":"user@test.com",
            "password1": "",
            "password2": "blabit2539"
        }
         
        self.form(dat)


    def test_signup_form6(Self):
        dat = {
            "username": "user",
            "first_name": "user",
            "last_name" : "seventy",
            "email":"user@test.com",
            "password1": "blabit2539",
            "password2": ""
        }
        
        self.form(dat) 


        
        
    def form(self,dat):
        form = forms.SignUpForm(data=dat)
        form.is_valid()
        self.assertFalse(form.errors) 
           




class UpdateTest(TestCase):
    def test_update(self):
        dat = {
            "heading" : "House",
            "description" : "this is video",
        }
        self.form(dat)
    
    def test_update1(self):
        dat = {
            "heading" : '',
            "description" : "this is video",
        }
        self.form(dat)

    def test_update2(self):
        dat = {
            "heading" : 122,
            "description" : "this is video",
        }
        self.form(dat)

    def test_update3(self):
        dat = {
            "heading" : "House",
            "description" : "",
        }
        self.form(dat)
    

    def form(self,dat):
        form = forms.UpdateForm(data=dat)
        form.is_valid()
        self.assertFalse(form.errors)




class SponsorForm(TestCase):
    def test(self):
        animal = models.Animal(name='animal')
        dat = {
            'name':'sudish',
            'existing_customer':'yes',
            'official_id':123456,
            'primary_contact':'09775432456',
            'secondary_contact':'8765433456',
            'address' :'samnkhamul',
            'web_address':'www.youtube.com',
            'animal':animal,
            'sponsor_band':'A',
            'total_fee':34567,
            'agreement_period':'june 1 to dec 5',
            'signage_area_percent':'1/2',
            'signage_photo' : '',
            'note' : 'hyyyyy'
        }
        self.form(dat)


    def test1(self):
        animal = models.Animal(name='animal')
        dat = {
            'name':'sudish',
            'existing_customer':'',
            'official_id':123456,
            'primary_contact':'09775432456',
            'secondary_contact':'8765433456',
            'address' :'samnkhamul',
            'web_address':'www.youtube.com',
            'animal':animal,
            'sponsor_band':'A',
            'total_fee':34567,
            'agreement_period':'june 1 to dec 5',
            'signage_area_percent':'1/2',
            'signage_photo' : '',
            'note' : 'hyyyyy'
        }
        self.form(dat)
    
    def test2(self):
        animal = models.Animal(name='animal')
        dat = {
            'name':'sudish',
            'existing_customer':'yes',
            'official_id':'',
            'primary_contact':'09775432456',
            'secondary_contact':'8765433456',
            'address' :'samnkhamul',
            'web_address':'www.youtube.com',
            'animal':animal,
            'sponsor_band':'A',
            'total_fee':34567,
            'agreement_period':'june 1 to dec 5',
            'signage_area_percent':'1/2',
            'signage_photo' : '',
            'note' : 'hyyyyy'
        }
        self.form(dat)


    def test3(self):
        animal = models.Animal(name='animal')
        dat = {
            'name':'sudish',
            'existing_customer':'yes',
            'official_id':123456,
            'primary_contact':'',
            'secondary_contact':'8765433456',
            'address' :'samnkhamul',
            'web_address':'www.youtube.com',
            'animal':animal,
            'sponsor_band':'A',
            'total_fee':34567,
            'agreement_period':'june 1 to dec 5',
            'signage_area_percent':'1/2',
            'signage_photo' : '',
            'note' : 'hyyyyy'
        }
        self.form(dat)
    
    def test4(self):
        animal = models.Animal(name='animal')
        dat = {
            'name':'sudish',
            'existing_customer':'yes',
            'official_id':123456,
            'primary_contact':'09775432456',
            'secondary_contact':'',
            'address' :'samnkhamul',
            'web_address':'www.youtube.com',
            'animal':animal,
            'sponsor_band':'A',
            'total_fee':34567,
            'agreement_period':'june 1 to dec 5',
            'signage_area_percent':'1/2',
            'signage_photo' : '',
            'note' : 'hyyyyy'
        }
        self.form(dat)

    def test5(self):
        animal = models.Animal(name='animal')
        dat = {
            'name':'sudish',
            'existing_customer':'yes',
            'official_id':123456,
            'primary_contact':'09775432456',
            'secondary_contact':'8765433456',
            'address' :'',
            'web_address':'www.youtube.com',
            'animal':animal,
            'sponsor_band':'A',
            'total_fee':34567,
            'agreement_period':'june 1 to dec 5',
            'signage_area_percent':'1/2',
            'signage_photo' : '',
            'note' : 'hyyyyy'
        }
        self.form(dat)


    def test6(self):
        animal = models.Animal(name='animal')
        dat = {
            'name':'sudish',
            'existing_customer':'yes',
            'official_id':123456,
            'primary_contact':'09775432456',
            'secondary_contact':'8765433456',
            'address' :'samnkhamul',
            'web_address':'',
            'animal':animal,
            'sponsor_band':'A',
            'total_fee':34567,
            'agreement_period':'june 1 to dec 5',
            'signage_area_percent':'1/2',
            'signage_photo' : '',
            'note' : 'hyyyyy'
        }
        self.form(dat)


    
    def test7(self):
        animal = models.Animal(name='animal')
        dat = {
            'name':'sudish',
            'existing_customer':'yes',
            'official_id':123456,
            'primary_contact':'09775432456',
            'secondary_contact':'8765433456',
            'address' :'samnkhamul',
            'web_address':'www.youtube.com',
            'animal':'',
            'sponsor_band':'A',
            'total_fee':34567,
            'agreement_period':'june 1 to dec 5',
            'signage_area_percent':'1/2',
            'signage_photo' : '',
            'note' : 'hyyyyy'
        }
        self.form(dat)



    def test8(self):
        animal = models.Animal(name='animal')
        dat = {
            'name':'sudish',
            'existing_customer':'yes',
            'official_id':123456,
            'primary_contact':'09775432456',
            'secondary_contact':'8765433456',
            'address' :'samnkhamul',
            'web_address':'www.youtube.com',
            'animal':animal,
            'sponsor_band':'',
            'total_fee':34567,
            'agreement_period':'june 1 to dec 5',
            'signage_area_percent':'1/2',
            'signage_photo' : '',
            'note' : 'hyyyyy'
        }
        self.form(dat)



    def test9(self):
        animal = models.Animal(name='animal')
        dat = {
            'name':'sudish',
            'existing_customer':'yes',
            'official_id':123456,
            'primary_contact':'09775432456',
            'secondary_contact':'8765433456',
            'address' :'samnkhamul',
            'web_address':'www.youtube.com',
            'animal':animal,
            'sponsor_band':'A',
            'total_fee':'',
            'agreement_period':'june 1 to dec 5',
            'signage_area_percent':'1/2',
            'signage_photo' : '',
            'note' : 'hyyyyy'
        }
        self.form(dat)



    def test10(self):
        animal = models.Animal(name='animal')
        dat = {
            'name':'sudish',
            'existing_customer':'yes',
            'official_id':123456,
            'primary_contact':'09775432456',
            'secondary_contact':'8765433456',
            'address' :'samnkhamul',
            'web_address':'www.youtube.com',
            'animal':animal,
            'sponsor_band':'A',
            'total_fee':34567,
            'agreement_period':'',
            'signage_area_percent':'1/2',
            'signage_photo' : '',
            'note' : 'hyyyyy'
        }
        self.form(dat)




    def test11(self):
        animal = models.Animal(name='animal')
        dat = {
            'name':'sudish',
            'existing_customer':'yes',
            'official_id':123456,
            'primary_contact':'09775432456',
            'secondary_contact':'8765433456',
            'address' :'samnkhamul',
            'web_address':'www.youtube.com',
            'animal':animal,
            'sponsor_band':'A',
            'total_fee':34567,
            'agreement_period':'june 1 to dec 5',
            'signage_area_percent':'1/2',
            'signage_photo' : '',
            'note' : 'hyyyyy'
        }
        self.form(dat)




    def test12(self):
        animal = models.Animal(name='animal')
        dat = {
            'name':'sudish',
            'existing_customer':'yes',
            'official_id':123456,
            'primary_contact':'09775432456',
            'secondary_contact':'8765433456',
            'address' :'samnkhamul',
            'web_address':'www.youtube.com',
            'animal':animal,
            'sponsor_band':'A',
            'total_fee':34567,
            'agreement_period':'june 1 to dec 5',
            'signage_area_percent':'',
            'signage_photo' : '',
            'note' : 'hyyyyy'
        }
        self.form(dat)


    def test13(self):
        animal = models.Animal(name='animal')
        dat = {
            'name':'sudish',
            'existing_customer':'yes',
            'official_id':123456,
            'primary_contact':'09775432456',
            'secondary_contact':'8765433456',
            'address' :'samnkhamul',
            'web_address':'www.youtube.com',
            'animal':animal,
            'sponsor_band':'A',
            'total_fee':34567,
            'agreement_period':'june 1 to dec 5',
            'signage_area_percent':'1/2',
            'signage_photo' : '',
            'note' : ''
        }
        self.form(dat)

    def form(self,dat):
        form = forms.VisitorSponsorForm(data=dat)
        form.is_valid()
        self.assertFalse(form.errors)



class Animalform(TestCase):
    def test(self):
        dat = {
           'species'  :'abcdde',
           'name':'abcdde',
           'gender' :'male',
           'dob':'06/08/1999',
           'date_joined':'06/08/1999',
           'location':'abcdde' ,
           'born_place':'abcdde',
           'population_distribution':'abcdde',
           'average_dimension':'abcdde',
           'average_life_span':'abcdde',
           'dietary_requirement':'abcdde',
           'natural_habitat':'abcdde',
           'colour_variant':'abcdde'
        }
        self.form(dat)

    def test1(self):
        dat = {
           'species'  :'',
           'name':'abcdde',
           'gender' :'male',
           'dob':'06/08/1999',
           'date_joined':'06/08/1999',
           'location':'abcdde' ,
           'born_place':'abcdde',
           'population_distribution':'abcdde',
           'average_dimension':'abcdde',
           'average_life_span':'abcdde',
           'dietary_requirement':'abcdde',
           'natural_habitat':'abcdde',
           'colour_variant':'abcdde'
        }
        self.form(dat)

    def test2(self):
        dat = {
           'species'  :'abcdde',
           'name':'',
           'gender' :'male',
           'dob':'06/08/1999',
           'date_joined':'06/08/1999',
           'location':'abcdde' ,
           'born_place':'abcdde',
           'population_distribution':'abcdde',
           'average_dimension':'abcdde',
           'average_life_span':'abcdde',
           'dietary_requirement':'abcdde',
           'natural_habitat':'abcdde',
           'colour_variant':'abcdde'
        }
        self.form(dat)

    def test3(self):
        dat = {
           'species'  :'abcdde',
           'name':'abcdde',
           'gender' :'',
           'dob':'06/08/1999',
           'date_joined':'06/08/1999',
           'location':'abcdde' ,
           'born_place':'abcdde',
           'population_distribution':'abcdde',
           'average_dimension':'abcdde',
           'average_life_span':'abcdde',
           'dietary_requirement':'abcdde',
           'natural_habitat':'abcdde',
           'colour_variant':'abcdde'
        }
        self.form(dat)

    def test4(self):
        dat = {
           'species'  :'abcdde',
           'name':'abcdde',
           'gender' :'male',
           'dob':'',
           'date_joined':'06/08/1999',
           'location':'abcdde' ,
           'born_place':'abcdde',
           'population_distribution':'abcdde',
           'average_dimension':'abcdde',
           'average_life_span':'abcdde',
           'dietary_requirement':'abcdde',
           'natural_habitat':'abcdde',
           'colour_variant':'abcdde'
        }
        self.form(dat)

    def test5(self):
        dat = {
           'species'  :'abcdde',
           'name':'abcdde',
           'gender' :'male',
           'dob':'06/08/1999',
           'date_joined':'',
           'location':'abcdde' ,
           'born_place':'abcdde',
           'population_distribution':'abcdde',
           'average_dimension':'abcdde',
           'average_life_span':'abcdde',
           'dietary_requirement':'abcdde',
           'natural_habitat':'abcdde',
           'colour_variant':'abcdde'
        }
        self.form(dat)

    def test6(self):
        dat = {
           'species'  :'abcdde',
           'name':'abcdde',
           'gender' :'male',
           'dob':'06/08/1999',
           'date_joined':'06/08/1999',
           'location':'' ,
           'born_place':'abcdde',
           'population_distribution':'abcdde',
           'average_dimension':'abcdde',
           'average_life_span':'abcdde',
           'dietary_requirement':'abcdde',
           'natural_habitat':'abcdde',
           'colour_variant':'abcdde'
        }
        self.form(dat)

    def test7(self):
        dat = {
           'species'  :'abcdde',
           'name':'abcdde',
           'gender' :'male',
           'dob':'06/08/1999',
           'date_joined':'06/08/1999',
           'location':'abcdde' ,
           'born_place':'',
           'population_distribution':'abcdde',
           'average_dimension':'abcdde',
           'average_life_span':'abcdde',
           'dietary_requirement':'abcdde',
           'natural_habitat':'abcdde',
           'colour_variant':'abcdde'
        }
        self.form(dat)

    def test8(self):
        dat = {
           'species'  :'abcdde',
           'name':'abcdde',
           'gender' :'male',
           'dob':'06/08/1999',
           'date_joined':'06/08/1999',
           'location':'abcdde' ,
           'born_place':'abcdde',
           'population_distribution':'',
           'average_dimension':'abcdde',
           'average_life_span':'abcdde',
           'dietary_requirement':'abcdde',
           'natural_habitat':'abcdde',
           'colour_variant':'abcdde'
        }
        self.form(dat)

    def test9(self):
        dat = {
           'species'  :'abcdde',
           'name':'abcdde',
           'gender' :'male',
           'dob':'06/08/1999',
           'date_joined':'06/08/1999',
           'location':'abcdde' ,
           'born_place':'abcdde',
           'population_distribution':'abcdde',
           'average_dimension':'',
           'average_life_span':'abcdde',
           'dietary_requirement':'abcdde',
           'natural_habitat':'abcdde',
           'colour_variant':'abcdde'
        }
        self.form(dat)

    def test10(self):
        dat = {
           'species'  :'abcdde',
           'name':'abcdde',
           'gender' :'male',
           'dob':'06/08/1999',
           'date_joined':'06/08/1999',
           'location':'abcdde' ,
           'born_place':'abcdde',
           'population_distribution':'abcdde',
           'average_dimension':'abcdde',
           'average_life_span':'',
           'dietary_requirement':'abcdde',
           'natural_habitat':'abcdde',
           'colour_variant':'abcdde'
        }
        self.form(dat)

    def test11(self):
        dat = {
           'species'  :'abcdde',
           'name':'abcdde',
           'gender' :'male',
           'dob':'06/08/1999',
           'date_joined':'06/08/1999',
           'location':'abcdde' ,
           'born_place':'abcdde',
           'population_distribution':'abcdde',
           'average_dimension':'abcdde',
           'average_life_span':'abcdde',
           'dietary_requirement':'',
           'natural_habitat':'abcdde',
           'colour_variant':'abcdde'
        }
        self.form(dat)

    def test12(self):
        dat = {
           'species'  :'abcdde',
           'name':'abcdde',
           'gender' :'male',
           'dob':'06/08/1999',
           'date_joined':'06/08/1999',
           'location':'abcdde' ,
           'born_place':'abcdde',
           'population_distribution':'abcdde',
           'average_dimension':'abcdde',
           'average_life_span':'abcdde',
           'dietary_requirement':'abcdde',
           'natural_habitat':'',
           'colour_variant':'abcdde'
        }
        self.form(dat)

    
    def test13(self):
        dat = {
           'species'  :'abcdde',
           'name':'abcdde',
           'gender' :'male',
           'dob':'06/08/1999',
           'date_joined':'06/08/1999',
           'location':'abcdde' ,
           'born_place':'abcdde',
           'population_distribution':'abcdde',
           'average_dimension':'abcdde',
           'average_life_span':'abcdde',
           'dietary_requirement':'abcdde',
           'natural_habitat':'abcdde',
           'colour_variant':''
        }
        self.form(dat)

    def form(self,dat):
        form = forms.AnimalForm(data=dat)
        form.is_valid()
        self.assertFalse(form.errors)



class WatchlistTest(TestCase):
    def test(self):
        animal = models.Animal(
           species  ='abcdde',
           name='abcdde',
        )
        dat = {
           'animal':animal,
           'condition':'Normal',
           'location':'sankh',
           'observation_date':'08/09/2020'
        }
        self.form(dat)

    

    def form(self,dat):
        form = forms.Watchlist(data=dat)
        form.is_valid()
        self.assertFalse(form.errors)



class BookingTest(TestCase):
    def test(self):
        dat = {
           'entry_date':'09/2/2020',
           'no_of_entries':2,
           'total_cost':222
        }
        self.form(dat)

    def test1(self):
        dat = {
           'entry_date':'',
           'no_of_entries':2,
           'total_cost':222
        }
        self.form(dat)

    def test2(self):
        dat = {
           'entry_date':'09/2/2020',
           'no_of_entries':'',
           'total_cost':222
        }
        self.form(dat)

    def test3(self):
        dat = {
           'entry_date':'09/2/2020',
           'no_of_entries':2,
           'total_cost':''
        }
        self.form(dat)

    

    def form(self,dat):
        form = forms.Booking(data=dat)
        form.is_valid()
        self.assertFalse(form.errors)