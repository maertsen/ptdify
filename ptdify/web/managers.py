from django.db import models

class UserManager(models.Manager):
    def for_user(self, user):
        return super(UserManager, self).get_query_set().filter(user=user)

