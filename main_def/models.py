from turtle import title
from django.db import models
from django.contrib.auth.models import User

class Page_Dairy(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField()
    data = models.DateTimeField(auto_now_add=True, db_index=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,blank=True)



    def __str__(self):
        return self.title

