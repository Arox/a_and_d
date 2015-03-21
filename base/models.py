from django.db import models
import myfields

# Create your models here.
class BaseParameters(models.Model):
    m_name = models.CharField(max_length=30)
    m_description = models.TextField()

class Legality(models.Model):
    m_name = models.CharField(max_length=15)
    m_description = models.TextField()

class WorldView(models.Model):
    m_name = models.CharField(max_length=15)
    m_description = models.TextField()

class Language(models.Model):
    m_name = models.CharField(max_length=30)
    m_description = models.TextField()

class Gods(models.Model):
    m_name = models.CharField(max_length=30)
    m_description = models.TextField()

class TypeGrowth(models.Model):
    m_name = models.CharField(max_length=30)
    m_armor_class = models.IntegerField()
    m_attack = models.IntegerField()
    m_secretiveness = models.IntegerField()
    m_max_weight = models.IntegerField()

class Vision(models.Model):
    m_name = models.CharField(max_length=50)

class Weapons(models.Model):
    pass

class Skill(models.Model):
    m_name = models.CharField(max_length=30)
    m_description = models.TextField()

class DDClass(models.Model):
    m_name = models.CharField(max_length=30)
    m_description = models.TextField()

    m_min_life = models.IntegerField()
    m_max_life = models.IntegerField()

    m_gods = models.ForeignKey(Gods)

    m_possible_classes = models.ManyToManyField(u'self', null=True)

class Level(models.Model):
    m_ddclass = models.ForeignKey(DDClass)
    m_attack = myfields.ListField()
    m_stamina = models.IntegerField()
    m_reflex = models.IntegerField()
    m_will = models.IntegerField()

    m_dop = models.TextField()

    m_number_of_spels = myfields.ListField()
    m_number_of_spels_in_day = myfields.ListField()
    
class SkillNotExistInDDClass(models.Model):
    m_ddclass = models.ForeignKey(DDClass)
    m_skill = models.ForeignKey(Skill)

class SkillBaseParametr(models.Model):
    m_skill = models.ForeignKey(Skill)
    m_ddclass = models.ForeignKey(DDClass)
    m_baseparametr = models.ForeignKey(BaseParameters, null=True)

class Race(models.Model):
    m_name = models.CharField(max_length=30)
    m_description = models.TextField()

    m_baseparameters_modificator = models.ManyToManyField(BaseParameters, through='RaceBaseParameters')

    m_min_growth = models.IntegerField()
    m_max_growth = models.IntegerField()

    m_min_weight = models.IntegerField()
    m_max_weight = models.IntegerField()

    m_min_age = models.IntegerField()
    m_max_age = models.IntegerField()

    m_legality = models.ManyToManyField(Legality)
    m_worldview = models.ManyToManyField(WorldView)

    m_skill_number_first = models.IntegerField()
    m_skill_number = models.IntegerField()
    m_speed = models.IntegerField()

    m_feature_number_first = models.IntegerField()
    m_feature_number = models.IntegerField()

    m_language_automatic = models.ManyToManyField(Language, related_name='authomatic_language')
    m_language = models.ManyToManyField(Language, related_name='variant_language')

    m_gods = models.ForeignKey(Gods)

    m_vision = models.ForeignKey(Vision)

    m_weapons = models.ManyToManyField(Weapons)

class RaceBaseParameters(models.Model):
    m_race = models.ForeignKey(Race)
    m_baseparametr = models.ForeignKey(BaseParameters)
    m_modificator = models.IntegerField()


