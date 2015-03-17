# -*- coding: utf-8 -*-
from django.contrib.auth.models import User, UserManager
# Create your models here.

class MyUser(User):
    #m_is_worker = models.BooleanField()
    #objects = UserManager()
    def __unicode__(self):
        return u"%s %s" % (self.last_name, self.first_name)

    def __str__(self):
        return unicode(self)