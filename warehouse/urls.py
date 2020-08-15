from django.urls import path
from . import views

app_name = "werehouse"

urlpatterns = [

    path('wherehouse/category',views.category_view, name="warehouse-category"),
    path('wherehouse/stock',views.stock_view, name="warehouse-stock"),
    path('wherehouse/stock/create',views.stock_create, name="warehouse-stock-create"),

]