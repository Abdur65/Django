from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        permissions = [
            ("can_view_mymodel", "Can view MyModel"),
        ]

    def __str__(self):
        return self.name
