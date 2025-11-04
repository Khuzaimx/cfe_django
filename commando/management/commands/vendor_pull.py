from django.core.management.base import BaseCommand


VENDOR_STATICFILES ={

    "flowbite.min.css": "https://cdn.jsdelivr.net/npm/flowbite@3.1.2/dist/flowbite.min.css",
    "flowbite.min.js": "https://cdn.jsdelivr.net/npm/flowbite@3.1.2/dist/flowbite.min.js",
}

class Command(BaseCommand):
    help = "Prints a hello world message"

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS("Hello, world!"))
