from django.db import models
from base.models import BaseParameters, Race
# Create your models here.
class Gamer(models.Model):
    m_baseparametr = models.ForeignKey(BaseParameters)