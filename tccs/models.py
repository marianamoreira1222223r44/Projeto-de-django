from django.db import models


class Autor(models.Model):

    primeiro_nome = models.CharField(max_length=100)
    ultimo_nome = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='fotos')

    def __str__(self):
        return self.primeiro_nome


class Orientador(models.Model):

    primeiro_nome = models.CharField(max_length=100)
    ultimo_nome = models.CharField(max_length=100)
    link_do_curriculo_lattes = models.URLField()

    def __str__(self):
        return self.primeiro_nome

class Curso(models.Model):

    modalidades = (
        ('Bacharelado', 'Bacharelado'), 
        ('Licenciatura', 'Licenciatura'), 
        ('Tecnológo', 'Tecnológo'))

    nome = models.CharField(max_length=100)
    modalidade = models.CharField(max_length=50, choices = modalidades)

    def __str__(self):
        return self.nome


class Tcc(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    orientador = models.ForeignKey(Orientador, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    ano_do_documento = models.IntegerField(verbose_name="ano_documento")
    resumo = models.TextField(max_length=300)
    arquivo_do_documento = models.FileField(upload_to='arquivos', verbose_name="arquivo_documento")
    palavras_chave = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo

