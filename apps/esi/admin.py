from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from apps.esi.models.category import Category
from apps.esi.models.group import Group
from apps.esi.models.type import Type, TypeAttribute
from apps.esi.models.attribute import Attribute
from apps.esi.models.market import MarketGroup, MarketGroupType


@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_name', 'attribute_id' )


class TypeAttributeAdminInline(admin.TabularInline):
    model = TypeAttribute
    raw_id_fields = ('attribute', )
    extra = 0


class MarketGroupTypeInline(admin.TabularInline):
    model = MarketGroupType
    raw_id_fields = ('type', )
    extra = 0


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_id', 'name', )


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('group_id', 'category', 'name', )
    list_filter = ('category__name', )


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('type_id', 'group__category', 'group', 'name', )
    search_fields = ('group__category__name', 'group__name', 'name', )
    list_filter = ('group__category__name', 'group__name', )
    raw_id_fields = ('group', )
    inlines = [TypeAttributeAdminInline, ]


@admin.register(MarketGroup)
class MarketGroupAdmin(admin.ModelAdmin):
    search_fields = ('name', 'market_group_id', 'parent_group_id', )
    list_display = ('name', 'parent', )
    inlines = [MarketGroupTypeInline, ]

    @admin.display(description=_('Parent'))
    def parent(self, obj):
        p_name = '-'
        if obj.parent_group_id != 0:
            p_name = MarketGroup.objects.get(market_group_id=obj.parent_group_id).name
        return p_name


@admin.register(MarketGroupType)
class MarketGroupTypeAdmin(admin.ModelAdmin):
    raw_id_fields = ('market_group', 'type', )
