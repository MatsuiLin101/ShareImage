from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

from . import models

# Create your views here.

def home(request):
    images = models.Image.objects.all()

    return render(request, 'shareimageapp/home.html', locals())

def upload(request):

    if request.method == "POST":
        img_name = request.FILES["img"].name
        img_file = request.FILES["img"]
        img_path = 'shareimageapp/' + img_name
        img_name = img_name.split(".")[0]
        img_upload = models.Image.objects.create(name=img_name)
        img_upload.img = FileSystemStorage().save(img_path, img_file)
        img_upload.save()

        return redirect(home)

    return render(request, 'shareimageapp/upload.html', locals())
