from django.core.management.base import BaseCommand
from django.conf import settings

import random
import string
import urllib
import urllib2


class Command(BaseCommand):
    args = ''
    help = 'generates names'

    def handle(self, *args, **options):
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

        url = "%sname/new/" % settings.REPORT_TO

        print "Randomizer started ..."
        while True:
            if name in names:
                data = urllib.urlencode({"name": name, "count": count})
                print "HOLY FUCK! WE FOUND ONE!: {}, at count: {}".format(
                    name, count)
                req = urllib2.Request(url, data)
                urllib2.urlopen(req)
                count = 0
            letter = random.choice(chars)
            name = "".join([name[1:], letter])
            count += 1
