from django.contrib import admin

from .models import Category, Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',  'surname', 'email',
                    'created_at', 'disabled',)
    list_editable = ('disabled',)


admin.site.register(Category)
admin.site.register(Contact, ContactAdmin)
