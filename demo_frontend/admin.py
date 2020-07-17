from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import UserExtension

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class UserExtentionInline(admin.StackedInline):
    model = UserExtension
    can_delete = False
    verbose_name_plural = 'user_extension'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (UserExtentionInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)