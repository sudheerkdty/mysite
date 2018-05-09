from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from portal.forms import SignupForm
# Create your views here.


class HomePageView(TemplateView):
    """docstring for HomeView"""
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        """Context data is overriddern for making similar to home page."""
        context = super(HomePageView, self).get_context_data(*args, **kwargs)
        context['home'] = True
        context['title'] = 'Home Page'
        context['request'] = self.request
        return context


class SignupView(FormView):
    template_name = 'registration/signup.html'
    form_class = SignupForm
    success_url = '/'


    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super(SignupView, self).form_valid(form)

    def form_invalid(self, form):
        """It is called when invalid form data has been POSTed."""
        context = self.get_context_data(form=form)
        return self.render_to_response(context)