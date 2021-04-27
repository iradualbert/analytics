import json
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .models import Post


@csrf_exempt
@require_POST
def add_view(request):
    data = json.loads(request.body)
    title = data.get('title')
    slug = data.get('slug')
    url = data.get('url')
    # print(data)
    # return JsonResponse({"status": "ok"})
    try:
        post = Post.objects.get(slug=slug)
        post.views = 1 + post.views
        post.save()
        post.add_view()
    
    except ObjectDoesNotExist:
        post = Post(
            title=title,
            slug=slug,
            url=url
        )
        post.save()
        post.add_view()
    
    return JsonResponse({'status': 'ok'}, status=201)    
    