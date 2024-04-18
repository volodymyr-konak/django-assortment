from django.forms import ModelForm, forms, fields, TextInput, CheckboxInput
from marketplace.models import (
    Category,
    Attribute,
    AttributeValue,
)


class CategoryForm(ModelForm):
    # catIsActive = fields.CharField()

    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'categoryId': TextInput(attrs={'readonly': 'readonly'}),
            'categoryName': TextInput(attrs={'readonly': 'readonly'}),
            'orgId': TextInput(attrs={'readonly': 'readonly'}),
            'orgName': TextInput(attrs={'readonly': 'readonly'}),
            'catLastModified': TextInput(attrs={'readonly': 'readonly'}),
        }


class AttributeForm(ModelForm):
    class Meta:
        model = Attribute
        fields = '__all__'
        widgets = {
            'attributeName': TextInput(attrs={'readonly': 'readonly'}),
            'attributeId': TextInput(attrs={'readonly': 'readonly'}),
            'attributeDescription': TextInput(attrs={'readonly': 'readonly'}),
            'dataType': TextInput(attrs={'readonly': 'readonly'}),
            'attrIsActive': TextInput(attrs={'readonly': 'readonly'}),
            'attrLastModified': TextInput(attrs={'readonly': 'readonly'}),
            'category': TextInput(attrs={'readonly': 'readonly'}),
        }


class AttributeValueForm(ModelForm):
    class Meta:
        model = AttributeValue
        fields = '__all__'
        widgets = {
            'attribute': TextInput(attrs={'readonly': 'readonly'}),
            'valueName': TextInput(attrs={'readonly': 'readonly'}),
            'valueId': TextInput(attrs={'readonly': 'readonly'}),
            'valLastModified': TextInput(attrs={'readonly': 'readonly'}),
            'valAddedToAssortment': TextInput(attrs={'readonly': 'readonly'}),
            # 'valNote': TextInput(attrs={'readonly': 'readonly'}),
        }


class CategorySearchForm(ModelForm):
    class Meta:
        model = Category
        exclude = ["id"]
        widgets = {
            # 'catIsActive': CheckboxInput(attrs={'checked': True}),

            # 'categoryId': TextInput(attrs={'readonly': 'readonly'}),
            # 'categoryName': TextInput(attrs={'readonly': 'readonly'}),
            # 'orgId': TextInput(attrs={'readonly': 'readonly'}),
            # 'orgName': TextInput(attrs={'readonly': 'readonly'}),
            # 'catLastModified': TextInput(attrs={'readonly': 'readonly'}),
        }

