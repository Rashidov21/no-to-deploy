from .models import Category


def main(request):
    context = {
        "categories": Category.objects.all()
    }
    return context
