from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('pdf1/',GeneratePDF.as_view(), name='pdf1'),
    path('pdf2/',GeneratePDF2.as_view(), name='pdf2'),
    path('pdf3/',GeneratePDF3.as_view(), name='pdf3'),
    path('pdf4/',GeneratePDF4.as_view(), name='pdf4'),
    path('pdf5/',GeneratePDF5.as_view(), name='pdf5'),
    path('pdf6/',GeneratePDF6.as_view(), name='pdf6'),

]
