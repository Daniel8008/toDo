from django.core.urlresolvers import reverse
from django.db import models
from django.forms import  forms,ModelForm
from django.contrib.auth.models import User
from django import forms






class MyList(models.Model):
    title=models.CharField(max_length=254)
    text_preview=models.TextField()
    Date=models.DateTimeField(blank=False)
    logo=models.FileField()
    Body=models.TextField(default="please enter some text")

    def __str__(self):
  		return  self.title
    def get_absolute_url(self):
        return reverse('Todo:details',kwargs={'id':self.id})



class UserProfile(models.Model):
    user=models.OneToOneField(User)
    picture=models.FileField(blank=True)
    def __unicode__(self):
        return self.user.username
class UserForm(forms.ModelForm):
        class Meta:
            model=User
            fields=['username','password','email']

class UserProfileForm(forms.ModelForm):
        class Meta:
            model=UserProfile
            fields =['user','picture']

