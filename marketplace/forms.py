from django.forms import ModelForm, forms, TextInput
from marketplace.models import (
    Category,
    Attribute,
    AttributeValue,
)


class CategoryForm(ModelForm):
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
            # 'minLength': TextInput(attrs={'readonly': 'readonly'}),
            # 'maxLength': TextInput(attrs={'readonly': 'readonly'}),
            'attrIsActive': TextInput(attrs={'readonly': 'readonly'}),
            'attrLastModified': TextInput(attrs={'readonly': 'readonly'}),
            'category': TextInput(attrs={'readonly': 'readonly'}),
        }


class AttributeValueForm(ModelForm):
    class Meta:
        model = AttributeValue
        fields = '__all__'

