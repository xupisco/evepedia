from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.esi.models.category import Category


class Group(models.Model):
    class Meta:
        ordering = ('category__category_id', 'group_id', 'name', )

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    group_id = models.IntegerField(_('Group ID'), blank=False)
    name = models.CharField(_('Name'), max_length=128, blank=True)
    published = models.BooleanField(_('Published'), default=True)

    def __str__(self):
        return self.name
