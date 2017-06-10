from django import forms
from .models import Appreq

class PostForm(forms.ModelForm):

    class Meta:
        model = Appreq
        fields = ('title', 'purpose', 'ename', 'cname', 'mail', 'phone', 'start_date', 'end_date')
