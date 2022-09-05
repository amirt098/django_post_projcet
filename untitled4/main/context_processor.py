from .models import  Tag,Category

def wiki_context_processor(request):
    return {
        'tags': Tag.objects.all(),
        'categorys': Category.objects.all(),

    }