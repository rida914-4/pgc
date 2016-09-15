from django import forms
import datetime
from models import Item
from crispy_forms.helper import FormHelper


class NameForm(forms.Form):
    # your_name = forms.CharField(label='Your name', max_length=100)
    new_date = forms.DateField(initial=datetime.date.today, required=False, error_messages={'required': 'Your Name is Required'})
    item_combo = forms.ModelChoiceField(queryset=Item.objects.all(), error_messages={'required': 'Item is Required'}, required=False)
    new_parc = forms.CharField(max_length=200, required=False)
    new_vid = forms.CharField(max_length=50, required=False)
    detail_table = forms
    class Meta:
        model = Item
        fields = ['description']

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50, required=False)
    file = forms.FileField(required=False)


class FileFieldForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField()
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

