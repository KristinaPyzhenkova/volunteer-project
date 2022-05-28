from django.contrib import admin

from events.models import Event, Function, Follow, Favorites


class EventAdmin(admin.ModelAdmin):
    list_display = ('pk',
                    'name',
                    'avatar_url',
                    'status',
                    'description',
                    'date_start',
                    'date_end',
                    'project',
                    'contact_user'
                    )
    search_fields = ('name', 'status')
    empty_value_display = '-пусто-'


class FunctionAdmin(admin.ModelAdmin):
    list_display = ('pk',
                    'name',
                    'description',
                    'task',
                    'condition',
                    'event',
                    'count')

    search_fields = ('name',)
    empty_value_display = '-пусто-'


class FollowAdmin(admin.ModelAdmin):
    list_display = ('pk',
                    'user',
                    'event')
    search_fields = ('user',)
    empty_value_display = '-пусто-'


class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('pk',
                    'user',
                    'event')
    search_fields = ('user',)
    empty_value_display = '-пусто-'


admin.site.register(Event, EventAdmin)
admin.site.register(Function, FunctionAdmin)
admin.site.register(Follow, FollowAdmin)
admin.site.register(Favorites, FavoriteAdmin)
