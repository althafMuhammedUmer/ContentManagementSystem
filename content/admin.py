from django.contrib import admin
from .models import Category, Content

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]

class ContentAdmin(admin.ModelAdmin):
    list_display = ["author", "title", "body", "summary",  "document"]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Content, ContentAdmin)
