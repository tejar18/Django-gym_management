from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Status(models.Model):
    status = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.status

class Alpha(models.Model):
    alphabet = models.CharField(max_length=30, null=True)
    def __str__(self):
        return self.alphabet

class Batch(models.Model):
    name = models.CharField(max_length=30, null=True)
    timing = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

class DietPlan(models.Model):
    meal = models.CharField(max_length=30, null=True)
    timing = models.CharField(max_length=100, null=True)
    what_to_eat = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.meal+" "+self.timing

class Member(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE, null=True)
    contact = models.CharField(max_length=10, null=True)
    address = models.CharField(max_length=10, null=True)
    height = models.CharField(max_length=10, null=True)
    weight = models.CharField(max_length=10, null=True)
    doj = models.DateField(max_length=10, null=True)
    dob = models.DateField(max_length=10, null=True)
    image = models.FileField(null=True)

    def __str__(self):
        return self.user.first_name

class Trainer(models.Model):
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    contact = models.CharField(max_length=10, null=True)
    address = models.CharField(max_length=10, null=True)
    doj = models.DateField(max_length=10, null=True)
    dob = models.DateField(max_length=10, null=True)
    image = models.FileField(null=True)

    def __str__(self):
        return self.user.first_name

class Product(models.Model):
    name = models.CharField(max_length=10, null=True)
    price = models.CharField(max_length=10, null=True)
    image = models.FileField(null=True)

    def __str__(self):
        return self.name

class Package(models.Model):
    name = models.CharField(max_length=10, null=True)
    price = models.CharField(max_length=10, null=True)
    image = models.FileField(null=True)

    def __str__(self):
        return self.name

class Activity(models.Model):
    name = models.CharField(max_length=10, null=True)
    image = models.FileField(null=True)

    def __str__(self):
        return self.name

class PackageActivity(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, null=True)
    package = models.ForeignKey(Package, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.activity.name+" "+self.package.name

class MemberPackage(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE, null=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE, null=True)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, null=True)
    dop = models.DateField(null=True)

    def __str__(self):
        return self.member.user.username+" "+self.package.name

class BatchActivity(models.Model):
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE, null=True)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, null=True)
    notes = models.FileField(null=True)
    date1 = models.DateField(null=True)

    def __str__(self):
        return self.batch.name+" "+self.activity.name

class TrainerActivity(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, null=True)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, null=True)
    timing = models.CharField(max_length=100,null=True)
    day1 = models.CharField(max_length=20,null=True)

    def __str__(self):
        return self.trainer.user.username+" "+self.activity.name

class TimeTable(models.Model):
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE, null=True)
    dot = models.DateField(null=True)

    def __str__(self):
        return self.batch.name

class Attendance(models.Model):
    trainer_activity = models.ForeignKey(TrainerActivity, on_delete=models.CASCADE, null=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE, null=True)
    attend = models.CharField(max_length=20,null=True)
    dot = models.DateField(null=True)

    def __str__(self):
        return self.member.user.username

class BatchMember(models.Model):
    trainer_activity = models.ForeignKey(TrainerActivity, on_delete=models.CASCADE, null=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.trainer_activity.trainer.user.username+" "+self.member.user.username

class Cart(models.Model):
    member = models.ForeignKey(Member,on_delete=models.CASCADE,null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.member.user.username + " . " + self.product.name


class Booking(models.Model):
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE, null=True)
    booking_id = models.CharField(max_length=200,null=True)
    quantity = models.CharField(max_length=100,null=True)
    book_date = models.CharField(max_length=30, null=True)
    total = models.IntegerField(null=True)

    def __str__(self):
        return self.book_date+" "+self.member.user.username

class Tips(models.Model):
    title = models.CharField(max_length=100,null=True)
    desc = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.title

