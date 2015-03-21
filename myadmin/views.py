from django.shortcuts import render
from django.views.generic import FormView
from base.forms import BaseParametersForm
from base.models import BaseParameters

# Create your views here.
class BaseParametrCreateView(FormView):
    template_name = 'administrator/create_base_parametr.html'
    success_url = ''
    form_class = BaseParametersForm

    def form_valid(self, a_form):
        v_parametr = BaseParameters(
            m_name=a_form.m_name,
            m_description=a_form.m_description
        )
        v_parametr.save()
        return super(BaseParametrCreateView, self).form_valid(a_form)