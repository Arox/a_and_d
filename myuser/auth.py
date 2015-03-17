# -*- coding: utf-8 -*-
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from models import MyUser

def get_user(a_request):
    v_user = auth.get_user(a_request)
    return v_user

def get_myuser(a_request):
    v_user = get_user(a_request)
    print v_user.pk
    return MyUser.objects.get(pk = v_user.pk)

def is_login(a_request):
    v_user = get_user(a_request)
    if v_user is not None and v_user.is_authenticated():
        if "id" in a_request.session:
            v_user_id = a_request.session['id']
            if v_user_id > 0:
                return True
        else:
            a_request.session['id'] = v_user.id
    return False

def user_exists(a_login, a_password):
    try:
        v_user = User.objects.get(username = a_login)
    except User.DoesNotExist:
        return False
    if v_user.check_password(a_password):
        return True
    return False

def login(a_request, a_login, a_password):
    if is_login(a_request):
        return True
    if not a_login or not a_password:
        return False
    if user_exists(a_login, a_password):
        v_user = auth.authenticate(username=a_login, password=a_password)
        if v_user is not None and v_user.is_active:
            auth.login(a_request, v_user)
            a_request.session['id'] = v_user.id
            return True
    return False

def logout(a_request):
    if is_login(a_request):
        del a_request.session['id']
        auth.logout(a_request)

def is_login_or_authenticate(a_request):
    if is_login(a_request):
        return None
    return HttpResponseRedirect('')

def login_or_authenticate(a_request, a_login, a_password):
    if not login(a_request, a_login, a_password):
        return HttpResponseRedirect('')
    return None

def user_id(a_request):
    if is_login(a_request):
        return a_request.session["id"]
    return None
