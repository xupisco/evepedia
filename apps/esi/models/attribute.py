from django.db import models
from django.utils.translation import gettext_lazy as _


class Attribute(models.Model):
    class Meta:
        ordering = ('name', )

    attribute_id = models.IntegerField(_('Attribute ID'), blank=False)
    name = models.CharField(_('Name'), max_length=128, blank=True)
    display_name = models.CharField(_('Display Name'), max_length=128, blank=True)
    default_value = models.CharField(_('Default Value'), max_length=128, default='0')
    description = models.TextField(_('Description'), blank=True)
    high_is_good = models.BooleanField(_('High is good'), default=False)
    icon_id = models.IntegerField(_('Icon ID'), blank=True, null=True)
    unit_id = models.IntegerField(_('Unit ID'), blank=True, null=True)
    published = models.BooleanField(_('Published'), default=True)

    def __str__(self):
        return self.display_name or self.name
