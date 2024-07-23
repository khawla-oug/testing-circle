from django.contrib import admin

# Register your models here.

from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date')
    search_fields = ('title', 'author')
    list_filter = ('pub_date',)

    def save_model(self, request, obj, form, change):
        # Set the current user as the author when saving a new article
        if not obj.pk:  # Check if it's a new article
            obj.author = request.user.username

        super().save_model(request, obj, form, change)

admin.site.register(Article, ArticleAdmin)
