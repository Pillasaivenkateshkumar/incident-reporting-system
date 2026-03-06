from django.db import models

class Incident(models.Model):

    STATUS_CHOICES = [
        ('New', 'New'),
        ('InProgress', 'In Progress'),
        ('Resolved', 'Resolved'),
    ]
    SEVERITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    comments = models.TextField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='New'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title