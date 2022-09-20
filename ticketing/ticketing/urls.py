from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='idnex'),
    path('submit', views.submit,name='submit'),
    path('tickets', views.tickets, name='tickets'),
]
