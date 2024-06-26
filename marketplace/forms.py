from django.forms import (
    ModelForm,
    forms,
    fields,
    TextInput,
    BaseFormSet,
    formset_factory,
)
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
        }


class AttributeSearchForm(ModelForm):
    class Meta:
        model = Attribute
        exclude = ["id", "category"]
        widgets = {
        }


class AttributeValueSearchForm(ModelForm):
    class Meta:
        model = AttributeValue
        exclude = ["id", "attribute"]
        widgets = {
        }


class XlsColumnsForm(BaseFormSet):
    def add_fields(self, form, index):
        super().add_fields(form, index)
        bool_field = lambda: fields.BooleanField(label=field.label, required=False)
        for field_name, field in CategoryForm().fields.items():
            form.fields[f"category.{field_name}"] = bool_field()
        for field_name, field in AttributeForm().fields.items():
            form.fields[f"attribute.{field_name}"] = bool_field()
        for field_name, field in AttributeValueForm().fields.items():
            form.fields[f"attribute_value.{field_name}"] = bool_field()


XlsColumnsFormSet = formset_factory(forms.Form, formset=XlsColumnsForm)
