from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.esi.models.type import Type


class MarketGroup(models.Model):
    market_group_id = models.IntegerField(_('Market Group ID'), blank=False)
    parent_group_id = models.IntegerField(_('Market Group Parent ID'), default=0, blank=False)
    name = models.CharField(_('Name'), max_length=128)
    description = models.TextField(_('Description'))

    def get_children(self):
        return MarketGroup.objects.filter(parent_group_id=self.market_group_id).order_by('name')

    def __str__(self):
        return self.name


class MarketGroupType(models.Model):
    market_group = models.ForeignKey(MarketGroup, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)

    def __str__(self):
        return self.type.name
