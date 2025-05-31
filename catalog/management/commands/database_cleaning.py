from django.core.management.base import BaseCommand
from catalog.models import Student


class Command(BaseCommand):
    help = "Delite test data to the databases"

    def handle(self):
        studens = Student.objects.all()

        for student in studens:
            student.delete()
            if student:
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Successfully delite: {student.first_name} {student.last_name}"
                    )
                )
            else:
                self.stdout.write(
                    self.style.WARNING(
                        f"Student already not exists: {student.first_name} {student.last_name}"
                    )
                )
