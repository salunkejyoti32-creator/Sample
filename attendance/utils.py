from django.http import HttpRequest

def ensure_django_request(request):
    """Return a django.http.HttpRequest instance.

    If a DRF Request is passed, it will return the underlying _request attribute.
    Otherwise returns the object unchanged.
    """
    # DRF Request wraps Django HttpRequest at attribute _request
    underlying = getattr(request, '_request', request)
    if isinstance(underlying, HttpRequest):
        return underlying
    return request
