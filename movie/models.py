from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    year = models.CharField(max_length=4, null=True, blank=True)
    rated = models.CharField(max_length=255, default="N/A")
    released = models.CharField(max_length=50, null=True, blank=True)
    runtime = models.CharField(max_length=20, null=True, blank=True)
    genre = models.CharField(max_length=50, null=True, blank=True)
    director = models.CharField(max_length=100, null=True, blank=True)
    writer = models.CharField(max_length=100, null=True, blank=True)
    actors = models.CharField(max_length=255, null=True, blank=True)
    plot = models.TextField(max_length=1000, null=True, blank=True)
    language = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    awards = models.CharField(max_length=255, default="N/A")
    poster = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"
        ordering = ["-year"]


class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie')
    text = models.TextField(max_length=500)

    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        ordering = ["-created"]
