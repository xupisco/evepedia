from esi_client.api.universe_api import UniverseApi
from esi_client.api.dogma_api import DogmaApi

from apps.esi.models.type import Type


def load_type_from_esi(type_id):
    uni = UniverseApi()
    dogma = DogmaApi()
    local_type = Type.objects.get(type_id=type_id)
    esi_type = uni.get_universe_types_type_id(type_id)

    local_type.name = esi_type.name
    local_type.description = esi_type.description
    local_type.graphic_id = esi_type.graphic_id
    local_type.market_group_id = esi_type.market_group_id if 'market_group_id' in esi_type else 0
    local_type.mass = esi_type.mass
    local_type.packaged_volume = esi_type.packaged_volume
    local_type.portion_size = esi_type.portion_size
    local_type.published = esi_type.published
    local_type.radius = esi_type.radius
    local_type.volume = esi_type.volume
    local_type.save()

    for attr in esi_type.dogma_attributes:
        attribute, created = Attribute.objects.get_or_create(attribute_id=attr.attribute_id)
        esi_attr = dogma.get_dogma_attributes_attribute_id(attr.attribute_id)
        attribute.default_value = esi_attr.default_value
        attribute.description = esi_attr.description
        attribute.name = esi_attr.name
        attribute.display_name = esi_attr.display_name
        attribute.high_is_good = esi_attr.high_is_good if 'high_is_good' in esi_attr else False
        attribute.icon_id = esi_attr.icon_id if 'icon_id' in esi_attr else 0
        attribute.published = esi_attr.published if 'published' in esi_attr else True
        attribute.unit_id = esi_attr.unit_id if 'unit_id' in esi_attr else 0
        attribute.save()

        type_attr, _ = TypeAttribute.objects.get_or_create(
            type=local_type,
            attribute=attribute
        )
        type_attr.value = attr.value
        type_attr.save()
