# popcorn/management/commands/import_csv.py
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('csv_file', nargs='+', type=str)

    def handle(self, *args, **options):
        for csf_file in options['csv_file']:
            dataReader = csv.reader(open(csv_file), delimiter=';')
            for row in dataReader:
                emp = Post()
                self.stdout.write(
                    'Created employee {} {}'.format(emp.first_name, emp.last_name)
                )
