from projects import views as project_view
from django.urls import path
from . import views

urlpatterns = [
    path('titanic/', project_view.titanic, name='titanic'),
    path('ipl/', project_view.ipl, name='ipl'),
    path('stock/', project_view.stock, name='stock'),
    path('url_shortner/', project_view.url_shortner, name='url_shortner')
]
    
    
