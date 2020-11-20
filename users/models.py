from django.db import models

from django.contrib.auth.models import User

class Customer(User):
    pass
    
    def get_products(self):
        pass