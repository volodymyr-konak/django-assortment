from django.shortcuts import render

from django.http import HttpResponse, HttpRequest
from django.views.generic import (
    ListView,
    UpdateView,
    DetailView
)
from django.shortcuts import render


from marketplace import models
from marketplace import forms


def index(request):
    return HttpResponse("Hello, you're in marketplace")


class CategoryListView(ListView):
    model = models.Category


class AttributeListView(ListView):
    model = models.Attribute

    def get_queryset(self):
        print(self.kwargs)
        is_required = None
        if self.kwargs.get("required") == "required":
            is_required = True
        if self.kwargs.get("required") == "required":
            is_required = False
        if is_required is None:
            return self.model.objects.filter(category__pk=self.kwargs["categoryId"])
        else:
            return self.model.objects.filter(category__pk=self.kwargs["categoryId"], required=is_required)


class AttributeValueListView(ListView):
    model = models.AttributeValue

    def get_queryset(self):
        return self.model.objects.filter(
            attribute__pk=self.kwargs["attributeId"],
            # category__pk=self.kwargs["categoryId"]
        )


def edit_category(request: HttpRequest, categoryId):
    if request.method == "POST":
        form = forms.CategoryForm(
            request.POST,
            instance=models.Category.objects.get(pk=categoryId)
        )
        if form.is_valid():
            form.save()
    else:
        form = forms.CategoryForm(instance=models.Category.objects.get(pk=categoryId))
    return render(request, "marketplace/edit_category.html", {"form": form})


def edit_attribute(request: HttpRequest, attributeId):
    if request.method == "POST":
        form = forms.AttributeForm(
            request.POST,
            instance=models.Attribute.objects.get(pk=attributeId)
        )
        if form.is_valid():
            form.save()
    else:
        form = forms.AttributeForm(instance=models.Attribute.objects.get(pk=attributeId))
    return render(request, "marketplace/edit_attribute.html", {"form": form})


def edit_attribute_value(request: HttpRequest, attributeValueId):
    if request.method == "POST":
        form = forms.CategoryForm(
            request.POST,
            instance=models.Category.objects.get(pk=attributeValueId)
        )
        if form.is_valid():
            form.save()
    else:
        form = forms.CategoryForm(instance=models.Category.objects.get(pk=attributeValueId))
    return render(request, "marketplace/edit_attribute_value.html", {"form": form})

