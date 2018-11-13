from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from ..views import drf_cbv as views

urlpatterns = [
    path('snippets/', views.SnippetList.as_view())
]
urlpatterns = format_suffix_patterns(urlpatterns)
