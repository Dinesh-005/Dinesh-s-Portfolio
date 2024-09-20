from django.urls import path
from. import views

urlpatterns=[
    path('',views.home,name='home'),
    path('education/', views.education,name='education'),
    path('services/', views.services,name='services'),
    path('projects/', views.projects,name='projects'),
    path('contactform/', views.contactform,name='contactform'),
    path('contact/', views.contact,name='contact')
]