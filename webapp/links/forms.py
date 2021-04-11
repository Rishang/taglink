from django import forms
from .models import Link, Category


class rssUrl:

    def __init__(self, url):
        self.url = url


class addLink(forms.ModelForm):

    def __init__(self,user_id,*args,**kwargs):
        super ().__init__(*args,**kwargs)
        self.fields['category'].queryset = Category.objects.filter(user=user_id)

    class Meta:
        model = Link
        fields = ["url","title","description","imageUrl","category","tags"]
