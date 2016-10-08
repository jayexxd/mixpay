from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from userauth.models import UserProfile, Organization

class Transaction(models.Model):
    organization = moedls.ForeignKey(Organization)
