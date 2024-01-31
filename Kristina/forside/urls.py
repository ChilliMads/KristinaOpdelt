from django.urls import path

from . import views

# Returns an element for inclusion in urlpatterns. See more at: Django Docs
urlpatterns = [ 
    path("", views.index, name="index"),
]