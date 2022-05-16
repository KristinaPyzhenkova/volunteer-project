from django.contrib import admin

from projects.models import Project


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
                    'organization'
                    )
    search_fields = ('name', 'status')
    empty_value_display = '-пусто-'


admin.site.register(Project, ProjectAdmin)
