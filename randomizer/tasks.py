""" celery tasks for the randomizer app """
from celery import task
from randomizer.models import Name

import random
import string


@task()
def generate_names():
    chars = string.ascii_uppercase.lower()

    names = [
        'imunizaga',
        'francisca',
        'alealmuna',
        'joaolopez',
        'contreras',
        'andteston',
        'mauricioc',
        'titrivera',
        'nachopara',
    ]

    name = ''.join(random.choice(chars) for x in range(9))
    count = 1

    while True:
        if name in names:
            Name.objects.create(name=name, count=count)
        letter = random.choice(chars)
        name = "".join([name[1:], letter])
        count += 1
