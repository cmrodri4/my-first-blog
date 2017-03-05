from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    """Class describing a user's post."""

    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        """Method to publis a post."""
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        """Return post title."""
        return self.title

    def approved_comments(self):
        """Method to filter approved comments."""
        return self.comments.filter(approved_comment=True)


class Comment(models.Model):
    """Class describing a comment on  post."""

    post = models.ForeignKey('myapp.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField()
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        """Method to authorize and save a comment."""
        self.approved_comment = True
        self.save()

    def __str__(self):
        """Return comment."""
        return self.text
