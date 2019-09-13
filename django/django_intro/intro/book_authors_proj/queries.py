#! usr/bin/python3

"""This is an experimental scrypt to imput data into database."""
from apps.books_authors_app.models import *

test = Books.objects.create(title="test", desc="testy mctestface")
test.save()


test2= Books.objects.get(id=1)
print(test2.title)
