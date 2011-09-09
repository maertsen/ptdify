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

class UserRealmModel(UserModel):
    realm = models.ForeignKey('Realm',blank=True,null=True)

    class Meta:
        abstract = True

# Normal classes
ACTIONSTATUS = (
    ('W', 'Waiting'),
    ('N', 'Next'),
    ('F', 'Future'),
)

class Action(UserRealmModel):
    description = models.CharField(max_length=100)
    notes = models.TextField(blank=True)
    contact = models.ForeignKey('Contact',blank=True,null=True)
    context = models.ForeignKey('Context')
    project = models.ForeignKey('Project',blank=True,null=True)
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

class Area(UserRealmModel):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

class Contact(UserRealmModel):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

class Context(UserRealmModel):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

class Project(UserRealmModel):
    active = models.BooleanField(default=True)
    area = models.ForeignKey('Area',blank=True,null=True)
    description = models.TextField(blank=True)
    defaultContact = models.ForeignKey(Contact,blank=True,null=True)
    defaultContext = models.ForeignKey(Context)
    name = models.CharField(max_length=50)
    order = models.PositiveIntegerField(blank=True,null=True)

    def __unicode__(self):
        return self.name

class Realm(UserModel):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name
