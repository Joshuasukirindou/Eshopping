from django.db import models


class Message(models.Model):
    id = models.AutoField(primary_key=True)
    message = models.TextField()

    class Meta:
        db_table = 'estore_message'


class EstoreUser(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_password = models.TextField()
    user_name = models.TextField()
    user_level = models.IntegerField()
    login_status = models.TextField()
    is_banned = models.IntegerField()
    is_delete = models.IntegerField()
    is_approved = models.IntegerField()

    class Meta:
        db_table = 'estore_user'

    def __str__(self):
        return f"User ID: {self.user_id}, User Name: {self.user_name}"
