from django.db import models
from django.contrib.auth.models import User


class Limit(models.Model):
    limit = models.IntegerField(default=0)
    set_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.limit)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile", null=True)
    limit = models.ForeignKey(Limit, on_delete=models.CASCADE, related_name="my_limit")

    def __str__(self):
        return str(self.user.username)


class Category(models.Model):
    title = models.CharField(max_length=100)
    emoji = models.CharField(max_length=100, blank=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="categories", null=True)

    def __str__(self):
        return str(self.title)


class Expense(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="expenses", null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    amount = models.PositiveSmallIntegerField(blank=False)
    set_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.amount)