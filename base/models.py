from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    """this is contains additional info that is not in the User Model"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(
        upload_to="profile_pic/Student/", null=True, blank=True
    )
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20, null=False)

    @property
    def get_name(self):
        return self.user.first_name + " " + self.user.last_name

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
    questions = models.FileField(upload_to="questions/", max_length=100)
    # to separate and know who made a quiz.
    uploaded_by = models.ForeignKey(Profile, on_delete=models.SET("deleted user"))

    def __str__(self) -> str:
        return self.course_name


class Question(models.Model):
    """this is for submitted questions"""

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    optionA = models.CharField(max_length=200)
    optionB = models.CharField(max_length=200)
    optionC = models.CharField(max_length=200)
    optionD = models.CharField(max_length=200)
    answer = models.PositiveSmallIntegerField()


class SessionID(models.Model):
    """this is to identify questions taken at a particular time."""

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    time_taken = models.DateTimeField(auto_now_add=True)
    questions = models.ManyToManyField(Question, related_name="questions", blank=True)
    mark = models.PositiveIntegerField(null=True, blank=True)
    no_question = models.PositiveIntegerField()

    class Meta:
        ordering = ["-time_taken"]

    def __str__(self):
        return f"{self.course.course_code} {self.profile}"

