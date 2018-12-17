from django.contrib import admin
from .models import senddata, ContactUs, Document,  HomeProject, industry, banks
from .models import	HomeSlider, OurNews, First_Photo_Slider, ProjectStatistics, Hospital
from .models import Public_build, Colleges_And_Institutes, private_school, public_schools
from .models import Residential_bulding, Compound, all_Moll, Hotel
# Register your models here.

class senddataadmin(admin.ModelAdmin):
	list_display = ["__str__", "Edu_Qualification", "years_of_Experience"]
	class Meta:
		model = senddata

class DocumentAdmin(admin.ModelAdmin):
    list_display = ['description', 'empemail', 'phonenumber','uploaded_at']
    class Meta:
    	model = Document

class HomeProjectAdmin(admin.ModelAdmin):
	lsit_display = ['Title', 'uploaded_at']
	class Meta:
		model = HomeProject

class ContactUsAdmin(admin.ModelAdmin):
	list_display = ['fullname', 'e_mail', 'text', 'pub_date']
	class Meta:
		model = ContactUs


admin.site.register(senddata, senddataadmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
admin.site.register(HomeProject, HomeProjectAdmin)
admin.site.register(ProjectStatistics)
admin.site.register(industry)
admin.site.register(banks)
admin.site.register(HomeSlider)
admin.site.register(Public_build)
admin.site.register(OurNews)
admin.site.register(Colleges_And_Institutes)
admin.site.register(First_Photo_Slider)
admin.site.register(private_school)
admin.site.register(public_schools)
admin.site.register(Hospital)
admin.site.register(Residential_bulding)
admin.site.register(Compound)
admin.site.register(all_Moll)
admin.site.register(Hotel)
