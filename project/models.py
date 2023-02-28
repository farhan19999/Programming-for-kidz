from django.db import models


class ReadingMaterial(models.Model):
    contentId = models.IntegerField()
    sectionId = models.IntegerField()
    contentTopic = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return f"{self.contentTopic}"

class Course(models.Model):
    course_name = models.CharField(max_length=50)
    course_level= models.CharField(max_length=10)               #beginner,medium,hard
    short_description=models.CharField(max_length=100)          #to show in course list

    def __str__(self):
        return f"{self.course_name}"

class Mcq(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    question = models.CharField(max_length = 100)
    right_option = models.CharField(max_length = 20)
    wrong_option1 = models.CharField(max_length = 20)
    wrong_option2 = models.CharField(max_length = 20)
    wrong_option3 = models.CharField(max_length = 20)

