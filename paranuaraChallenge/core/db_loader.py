import json, requests

class DBLoader():


    def load(self, is_test_db=False):
        self.__check_database(is_test_db)


    def __check_database(self, is_test_db):
        from .models import Company  # I cannot import models at module-level https://docs.djangoproject.com/en/2.0/ref/applications/#django.apps.AppConfig.ready

        if Company.objects.count() <= 0:  # Database is empty
            print('Database is empty. This may take a few minutes.')
            self.__load_companies()
            self.__load_people(is_test_db)
            print('Database loaded.')


    def __load_companies(self):
        from .models import Company

        print('Loading JSON companies into database...')
        url = 'https://raw.githubusercontent.com/joaosgreccia/hivery-backend-challenge/master/resources/companies.json'
        companies_json = json.loads(requests.get(url).text)

        companies = []
        for company_json in companies_json:
            company = Company(index=company_json['index'], name=company_json['company'])
            companies.append(company)

        Company.objects.bulk_create(companies)
        print('Companies loaded.')


    def __load_people(self, is_test_db):
        from .models import Person, Fruits, Vegetables, load_person

        url = 'https://raw.githubusercontent.com/joaosgreccia/hivery-backend-challenge/master/resources/people.json'
        json_people = json.loads(requests.get(url).text)

        if is_test_db:
            json_people = json_people[0:int(len(json_people)/5)] # 200 people for the in-memory testing database

        print('Loading JSON people into database...')

        vegetables_types = self.__load_vegetables(json_people)
        people, fruits, vegetables =  [], [], []
        friends = {}

        for json_person in json_people:
            person = load_person(json_person)
            people.append(person)

            friends[person.index] = [friend['index'] for friend in json_person['friends'] if
                                     person.index != friend['index']]

            for food in json_person['favouriteFood']:
                if food in vegetables_types:
                    vegetables.append(Vegetables(name=food, person=person))
                else:
                    fruits.append(Fruits(name=food, person=person))

        Person.objects.bulk_create(people)
        Fruits.objects.bulk_create(fruits)
        Vegetables.objects.bulk_create(vegetables)

        for person_index, friends_index in friends.items():
            person = Person.objects.get(index=person_index)
            friends = Person.objects.filter(index__in=friends_index)
            person.friends.set(friends)

        print('People loaded.')


    def __load_vegetables(self, json_people):

        food_list = []
        for json_person in json_people:
            for food in json_person['favouriteFood']:
                food_list.append(food)

        food_list = set(food_list)
        print("Different types of food: ", food_list)  # {'cucumber', 'strawberry', 'apple', 'carrot', 'celery', 'orange', 'beetroot', 'banana'}
        vegetables_types = ['cucumber', 'carrot', 'celery', 'beetroot']

        return [food for food in food_list if food in vegetables_types]