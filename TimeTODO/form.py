import datetime

from django import forms
from django.forms import widgets
from django.contrib.auth.models import User

from .models import TODO

Radio_CHOICES = [
    ('True', "True"),
    ('False', "False")
]


class TODOForm(forms.ModelForm):
    todo_title = forms.CharField(max_length="200")
    todo_contents = forms.Textarea()
    todo_is_prior = forms.ChoiceField(choices=Radio_CHOICES, widget=widgets.RadioSelect())
    todo_has_expire_date = forms.ChoiceField(choices=Radio_CHOICES, widget=widgets.RadioSelect())
    todo_expire_date = forms.DateTimeField(initial=datetime.datetime.now)

    class Meta:
        model = TODO
        fields = ('todo_title', 'todo_contents', 'todo_is_prior', 'todo_has_expire_date', 'todo_expire_date',)


class TODOUpdateForm(forms.ModelForm):
    todo_title = forms.CharField(max_length="200")
    todo_contents = forms.Textarea()
    todo_is_prior = forms.ChoiceField(choices=Radio_CHOICES, widget=widgets.RadioSelect())
    todo_has_expire_date = forms.ChoiceField(choices=Radio_CHOICES, widget=widgets.RadioSelect())
    todo_is_finished = forms.ChoiceField(choices=Radio_CHOICES, widget=widgets.RadioSelect())
    todo_expire_date = forms.DateTimeField(initial=datetime.datetime.now)

    class Meta:
        model = TODO
        fields = (
            'todo_title', 'todo_contents', 'todo_is_prior', 'todo_has_expire_date', 'todo_is_finished',
            'todo_expire_date',)


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', ]
