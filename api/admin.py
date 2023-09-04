from django.contrib import admin
from api.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.
class UserModelAdmin(BaseUserAdmin):
    list_display = ["id", "email", "name", "tc", "is_admin","created_at","updated_at"]
    list_filter = ["is_admin"]
    fieldsets = [
        #This block defines the organization of the form fields in the user detail view. It groups related fields into sections or "fieldsets.
        ('User Crendentials', {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ["name", "tc"]}),
        ("Permissions", {"fields": ["is_admin"]}),
    ]
    add_fieldsets = [
        ( # this block defines the organization of fields for adding a new user.
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "name", "tc", "password1", "password2"],
            },
        ),
    ]
    search_fields = ["email"]
    ordering = ["email", "id"]
    filter_horizontal = []
#The filter_horizontal attribute is typically used for ManyToMany fields in Django admin.


admin.site.register(User, UserModelAdmin)