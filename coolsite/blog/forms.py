from django import forms
from django.core.exceptions import ValidationError

from .models import *

class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = "Category not chosen"

    class Meta:
        model = News
        fields = ["title", "slug", "content","photo", "is_published", "cat"]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows':10}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        print(type(title), "\n", title)
        if len(title) > 200:
            raise ValidationError("Length more than 200 simblos")
        if "ass" in title:
            raise ValidationError("Bad wards")

        return title