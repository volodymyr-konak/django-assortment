from datetime import datetime

from django.db import models
import uuid


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    categoryId = models.CharField(max_length=200)
    categoryName = models.CharField(max_length=200)
    orgId = models.CharField(max_length=200)
    orgName = models.CharField("Org Name", max_length=200)
    assortCategoryName = models.CharField(max_length=200)
    assortCategoryRSXKey = models.CharField(max_length=200)
    catConversionPlace = models.CharField(max_length=200)
    catAddedToAssortment = models.BooleanField("Added to system?")
    catIsActive = models.BooleanField("Is active?")
    # catLastModified = models.DateTimeField("Last Modified", default=datetime.now, blank=True)
    catLastModified = models.CharField(max_length=200)
    catNote = models.CharField("Note", max_length=200)


class Attribute(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    required = models.BooleanField(editable=False)

    attributeName = models.CharField(max_length=200)
    attributeId = models.CharField(max_length=200)
    attributeDescription = models.CharField(max_length=200)
    assortAttributeName = models.CharField(max_length=200)
    assortAttributeRSXKey = models.CharField(max_length=200)
    attrConversionPlace = models.CharField(max_length=200)
    dataType = models.CharField(max_length=200)
    minLength = models.CharField(max_length=200, null=True)
    maxLength = models.CharField(max_length=200, null=True)
    attrAddedToAssortment = models.BooleanField()
    attrIsActive = models.BooleanField()
    # attrLastModified = models.DateTimeField("Last Modified", default=datetime.now, blank=True)
    attrLastModified = models.CharField(max_length=200)
    attrNote = models.CharField(max_length=200)


class AttributeValue(models.Model):
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    valueName = models.CharField(max_length=200)
    valueId = models.CharField(max_length=200)
    assortValueName = models.CharField(max_length=200)
    assortValueRSXKey = models.CharField(max_length=200)
    valConversionPlace = models.CharField(max_length=200)
    # valLastModified = models.DateTimeField("Last Modified", default=datetime.now, blank=True)
    valLastModified = models.CharField(max_length=200)
    valAddedToAssortment = models.BooleanField()
    valIsActive = models.BooleanField()
    valNote = models.CharField(max_length=200)

