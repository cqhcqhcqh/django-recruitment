import csv
import os
from interview.models import Candidate
from django.core.management import BaseCommand

# python manage.py import_candidates --path [file_path]
class Command(BaseCommand):
    help = '从一个csv文件中读取数据导入到数据库中'
    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)

    def handle(self, *args, **options):
        path = options['path']
        with open(path, 'rt', encoding='utf-8') as file:
            reader = csv.reader(file, dialect='excel', delimiter=',')
            for row in reader:
                candidate = Candidate.objects.create(user_name= row[0],
                                                     phone=row[1],
                                                     city = row[2],
                                                     bachelor_school = row[3],
                                                     major = row[4],
                                                     degree = row[5],
                                                     test_score_of_general_ability = row[6],
                                                     paper_score = row[7])
                print(candidate)


