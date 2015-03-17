# -*- coding: utf-8 -*-
from django import forms
from myuser.auth import login_or_authenticate, user_exists

class AuthForm(forms.Form):
    login = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def login_user(self, a_request):
        v_cleaned_data = super(AuthForm, self).clean()
        v_login = v_cleaned_data.get('login')
        v_password = v_cleaned_data.get('password')
        if not v_login or not v_password:
            return False
        if login_or_authenticate(a_request, v_login, v_password) is None:
            return True
        return False

    def clean(self):
        v_cleaned_data = super(AuthForm, self).clean()
        v_login = v_cleaned_data.get('login')
        v_password = v_cleaned_data.get('password')
        if not v_login or not v_password:
            raise forms.ValidationError("Empty field")
        if not user_exists(v_login, v_password):
            raise forms.ValidationError("Login or password not found")
        return v_cleaned_data