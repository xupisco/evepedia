from django.contrib import admin

from apps.esi.models.category import Category
from apps.esi.models.group import Group
from apps.esi.models.type import Type, TypeAttribute
from apps.esi.models.attribute import Attribute


@admin.register(Attribute)
class AttributeAdmin(admin.ModelAdmin):
    list_display = ('name', 'display_name', 'attribute_id' )


class TypeAttributeAdminInline(admin.TabularInline):
    model = TypeAttribute
    raw_id_fields = ('attribute', )
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
    inlines = [TypeAttributeAdminInline, ]
