from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . import models


class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "password1", "password2"]


class ProfileCreationForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ["profile_pic"]


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)


class CourseCreationForm(forms.ModelForm):
    class Meta:
        model = models.Course
        fields = "__all__"
        exclude = ["uploaded_by"]


class QuizForm(forms.Form):
    def __init__(self, sessions, *args, **kwargs):
        super(QuizForm, self).__init__(*args, **kwargs)
        questions = sessions.questions.all()
        for question in questions:
            self.fields[str(question.id)] = forms.ChoiceField(
                label=question.question_text,
                choices=[
                    (1, question.optionA),
                    (2, question.optionB),
                    (3, question.optionC),
                    (4, question.optionD),
                ],
                widget=forms.RadioSelect,
                required=False,
            )

    def check_answers(self, sessions):
        questions = sessions.questions.all()
        print(self.cleaned_data)
        correct_count = 0
        for question in questions:
            answer = self.cleaned_data.get(str(question.id))
            if answer and answer == str(question.answer):
                correct_count += 1
        return correct_count
