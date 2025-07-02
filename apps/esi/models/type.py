from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.esi.models.group import Group
from apps.esi.models.attribute import Attribute


class Type(models.Model):
    class Meta:
        ordering = ('group__group_id', 'type_id', 'name', )

    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    type_id = models.IntegerField(_('Type ID'), blank=False)
    name = models.CharField(_('Name'), max_length=128, blank=True)
    description = models.TextField(_('Description'))
    graphic_id = models.IntegerField(_('Graphic ID'), default=0, blank=True)
    market_group_id = models.IntegerField(_('Market Group ID'), default=0, blank=True)
    mass = models.FloatField(_('Mass'), default=0, blank=True)
    volume = models.FloatField(_('Packaged'), default=0, blank=True)
    packaged_volume = models.FloatField(_('Packaged Volume'), default=0, blank=True)
    portion_size = models.FloatField(_('Portion Size'), default=0, blank=True)
    radius = models.FloatField(_('Radius'), default=0, blank=True)
    capacity = models.FloatField(_('Capacity'), default=0, blank=True)
    published = models.BooleanField(_('Published'), default=True)


class TypeAttribute(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    value = models.CharField(_('Value'), max_length=128, null=True)

    def __str__(self):
        return self.attribute.display_name or self.attribute.name
