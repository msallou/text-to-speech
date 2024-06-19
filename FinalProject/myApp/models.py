from django.db import models

class PreviousTextToSpeech(models.Model):
    date = models.DateTimeField()
    text = models.TextField()

    def __str__(self):
        return f"{self.date} - {self.text[0:50]}"
