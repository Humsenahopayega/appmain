from django import forms
from .models import Appreq
from .models import User

class PostForm(forms.ModelForm):

    class Meta:
        model = Appreq
        fields = ('title', 'purpose', 'ename', 'cname', 'mail', 'phone', 'start_date', 'end_date')
class RegForm(forms.ModelForm):

    class Meta:
	    model = User
	    fields = ('name', 'mail')
