from django.db import models

class addBlog(models.Model):
    name = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=100, null=True)
    content = models.CharField(max_length=100, null=True)
    date_added = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural = 'Add Blog'

    def __str__(self):
        return f'{self.name}'
