"""User admin classes."""

# Django
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

# models
from django.contrib.auth.models import User
from users.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile Admin"""
    #List of attributes that will show in the admin
    list_display = ('pk', 'user', 'phone_number', 'website', 'picture')
   #read-only fields
    list_display_links = ('pk', 'user')
    #List of editable
    list_editable = ('phone_number', 'website', 'picture')
    #search fields
    search_fields = (
        'user__name', 
        'user__email',
        'user__username',
        'user__first_name',
        'user__last_name',
        'phone_number'
    )
    # Fields you can filter by
    list_filter = (
        'user__is_active',
        'user__is_staff',
        'created',
        'modified',
    )
    # Group fields
    fieldsets = (
        (
            'Profile',
            {  
                'fields': (('user', 'picture'),)
            }
        ),
        #If we don't want it to appear
       
        #the blue title bar we can pass None
        (
            'Extra info',
            {
                'fields': (
                    ('phone_number', 'website'),
                    ('biography'),
                )
            }
        ),
        (
            'Metadata',
            {
                'fields': (('created', 'modified'),)
            }
        ),
    )
    readonly_fields = ('created', 'modified')


#For both admins to be seen in one, it is done in the following way


class ProfileInline(admin.StackedInline):
        """Profile in-line admin for users."""
        model = Profile
        can_delete = False
        verbose_name_plural = 'profiles'


class UserAdmin(BaseUserAdmin):
    """Add profile admin to base user admin."""
    inlines = (ProfileInline, )
    list_display = (
        'username',
        'first_name',
        'last_name',
        'is_active',
        'is_staff',
    )


admin.site.unregister(User)
# admin.site.register(Model,Class)
admin.site.register(User, UserAdmin)
