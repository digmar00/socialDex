from django.contrib.auth.models import User
from django.db import models
from .utils import send_transaction
import hashlib


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    hash = models.CharField(max_length=32, default=0, null=True)
    tx_id = models.CharField(max_length=66, default=0, null=True)

    # Useful method to write the post on the blockchain
    def write_on_chain(self):
        # To avoid exceeding the max_length of the InputData field,SHA-256 hash function is performed on the content
        self.hash = hashlib.sha256(self.content.encode('utf-8')).hexdigest()
        self.tx_id = send_transaction(self.hash)
        self.save()
