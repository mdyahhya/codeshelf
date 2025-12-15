from django.urls import path
from .views import LanguageListView, LanguageDetailView, import_languages_view

urlpatterns = [
    path('languages/', LanguageListView.as_view(), name='language-list'),
    path('languages/<int:pk>/', LanguageDetailView.as_view(), name='language-detail'),
    path('import-languages/', import_languages_view, name='import-languages'),
]
