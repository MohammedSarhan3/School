from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
NAME_OF_CLASS = [
    ('KG1', 'KG1'),
    ('KG2', 'KG2'),
    ('الأول الإبتدائي', 'الأول الإبتدائي'),
    ('الثاني الإبتدائي', 'الثاني الإبتدائي'),
    ('الثالث الإبتدائي', 'الثالث الإبتدائي'),
    ('الرابع الإبتدائي', 'الرابع الإبتدائي'),
    ('الخامس الإبتدائي', 'الخامس الإبتدائي'),
    ('السادس الإبتدائي', 'السادس الإبتدائي'),
    ('الأول الإعدادي', 'الأول الإعدادي'),
    ('الثاني الإعدادي', 'الثاني الإعدادي'),
    ('الثالث الإعدادي', 'الثالث الإعدادي'),
]
TYPE = [
    ('عربي', 'عربي'),
    ('لغات', 'لغات'),
    
]

class Level(models.Model):
    level=models.CharField(verbose_name=_('الصف'),max_length=20,choices=NAME_OF_CLASS,null=True,blank=True)
    typee=models.CharField(verbose_name=_('اللغة'),max_length=20,choices=TYPE,null=True,blank=True)
    

    def __str__(self):
        return self.level

class Classes(models.Model):
    level=models.ForeignKey(Level, on_delete=models.CASCADE,null=True,blank=True)
    classs=models.CharField(verbose_name=_('الفصل'),max_length=7,null=True,blank=True)
    capasity=models.IntegerField(verbose_name=_("العدد"),null=True,blank=True)   
    def __str__(self):
        return self.classs


class Student(models.Model):
    clas=models.ForeignKey(Classes,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(_("الإسم"), max_length=100,null=True,blank=True)
    telphone=models.CharField(_("رقم الهاتف"), max_length=50,null=True,blank=True)
    def __str__(self):
        return self.name