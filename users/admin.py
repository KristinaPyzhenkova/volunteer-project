from django.contrib import admin

from .models import User, Project, Event, Function, Organization


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


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('pk',
                    'full_name',
                    'name',
                    'email',
                    'address',
                    'created'
                    )
    search_fields = ('created',)
    empty_value_display = '-пусто-'


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('pk',
                    'name',
                    'full_name',
                    'website',
                    'material_url',
                    'avatar_url',
                    'status',
                    'description',
                    'goal',
                    'result',
                    'slug',
                    'organization',
                    'user')
    search_fields = ('name', 'status')
    empty_value_display = '-пусто-'


class EventAdmin(admin.ModelAdmin):
    list_display = ('pk',
                    'name',
                    'avatar_url',
                    'status',
                    'description',
                    'date_start',
                    'date_end',
                    'project',
                    'slug',
                    'contact_user',
                    'client')
    search_fields = ('name', 'status')
    empty_value_display = '-пусто-'


class FunctionAdmin(admin.ModelAdmin):
    list_display = ('pk',
                    'name',
                    'description',
                    'task',
                    'condition',
                    'event',
                    'client',
                    'slug')
    search_fields = ('name',)
    empty_value_display = '-пусто-'


admin.site.register(User, UserAdmin)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Function, FunctionAdmin)
