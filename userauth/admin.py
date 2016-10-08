from django.contrib import admin
from userauth.models import UserProfile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from models import Organization
from mixpay.admin import *

class UserProfileAdmin(CustomModelAdmin):
    pass


class UserAdmin(CustomModelAdmin):
    pass

class OrganizationAdmin(CustomModelAdmin):
    pass


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Organization, OrganizationAdmin)
