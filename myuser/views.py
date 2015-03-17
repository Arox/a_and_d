# -*- coding: utf-8 -*-
from django.views.generic.edit import FormView
from forms import AuthForm
from django.http import HttpResponseRedirect

# Create your views here.
class AuthView(FormView):
    template_name = 'auth.html'
    form_class = AuthForm
    success_url = '/main/'

    def form_valid(self, a_form):
        if a_form.login_user(self.request):
            return super(AuthView, self).form_valid(a_form)
        return HttpResponseRedirect('')
