from django import forms


class AddReviewForm(forms.Form):
    review_text = forms.CharField()
    marks = [('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7), ('8', 8), ('9', 9), ('10', 10)]
    rating = forms.ChoiceField(widget=forms.RadioSelect, choices=marks)


class RegisterForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

