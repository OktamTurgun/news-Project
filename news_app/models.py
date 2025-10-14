from django.urls import reverse
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.utils import translation


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True)

    name_en = models.CharField(max_length=100, blank=True, null=True)
    name_ru = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("news:category_detail", kwargs={"slug": self.slug})
    
    def get_translate_name(self):
        from django.utils import translation
        lang = translation.get_language()
        if lang == "en" and self.name_en:
            return self.name_en
        elif lang == "ru" and self.name_ru:
            return self.name_ru
        return self.name


# Custom Manager (PublishedManager) ni tashqarida aniqlaymiz
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=self.model.Status.PUBLISHED)


class News(models.Model):

    class Status(models.TextChoices):
        DRAFT = 'Df', 'Draft'
        PUBLISHED = 'Pu', 'Published'
        ARCHIVED = 'Ar', 'Archived'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    content = models.TextField()
    # 🌍 Tarjima maydonlari
    
    title_en = models.CharField(max_length=250, blank=True, null=True)
    title_ru = models.CharField(max_length=250, blank=True, null=True)

    content_en = models.TextField(blank=True, null=True)
    content_ru = models.TextField(blank=True, null=True)

    image = models.ImageField(upload_to='news/images/', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='news', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='news')
    published_at = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.DRAFT
    )

    views = models.PositiveIntegerField(default=0) # Ko'rishlar soni

    # Managers
    objects = models.Manager()   # Default manager
    published = PublishedManager()  # Custom manager faqat PUBLISHED postlarni qaytaradi

    def get_translated_title(self):
        lang = translation.get_language()
        if lang == 'en' and self.title_en:
            return self.title_en
        elif lang == 'ru' and self.title_ru:
            return self.title_ru
        return self.title  # default uzbekcha

    def get_translated_content(self):
        lang = translation.get_language()
        if lang == 'en' and self.content_en:
            return self.content_en
        elif lang == 'ru' and self.content_ru:
            return self.content_ru
        return self.content  # default uzbekcha
    class Meta:
        ordering = ['-published_at']

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("news:news_detail", kwargs={"slug": self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug:  
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField (auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_at']
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return f'Comment by {self.author.username} - {self.news.title}'

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Contact Message'
        verbose_name_plural = 'Contact Messages'

    def __str__(self):
        return f'Message from {self.name} <{self.email}>'
