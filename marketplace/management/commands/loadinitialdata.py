from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from marketplace.models import Category, Attribute, AttributeValue

import ujson
import time


# @transaction.atomic
def create_and_save_attributes_for_category(category_data, category_instance):
    # with transaction.atomic():
    for [is_required, attributes] in [
        [True, category_data.get("requiredAttributes", [])],
        [False, category_data.get("optionalAttributes", [])]
    ]:
        for attr in attributes:
            values = attr.get("attributeValues", [])
            del attr["attributeValues"]
            del attr["attributeLevel"]
            this_attr = Attribute(**attr)
            this_attr.category = category_instance
            this_attr.required = is_required
            this_attr.save()
            for attr_val in values:
                this_val = AttributeValue(**attr_val)
                this_val.attribute = this_attr
                this_val.save()
    return 0


class Command(BaseCommand):
    def handle(self, *args, **options):
        start_time = time.time()

        # json_file_path = "/Users/volodymyr/dev/assortment/canonical.json"
        json_file_path = "/Users/volodymyr/Downloads/Telegram Desktop/item_types_with_attributes_and_values.json"
        with open(json_file_path) as file:
            data_tree = ujson.load(file)
            for category in data_tree:
                reqAttrs = category.get("requiredAttributes", [])
                del category["requiredAttributes"]
                optAttrs = category.get("optionalAttributes", [])
                del category["optionalAttributes"]
                this_cat = Category(**category)
                this_cat.save()

                # create_and_save_attributes_for_category(category, this_cat)

                with transaction.atomic():
                    for [is_required, attributes] in [
                        [True, reqAttrs],
                        [False, optAttrs]
                    ]:
                        for attr in attributes:
                            values = attr.get("attributeValues", [])
                            del attr["attributeValues"]
                            del attr["attributeLevel"]
                            this_attr = Attribute(**attr)
                            this_attr.category = this_cat
                            this_attr.required = is_required
                            this_attr.save()
                            for attr_val in values:
                                this_val = AttributeValue(**attr_val)
                                this_val.attribute = this_attr
                                this_val.save()

        print("FINISHED IN " + str(time.time() - start_time) + " seconds")

        return ujson.dumps({"message": "Successfully loaded initial data"})
