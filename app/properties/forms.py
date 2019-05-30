from django import forms


class SearchPropertyForm(forms.Form):
    city = forms.CharField(label='City', max_length=100)
    people = forms.IntegerField(label='People')
    date_from = forms.DateField(label='Date from') #, input_formats=['%d-%m-%Y'])
    date_to = forms.DateField(label='Date to')
