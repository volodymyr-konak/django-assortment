from datetime import datetime

from django.db import models
import uuid

from marketplace.utils import execute_query


class Category(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    # id = models.AutoField(primary_key=True, editable=False)

    categoryId = models.CharField(max_length=200, blank=True)
    categoryName = models.CharField(max_length=200, blank=True)
    orgId = models.CharField(max_length=200, blank=True)
    orgName = models.CharField("Org Name", max_length=200, blank=True)
    assortCategoryName = models.CharField(max_length=200, blank=True)
    assortCategoryRSXKey = models.CharField(max_length=200, blank=True)
    catConversionPlace = models.CharField(max_length=200, blank=True)
    catAddedToAssortment = models.BooleanField("Added to system?", blank=True)
    catIsActive = models.BooleanField("Is active?", blank=True, default=True)
    # catLastModified = models.DateTimeField("Last Modified", default=datetime.now, blank=True)
    catLastModified = models.CharField(max_length=200, blank=True)
    catNote = models.CharField("Note", max_length=200, blank=True)


class Attribute(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    # id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    # id = models.AutoField(primary_key=True, editable=False)

    required = models.BooleanField(editable=False)

    attributeName = models.CharField(max_length=200, blank=True)
    attributeId = models.CharField(max_length=200, blank=True)
    attributeDescription = models.CharField(max_length=200, blank=True)
    assortAttributeName = models.CharField(max_length=200, blank=True)
    assortAttributeRSXKey = models.CharField(max_length=200, blank=True)
    attrConversionPlace = models.CharField(max_length=200, blank=True)
    dataType = models.CharField(max_length=200, blank=True)
    minLength = models.CharField(max_length=200, null=True, blank=True)
    maxLength = models.CharField(max_length=200, null=True, blank=True)
    attrAddedToAssortment = models.BooleanField(blank=True)
    attrIsActive = models.BooleanField(default=True, blank=True)
    # attrLastModified = models.DateTimeField("Last Modified", default=datetime.now, blank=True)
    attrLastModified = models.CharField(max_length=200, blank=True)
    attrNote = models.CharField(max_length=200, blank=True)


class AttributeValue(models.Model):
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)

    # id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    # id = models.AutoField(primary_key=True, editable=False)

    valueName = models.CharField(max_length=200, blank=True)
    valueId = models.CharField(max_length=200, blank=True)
    assortValueName = models.CharField(max_length=200, blank=True)
    assortValueRSXKey = models.CharField(max_length=200, blank=True)
    valConversionPlace = models.CharField(max_length=200, blank=True)
    # valLastModified = models.DateTimeField("Last Modified", default=datetime.now, blank=True)
    valLastModified = models.CharField(max_length=200, blank=True)
    valAddedToAssortment = models.BooleanField(blank=True)
    valIsActive = models.BooleanField(default=True, blank=True)
    valNote = models.CharField(max_length=200, blank=True)


def query_db(search_values: dict, columns_to_select: list):
    print("search clauses")
    print(search_values)
    print("active_columns")
    print(columns_to_select)
    search_clauses = {'categoryId': 'Printer Paper', 'catAddedToAssortment': False, 'catIsActive': True}
    search_clauses = {'valueName': '100% Recycled Paper'}
    active_columns = ['categoryId', 'valueName']
    active_columns = ['valueId', 'valueName', 'attribute__attributeName']

    columns = ", ".join(columns_to_select)
    if not columns:
        columns = "*"

    def to_sql(value):
        if isinstance(value, bool):
            return f"{int(value)}"
        if isinstance(value, str):
            return f"'{value}'"
        return value

    where_clauses = " AND ".join([
        f"{key} = {to_sql(val)}"
        for key, val in search_values.items()
        if val != ''
    ])
    if where_clauses:
        where_clauses = f" WHERE {where_clauses}"
    print("where_clauses")
    print(where_clauses)

    query = f"""
    SELECT {columns} 
    FROM marketplace_category as category
     JOIN marketplace_attribute as attribute 
     ON attribute.category_id = category.id 
     JOIN marketplace_attributevalue as attribute_value 
     ON attribute.id = attribute_value.attribute_id 
    {where_clauses}
    """
    print(query)
    result = execute_query(query)
    return result
