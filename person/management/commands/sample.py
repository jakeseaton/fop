from django.core.management.base import BaseCommand
from dateutil.parser import parse
import pandas as pd
from person.models import Fopper
import json
from django.conf import settings

class Command(BaseCommand):
    def handle(self, *args, **options):
        LOCATION = "%s/person/sample_data/" % settings.BASE_DIR
        FILE_NAMES = ["1", "2", "3", "4", "5"]
        for file_name in FILE_NAMES:
            f = "%s%s.csv" % (LOCATION, file_name)
            df = pd.read_csv(f)
            j = json.loads(df.to_json(orient="records"))
            for fopper in j:
                fopper['requests_fop_financial_aid'] = fopper.pop('requests_aid')
                fopper['birthdate'] = parse(fopper['birthdate'])
                fopper, created = Fopper.objects.get_or_create(**fopper)
                if created:
                    print "Created Fopper", fopper
