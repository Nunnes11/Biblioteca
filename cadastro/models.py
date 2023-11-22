from django.db import models

class Livro(models.Model):
    titulo = models.CharField("título", max_length=100)
    autor = models.CharField("autor", max_length=50)
    editora = models.CharField("editora", max_length=30)
    ano_pub = models.PositiveSmallIntegerField("ano de publicação")
    num_pag = models.PositiveSmallIntegerField("número de páginas")

    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name = "Livro"
        verbose_name_plural = "Livros"


