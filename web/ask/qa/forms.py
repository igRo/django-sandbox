from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from qa.models import Question, Answer


class AskForm(forms.Form):
    title = forms.CharField(min_length=1, max_length=255)
    text = forms.CharField(min_length=1, widget=forms.Textarea)

    def save(self):
        question = Question(**self.cleaned_data)
        question.author_id = self._user.id
        question.save()
        return question


class AnswerForm(forms.Form):
    text = forms.CharField(min_length=1, widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput)

    def clean_question(self):
        question_id = self.cleaned_data['question']
        try:
            question = Question.objects.get(pk=question_id)
        except Question.DoesNotExist:
            raise forms.ValidationError('Question %s not found' % id)
        return question

    def save(self):
        answer = Answer(**self.cleaned_data)
        answer.author_id = self._user.id
        answer.save()
        return answer


class LoginForm(forms.Form):
    username = forms.CharField(min_length=1, max_length=255, required=True)
    password = forms.CharField(min_length=1, max_length=255, widget=forms.PasswordInput, required=True)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user:
            raise forms.ValidationError('Authorization failed')
        self.cleaned_data['user'] = user
        return self.cleaned_data

    def save(self):
        return self.cleaned_data['user']


class SignupForm(LoginForm):
    email = forms.EmailField(min_length=1, max_length=255, required=True)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError('Username "%s" already used' % username)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('Email "%s" already used' % email)

    def clean(self):
        if self._errors:
            raise forms.ValidationError('Registration failed')
        User.objects.create_user(**self.cleaned_data)
        return super(SignupForm, self).clean()
