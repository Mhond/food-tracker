from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Food, Meal
from django.urls import reverse_lazy
from .forms import MealForm


def index(request):
	template = 'list.html'
	meals = Meal.objects.all()
	context = {
		'meals': meals,
	}
	return render(request, template, context)


def add_meal(request):
	template = "add_meal.html"

	if request.method == "POST":
		form = MealForm(request.POST)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse_lazy('food:index'))
	else:
		context = {
			'meal_form': MealForm(),
		}
	return render(request, template, context) 


def delete_meal(request, meal_id):
	meal = Meal.objects.get(id=int(meal_id))
	meal.delete()
	return HttpResponseRedirect(reverse_lazy('food:index'))


def update_meal(request, meal_id):
	template = "update_meal.html"
	meal = Meal.objects.get(id=int(meal_id))

	if request.method == "POST":
		form = MealForm(request.POST, instance=meal)
		if form.is_valid():
			form.save()
		return HttpResponseRedirect(reverse_lazy('food:index'))
	else:
		context = {
			'meal_form': MealForm(instance=meal),
		}
	return render(request, template, context)


def view_meal(request, meal_id):
	template = "view_meal.html"
	meal = Meal.objects.get(id=int(meal_id))
	context = {
		'meal':meal,
		}
	return render(request, template, context)

def login(request):
	if request.user.is_authenticated:
	    return HttpResponseRedirect(reverse_lazy('food:index'))
	else:
	    return HttpResponseRedirect(reverse_lazy('auth_login'))

#from django.shortcuts import render
# Create your views here.
