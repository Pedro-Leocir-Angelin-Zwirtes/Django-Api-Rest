from django.db import models

class Chamado(models.Model):
    STATUS_CHOICES = [
        ('aberto', 'Aberto'),
        ('fechado', 'Fechado'),
    ]
    
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='aberto')
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        if self.status == 'fechado':
            self.delete()
        else:
            super().save(*args, **kwargs)

    def __str__(self):
        return self.titulo
