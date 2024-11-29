from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView  # Для перенаправления на статику
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Админка
    path('admin/', admin.site.urls),

    # API эндпоинты
    path('api/comments/', include('comments.urls')),  # Префикс для API

    # Раздача Vue.js SPA (index.html)
    path('', RedirectView.as_view(url='/static/index.html', permanent=False), name='index'),
]

# Добавляем обработку статики и медиафайлов в режиме разработки
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

