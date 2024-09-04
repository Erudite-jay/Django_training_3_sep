from django.urls import path,include
from . import views

urlpatterns = [
    path('print-h/',views.print_hello, name="print-hello" ),
    path('p-name/',views.p_name, name="p-name" ),
    path('get-all-data/',views.get_all_data, name="get-all-data")
]
