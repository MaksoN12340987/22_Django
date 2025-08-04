from django import forms

from config.settings import WORDS_PROHIBITED

from .models import Product


class CreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "name",
            "description",
            "price",
            "image",
            "category",
            "on_sale",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["name"].widget.attrs.update(
            {
                "class": "contact-form-catalog",
                "placeholder": "Введите наименование продукта",
            }
        )
        self.fields["description"].widget.attrs.update(
            {
                "class": "contact-form-catalog",
                "placeholder": "Введите описание продукта",
            }
        )
        self.fields["price"].widget.attrs.update(
            {"class": "contact-form-catalog", "type": "date"}
        )
        self.fields["category"].widget.attrs.update(
            {"class": "form-select", "type": "date"}
        )
        self.fields["image"].widget.attrs.update({"class": "img"})
        self.fields["on_sale"].widget.attrs.update({"class": "form-check"})

    def clean(self):
        data_array = super().clean()
        name = data_array.get("name")
        description = data_array.get("description")

        if name.lower() in WORDS_PROHIBITED:  # type: ignore
            self.add_error(
                "name", "В наименовании продукта присутствуют недопустимые слова"
            )
        elif description.lower() in WORDS_PROHIBITED:  # type: ignore
            self.add_error(
                "description", "В описании продукта присутствуют недопустимые слова"
            )

        repetitions_name = 0
        item = ""
        for i, value in enumerate(name):  # type: ignore
            if i > 0:
                if item == value:
                    repetitions_name += 1
                item = value
            elif i == 0:
                item = value

        repetitions_description = 0
        item = ""
        for i, value in enumerate(description):  # type: ignore
            if i > 0:
                if item == value:
                    repetitions_description += 1
                item = value
            elif i == 0:
                item = value

        if repetitions_name > 5:
            self.add_error("name", "Странно много повторяющихся символов...")
        elif repetitions_description > 5:
            self.add_error("description", "Странно много повторяющихся символов...")

        return data_array

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price < 0:  # type: ignore
            self.add_error("price", "Цена продукта не должна быть отрицательной")

        return price


class UpdateProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "name",
            "description",
            "price",
            "image",
            "category",
            "on_sale",
            "owner",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["name"].widget.attrs.update(
            {
                "class": "contact-form-catalog",
                "placeholder": "Введите наименование продукта",
            }
        )
        self.fields["description"].widget.attrs.update(
            {
                "class": "contact-form-catalog",
                "placeholder": "Введите описание продукта",
            }
        )
        self.fields["price"].widget.attrs.update(
            {"class": "contact-form-catalog", "type": "date"}
        )
        self.fields["image"].widget.attrs.update({"class": "contact-form"})
        self.fields["on_sale"].widget.attrs.update({"class": "form-check"})
        self.fields["owner"].widget.attrs.update(
            {"class": "form-select", "type": "date"}
        )

    def clean(self):
        data_array = super().clean()
        name = data_array.get("name")
        description = data_array.get("description")

        if name.lower() in WORDS_PROHIBITED:  # type: ignore
            self.add_error(
                "name", "В наименовании продукта присутствуют недопустимые слова"
            )
        elif description.lower() in WORDS_PROHIBITED:  # type: ignore
            self.add_error(
                "description", "В описании продукта присутствуют недопустимые слова"
            )

        repetitions_name = 0
        item = ""
        for i, value in enumerate(name):  # type: ignore
            if i > 0:
                if item == value:
                    repetitions_name += 1
                item = value
            elif i == 0:
                item = value

        repetitions_description = 0
        item = ""
        for i, value in enumerate(description):  # type: ignore
            if i > 0:
                if item == value:
                    repetitions_description += 1
                item = value
            elif i == 0:
                item = value

        if repetitions_name > 5:
            self.add_error("name", "Странно много повторяющихся символов...")
        elif repetitions_description > 5:
            self.add_error("description", "Странно много повторяющихся символов...")

        return data_array

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price < 0:  # type: ignore
            self.add_error("price", "Цена продукта не должна быть отрицательной")

        return price
