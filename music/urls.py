# from django.conf import settings  
# from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'music'

urlpatterns = [
    path('', views.main, name='main'),
    path('add/', views.add, name='add'),
    path('home/', views.index, name='home'),
    # path('vocab/', views.vocab, name='vocab')
]