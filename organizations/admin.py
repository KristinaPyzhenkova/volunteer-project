from django.contrib import admin

from organizations.models import Organization, ReviewOrganization


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


class ReviewOrganizationAdmin(admin.ModelAdmin):
    list_display = ('pk',
                    'organization',
                    'volunteer',
                    'review',
                    'created'
                    )
    search_fields = ('created',)
    empty_value_display = '-пусто-'


admin.site.register(Organization, OrganizationAdmin)
admin.site.register(ReviewOrganization, ReviewOrganizationAdmin)
