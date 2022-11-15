from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexPageView.as_view(), name='index_page'),
    path('about', views.AboutPageView.as_view(), name='about_page'),
    path('projects', views.ProjectsPageView.as_view(), name='projects_page'),
    path('contact-me', views.ContactMeView.as_view(), name='contact_page'),
    path('my-hobbies', views.HobbiesView.as_view(), name='my_hobbies'),
    path('thank-you', views.ThankYouView.as_view(), name='thank-you')
]