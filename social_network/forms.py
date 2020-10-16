from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    content = forms.CharField(required=True, widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}))

    class Meta:
        model = Post
        fields = ['content']

    # I check if the word "hack" has been inserted in the post form
    def clean_content(self):
        content = self.cleaned_data.get("content")
        if "hack" in content:
            raise forms.ValidationError("La parola hack non è ammessa")
        else:
            return content
