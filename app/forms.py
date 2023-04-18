from django import forms
G=[('MALE','male'),('FEMALE','female')]
T=[['RCB','rcb'],('SRH','srh'),['CSK','csk']]
class CricketForm(forms.Form):
    Name=forms.CharField(max_length=100)
    Age=forms.IntegerField()
    Email=forms.CharField()
    Date=forms.DateTimeField()
    Password=forms.CharField(max_length=100,widget=forms.PasswordInput)
    Address=forms.CharField(max_length=100,widget=forms.Textarea(attrs={'cols':5,'rows':5}))
    #Gender=forms.ChoiceField(choices=G)
    Gender=forms.ChoiceField(choices=G,widget=forms.RadioSelect)
    #Team=forms.MultipleChoiceField(choices=T)
    Team=forms.MultipleChoiceField(choices=T,widget=forms.CheckboxSelectMultiple)

