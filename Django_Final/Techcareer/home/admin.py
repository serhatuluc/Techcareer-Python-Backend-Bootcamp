from django.contrib import admin
from .models import Bootcamp,Student,Contact
# Register your models here.

#Modeller admine bağlandı. Bu şekilde Django admin sayfasında modifiye edilebilecek
admin.site.register(Bootcamp)
admin.site.register(Student)
admin.site.register(Contact)