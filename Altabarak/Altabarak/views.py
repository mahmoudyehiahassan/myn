from django.http import HttpResponse
from django.shortcuts import render
from projects.models import HomeProject, HomeSlider, OurNews, First_Photo_Slider
from projects.models import ProjectStatistics

def home(request):
	documents = HomeProject.objects.all()
	slider = HomeSlider.objects.all()
	news = OurNews.objects.all()
	FPhoto = First_Photo_Slider.objects.all()
	Statics = ProjectStatistics.objects.all()
	return render(request, 'home.html', { 'documents': documents,
											'slider': slider,
											'news': news,
											'FPhoto': FPhoto,
											'Statics': Statics})
