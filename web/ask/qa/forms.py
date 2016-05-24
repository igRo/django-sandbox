from django import forms
from qa.models import Question, Answer


class AskForm(forms.Form):
    title = forms.CharField(min_length=1, max_length=150)
    text = forms.CharField(min_length=1, widget=forms.Textarea)

    def save(self):
        post = Question(**self.cleaned_data)
        post.save()
        return post


class AnswerForm(forms.Form):
    text = forms.CharField(min_length=1, widget=forms.Textarea)
    id = forms.IntegerField()

    def clean_id(self):
        id = self.cleaned_data['id']
        try:
            question = Question.objects.get(pk=id)
        except Question.DoesNotExist:
            raise forms.ValidationError('Question %s not found' % id)
        return question

    def save(self):
        post = Answer(**self.cleaned_data)
        post.save()
        return post
