from django.db import models
from jsonfield import JSONField


class Name(models.Model):

    name = JSONField(max_length=254)
    number = models.CharField(max_length=13)

    class Meta:
        db_table = 'names'

    def __str__(self):
        return self.name

    def get_names(self):
        return ', '.join(self.names.all().values_list('name', flat=True))