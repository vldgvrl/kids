from django import forms

class GetTime(forms.Form):
    start_time = forms.TimeField(label = 'From:')
    end_time = forms.TimeField(label = 'To:')
