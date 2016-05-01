from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):#model.paquete
     class Meta:
         db_table ="app_facebook_users"
     
     fb_id = models.BigIntegerField(null=False,db_index=True,
     verbose_name=u'FB_ID')
     firt_name=models.CharField(null=False,max_length=200,
       verbose_name=u'Nombres')
     last_name=models.CharField(null=False,max_length=200,
       verbose_name=u'Apellidos')
     create_at =models.DateTimeField(
     auto_now_add=True,
           verbose_name=u'Fecha de creacion')
     update_at =models.DateTimeField(
           auto_now_add=True,
           verbose_name=u'Fecha de actualizacion')
           
class UserScore(models.Model):
     class Meta:
          db_table="app_facebook_user_score"
    
     user=models.ForeignKey(User,null=False)# null false para que sea obligatprio      
     score = models.IntegerField(null=False,
     verbose_name=u'puntaje')
     create_at =models.DateTimeField(
         auto_now_add=True,
         verbose_name=u'Fecha de creacion') 
        
class Settings(models.Model):
    class Meta:
         db_table="app_facebook_settings"
         
    app_id=models.CharField(null=False,max_length=200,
         verbose_name=u'APP_ID')
         
    def __unicode__(self):
        return self.app_id
         
       
          