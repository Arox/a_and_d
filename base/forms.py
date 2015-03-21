# -*- coding: utf-8 -*-
from django import forms

class BaseParametersForm(forms.Form):
    m_name = forms.CharField(max_length=30)
    m_descriptions = forms.CharField(widget=forms.Textarea)

    def clean(self):
        v_cleaned_data = super(BaseParametersForm, self).clean()
        v_name = v_cleaned_data.get('name')
        v_descriptions = v_cleaned_data.get(descriptions)

        if len(v_name) < 1:
            raise forms.ValidationError('Name is empty')
        if len(v_descriptions) < 1:
            raise forms.ValidationError('Description is empty')
        return v_cleaned_data