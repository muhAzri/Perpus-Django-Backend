from django.contrib import admin
from perpustakaan.models import *
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ['title','writter','group_id','amount']
    search_fields = ['title', 'writter', 'publisher']
    list_filter = ['group_id']
    list_per_page = 5

admin.site.register(Book, BookAdmin)
admin.site.register(Group)
