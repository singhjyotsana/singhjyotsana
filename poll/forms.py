from django.db import models
from django.db.models import fields
from django.forms import ModelForm

from .models import poll

class Createpollform(ModelForm):
    class meta:
        model = poll
        fields = ['question','option_one','option_two','option_three','option_four','option_five',]