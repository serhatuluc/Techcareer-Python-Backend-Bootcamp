from django.urls import path
from . import views

#URL patternlar oluşturuldu. Bootcamps sayfasından başvuru sayfasına geçiş yapılabilir
urlpatterns = [
    path('', views.index,name='index'),
    path('bootcamps/application/', views.register,name='register'),
    path('bootcamps/', views.show,name='show'),
    path('contact/',views.contact,name='contact')
]
