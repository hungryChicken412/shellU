from django.http import HttpResponse
from django.shortcuts import render, redirect
from main.models import Course,CourseCategory, CourseSeries
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm




def singleSlug(request, single_slug):
	categories = [c.category_slug for c in CourseCategory.objects.all()]
	if (single_slug in categories):
		matching_series = CourseSeries.objects.filter(course_category__category_slug=single_slug)

		series_url = {}
		for m in matching_series.all():
			part_one = Course.objects.filter(course_series__course_series=m.course_series).earliest('published')
			series_url[m] = part_one.course_slug

		

		context = {
			'part_ones': series_url,
			
		}
		return render(request, "main/category.html", context)
	
	course = [c.course_slug for c in Course.objects.all()]

	if (single_slug in course):

		this_course = Course.objects.get(course_slug=single_slug)
		tutorials_from_series = Course.objects.filter(course_series__course_series=this_course.course_series).order_by('published')
		this_tutorial_idx = list(tutorials_from_series).index(this_course)
        
		context = {
			"course" : this_course,
			"sidebar": tutorials_from_series,
			"this_tut_idx": this_tutorial_idx,

		}
		return render(request, "main/course.html", context)

	return HttpResponse(f"{single_slug} does not correspond to anything.")





def home_view(request):
	# return HttpResponse('Hello World')
	user = request.user
	hello = 'hello world'
	context = {
		'user':user,
		'hello':hello,
		'categories': CourseCategory.objects.all,
	}
	return render(request, 'main/categories.html', context)




def register(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')
			messages.success(request,  f"New Account Created: {username}")
			login(request, user)
			messages.info(request,  f"You are now logged in as {username}")
			return redirect('http://35048c338b4d.ngrok.io/app/')
		else:
			for msg in form.error_messages:
				messages.error(request, f"{msg}: {form.error_messages[msg]}")
	


	form = NewUserForm
	context = {
		'form': form,
	}
	return render(request, 'main/register.html', context )


def logout_request(request):
	logout(request)
	messages.info(request, f"Logged Out Successfully!")
	return redirect('http://35048c338b4d.ngrok.io/app/')

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if (user is not None):
				login(request, user)
				messages.info(request,  f"You are now logged in as {username}")
				return redirect('http://35048c338b4d.ngrok.io/app/')
		else:
			for msg in form.error_messages:
				messages.error(request, f"{msg}: {form.error_messages[msg]}")



	form = AuthenticationForm()
	context = {
		"form": form,
	}
	return render(request, "main/login.html", context)