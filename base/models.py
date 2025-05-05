from django.db import models

class Message(models.Model):
    alert_id = models.IntegerField()  # Link to alert ID from your JSON
    username = models.CharField(max_length=100)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} on alert {self.alert_id}"
