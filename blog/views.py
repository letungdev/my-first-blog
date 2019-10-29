from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect



	
def about_us(request):
	return render(request, "about_us.html")	
def homepage(request):
	return render(request, "blog/home.html")
def blogs(request):
	return render(request, "blog/blog.html")
def contact_us(request):
	return render(request, "blog/contact.html")
def course_detail(request):
	return render(request, "blog/course_details.html")
def course(request):
	return render(request, "blog/course.html")
def students(request):
	return render(request, "blog/students.html")
def invest(request):
	return render(request, "blog/invest.html")