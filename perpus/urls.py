from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from perpustakaan.views import *
from django.conf.urls.static import static
from django.conf import settings
from perpustakaan.viewset_api import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('group', GroupViewSet)
router.register('book', BookViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', home),
    path('admin/', admin.site.urls),
    path('buku/',buku, name='buku'),
    path('penerbit/', penerbit, name='penerbit'),
    path('tambah-buku/', tambah_buku, name='tambah_buku'),
    path('buku/ubah/<int:book_id>', ubah_buku, name='ubah_buku'),
    path('buku/hapus/<int:book_id>', hapus_buku, name='hapus_buku'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path("signup/", signup, name="signup"),
    path('export/xls/', export_xls, name='export_xls')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
