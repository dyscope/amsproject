from django.db import models

class Anime(models.Model):
     title = models.CharField("Title", max_length=100)
     synopsis = models.TextField("Synopsis")
     img = models.ImageField("Image", upload_to="image/%Y/%m")
     started_airing = models.DateField("Started airing")
     finished_airing = models.DateField("Finished airing")
     publish_date = models.DateField("Publish date")
     
     def __str__(self) -> str:
          return f"{self.title}, {self.started_airing}"

     class Meta:
          verbose_name = "Anime"
          verbose_name_plural = "Animes"