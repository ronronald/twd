from django.contrib import admin
from .models import Category, Page, UserProfile

class PageAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "url", "views")

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name", )}


admin.site.register(UserProfile)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
