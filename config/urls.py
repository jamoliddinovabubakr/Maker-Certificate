from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from rest_framework.routers import SimpleRouter

from refresher_course.api import CertificatePDFView

urlpatterns = [
    re_path(r'malaka/media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'malaka/static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]

# Todo PNFL, PASPROT seria, apchat
#
urlpatterns += {
    path('malaka/', include('refresher_course.urls')),
    path('malaka/admin/', admin.site.urls),
    path('malaka/api/', CertificatePDFView.as_view()),
    # re_path(r'^auth/', include('djoser.urls.authtoken')),  # new
}
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
