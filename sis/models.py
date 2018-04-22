# from django.db import models
# # Create your models here.
# from django.contrib.auth.models import User
# from django.db.models import DecimalField
#
#
# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     choice = (('Female', 'Female'), ('Male', 'Male'), ('Other', 'Other'))
#     picture = models.ImageField(upload_to='profile_images', blank=True)
#     gender = models.CharField(max_length=6, choices=choice)
#     contact = models.BigIntegerField(unique=True)
#     choice1 = (('CSC', 'CSC'), ('CSE', 'CSE'), ('MEC', 'MEC'), ('CVL', 'CVL'), ('ECE', 'ECE'))
#     branch = models.CharField(max_length=6, choices=choice1)
#     choice2 = (('2015', '2015'), ('2016', '2016'), ('2017', '2017'), ('2018', '2018'))
#     year = models.CharField(max_length=6, choices=choice2)
#     club1 = models.ForeignKey(Clubs, on_delete=models.CASCADE)
#     club2 = models.ForeignKey(Clubs, on_delete=models.CASCADE)
#     club3 = models.ForeignKey(Clubs, on_delete=models.CASCADE)
#
#     def __unicode__(self):
#         return self.user.username
#
#
# class Marksheets(models.Model):
#     username = models.ForeignKey(User, on_delete=models.CASCADE)
#     picture = models.ImageField(upload_to='marksheets', blank=True)
#     sgpa = models.DecimalField(max_digits=5, decimal_places=2)
#     cgpa = models.DecimalField(max_digits=5, decimal_places=2)
#     semester = models.IntegerField()
#
#
# class News(models.Model):
#     description = models.CharField(max_length=500)
#     date = models.DateField()
#     time = models.TimeField()
#     picture = models.ImageField(upload_to='news', blank=True)
#     heading = models.CharField(max_length=30)
#
#
# class Hostel(models.Model):
#     username = models.ForeignKey(User, on_delete=models.CASCADE)
#     choice2 = (
#     ('Tower A', 'Tower A'), ('Tower B', 'Tower B'), ('Apartment A', 'Apartment A'), ('Apartment B', 'Apartment B'),
#     ('Apartment C', 'Apartment C'), ('Apartment D', 'Apartment D'))
#     hostel = models.CharField(max_length=15, choices=choice2)
#     room_no = models.IntegerField()
#     choice1 = (('AC', 'AC'), ('Non-AC', 'Non-AC'))
#     room_type = models.CharField(max_length=7, choices=choice1)
#
#
# class DAC(models.Model):
#     username = models.ForeignKey(User, on_delete=models.CASCADE)
#     points = models.IntegerField()
#     reason = models.CharField(max_length=300)
#     date = models.DateField()
#
#
# class Clubs(models.Model):
#     name = models.CharField(max_length=30)
#
#
# class Club_Events(models.Model):
#     club_name = models.ForeignKey(Clubs, on_delete=models.CASCADE)
#     event_name = models.CharField(max_length=30)
#     event_description = models.CharField(max_length=300)
#     date = models.DateField()
#     time = models.TimeField()
#
#
# class Exams(models.Model):
#     subject = models.CharField(max_length=20)
#     year = models.IntegerField()
#     semester = models.IntegerField()
#