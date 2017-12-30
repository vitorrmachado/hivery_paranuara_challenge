from .models import Company, Person, Fruits, Vegetables
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse, HttpResponse
from django.db.models import Q
from django.forms.models import model_to_dict

def get_employees(request, index):

    try:
        company = Company.objects.get(index=index)
        employees = Person.objects.filter(company=company)

        return_json = {}
        if len(employees) == 0:
            return_json[company.name] = 'No employees found for this company'
        else:
            return_json[company.name] = {'employees' : [employee.name for employee in employees]}

        return JsonResponse(return_json)

    except ObjectDoesNotExist:
        return HttpResponse('No company found for the given index')


def get_people(request, index_p1, index_p2):

    people = Person.objects.filter(Q(index=index_p1) | Q(index=index_p2))

    if len(people) != 2:
        return HttpResponse('Error: The call didn`t returned 2 people. Please check the indexes.')
    else:
        return_json = {}
        for person in people:
            dict_person = model_to_dict(person, fields=['name', 'age', 'address', 'phone'])
            return_json[dict_person['name']] = dict_person
        common_friends = people[0].friends.all() & people[1].friends.all()
        return_json['common_friends'] = [friend.name for friend in common_friends]
        return JsonResponse(return_json)


def get_person(request, index):

    try:
        person = Person.objects.get(index=index)
        fruits = Fruits.objects.filter(person=person)
        vegetables = Vegetables.objects.filter(person=person)

        return_json = model_to_dict(person, fields=['name','age'])
        return_json['fruits'] = [fruit.name for fruit in fruits]
        return_json['vegetables'] = [vegetable.name for vegetable in vegetables]

        return JsonResponse(return_json)
    except ObjectDoesNotExist:
        return HttpResponse('No person found for the given index')
