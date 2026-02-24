
from django.contrib import admin
from django.urls import path

from mul_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mul_two/', mul_number, name='mul_two'),
]
