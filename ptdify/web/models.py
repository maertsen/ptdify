from django.contrib.auth.models import User
from django.db import models
from web.managers import UserManager

# Abstract base classes
class UserModel(models.Model):
    user = models.ForeignKey(User)

    # Managers
    objects = UserManager()

    class Meta:
        abstract = True

class AreaUserModel(UserModel):
    area = models.ForeignKey('Area')

    class Meta:
        abstract = True

# Normal classes
class Area(UserModel):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

class Context(AreaUserModel):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

class Project(AreaUserModel):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    defaultContext = models.ForeignKey(Context)
    order = models.PositiveIntegerField(blank=True,null=True)

    def __unicode__(self):
        return self.name

ACTIONSTATUS = (
    ('W', 'Waiting'),
    ('N', 'Next'),
    ('F', 'Future'),
)

class Action(AreaUserModel):
    description = models.CharField(max_length=100)
    notes = models.TextField(blank=True)
    context = models.ForeignKey(Context)
    project = models.ForeignKey(Project,blank=True,null=True)
    dependsOn = models.ForeignKey('Action',blank=True,null=True)
    # are these still necessary?
    # due = models.DateField(blank=True,null=True)
    # showFrom = models.DateField(blank=True,null=True)
    completed = models.BooleanField()
    status = models.CharField(max_length=1, choices=ACTIONSTATUS, default='N')

    def __unicode__(self):
        return self.description
