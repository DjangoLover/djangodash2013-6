from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt

from models import Action, Request


@csrf_exempt
def services(request):
    r = Request(request_method=request.method,
                request_path=request.path,
                request_accept=request.META['HTTP_ACCEPT'],
                request_body=request.body)
    try:
        action = Action.objects.get(request_method=request.method,
                                    request_path=request.path,
                                    request_accept=request.META['HTTP_ACCEPT'])
    except ObjectDoesNotExist:
        r.response_status_code = 404
        r.save()
        return HttpResponse(status=404)
    else:
        r.response_status_code = action.response_status_code
        r.response_content = action.response_content
        r.response_content_type = action.response_content_type
        r.save()
        return HttpResponse(status=action.response_status_code,
                            content=action.response_content,
                            content_type=action.response_content_type)
