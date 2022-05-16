from django.contrib import admin

from organizations.models import Organization


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


admin.site.register(Organization, OrganizationAdmin)
