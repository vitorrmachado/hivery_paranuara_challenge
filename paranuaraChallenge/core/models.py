from django.db import models

# Create your models here.

'''
Representation of the companies JSON
'''
class Company(models.Model):
    index = models.IntegerField('index',primary_key=True)
    name = models.CharField('company', max_length=200)

    employees = []

    def __str__(self):
        return str(self.index)


'''
    Representation of the People Json
    Some attributes from person were removed in order to have a clean and organised data.
'''
class Person(models.Model):
    index = models.IntegerField('index',primary_key=True)
    _id = models.CharField('_id', max_length=250)
    has_died = models.BooleanField('has_died')
    age = models.IntegerField('age')
    eyeColor = models.CharField('eyeColor', max_length=50)
    name = models.CharField('name', max_length=200)
    gender = models.CharField('gender', max_length=20)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)
    email = models.TextField('email')
    phone = models.TextField('phone')
    address = models.TextField('address', blank=True)

    friends = models.ManyToManyField('self',related_name='friends_of', symmetrical=False)
    fruits = []
    vegetables = []

    def __str__(self):
        return self.name

    def __hash__(self):
        return hash((self.index))

    def __eq__(self, other):
        return (self.index) == (other.index)


class Fruits(models.Model):
    name = models.CharField('name', max_length=50)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Vegetables(models.Model):
    name = models.CharField('name', max_length=50)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


def load_person(json_object):
    person = Person()
    person.index = json_object['index']
    person.name = json_object['name']
    person._id = json_object['_id']
    person.has_died = json_object['has_died']
    person.age = json_object['age']
    person.eyeColor = json_object['eyeColor']
    person.gender = json_object['gender']
    person.email = json_object['email']
    person.phone = json_object['phone']
    person.address = json_object['address']
    person.company = Company(index=json_object['company_id'] - 1)  # I decided to use the index as primary key since it is unique, but the company ID is the index + 1
    return person