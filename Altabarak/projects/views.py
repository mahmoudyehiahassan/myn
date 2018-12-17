from django.shortcuts import render, redirect, HttpResponseRedirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.urls import reverse
from .models import senddata, Colleges_And_Institutes, private_school, public_schools
from .models import Document, industry, HomeProject, banks, Public_build, Hotel
from .models import private_school, Hospital, Residential_bulding, Compound, all_Moll
from .forms import DocumentForm, ContactUsForm
from django.contrib import messages
from django.utils.html import format_html, html_safe

# Create your views here.
def our_customer(request):
	return render(request, 'projects/our_customers.html')

def projects_list(request):
	hosp = Hospital.objects.order_by('-add_Date')
	context = {'hosp':hosp}
	return render(request, 'projects/hospitals.html', context)

def moll(request):
	mol = all_Moll.objects.order_by('-add_Date')
	context = {'mol':mol}
	return render(request, 'projects/moll.html', context)

def Hotels(request):
	hot = Hotel.objects.order_by('-add_Date')
	context = {'hot':hot}
	return render(request, 'projects/Hotel.html', context)

def aboucom(request):
    return render(request, 'projects/about_us.html')

def institute(request):
	col = Colleges_And_Institutes.objects.order_by('-add_Date')
	context = {'col':col}
	return render(request, 'projects/Colleges&Institutes.html', context)


def allbuilding(request):
	pub = Public_build.objects.order_by('-add_Date')
	context = {'pub':pub}
	return render(request, 'projects/Public_buildings.html', context)

def Factories(request):
	ind = industry.objects.order_by('-add_Date')
	context = {'ind':ind}
	return render(request, 'projects/Factories.html', context)

def allBanks(request):
	ban = banks.objects.order_by('-add_Date')
	context = {'ban':ban}
	return render(request, 'projects/banks.html', context)

def Schools(request):
	sho = public_schools.objects.order_by('-add_Date')
	context = {'sho':sho}
	return render(request, 'projects/public_Schools.html', context)

def Private_Schools(request):
	pshc = private_school.objects.order_by('-add_Date')
	context = {'pshc':pshc}
	return render(request, 'projects/private_Schools.html', context)

def Residential(request):
	res = Residential_bulding.objects.order_by('-add_Date')
	context = {'res':res}
	return render(request, 'projects/Residential_Projects.html', context)

def allCompound(request):
	com = Compound.objects.order_by('-add_Date')
	context = {'com':com}
	return render(request, 'projects/Compound.html', context)

def our_job(request):

	# job is a object from 'senddata class in models.py'
	job = senddata.objects.all()
	context = {'job':job}
	return render(request, 'projects/jobs.html', context)
##########################################

'''
def testupload(request):

    documents = HomeProject.objects.all()

    #context = {'documents' : documents}

    return render(request, 'home.html', { 'documents': documents})
'''

def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'projects/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'projects/simple_upload.html')


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form_description = form.cleaned_data.get('description')
            form_document = form.cleaned_data.get('document')
            form_empemail = form.cleaned_data.get('empemail')
            form_phonenumber = form.cleaned_data.get('phonenumber')
            form.save()
            messages.success(request, 'تم ارسال البيانات بنجاح , نشكركم للتسجيل بشركتنا, سوف يتم التواصل بحضرتكم')
    else:
        form = DocumentForm()
    return render(request, 'projects/model_form_upload.html', {
        'form': form
    })


def contact_us(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form_fullname = form.cleaned_data.get('fullname')
            form_e_mail = form.cleaned_data.get('e_mail')
            form_text = form.cleaned_data.get('text')
            form.save()
            messages.success(request, 'تم ارسال البيانات بنجاح شكرا لاهتمامكم سوف يتم الرد على رسالتكم')
    else:
        form = ContactUsForm()
    return render(request, 'projects/contact_us.html', {
        'form' : form
        })
