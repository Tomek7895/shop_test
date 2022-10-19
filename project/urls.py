from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',
         RedirectView.as_view(pattern_name='expenses:expense-list'),
         name='dashboard'),
    path('expenses/',
         include(('expenses.urls', 'expenses'), namespace='expenses')),
]
