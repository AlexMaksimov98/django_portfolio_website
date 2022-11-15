from django.shortcuts import render
from django.views.generic import TemplateView, ListView, FormView
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Skill, Degree, Project, Dish
from .forms import ContactForm


class IndexPageView(TemplateView):  
    template_name = 'main/index.html'

class AboutPageView(TemplateView):
    template_name = 'main/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['degrees'] = Degree.objects.all()
        context['backend'] = Skill.objects.filter(skill_type__type_of_skill='Backend').all()
        context['frontend'] = Skill.objects.filter(skill_type__type_of_skill='Frontend').all()
        context['databases'] = Skill.objects.filter(skill_type__type_of_skill='Databases').all()
        context['devops'] = Skill.objects.filter(skill_type__type_of_skill='DevOps').all()
        return context

class ProjectsPageView(ListView):
    template_name = 'main/projects.html'
    model = Project
    context_object_name = 'projects'

class ThankYouView(TemplateView):
    template_name = 'main/thank-you.html'

class ContactMeView(FormView):
    template_name = 'main/contact.html'
    form_class = ContactForm
    success_url = '/thank-you'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    

class HobbiesView(TemplateView):
    template_name = 'main/hobbies.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['first_dish'] = Dish.objects.all()[0]
        context['dishes'] = Dish.objects.all()[1:]
        return context