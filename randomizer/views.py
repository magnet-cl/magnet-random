""" This file contains some generic purpouse views """

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from randomizer.models import Name


@csrf_exempt
def name_new(request):
    """ creates a new name object with the given parameters"""
    name = request.POST['name']
    count = request.POST['count']

    Name.objects.create(name=name, count=count)

    return HttpResponse(True, mimetype='application/json')
