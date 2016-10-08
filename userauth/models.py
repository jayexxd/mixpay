from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


gender_choices = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
)


# UserProfile class is to add the additional form fields we require from a user on top of the template User model by Django which provides only basic attribs
class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    first_name = models.CharField(default='',max_length=100)
    last_name = models.CharField(default='', max_length=100)

    business_name = models.CharField(default='Not Applicable', max_length = 30)

    desc = models.CharField('Describe yourself', max_length=1000, default='', null=True)

    email = models.CharField('Your Email', max_length=100, default='', null=True)
    phone_number = PhoneNumberField(null=True, blank=True)

    work = models.CharField('Your occupation', null=True, max_length=100)

    org = models.OneToOneField(Organization)

    def __unicode__(self):
        return self.user.username.encode('utf8')

class Organization(models.Model):
    user = models.OneToOneField(User)

    org_name = models.CharField(default='', max_length=30)

    desc = models.CharField('Describe your Organization', max_length=1000, default='', null=True)


    def __unicode__(self):
        return self.user.username.encode('utf8')
