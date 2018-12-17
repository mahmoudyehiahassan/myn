from __future__ import unicode_literals
from django.db import models


# Create your models here.
class senddata(models.Model):
	Job_title = models.CharField(max_length=60)
	Edu_Qualification = models.CharField(max_length=100)
	years_of_Experience = models.CharField(max_length=2)
	pub_date = models.DateField()

	def __str__(self):
		return self.Job_title

class Document(models.Model):
    description = models.CharField(max_length=100)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    empemail = models.EmailField()
    phonenumber = models.CharField(max_length=50, blank=True)

class HomeProject(models.Model):
	mainPhoto = models.FileField(upload_to='documents/')
	uploaded_at = models.DateTimeField(auto_now_add=True)
	subPhoto = models.FileField(upload_to='documents/')
	Title = models.CharField(max_length=60)

	def __str__(self):
		return self.Title

class HomeSlider(models.Model):
	Photo = models.FileField(upload_to='documents/')
	PhotoTitile = models.CharField(max_length=100)
	uploaded_at = models.DateTimeField(auto_now_add=True)

class First_Photo_Slider(models.Model):
	Photo = models.FileField(upload_to='documents')
	Titile = models.CharField(max_length=50)

class OurNews(models.Model):
	NewsTitile = models.CharField(max_length=100)
	NewsDescription = models.CharField(max_length=180)

class ProjectStatistics(models.Model):
	Hospitals = models.IntegerField(default=0)
	Banks = models.IntegerField(default=0)
	Hotels = models.IntegerField(default=0)
	Malls = models.IntegerField(default=0)
	Administration_Buildings = models.IntegerField(default=0)
	Private_Schools = models.IntegerField(default=0)
	General_Schools = models.IntegerField(default=0)
	Factories = models.IntegerField(default=0)
	Residential_Projects = models.IntegerField(default=0)
	Compound = models.IntegerField(default=0)
	Colleges_Institutes = models.IntegerField(default=0)


class ContactUs(models.Model):
	fullname = models.CharField(max_length=60)
	e_mail = models.EmailField()
	text = models.CharField(max_length=500)
	pub_date = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.fullname


class industry(models.Model):
	project_name = models.CharField(max_length=300)
	project_nature = models.CharField(max_length=30)
	royal_side = models.CharField(max_length=150)
	consultant = models.CharField(max_length=150)
	executive_status = models.CharField(max_length=150)
	youtube_url = models.CharField(max_length=500)
	add_Date = models.DateField(auto_now=False, auto_now_add=False)

	def __str__(self):
		return self.project_name

class banks(models.Model):
	project_name = models.CharField(max_length=300)
	project_nature = models.CharField(max_length=30)
	royal_side = models.CharField(max_length=150)
	consultant = models.CharField(max_length=150)
	executive_status = models.CharField(max_length=150)
	youtube_url = models.CharField(max_length=500)
	add_Date = models.DateField(auto_now=False, auto_now_add=False)

	def __str__(self):
		return self.project_name

class Public_build(models.Model):
	project_name = models.CharField(max_length=300)
	project_nature = models.CharField(max_length=30)
	royal_side = models.CharField(max_length=150)
	consultant = models.CharField(max_length=150)
	executive_status = models.CharField(max_length=150)
	youtube_url = models.CharField(max_length=500)
	add_Date = models.DateField(auto_now=False, auto_now_add=False)

	def __str__(self):
		return self.project_name


class Colleges_And_Institutes(models.Model):
	project_name = models.CharField(max_length=300)
	project_nature = models.CharField(max_length=30)
	royal_side = models.CharField(max_length=150)
	consultant = models.CharField(max_length=150)
	executive_status = models.CharField(max_length=150)
	youtube_url = models.CharField(max_length=500)
	add_Date = models.DateField(auto_now=False, auto_now_add=False)

	def __str__(self):
		return self.project_name

class private_school(models.Model):
	project_name = models.CharField(max_length=300)
	project_nature = models.CharField(max_length=30)
	royal_side = models.CharField(max_length=150)
	consultant = models.CharField(max_length=150)
	executive_status = models.CharField(max_length=150)
	youtube_url = models.CharField(max_length=500)
	add_Date = models.DateField(auto_now=False, auto_now_add=False)

	def __str__(self):
		return self.project_name

class public_schools(models.Model):
	project_name = models.CharField(max_length=300)
	project_nature = models.CharField(max_length=30)
	royal_side = models.CharField(max_length=150)
	consultant = models.CharField(max_length=150)
	executive_status = models.CharField(max_length=150)
	youtube_url = models.CharField(max_length=500)
	add_Date = models.DateField(auto_now=False, auto_now_add=False)

	def __str__(self):
		return self.project_name

class Hospital(models.Model):
	project_name = models.CharField(max_length=300)
	project_nature = models.CharField(max_length=30)
	royal_side = models.CharField(max_length=150)
	consultant = models.CharField(max_length=150)
	executive_status = models.CharField(max_length=150)
	youtube_url = models.CharField(max_length=500)
	add_Date = models.DateField(auto_now=False, auto_now_add=False)

	def __str__(self):
		return self.project_name

class Residential_bulding(models.Model):
	project_name = models.CharField(max_length=300)
	project_nature = models.CharField(max_length=30)
	royal_side = models.CharField(max_length=150)
	consultant = models.CharField(max_length=150)
	executive_status = models.CharField(max_length=150)
	youtube_url = models.CharField(max_length=500)
	add_Date = models.DateField(auto_now=False, auto_now_add=False)

	def __str__(self):
		return self.project_name

class Compound(models.Model):
	project_name = models.CharField(max_length=300)
	project_nature = models.CharField(max_length=30)
	royal_side = models.CharField(max_length=150)
	consultant = models.CharField(max_length=150)
	executive_status = models.CharField(max_length=150)
	youtube_url = models.CharField(max_length=500)
	add_Date = models.DateField(auto_now=False, auto_now_add=False)

	def __str__(self):
		return self.project_name

class all_Moll(models.Model):
	project_name = models.CharField(max_length=300)
	project_nature = models.CharField(max_length=30)
	royal_side = models.CharField(max_length=150)
	consultant = models.CharField(max_length=150)
	executive_status = models.CharField(max_length=150)
	youtube_url = models.CharField(max_length=500)
	add_Date = models.DateField(auto_now=False, auto_now_add=False)

	def __str__(self):
		return self.project_name

class Hotel(models.Model):
	project_name = models.CharField(max_length=300)
	project_nature = models.CharField(max_length=30)
	royal_side = models.CharField(max_length=150)
	consultant = models.CharField(max_length=150)
	executive_status = models.CharField(max_length=150)
	youtube_url = models.CharField(max_length=500)
	add_Date = models.DateField(auto_now=False, auto_now_add=False)

	def __str__(self):
		return self.project_name

		
