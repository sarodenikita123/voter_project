from django.db import models
import uuid


class Voter(models.Model):
    gen = [("Male", 'Male'), ("Female", "Female"), ("Other", "Other")]
    voter_id = models.CharField(max_length=10, unique=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=10, choices=gen)
    address = models. CharField(max_length=30)
    city = models.CharField(max_length=10)
    state = models.CharField(max_length=20)
    pincode = models.IntegerField()
    dob = models.DateField()
    contact = models.IntegerField()

    def save(self, *args, **kwargs):
        if not self.voter_id:
            self.voter_id = 'V' + uuid.uuid4().hex[:9].upper()
        super().save(*args, **kwargs)