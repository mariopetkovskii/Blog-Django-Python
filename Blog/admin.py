from django.contrib import admin
from .models import BlogUser, Post, Comment
from django.contrib.admin import DateFieldListFilter


# Register your models here.
class BlogUserAdmin(admin.ModelAdmin):
    list_display = ("name", "last_name", "user")

    def has_change_permission(self, request, obj=None):
        if obj and (request.user == obj.user) or request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if obj and (request.user == obj.user) or request.user.is_superuser:
            return True
        return False

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return False


admin.site.register(BlogUser, BlogUserAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ("content_of_comment", "post")

    def has_change_permission(self, request, obj=None):
        if obj and (request.user == obj.comment_by) or request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if obj and (request.user == obj.comment_by) or request.user.is_superuser:
            return True
        return False

    def has_add_permission(self, request, obj=None):
        if obj and (request.user in obj.comment_by.blocked_users.all()):
            return False
        return True


admin.site.register(Comment, CommentAdmin)


class CommentPostAdmin(admin.StackedInline):
    model = Comment
    extra = 0


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "date_of_creating", "date_of_last_update")

    inlines = [CommentPostAdmin]

    search_fields = ["title", "content"]

    list_filter = (('date_of_creating', DateFieldListFilter),)

    def has_change_permission(self, request, obj=None):
        if obj and (request.user == obj.user.user) or request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if obj and (request.user == obj.user.user) or request.user.is_superuser:
            return True
        return False

    def has_view_permission(self, request, obj=None):
        if obj and (request.user in obj.user.blocked_users.all()):
            return False
        return True


admin.site.register(Post, PostAdmin)
