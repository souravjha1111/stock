from django.urls import path
from .views import urlshortner_home,urlshortner_request_view

urlpatterns = [
    path('',urlshortner_home.as_view(),name = "urlshortner_home"),
    path('<shortcode>/', urlshortner_request_view.as_view(), name = "urlshortner_request_view"),

]
    
    
