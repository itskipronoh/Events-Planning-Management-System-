from django.urls import path
from . import views
from django.contrib import admin

admin.site.site_header = "Event Management System Admin"
admin.site.site_title = "Event Management System Admin Portal"
admin.site.index_title = "Welcome to Event Management System "

urlpatterns = [
    path('',views.index,name='index'),
     path('about/',views.about,name='about'),
      path('gallery/',views.gallery,name='gallery'),
       path('events/',views.events,name='events'),
        path('booking/',views.booking,name='booking'),
         path('contact/',views.contact,name='contact'),
          path('feedback/', views.feedback_view, name='feedback'),
]