from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

from . import models

import random, string

# Create your views here.

def home(request):
    images = models.Image.objects.all()

    return render(request, 'shareimageapp/home.html', locals())

def upload(request):

    if request.method == "POST":
        # Check the random file name is unique
        file_name = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(8))
        while True:
            try:
                exist = models.Image.objects.get(name=file_name)
                file_name = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(8))
            except:
                break
        img_name = file_name + "." + request.FILES["img"].name.split(".")[-1]
        img_path = 'shareimageapp/' + img_name
        img_name = img_name.split(".")[0]
        img_file = request.FILES["img"]
        img_upload = models.Image.objects.create(name=img_name)
        img_upload.img = FileSystemStorage().save(img_path, img_file)
        img_upload.save()

        return redirect(home)

    return render(request, 'shareimageapp/upload.html', locals())
