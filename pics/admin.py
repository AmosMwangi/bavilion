from django.contrib import admin
from .models import Editor,Pics,tags,Category,Location

# Register your models here.
class PicsAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)

admin.site.register(Editor)
admin.site.register(Pics,PicsAdmin)
admin.site.register(tags)
admin.site.register(Category)
admin.site.register(Location)