from django.contrib import admin

from .models import User, ReviewUser, Direction, UserDirection


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


class ReviewUserAdmin(admin.ModelAdmin):
    list_display = ('pk',
                    'volunteer',
                    'organization',
                    'review',
                    'created'
                    )
    search_fields = ('created',)
    empty_value_display = '-пусто-'


class UserDirectionAdmin(admin.ModelAdmin):
    list_display = ('pk',
                    'user',
                    'direction',
                    )
    search_fields = ('user',)
    empty_value_display = '-пусто-'


class DirectionAdmin(admin.ModelAdmin):
    list_display = ('pk',
                    'name',
                    'created'
                    )
    search_fields = ('created',)
    empty_value_display = '-пусто-'


admin.site.register(Direction, DirectionAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(ReviewUser, ReviewUserAdmin)
admin.site.register(UserDirection, UserDirectionAdmin)
