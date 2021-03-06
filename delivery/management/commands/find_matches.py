from django.core.management.base import BaseCommand

from delivery.matching import find_matches

class Command(BaseCommand):
    help='finds matches and sends match reports'

    def handle(self, *args, **options):
        find_matches()
        self.stdout.write('Matching run')