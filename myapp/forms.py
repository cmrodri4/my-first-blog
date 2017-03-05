from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    """Class used to add and edit posts using a Modelform."""

    class Meta:
        """Choose which model should be used to create PostForm."""

        model = Post
        fields = ('title', 'text',)


class CommentForm(forms.ModelForm):
    """Class used to add comments to posts."""

    class Meta:
        """Assign comment model to form."""

        model = Comment
        fields = ('author', 'text',)
