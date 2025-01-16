from django.db import models

class ReporteManager(models.Manager):
    
    def obtener_reporte(self):
        id_reporte = self.count()
        return self.filter(
            id= id_reporte
        )