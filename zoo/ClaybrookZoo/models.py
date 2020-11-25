from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    a = 'admin'
    b = 'zoo keeper'
    c = 'manager'
    d = 'visitor'
    e = 'temporary staff'
    role = [
        (a, 'admin'),
        (b, 'zoo keeper'),
        (c,'manager'),
        (d,'visitor'),
        (e, 'temporary staff')
    ]
    first_name = models.CharField(('first name'),max_length=30,blank=False)
    last_name = models.CharField(('last name'),max_length=30,blank=False)
    email = models.EmailField(('email address'), unique=True,blank=False)
    role  = models.CharField(max_length=15,choices=role,default=d)

    def __str__(self):
        return self.username



class Animal(models.Model):
    a = 'male'
    b = 'female'
    gender = [
        (a, 'male'),
        (b, 'female')
    ]
      
    classification = models.CharField(max_length=50,blank=True)
    species = models.CharField(max_length=50,blank=False)
    name = models.CharField(max_length=50,blank=False) 
    gender = models.CharField(max_length=10,choices=gender,default=b)
    dob = models.DateField()
    date_joined = models.DateField()
    condition = models.CharField(max_length=10,blank=True)
    location = models.CharField(max_length=50,blank=False)
    born_place = models.CharField(max_length=50)
    population_distribution = models.CharField(max_length=6)
    average_dimension =models.TextField()
    average_life_span = models.CharField(max_length=50)
    dietary_requirement = models.TextField()
    natural_habitat = models.TextField()
    colour_variants =models.CharField(max_length=50,blank=True)
    visibility = models.CharField(max_length=10,default='visible')

    def __str__(self):
        return str(self.id)+'   '+self.name

class AnimalPhoto(models.Model):
    photo = models.ImageField(upload_to='animals')
    animal = models.ForeignKey(Animal,on_delete='CASCADE',related_name='animal_photo')



class Mammal(models.Model):
    animal = models.ForeignKey(Animal,on_delete='CASCADE',null=True,related_name='mammal')
    gestational_period = models.CharField(max_length=50,blank=False)
    mammal_category =models.CharField(max_length=50,blank=False)
    average_temperature = models.CharField(max_length=20,blank=False)

    def __str__(self):
        return self.animal.name




class Bird(models.Model):
    animal = models.ForeignKey(Animal,on_delete='CASCADE',null=True,related_name='bird')
    nest_construction = models.CharField(max_length=100,blank=False)
    clutch_size = models.CharField(max_length=50,blank=False)
    wing_span = models.CharField(max_length=50,blank=False)
    fly_ability = models.CharField(max_length=3,blank=False)

    def __str__(self):
        return self.animal.name



class Fish(models.Model):
    animal = models.ForeignKey(Animal,on_delete='CASCADE',null=True,related_name='fish')
    average_temperature = models.CharField(max_length=20,blank=False)
    water_type = models.CharField(max_length=50,blank=False)


    def __str__(self):
        return self.animal.name



class Reptile(models.Model):
    animal = models.ForeignKey(Animal,on_delete='CASCADE',null=True,related_name='reptile')
    reproduction_type = models.CharField(max_length=50,blank=False)
    offspring_number = models.IntegerField(blank=False)
    clutch_size = models.CharField(max_length=50,blank=False)

    def __str__(self):
        return self.animal.name




class WatchList(models.Model):
    A = 'Normal'
    B = 'Critical'
    C = 'Dead'
    cond = [
        (A, 'Normal'),
        (B, 'Critical'),
        (C, 'Dead')
    ]  
    animal = models.ForeignKey(Animal,on_delete='CASCADE',related_name='animal_watchlist')
    condition = models.CharField(max_length=10,choices=cond,default=A)
    location = models.CharField(max_length=100,blank=False)
    observation_date = models.DateField()
    
    def __str__(self):
        return self.animal.name


    class Meta:
        ordering = ('-observation_date',)


class Sponsor(models.Model):
    a = 'yes'
    b = 'no'
    payment = [
        (a, 'yes'),
        (b, 'no'),
    ]

    A = 'A'
    B = 'B'
    C = 'C'
    D = 'D'
    E = 'E'
    band = [
        (A , 'A'),( B , 'B'),(C , 'C'),(D , 'D'),(E , 'E')
    ]
    name = models.CharField(max_length=100,blank=False)
    existing_customer = models.CharField(max_length=10,choices=payment,default=a)
    official_id = models.CharField(max_length=70,blank=False)
    primary_contact = models.IntegerField()
    secondary_contact = models.IntegerField(blank=False)
    address = models.CharField(max_length=100,blank=False)
    web_address = models.CharField(max_length=100,blank=True)
    animal = models.ManyToManyField(Animal,related_name='sponsored_animal',blank=True)
    sponsor_band = models.CharField(max_length=2,blank=False,choices=band,default=A)
    total_fee = models.IntegerField(default=2500)
    agreement_period = models.CharField(max_length=100,blank=False)
    signage_area_percent = models.CharField(max_length=5,blank=True)
    signage_photo = models.ImageField(upload_to='signage',blank=True)
    note = models.CharField(max_length=255,blank=True)
    sponsored_user = models.ManyToManyField(User,related_name='sponsored_user',blank=True)
    payment_detail = models.CharField(max_length=50,blank=True)
    payment_received = models.CharField(max_length=3,choices=payment,default=b)
    review_date = models.DateField(null=True,blank=True)
    confirmed_staff = models.ForeignKey(User,on_delete='CASCADE',null=True,related_name='sponsor_confirmed')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-review_date',)



class Update(models.Model):
    heading = models.CharField(max_length=150,blank=False)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
    uploaded_by = models.ForeignKey(User,on_delete='CASCADE',related_name='updater')

    def __str__(self):
        return self.heading

    
    class Meta:
        ordering = ('-date',)
        



class Message(models.Model):
    content = models.CharField(max_length=255,blank=False)
    sender = models.ForeignKey(User,on_delete='CASCADE',related_name='message_sender')
    receiver = models.ManyToManyField(User,blank=True,related_name='message_receiver')
    date = models.DateField(auto_now_add=True)
    seen = models.BooleanField(default=False)

    def __str__(self):
        return self.sender.username


    class Meta:
        ordering = ('-date',)


class Feedback(models.Model):
    description = models.TextField(blank=False)
    sender = models.ForeignKey(User,on_delete='CASCADE',related_name='feedback_sender')
    date = models.DateField(auto_now_add=True)
    highlight = models.BooleanField(default=False)

    def __str__(self):
        return self.sender.username


    class Meta:
        ordering = ('-date',)






class Booking(models.Model):
    a = 'yes'
    b = 'no'
    payment = [
        (a, 'yes'),
        (b, 'no'),
    ]
    name = models.CharField(max_length=30,blank=True)
    entry_date = models.DateField()
    no_of_entries = models.IntegerField(blank=False)
    booked_by = models.ForeignKey(User,on_delete='CASCADE',related_name='booked_by',null=True)
    total_cost = models.CharField(max_length=20,blank=True)
    payment = models.CharField(max_length=10,blank=True,choices=payment,default=b)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.booked_by.username

    class Meta:
        ordering = ('-date',)










































































