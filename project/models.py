from django.db import models


class ReadingMaterial(models.Model):
    contentId = models.IntegerField()
    sectionId = models.IntegerField()
    contentTopic = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return f"{self.contentTopic}"
