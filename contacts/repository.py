from django.db.models import Q, Value
from django.db.models.functions import Concat

from .models import Contact


class ContactRepository:
    def __init__(self):
        self.model = Contact

    def search_by(self, term=''):
        fullname = Concat('name', Value(' '),  'surname')

        fullname_query = Q(fullname__icontains=term)
        telephone_query = Q(telephone__icontains=term)

        contacts = self.model.objects.annotate(
            fullname=fullname,
        ).filter(fullname_query | telephone_query)

        return contacts

    def order_all_by(self, field, ascending=True):
        field = field if ascending else f'-{field}'
        return self.model.objects.order_by(field)

    def get_by_id(self, id):
        return self.model.objects.get(id=id)
