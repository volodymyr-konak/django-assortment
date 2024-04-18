from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),

    path("categories", views.CategoryListView.as_view(), name="categories_list"),
    path("<categoryId>/attributes/<required>", views.AttributeListView.as_view(), name="attributes_list"),
    path("<attributeId>/attribute_values", views.AttributeValueListView.as_view(), name="attribute_values_list"),

    path("edit_category/<categoryId>", views.edit_category, name="edit_category_view"),
    path("edit_attribute/<attributeId>", views.edit_attribute, name="edit_attribute_view"),
    path("edit_attribute_value/<attributeValueId>", views.edit_attribute_value, name="edit_attribute_value_view"),

    path("export_xls", views.export_xls_config_view, name="export_xls_view"),
]
