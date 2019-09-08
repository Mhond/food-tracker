from django.conf.urls import url
from .views import index
from .views import index, add_meal
from .views import index, add_meal, delete_meal
from .views import index, add_meal, delete_meal, update_meal
from .views import index, add_meal, delete_meal, update_meal, view_meal
from .views import index, add_meal, delete_meal, update_meal, login



urlpatterns = [
    url(r'^$', login, name='login'),

	url(r'^index$', index, name='index'),
	url(r'^add_meal$', add_meal, name='add-meal'),
	url(r'^delete_meal/(?P<meal_id>\d+)$', delete_meal, name='delete-meal'),
	url(r'^update_meal/(?P<meal_id>\d+)$', update_meal, name='update-meal'),
	url(r'^view_meal/(?P<meal_id>\d+)$', view_meal, name='view-meal'),
]