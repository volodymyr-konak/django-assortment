
from django.http import HttpResponse, HttpRequest
from django.views.generic import (
    ListView,
    UpdateView,
    DetailView
)
from django.shortcuts import render, redirect
from django.urls import reverse


from marketplace import models
from marketplace import forms


def index(request):
    return HttpResponse("Hello, you're in marketplace")


class CategoryListView(ListView):
    model = models.Category

    def get_queryset(self):
        f = forms.CategorySearchForm(self.request.GET)
        f.is_valid()
        not_empty_params_dict = dict(filter(lambda kv: kv[1] != '', f.cleaned_data.items()))

        return self.model.objects.filter(
            **not_empty_params_dict
        )

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = forms.CategorySearchForm(self.request.GET)
        return context


class AttributeListView(ListView):
    model = models.Attribute

    def get_queryset(self):
        f = forms.AttributeSearchForm(self.request.GET)
        f.is_valid()
        not_empty_params_dict = dict(filter(lambda kv: kv[1] != '', f.cleaned_data.items()))

        if self.kwargs.get("required") == "required":
            is_required = True
        else:
            is_required = False
        return self.model.objects.filter(
            category__pk=self.kwargs["categoryId"],
            required=is_required,
            **not_empty_params_dict,
        )

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = forms.AttributeSearchForm(self.request.GET)
        return context


class AttributeValueListView(ListView):
    model = models.AttributeValue

    def get_queryset(self):
        f = forms.AttributeValueSearchForm(self.request.GET)
        f.is_valid()
        not_empty_params_dict = dict(filter(lambda kv: kv[1] != '', f.cleaned_data.items()))

        return self.model.objects.filter(
            attribute__pk=self.kwargs["attributeId"],
            **not_empty_params_dict,
        )

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = forms.AttributeValueSearchForm(self.request.GET)
        return context


def edit_category(request: HttpRequest, categoryId):
    if request.method == "POST":
        form = forms.CategoryForm(
            request.POST,
            instance=models.Category.objects.get(pk=categoryId)
        )
        if form.is_valid():
            form.save()
            return redirect("categories_list")
    else:
        form = forms.CategoryForm(instance=models.Category.objects.get(pk=categoryId))
    return render(request, "marketplace/edit_category.html", {"form": form})


def edit_attribute(request: HttpRequest, attributeId):
    model_instance = models.Attribute.objects.get(pk=attributeId)
    if request.method == "POST":
        form = forms.AttributeForm(
            request.POST,
            instance=model_instance
        )
        if form.is_valid():
            form.save()
            return redirect(reverse("attributes_list", args=(model_instance.category.id, model_instance.required)))
    else:
        form = forms.AttributeForm(instance=model_instance)
    return render(request, "marketplace/edit_attribute.html", {"form": form})


def edit_attribute_value(request: HttpRequest, attributeValueId):
    model_instance = models.AttributeValue.objects.get(pk=attributeValueId)
    if request.method == "POST":
        form = forms.AttributeValueForm(
            request.POST,
            instance=model_instance
        )
        if form.is_valid():
            form.save()
            return redirect(reverse("attribute_values_list", args=(model_instance.attribute.id,)))
    else:
        form = forms.AttributeValueForm(instance=model_instance)
    return render(request, "marketplace/edit_attribute_value.html", {"form": form})


def export_xls_config_view(request):
    import json
    from django.core import serializers
    from marketplace.utils import save_excel
    if request.method == "POST":
        category_form = forms.CategorySearchForm(request.POST, prefix="category")
        attribute_form = forms.AttributeSearchForm(request.POST, prefix="attribute")
        attribute_values_form = forms.AttributeValueSearchForm(request.POST, prefix="attribute_value")
        columns_config_form = forms.XlsColumnsFormSet(request.POST)
        if columns_config_form.is_valid() \
                and category_form.is_valid()\
                and attribute_form.is_valid()\
                and attribute_values_form.is_valid():
            # not_empty_params_dict = dict(filter(lambda kv: kv[1] != '', category_form.cleaned_data.items()))
            active_columns = [column_name
                              for column_name, column_status in columns_config_form.forms[0].cleaned_data.items()
                              if column_status]

            with open("/Users/volodymyr/dev/assortment/dump.json", "w") as file:
                result = models.query_db(category_form.cleaned_data, active_columns)
                save_excel(result, included_header=active_columns)
                # json.dump([v for v in result], file)

    return render(request, 'marketplace/export_xls.html',
                  {
                      "category_form": forms.CategorySearchForm(prefix="category"),
                      "attribute_form": forms.AttributeSearchForm(prefix="attribute"),
                      "attribute_values_form": forms.AttributeValueSearchForm(prefix="attribute_value"),

                      "columns_config_form": forms.XlsColumnsFormSet()
                  }
                  )
