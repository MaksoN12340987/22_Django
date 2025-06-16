from django import forms  # type: ignore


class PostForm(forms.Form):
    post_name = forms.CharField(max_length=100, label="Название поста", required=True)
    post_description = forms.EmailField(
        label="Описание поста", initial="Опшите новость", required=False
    )
    post_view = forms.CharField(
        widget=forms.CheckboxInput, label="Видно всем", required=True
    )
