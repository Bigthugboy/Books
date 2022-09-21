from django.contrib import admin


class BooksAdminSite(admin.AdminSite):
    site_title = "Books admin site"
    site_header = "Welcome to the Books admin Interface"
    index_title = "Books index"
