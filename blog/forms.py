from django import forms

from Django.blog.models import Posts  # type: ignore


class CreatePostForm(forms.Form):
    class Meta:
        model = Posts
        fields = ['title', 'content', 'publication_flag']


class UpdatePostForm(forms.Form):
    class Meta:
        model = Posts
        fields = ['title', 'content', 'publication_flag']
