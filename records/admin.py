from django.contrib import admin
from .models import RecordItem, Record


# Register your models here.
class RecordItemInline(admin.TabularInline):
    model = RecordItem
    raw_id_fields = ['doctor']


class RecordAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'address',
                    'postal_code', 'city', 'paid', 'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [RecordItemInline]


admin.site.register(Record, RecordAdmin)
