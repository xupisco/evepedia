from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    class Meta:
        ordering = ('category_id', )

    category_id = models.IntegerField(_('Category ID'), blank=False)
    name = models.CharField(_('Name'), max_length=128, blank=True)
    published = models.BooleanField(_('Published'), default=True)

    def __str__(self):
        return self.name
