from django.urls import path
from .import views

app_name='projects'
urlpatterns = [
    path('hospitals/', views.projects_list, name='hospitals'),
    # our_job is def name in views and 'jobs/' is page.html
    path('our_customer/', views.our_customer, name='our_customer'),
    path('jobs/', views.our_job, name='jobs'),
    #path('testupload/', views.testupload, name='testupload'),
    path('simple/', views.simple_upload, name='simple_upload'),
    path('form/', views.model_form_upload, name='model_form_upload'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('aboutus/', views.aboucom, name='aboucom'),
    path('banks/', views.allBanks, name='banks'),
    path('Colleges&Institutes', views.institute, name='Colleges&Institutes'),
    path('Factories/', views.Factories, name='Factories'),
    path('Schools/', views.Schools, name='Schools'),
    path('Private_Schools/', views.Private_Schools, name='Private_Schools'),
    path('Residential_Projects/', views.Residential, name='Residential_Projects'),
    path('Public_buildings/', views.allbuilding, name='Public_buildings'),
    path('allCompound/', views.allCompound, name='Compound'),
    path('moll/', views.moll, name='moll'),
    path('Hotels/', views.Hotels, name='Hotels'),
]
