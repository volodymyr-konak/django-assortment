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
    ...

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

     # super(XlsColumnsForm, self).__init__(*args, attrs=zip(field_names, field_names), **kwargs)
    # categoryId = fields.BooleanField(initial=True, required=False)
    # categoryName = fields.BooleanField(initial=True, required=False)
    # orgId = fields.BooleanField(initial=True, required=False)
    # orgName = fields.BooleanField(initial=True, required=False)
    # assortCategoryName = fields.BooleanField(initial=True, required=False)
    # assortCategoryRSXKey = fields.BooleanField(initial=True, required=False)
    # catConversionPlace = fields.BooleanField(initial=True, required=False)
    # catAddedToAssortment = fields.BooleanField(initial=True, required=False)
    # catIsActive = fields.BooleanField(initial=True, required=False)
    # catLastModified = fields.BooleanField(initial=True, required=False)
    # catNote = fields.BooleanField(initial=True, required=False)
    #
    # attributeName = fields.BooleanField(initial=True, required=False)
    # attributeId = fields.BooleanField(initial=True, required=False)
    # attributeDescription = fields.BooleanField(initial=True, required=False)
    # assortAttributeName = fields.BooleanField(initial=True, required=False)
    # assortAttributeRSXKey = fields.BooleanField(initial=True, required=False)
    # attrConversionPlace = fields.BooleanField(initial=True, required=False)
    # dataType = fields.BooleanField(initial=True, required=False)
    # minLength = fields.BooleanField(initial=True, required=False)
    # maxLength = fields.BooleanField(initial=True, required=False)
    # attrAddedToAssortment = fields.BooleanField(initial=True, required=False)
    # attrIsActive = fields.BooleanField(initial=True, required=False)
    # attrLastModified = fields.BooleanField(initial=True, required=False)
    # attrNote = fields.BooleanField(initial=True, required=False)
    #
    # valueName = fields.BooleanField(initial=True, required=False)
    # valueId = fields.BooleanField(initial=True, required=False)
    # assortValueName = fields.BooleanField(initial=True, required=False)
    # assortValueRSXKey = fields.BooleanField(initial=True, required=False)
    # valConversionPlace = fields.BooleanField(initial=True, required=False)
    # valLastModified = fields.BooleanField(initial=True, required=False)
    # valAddedToAssortment = fields.BooleanField(initial=True, required=False)
    # valIsActive = fields.BooleanField(initial=True, required=False)
    # valNote = fields.BooleanField(initial=True, required=False)
