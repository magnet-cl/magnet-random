# -*- coding: utf-8 -*-
""" This file contains some generic purpouse views """

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.db.models import Count

from randomizer.models import Name


def index(request):
    """ view that renders a default home"""
    names = Name.objects.values('name').annotate(count=Count('id'))
    return render_to_response('index.html', {"names": names},
                              context_instance=RequestContext(request))
