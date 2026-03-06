from django.db import models

class Incident(models.Model):

    STATUS_CHOICES = [
        ('New', 'New'),
        ('InProgress', 'In Progress'),
        ('Resolved', 'Resolved'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='New'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title