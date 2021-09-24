from django.contrib import admin

from poll.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title',)
