from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Skill, Degree, Project, Book, Dish
from .forms import ContactForm


class IndexPageView(TemplateView):
    template_name = 'main/index.html'

class AboutPageView(TemplateView):
    template_name = 'main/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['degrees'] = Degree.objects.all()
        context['skills'] = Skill.objects.all()
        return context

class ProjectsPageView(ListView):
    template_name = 'main/projects.html'
    model = Project
    context_object_name = 'projects'

class ContactMeView(View):
    
    def get(self, request):
        form = ContactForm()
        return render(request, 'main/contact.html', {
            'form': form
        })

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid:
            form.save()
        return HttpResponseRedirect(reverse('contact_page'))

class HobbiesView(TemplateView):
    template_name = 'main/hobbies.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['first_dish'] = Dish.objects.all()[0]
        context['dishes'] = Dish.objects.all()[1:]
        context['books'] = Book.objects.all()
        return context