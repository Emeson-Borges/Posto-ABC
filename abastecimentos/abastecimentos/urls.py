from django.contrib import admin
from django.urls import path, include
from core.views import relatorio_abastecimentos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),
    path('relatorio-abastecimentos/', relatorio_abastecimentos, name='relatorio_abastecimentos'),
]
