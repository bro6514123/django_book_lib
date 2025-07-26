from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views


app_name = 'main'


urlpatterns = [
    path('', views.product_list_page, name='books'),
    path('<slug:slug>/', views.product_list_page, name='books_by_category'),
    path('book/<int:id>/', views.details_page, name='details_of_book'),
    path('author/<slug:slug>/', views.author_page, name='author'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

