from django.contrib.admin.apps import AdminConfig


class BookAdminConfig(AdminConfig):
    default_site = 'Books.admin.BooksAdminSite'
