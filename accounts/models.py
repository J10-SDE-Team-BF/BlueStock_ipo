
from django.db import models

# Create your models here.
from django.db import models

class User(models.Model):  
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    staff_status = models.BooleanField(default=False)

    class Meta:
        db_table = "users"  # Maps to bf_info.users in PostgreSQL
