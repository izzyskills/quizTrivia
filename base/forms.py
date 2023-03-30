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
        fields = ["address", "mobile", "profile_pic"]


class CourseCreationForm(forms.ModelForm):
    class Meta:
        model = models.Course
        fields = "__all__"
        exclude = ["uploaded_by"]


class QuizForm(forms.Form):
    def __init__(self, session_id, *args, **kwargs):
        super(QuizForm, self).__init__(*args, **kwargs)
        questions = session_id.questions.all()
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
                required=True,
            )

    def check_answers(self, session_id):
        questions = session_id.questions.all()
        correct_count = 0
        for question in questions:
            answer = self.cleaned_data[str(question.id)]
            if answer == str(question.answer):
                correct_count += 1
        return correct_count
