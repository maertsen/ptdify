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

    def save(self, *args, **kwargs):
        # if:
        # - we are not yet completed
        # AND
        # - we are depending on some other action
        # then become future if:
        #       - the action we depend on is future 
        #       OR
        #       - the action we depend on is not yet completed
        if not self.completed and self.dependsOn_id is not None:
            if self.dependsOn.status == 'F' or not self.dependsOn.completed:
                self.status = 'F'

        super(Action, self).save(*args, **kwargs) # Call the "real" save() method.

        # some postprocessing
        if self.completed: # all future actions depending on this one become next
            searchFor = 'F'
            turnInto = 'N'
        else: # all next actions depending on this one become future
            searchFor = 'N'
            turnInto = 'F'
        
        depending = self.action_set.filter(completed=False).filter(status__exact=searchFor)
        for d in depending:
            d.status = turnInto
            d.save()
