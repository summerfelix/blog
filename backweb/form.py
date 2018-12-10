from django import forms


class AddArtForm(forms.Form):
    title = forms.CharField(min_length=2, required=True)
    desc = forms.CharField(min_length=5, required=True)
    content = forms.CharField(required=True)
    tags = forms.CharField(min_length=2, required=True)
    titlepic = forms.ImageField(required=False)
    column = forms.CharField(required=True)

