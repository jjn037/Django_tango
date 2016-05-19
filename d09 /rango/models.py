from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class Students(models.Model):
    name = models.CharField(max_length=100)
    grade = models.CharField(max_length=100)
    card_no = models.IntegerField(primary_key=True)   # default=0 important!!!
    sex = models.CharField(max_length=100)
    slug = models.SlugField(default=0)
    picture = models.ImageField(upload_to='profile_images', default='media', blank=True)

    def save(self, *args, **kwargs):

        self.slug = slugify(self.name)
        super(Students, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Students"

    def __unicode__(self):
        return self.name


# class UserProfile(models.Model):
#     user =models.OneToOneField(User)

