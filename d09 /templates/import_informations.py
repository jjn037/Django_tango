import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'd09.settings')

import django
django.setup()

from rango.models import Students


def import_stu():
    add_stu(name="Peter",
            grade="Ph.D",
            card_no=2011111111,
            sex="boy")

    add_stu(name="Li",
            grade="master",
            card_no=2012111111,
            sex="girl")

    add_stu(name="Curry",
            grade="master",
            card_no=2013111111,
            sex="boy")


def add_stu(name, grade, card_no, sex):
    s = Students.objects.get_or_create(name=name)[0]  #[0] important!!!!

    s.grade = grade
    s.sex = sex
    s.card_no = card_no
    s.save()
    return s


if __name__ == '__main__':
    print "Starting import script..."
    import_stu()