from django.urls import path
from . import views

app_name = "reporte_app"

urlpatterns = [
    path(
        "add-reporte/",
        views.ReporteCreateView.as_view(),
        name="add-reporte"
    ),
]