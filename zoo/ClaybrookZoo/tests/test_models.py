from django.test import TestCase
from ClaybrookZoo import models


# class UserTest(TestCase):
#     def test_string_representation(self):
#         data = models.User(username='nami',
#           first_name = 'sanam',
#           last_name = 'basnet',
#           email='sanam@test.com',
#           password = 'Blabitw1234',
#           role = 'Visitor')
#         self.assertEqual(str(data), data.username)



# class AnimalTest(TestCase):
#     def test_string_representation(self):
#         data = models.Animal(
#             id=1,
#             classification = 'abcdee',
#             species = 'abcdee',
#             name = 'abcdee',
#             gender= 'male',
#             dob = '02/2/2020',
#             date_joined = '22/2/2020',
#             condition ='Normal',
#             location = 'abcdee',
#             born_place= 'abcdee',
#             population_distribution= 'abcdee',
#             average_dimension= 'abcdee',
#             average_life_span= 'abcdee',
#             dietary_requirement= 'abcdee',
#             natural_habitat= 'abcdee',
#             colour_variants= 'abcdee',
#             visibility = 'visible'

#         )
#         self.assertEqual(str(data), str(data.id)+'   '+data.name)



class MammalTest(TestCase):
    def test_string_representation(self):
        ann = models.Animal(
            id=1,
            name = 'abcdee',
        )
        data = models.Mammal(
            animal = ann,
            gestational_period = '22 moth',
            mammal_category = 'speddd',
            average_temperature = '25c'

        )
        self.assertEqual(str(data),data.animal.name)



class ReptileTest(TestCase):
    def test_string_representation(self):
        ann = models.Animal(
            id=1,
            name = 'abcdee',
        )
        data = models.Reptile(
            animal = ann,
            reproduction_type = 'birth',
            offspring_number = 1,
            clutch_size = 'big',

        )
        self.assertEqual(str(data),data.animal.name)



class BirdTest(TestCase):
    def test_string_representation(self):
        ann = models.Animal(
            id=1,
            name = 'abcdee',
        )
        data = models.Bird(
            animal = ann,
            nest_construction='yes',
            clutch_size ='22',
            wing_span ='big',
            fly_ability = 'no'
        )
        self.assertEqual(str(data),data.animal.name)



class FishTest(TestCase):
    def test_string_representation(self):
        ann = models.Animal(
            id=1,
            name = 'abcdee',
        )
        data = models.Fish(
            animal = ann,
           average_temperature ='22',
           water_type='clean'
        )
        self.assertEqual(str(data),data.animal.name)



class WatchlistTest(TestCase):
    def test_string_representation(self):
        ann = models.Animal(
            id=1,
            name = 'abcdee',
        )
        data = models.WatchList(
            animal = ann,
           condition ='Normal',
           location = 'sddsds',
           observation_date='2/7/2020'
        )
        self.assertEqual(str(data),data.animal.name)



class SponsorTest(TestCase):
    def test_string_representation(self):
        data = models.Sponsor(
            name = 'sudish',
        )
        self.assertEqual(str(data),data.name)


class UpdateTest(TestCase):
    def test_string_representation(self):
        data = models.Update(
            heading = 'sudish',
        )
        self.assertEqual(str(data),data.heading)


class UpdateTest(TestCase):
    def test_string_representation(self):
        data = models.Update(
            heading = 'sudish',
        )
        self.assertEqual(str(data),data.heading)




class MessageTest(TestCase):
    def test_string_representation(self):
        sender = models.User(username='alex',)
        data = models.Message(sender=sender)
        self.assertEqual(str(data), data.sender.username)

class FeddbackTest(TestCase):
    def test_string_representation(self):
        sender = models.User(username='alex',)
        data = models.Feedback(sender=sender)
        self.assertEqual(str(data), data.sender.username)



class BookingTest(TestCase):
    def test_string_representation(self):
        user = models.User(username='alex',)
        data = models.Booking(
            booked_by = user,
        )
        self.assertEqual(str(data),data.booked_by.username)