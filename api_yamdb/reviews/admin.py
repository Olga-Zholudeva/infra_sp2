from django.contrib import admin

from .models import User, Category, Genre, Title, Review, Comment


class TitleAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'genre', 'year', 'description',)
    search_fields = ('name',)
    list_filter = ('category',)
    empty_value_display = '-пусто-'


admin.site.register(Title, TitleAdmin)
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Review)
admin.site.register(Comment)
