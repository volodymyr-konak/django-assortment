from django.core.management.base import BaseCommand, CommandError

from marketplace.models import Category, Attribute, AttributeValue

import json
import time


class Command(BaseCommand):
    def handle(self, *args, **options):
        start_time = time.time()

        # json_file_path = "/Users/volodymyr/dev/assortment/canonical.json"
        json_file_path = "/Users/volodymyr/Downloads/Telegram Desktop/item_types_with_attributes_and_values.json"
        with open(json_file_path) as file:
            data_tree = json.load(file)
            for category in data_tree:
                reqAttrs = category.get("requiredAttributes", [])
                del category["requiredAttributes"]
                optAttrs = category.get("optionalAttributes", [])
                del category["optionalAttributes"]
                this_cat = Category(**category)
                this_cat.save()

                for attr in reqAttrs:
                    values = attr.get("attributeValues", [])
                    del attr["attributeValues"]
                    del attr["attributeLevel"]
                    this_attr = Attribute(**attr)
                    this_attr.category = this_cat
                    this_attr.required = True
                    this_attr.save()
                    for attr_val in values:
                        this_val = AttributeValue(**attr_val)
                        this_val.attribute = this_attr
                        this_val.save()

                for attr in optAttrs:
                    values = attr.get("attributeValues", [])
                    del attr["attributeValues"]
                    del attr["attributeLevel"]
                    this_attr = Attribute(**attr)
                    this_attr.category = this_cat
                    this_attr.required = False
                    this_attr.save()
                    for attr_val in values:
                        this_val = AttributeValue(**attr_val)
                        this_val.attribute = this_attr
                        this_val.save()



        print("FINISHED IN " + str(time.time() - start_time) + " seconds")

        return json.dumps({"message": "Successfully loaded initial data"})
