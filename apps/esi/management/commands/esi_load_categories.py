from django.core.management.base import BaseCommand, CommandError

from esi_client.api.universe_api import UniverseApi

from apps.esi.models.category import Category
from apps.esi.models.group import Group
from apps.esi.models.type import Type


def load_category(api, category_id):
    esi_cat = api.get_universe_categories_category_id(category_id)
    local_cat, _ = Category.objects.get_or_create(category_id=category_id)
    local_cat.published = esi_cat.published
    local_cat.name = esi_cat.name
    local_cat.save()

    return esi_cat, local_cat


def build_groups(api, cat, groups, fetch):
    for esi_group in groups:
        group, _ = Group.objects.get_or_create(
            category=cat,
            group_id=esi_group
        )

        if fetch: load_group(api, esi_group)


def load_group(api, group_id):
    esi_group = api.get_universe_groups_group_id(group_id)
    category = Category.objects.get(category_id=esi_group.category_id)

    group = Group.objects.get(group_id=esi_group.group_id)
    group.name = esi_group.name
    group.published = esi_group.published
    group.save()

    for t in esi_group.types:
        type, _ = Type.objects.get_or_create(
            group=group,
            type_id=t
        )


class Command(BaseCommand):
    help = 'Load ESI categories'

    def add_arguments(self, parser):
        parser.add_argument(
            '--id',
            type=int,
            default='0',
            help='Category ID to parse, if especified groups will be loaded.'
        )
        parser.add_argument(
            '--fetch-group',
            type=bool,
            default=False,
            help='Should also load group data?'
        )

    def handle(self, *args, **options):
        uni = UniverseApi()
        total = 0
        category_id = options['id']
        fetch_group = options['fetch_group']

        if category_id == 0:
            categories = uni.get_universe_categories()

            for category in categories:
                esi_cat, local_cat = load_category(uni, category)
                build_groups(uni, local_cat, esi_cat.groups, fetch_group)
                total += 1
        else:
            esi_cat, local_cat = load_category(uni, category_id)
            build_groups(uni, local_cat, esi_cat.groups, fetch_group)
            total = 1

        self.stdout.write(
            self.style.SUCCESS(f'Imported {total} categories...')
        )
