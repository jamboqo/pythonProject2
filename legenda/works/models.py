from django.db import models
class Articles(models.Model):
    title=models.CharField('Название работы',max_length=50)
    anons = models.CharField('Анонсыы',max_length=50)
    full_text = models.TextField('Описание работы')
    date = models.DateField('Дата загрузки')

    def _str_(self):
        return self.title
    class Meta:
        verbose_name = 'Документы'
        verbose_name_plural = 'Документы'