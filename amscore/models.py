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


class Reviews(models.Model):
    name = models.CharField("Name", max_length=50)
    text_review = models.TextField("Review", max_length=1000)
    anime = models.ForeignKey(Anime, verbose_name="Anime", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.name}, {self.anime}"

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"