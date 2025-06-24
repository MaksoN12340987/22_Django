from django import forms  # type: ignore

from .models import Posts  # type: ignore

from django.core.validators import EmailValidator, MaxLengthValidator  # type: ignore
from django.core.exceptions import ValidationError  # type: ignore


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ["title", "content", "preview", "publication_flag"]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['title'].widget.attrs.update({
            'class': 'form-control-CreatePost',
            'placeholder': 'Введите имя'
        })
        self.fields['content'].widget.attrs.update({
            'class': 'form-control-CreatePost',
            'placeholder': 'Введите фамилию'
        })
        self.fields['preview'].widget.attrs.update({
            'class': 'form-control-CreatePost'
        })
        self.fields['publication_flag'].widget.attrs.update({
            'class': 'form-check-input'
        })

    def clean(self):
        data_array = super().clean()
        title = data_array.get("title")
        content = data_array.get("content")

        if content == title:
            self.add_error("content", "Заголовок и описание одинаковые")

        if len(content) < 40:
            self.add_error("content", "Скудное описание(")

        repetitions = 0
        item = ""
        for i, value in enumerate(content):
            if i > 0:
                if item == value:
                    repetitions += 1
                item = value
            elif i == 0:
                item = value

        if repetitions > 4:
            self.add_error("content", "Странно много повторяющихся символов...")



class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ["title", "content", "preview", "number_views", "publication_flag"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['title'].widget.attrs.update({
            'class': 'form-control-CreatePost',
            'placeholder': 'Отредактируйте заголовок'
        })
        self.fields['content'].widget.attrs.update({
            'class': 'form-control-CreatePost',
            'placeholder': 'Отредактируйте описание'
        })
        self.fields['preview'].widget.attrs.update({
            'class': 'form-control-CreatePost'
        })
        self.fields['publication_flag'].widget.attrs.update({
            'class': 'form-check-input'
        })

    def clean(self):
        data_array = super().clean()
        title = data_array.get("title")
        content = data_array.get("content")

        if content == title:
            self.add_error("content", "Заголовок и описание одинаковые")

        if len(content) < 40:
            self.add_error("content", "Скудное описание(")

        repetitions = 0
        item = ""
        for i, value in enumerate(content):
            if i > 0:
                if item == value:
                    repetitions += 1
                item = value
            elif i == 0:
                item = value

        if repetitions > 4:
            self.add_error("content", "Странно много повторяющихся символов...")

        self.fields["field_name"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Текст плейсхолдера"}
        )
