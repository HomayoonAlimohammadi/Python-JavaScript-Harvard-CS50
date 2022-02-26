from django import forms
from .models import Category

class CreateListingForm(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(widget=forms.Textarea)
    category = forms.ModelMultipleChoiceField(queryset= Category.objects.all(), widget= forms.CheckboxSelectMultiple)
    starting_price = forms.FloatField()

class CreateCategoryForm(forms.Form):
    name = forms.CharField(max_length=20)

class CreateBidForm(forms.Form):
    amount = forms.FloatField()


class CreateCommentForm(forms.Form):
    content = forms.Textarea()
