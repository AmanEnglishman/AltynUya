from django.contrib import admin

from apps.user.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'email',
        'second_name',
    )
    list_display_links = (
        'id',
    )
    list_filter = (
        'id',
    )
    search_fields = (
        'id',
    )

