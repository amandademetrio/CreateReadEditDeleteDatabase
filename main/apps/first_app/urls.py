from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'users$', views.index), #Route 1: displays all users
    url(r'users/new$', views.new), #Route 2: displays form to create a new user
    url(r'users/(?P<number>[0-9]+)$', views.show), #Route 3: Show user record, given an id
    url(r'users/(?P<number>[0-9]+)/edit$', views.edit), #Route 4: Edits specific user, given id
    url(r'users/create$',views.create), #Route 5: Post route to create new user
    url(r'users/(?P<number>[0-9]+)/destroy$', views.destroy), #Route 6: destroy current user
    url(r'users/update',views.update) #Route 7: Post route to update user
] 