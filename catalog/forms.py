from django import forms  # type: ignore

from .models import Users  # type: ignore

from config.settings import WORDS_PROHIBITED # type: ignore


class ContactForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ["name", "surname", "birthday", "image"]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['name'].widget.attrs.update({
            'class': 'contact-form-catalog',
            'placeholder': 'Введите имя'
        })
        self.fields['surname'].widget.attrs.update({
            'class': 'contact-form-catalog',
            'placeholder': 'Введите фамилию'
        })
        self.fields['birthday'].widget.attrs.update({
            'class': 'contact-form-catalog',
            'type': 'date'
        })
        self.fields['image'].widget.attrs.update({
            'class': 'form-check'
        })

    def clean(self):
        data_array = super().clean()
        name = data_array.get("name")
        surname = data_array.get("surname")

        if name == surname:
            self.add_error("content", "Имя и Фамилия совпадают")

        repetitions_name = 0
        item = ""
        for i, value in enumerate(name):
            if i > 0:
                if item == value:
                    repetitions += 1
                item = value
            elif i == 0:
                item = value

        repetitions_surname = 0
        item = ""
        for i, value in enumerate(surname):
            if i > 0:
                if item == value:
                    repetitions += 1
                item = value
            elif i == 0:
                item = value

        if repetitions_name or repetitions_surname > 5:
            self.add_error("content", "Странно много повторяющихся символов...")



# class UpdatePostForm(forms.ModelForm):
#     class Meta:
#         model = Posts
#         fields = ["title", "content", "preview", "number_views", "publication_flag"]

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
        
#         self.fields['title'].widget.attrs.update({
#             'class': 'form-control-CreatePost',
#             'placeholder': 'Отредактируйте заголовок'
#         })
#         self.fields['content'].widget.attrs.update({
#             'class': 'form-control-CreatePost',
#             'placeholder': 'Отредактируйте описание'
#         })
#         self.fields['preview'].widget.attrs.update({
#             'class': 'form-control-CreatePost'
#         })
#         self.fields['publication_flag'].widget.attrs.update({
#             'class': 'form-check-input'
#         })



#     def clean(self):
#         data_array = super().clean()
#         title = data_array.get("title")
#         content = data_array.get("content")

#         if content == title:
#             self.add_error("content", "Заголовок и описание одинаковые")

#         if len(content) < 40:
#             self.add_error("content", "Скудное описание(")

#         repetitions = 0
#         item = ""
#         for i, value in enumerate(content):
#             if i > 0:
#                 if item == value:
#                     repetitions += 1
#                 item = value
#             elif i == 0:
#                 item = value

#         if repetitions > 4:
#             self.add_error("content", "Странно много повторяющихся символов...")

#         self.fields["field_name"].widget.attrs.update(
#             {"class": "form-control", "placeholder": "Текст плейсхолдера"}
#         )
