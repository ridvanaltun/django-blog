from django.db import models

class Blog(models.Model):
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name="Username")
    title = models.CharField(max_length=120, verbose_name="Title")
    content = models.TextField(verbose_name="Content")
    thumbnail = models.ImageField(blank=True, null=True, verbose_name="Thumbnail", upload_to='images/blog/thumbnail/')
    created_date = models.DateTimeField(auto_now=True, verbose_name="Created Date")

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=50, verbose_name="Name")
    email = models.EmailField(verbose_name='Email', blank=False, null=False)
    title = models.CharField(max_length=200, verbose_name="Title")
    message = models.TextField(blank=True, null=True, verbose_name='Message')
    created_date = models.DateTimeField(auto_now=True, verbose_name="Date")

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return self.title