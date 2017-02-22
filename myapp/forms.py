from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    """Class used to add and edit posts using a Modelform."""

    class Meta:
        """Choose which model should be used to create PostForm."""

        model = Post
        fields = ('title', 'text',)
