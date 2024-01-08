from django.contrib import admin
from.models import JobPost,Location,Author,Skills

class JobAdmin(admin.ModelAdmin):
    list_display = ('title','salary','date')
    list_filter = ('date',)
    search_fields = ('title',)
    search_help_text = "search jobs here"
    # fields = ('title',)

admin.site.register(JobPost,JobAdmin)
admin.site.register(Location)
admin.site.register(Author)
admin.site.register(Skills)
