from django import forms
from .models import Appreq
from .models import User

class PostForm(forms.ModelForm):
    class Meta:
        model = Appreq
        fields = ('ename', 'title', 'purpose', 'start_date', 'end_date', 'myname', 'cname', 'mail', 'phone',)
        labels = {
                   'title': "Purpose",
                   'purpose': "Description",
                   'ename': "Employee's Name",
                   'cname': "Company",
                   'myname': "Your Name",
                   'mail': "Your Mail",
                   'phone': "Contact No.",
                   'start_date': "Start Time",
                   'end_date': "End Time",
    }
class RegForm(forms.ModelForm):
    class Meta:
	    model = User
	    fields = ('name', 'mail')
