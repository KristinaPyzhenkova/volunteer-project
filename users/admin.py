from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('pk',
                    'email',
                    'first_name',
                    'last_name',
                    'status',
                    'create_at'
                    )
    search_fields = ('first_name',)
    empty_value_display = '-пусто-'
    list_filter = ('create_at',)


admin.site.register(User, UserAdmin)


