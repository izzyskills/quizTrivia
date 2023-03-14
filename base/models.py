from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    """this is contains addtional info that is not in the User Model"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(
        upload_to='profile_pic/Student/', null=True, blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20, null=False)

    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name

    @property
    def get_instance(self):
        return self

    def __str__(self):
        return self.user.first_name


class Course(models.Model):
    """this is for the submitted quizzes """
    course_name = models.CharField(max_length=50)
    course_code = models.CharField(max_length=10)
    num_of_question = models.PositiveIntegerField()
    questions = models.FileField(upload_to='questions/', max_length=100)
    # to seprate and know who made a quiz.
    uploaded_by = models.ForeignKey(
        Profile, on_delete=models.SET("deleted user"))

    def __str__(self) -> str:
        return self.course_name


class SessionID(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    time_taken = models.DateTimeField(auto_now_add=True)


class Question(models.Model):
    """this is for submitted questions"""
    student = models.ForeignKey(Profile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    question_no = models.PositiveIntegerField()
    question_text = models.CharField(max_length=200)
    optionA = models.CharField(max_length=200)
    optionB = models.CharField(max_length=200)
    optionC = models.CharField(max_length=200)
    optionD = models.CharField(max_length=200)
    option_picked = models.PositiveSmallIntegerField(null=True)
    answer = models.PositiveSmallIntegerField()
    mark = models.PositiveSmallIntegerField(null=True)
    session_id = models.ForeignKey(SessionID, on_delete=models.CASCADE)
