from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = "__all__"


    def clean_title(self):
        title = self.cleaned_data.get("title")

        if "bangladesh" not in title.lower():
            raise forms.ValidationError("Title must contain the word 'Bangladesh'.")
        
        return title