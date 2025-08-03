from django.core.management.base import BaseCommand

from blog.models import Posts


class Command(BaseCommand):
    help = "Delete test data to the databases"

    def handle(self, *args, **kwargs):
        posts = Posts.objects.all()

        for post in posts:
            post.delete()
            if post:
                self.stdout.write(
                    self.style.SUCCESS(f"Successfully delete: {post.title}")
                )
            else:
                self.stdout.write(self.style.WARNING(f"Student already not exists"))
