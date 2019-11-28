from django import forms


class NumberForm(forms.Form):
    number = forms.IntegerField(label="",
                                widget=forms.NumberInput(
                                    attrs={'class': 'form-control', 'placeholder': 'Enter integer'}),
                                min_value=1)
