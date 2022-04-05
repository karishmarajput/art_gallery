from dataclasses import field
from django import forms
from .models import Image
from .models import Category

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        print(model)
        fields = "__all__"

class uploadcategory(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"