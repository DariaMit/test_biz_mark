from django import forms
from django.core.exceptions import ValidationError

from .models import *


class AddReviewForm(forms.Form):
    review_text = forms.CharField()
    # rating = forms.RadioSelect(attrs=())
    marks = [('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7), ('8', 8), ('9', 9), ('10', 10)]
    rating = forms.ChoiceField(widget=forms.RadioSelect, choices=marks)


    # def clean_title(self):
    #     title = self.cleaned_data['title']
    #     if len(title) > 200:
    #         raise ValidationError('Длина превышает 200 символов')

        # return title


class RegisterForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
            # 'login': forms.TextInput(),
            # 'password': forms.TextInput(),
        # }


# class SortingForm(forms.Form):
