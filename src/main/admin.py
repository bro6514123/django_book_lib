from django.contrib import admin

from .models import Ganre, Author, Book


@admin.register(Ganre)
class GanreAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'slug']
    prepopulated_fields = {'slug': ('fullname',)}

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', "display_ganres"]

    def display_ganres(self, obj):
        return ", ".join([ganre.name for ganre in obj.ganres.all()])
    display_ganres.short_description = "Genres"
