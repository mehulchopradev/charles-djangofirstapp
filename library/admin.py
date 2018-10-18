from django.contrib import admin

from library.models import Book, Publication, Review

class ReviewInline(admin.TabularInline):
    model = Review
    extra = 0

class BookAdmin(admin.ModelAdmin):
    list_display = ['title','pages','price']
    list_filter = ['price']
    search_fields = ['title']
    fields = ['title', 'pages', 'price', 'publication']

    inlines = [ReviewInline]

# Register your models here.
admin.site.register(Book, BookAdmin)
admin.site.register(Publication)
