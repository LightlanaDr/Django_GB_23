from django.contrib import admin

from .models import Post, Comment, Author

@admin.action(description='обнулить показы')
def reset_quant(modeladmin, request, queryset):
    queryset.update(show_content=0)



class NewPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'status', 'publication']
    list_filter = ['author', 'publication']
    # readonly_fields = [''] запретить редактирование
    search_fields = ['author']
    list_per_page = 5
    actions = [reset_quant]


admin.site.register(Author)
admin.site.register(Post, NewPostAdmin)
admin.site.register(Comment)