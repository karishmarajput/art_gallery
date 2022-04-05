from pyexpat.errors import messages
from django.shortcuts import redirect, render
from .models import *
from django.contrib import messages


# Create your views here.
from .forms import ImageForm

def uploadforform(request):
    context ={}
  
    # create object of form
    form = ImageForm(request.POST or None, request.FILES or None)
      
    # check if form data is valid
    if form.is_valid():
        messages.success(request, 'Image added successful')
        # save the form data to model
        form.save()
  
    context['form']= form
    return render(request, "main/upload.html", context)

from .forms import uploadcategory

def uploadcategoryform(request):
    context ={}
  
    # create object of form
    forms = uploadcategory(request.POST or None, request.FILES or None)
      
    # check if form data is valid
    if forms.is_valid():
        messages.success(request, 'Category added successful')
        # save the form data to model
        forms.save()
  
    context['form']= forms
    return render(request, "main/uploadcategory.html", context)


def home(request):
    categories = Category.objects.all()

    context = {}
    context['categories'] = categories

    return render(request, 'main/index.html', context)


def upload(request):
    categories = Category.objects.all()

    context = {}
    context['categories'] = categories

    return render(request, 'main/upload.html', context)


def categoryPage(request, slug):

    category = Category.objects.get(slug=slug)
    images = Image.objects.filter(category=category).order_by('-date_created')[:6]
    for x in images:
        x.shortDescription = x.description[:130]

    context = {}
    context['images'] = images
    context['category'] = category

    return render(request, 'main/category.html', context)


def imageDetailPage(request, slug1, slug2):

    category = Category.objects.get(slug=slug1)
    image = Image.objects.get(slug=slug2)

    context = {}
    context['category'] = category
    context['image'] = image

    return render(request, 'main/image.html', context)






















###
