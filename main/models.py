from django.db import models


class Article(models.Model):
    link = models.TextField('Ссылка')
    head_title = models.CharField('Head заголовок',max_length=500)
    keywords = models.TextField('Ключевые слова')
    description = models.TextField('Описание')
    title = models.CharField('Заголовок', max_length=500)
    preview_img = models.ImageField('Главная картинка', upload_to="articles_images")
    subtitle = models.CharField('Подзаголовок', max_length=500)
    photo_text = models.TextField('Текст фотографии')
    markup = models.TextField()
    is_published = models.BooleanField('Опубликовано', default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class ImageArticle(models.Model):
    image = models.ImageField('Изображение', upload_to="articles_images")
    article = models.ForeignKey('Article', on_delete=models.CASCADE, related_name='images', verbose_name='Статья')

    def __str__(self):
        return self.article.title
