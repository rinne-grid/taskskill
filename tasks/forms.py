# coding: utf-8
from django import forms
from tasks.models import TaskItem, TaskItemDetail


class LoginForm(forms.Form):
    username = forms.CharField(label="ユーザー",max_length=200)
    password = forms.CharField(label="パスワード",widget=forms.PasswordInput, max_length=30)


class TaskReportForm(forms.Form):
    task_item = forms.ModelChoiceField(queryset=TaskItem.objects.all())
    task_item_detail = forms.ModelChoiceField(queryset=TaskItemDetail.objects.all())
    memo = forms.CharField(widget=forms.Textarea, required=False)


    def clean(self):
        clnd = self.cleaned_data

        #if not self.is_valid():
        #    return clnd


