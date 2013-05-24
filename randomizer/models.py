# -*- coding: utf-8 -*-
""" models for the randomizer app """
# models
from base.models import BaseModel

# django
from django.db import models


class Name(BaseModel):
    """ Stores contest data """
    # required fields
    name = models.CharField(
        max_length=120,
        help_text="The random name generated",
    )
    count = models.BigIntegerField()
