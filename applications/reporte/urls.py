from django.urls import path
from . import views

app_name = "reporte_app"

urlpatterns = [
    path(
        "add-reporte/",
        views.ReporteCreateView.as_view(),
        name="add-reporte"
    ),
    path(
        "lista-reportes/",
        views.ListaReporte.as_view(),
        name="lista-reportes"
    ),
    path(
        "listar-reportes/",
        views.ListaReportePDF.as_view(),
        name="listar-reportes"
    ),
]