
from django.contrib import admin
from django.urls import path

from Display_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add-two/',add_number, name='add_two'),
]
