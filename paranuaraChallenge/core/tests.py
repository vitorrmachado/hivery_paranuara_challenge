from django.test import TestCase, Client
import random
from .db_loader import DBLoader
# Create your tests here.


class UnitTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        DBLoader().load(is_test_db=True)

    def test_employees(self):
        print('------------------------------------------------------\n\nTesting the get-employees endpoint: \n')
        random_indexes = self.__generate_random_list(120)
        c = Client()
        for index in random_indexes:
            response = c.get('/get-employees/'+str(index))
            print('Testing index {} -> {}'.format(index, response.content))

    def test_two_people(self):
        print('------------------------------------------------------\n\nTesting the get-people endpoint: \n')

        random_indexes_p1 = self.__generate_random_list(250)
        random_indexes_p2 = self.__generate_random_list(250)
        c = Client()

        for index in range(len(random_indexes_p1)):
            response = c.get('/get-people/' + str(random_indexes_p1[index]) + '/' + str(random_indexes_p2[index]))
            print('Testing indexes {} and {} -> {}'.format(random_indexes_p1[index], random_indexes_p2[index], response.content))

    def test_person(self):
        print('------------------------------------------------------\n\nTesting the get-person endpoint: \n')

        random_indexes = self.__generate_random_list(250)
        c = Client()
        for index in random_indexes:
            response = c.get('/get-person/'+str(index))
            print('Testing index {} -> {}'.format(index, response.content))


    #Generates a random list with 7 random ints and 3 strs
    @staticmethod
    def __generate_random_list(range_list):
        list = random.sample(range(range_list), 7) + ['aaa', 'b78gre247th8rf', '@/$Tgs%']
        return random.sample(list, k=len((list))) #shuffle the lists combined