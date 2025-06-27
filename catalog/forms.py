from django import forms  # type: ignore

from .models import Product  # type: ignore

from config.settings import WORDS_PROHIBITED # type: ignore


class ContactForm(forms.ModelForm):
    class Meta:
        model = Product
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

        return data_array

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0: # type: ignore
            self.add_error('price', '')
        
        return price
