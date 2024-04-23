import time
import ujson
import pathlib
import zipfile

from django.core.management.base import BaseCommand, CommandError
from marketplace.models import Category, Attribute, AttributeValue


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("data_file", type=str)

    def handle(self, *args, **options):
        start_time = time.time()
        file_path = options["data_file"]
        # if not pathlib.Path(file_path).exists():
        #     raise FileNotFoundError(f"File does not exist: `{file_path}`")

        # # TODO truncate
        # with zipfile.ZipFile(file_path) as file:
        #     print("Reading input file...")
        #     data = ujson.load(file)
        #     print("Importing to local DB...")
        #     create_db_instances(data)
        #     # run_insert(data)
        from django.core.serializers import serialize
        from django.core.serializers.json import DjangoJSONEncoder
        from django.forms.models import model_to_dict

        with open("/Users/volodymyr/Downloads/canonical.json", "w") as file:
        # with zipfile.ZipFile(file_path, "a") as file:
            data = []
            categories = Category.objects.all()
            for category in categories:
                category_dict = model_to_dict(category)
                category_dict["requiredAttributes"] = [
                    model_to_dict(attribute)
                    for attribute in category.attribute_set.filter(required=True)
                ]
                category_dict["requiredAttributes"] = []
                category_dict["optionalAttributes"] = []
                for attribute in category.attribute_set.filter(required=True):
                    attr_vals = attribute.attributevalue_set.all()
                    attribute_dict = model_to_dict(attribute)
                    # del attribute_dict["required"]
                    attribute_dict["attributeValues"] = [
                        model_to_dict(aval)
                        for aval in attr_vals
                    ]
                    category_dict["requiredAttributes"].append(attribute_dict)
                for attribute in category.attribute_set.filter(required=False):
                    attr_vals = attribute.attributevalue_set.all()
                    attribute_dict = model_to_dict(attribute)
                    # del attribute_dict["required"]
                    attribute_dict["attributeValues"] = [
                        model_to_dict(aval)
                        for aval in attr_vals
                    ]
                    category_dict["optionalAttributes"].append(attribute_dict)


                data.append(category_dict)
                # for attribute in category.attribute_set.all():
                #     print(attribute.attributeId)
            # print(data)
            # file.writestr("canonical.json", ujson.dumps(data))
            ujson.dump(data, file)

        print("FINISHED IN " + str(time.time() - start_time) + " seconds")

        return ujson.dumps({"message": "Successfully dumped data"})
