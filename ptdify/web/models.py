from django.db import models
from django.contrib.auth.models import User

class Context(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=50)
    order = models.PositiveIntegerField(blank=True,null=True)

    def __unicode__(self):
        return self.name


class Project(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    defaultContext = models.ForeignKey(Context)
    order = models.PositiveIntegerField(blank=True,null=True)

    def __unicode__(self):
        return self.name

class Action(models.Model):
    user = models.ForeignKey(User)
    description = models.CharField(max_length=100)
    notes = models.TextField(blank=True)
    context = models.ForeignKey(Context)
    project = models.ForeignKey(Project,blank=True,null=True)
    due = models.DateField(blank=True,null=True)
    showFrom = models.DateField(blank=True,null=True)
    completed = models.BooleanField()

    def __unicode__(self):
        return self.description

