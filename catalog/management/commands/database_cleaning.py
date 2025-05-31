from django.core.management.base import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Delite test data to the databases"

    def handle(self, *args, **kwargs):
        studens = Product.objects.all()

        for student in studens:
            student.delete()
            if student:
                self.stdout.write(
                    self.style.SUCCESS(f"Successfully delite: {student.name}")
                )
            else:
                self.stdout.write(self.style.WARNING(f"Student already not exists"))

        categories = Category.objects.all()

        for category in categories:
            category.delete()
            if category:
                self.stdout.write(
                    self.style.SUCCESS(f"Successfully delite: {category.name}")
                )
            else:
                self.stdout.write(self.style.WARNING(f"Student already not exists"))
