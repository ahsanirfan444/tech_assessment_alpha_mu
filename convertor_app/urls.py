# myproject/urls.py
from django.urls import path
from convertor_app import views

urlpatterns = [
    path('word-to-number/', views.ConvertToNumberView.as_view(), name='convert_to_number'),
    path('number-to-word/', views.ConvertToWordView.as_view(), name='convert_to_word'),
 
]
