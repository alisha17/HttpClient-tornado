from django.shortcuts import render, render_to_response
from .forms import ImageUploadForm,DeleteImageForm
from .models import ExampleModel
from django.http import *
import os

#for saving the file in the folder
def handle_uploaded_file(f,full_filename):
    with open(full_filename, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def upload_pic(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        # BASE_PATH = '/home/alisha/mydjango/HelloWorld/ImageGallery/static'
        # f = request.FILES.get('image')
        if form.is_valid():
            # SAVING THE FILE IN THE FOLDER
            # folder = request.path.replace("/", "_")
            # uploaded_filename = request.FILES['image'].name
            # try:
            #     os.mkdir(os.path.join(BASE_PATH, folder))
            # except:
            #     pass
            # full_filename = os.path.join(BASE_PATH, folder, uploaded_filename)
            # handle_uploaded_file(f,full_filename)
            m = ExampleModel(model_pic=request.FILES['image'])
            m.save()
            print m.model_pic
            print m.id
            return HttpResponse('image upload success')
        else:
            form = ImageUploadForm()
    else:
        form = ImageUploadForm()
        return render(request, 'index.html')   

def delete_pic(request):
    print request.method
    if request.method == 'POST':
        form = DeleteImageForm(request.POST)
        print form
        if form.is_valid():
            print "here inside"
            image_id = form.cleaned_data['image_id']
            print image_id
            ExampleModel.objects.get(id = image_id).delete()
            return HttpResponse('image delete success')
        else:
            print "form is invalid"
            form = DeleteImageForm()
    else:
        print "inside delete"
        form = DeleteImageForm()
        return render(request, 'delete.html')  

def show_pic(request): 
    img = list() 
    if request.method == 'POST':
        for item in ExampleModel.objects.all():
            img.append(item.model_pic)
        return render_to_response("list.html", {"img": img})      
    else:
        return render(request,'showall.html')  




