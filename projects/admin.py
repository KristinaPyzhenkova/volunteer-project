from django.contrib import admin

from projects.models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('pk',
                    'name',
                    'avatar_url',
                    'description',
                    'goal',
                    'result',
                    )
    search_fields = ('name',)
    empty_value_display = '-пусто-'


admin.site.register(Project, ProjectAdmin)
