from django.urls import path
from . import views


urlpatterns = [
path('',views.home, name='home'),
path('category/<slug:slug>', views.categoryPage, name='image-category'),
path('category/<slug:slug1>/<slug:slug2>', views.imageDetailPage, name='image-detail'),
path('upload', views.uploadforform, name='upload'),
path('uploadcategory', views.uploadcategoryform, name='uploadcategory'),

]
