from django.contrib import admin

from .models import BookName, BookAuthor, Section, Book


class BookInline(admin.TabularInline):
    model = Book

@admin.register(BookName)
class BookNameAdmin(admin.ModelAdmin):
    inlines = [
        BookInline,
    ]

@admin.register(BookAuthor)
class BookAuthorAdmin(admin.ModelAdmin):
    inlines = [
        BookInline,
    ]

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    inlines = [
        BookInline,
    ]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', 'isbn']
    prepopulated_fields = {'slug': ('isbn',)}
