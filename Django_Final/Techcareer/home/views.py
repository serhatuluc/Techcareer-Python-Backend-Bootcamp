from django.shortcuts import render
from .models import Bootcamp,Student,Contact
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request,'home.html')

def show(request):
    #Eklenmiş bootcampler 'bootcamps' html'inde gösterilecek. Bundan dolayı objects.all kullanılarak html'e gönderildi
    bootcamps = Bootcamp.objects.all()
    context = {'bootcamps':bootcamps}
    return render(request,'bootcamps.html',context)

def register(request):
    bootcamps = Bootcamp.objects.all()
    context = {'bootcamps': bootcamps}
    if request.method == 'POST':
        #Değişkenler alınarak başvuru formu kaydı yapıldı.
        student = Student()
        name=request.POST.get('name')
        surname=request.POST.get('surname')
        age=request.POST.get('birthdate')
        email=request.POST.get('email')
        school=request.POST.get('school')
        github=request.POST.get('github')
        linkedn=request.POST.get('linkedn')
        definition=request.POST.get('definition')
        bootcamp=request.POST.get('bootcamp')


        student.name = name
        student.surname = surname
        student.birthdate = age
        student.email = email
        student.school = school
        student.github = github
        student.linkedn = linkedn
        student.definition = definition
        student.bootcamp = bootcamp
        student.save()
    else:
        return render(request, "application.html",context)
    return render(request,"application.html",context)

def contact(request):
    if request.method == 'POST':
        form = Contact()
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        form.name = name
        form.email = email
        form.message = message
        form.save()
        #Measj alıındıktan sonra HttpResponse döndürüldü
        return HttpResponse("Thanks for contacting")
    return render(request,"contact.html")