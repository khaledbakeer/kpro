from __future__ import unicode_literals
from django.contrib import admin

from subjects.models import Subject


class PageAdmin(admin.ModelAdmin):
    list_display = (
        'subject_number',
        'subject_name',
        'author',
        'responsible_lecturer_name',
        'responsible_lecturer_email',
        'date_updated')
    list_display_links = ('subject_number', 'subject_name')
    search_fields = ('subject_number', 'subject_name', 'responsible_lecturer_name', 'content_and_goals')
    list_per_page = 25


admin.site.register(Subject, PageAdmin)
