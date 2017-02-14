from django.shortcuts import redirect

from functools import wraps


def anon_required(redirect_url):
    def accepter(func):
        @wraps(func)
        def decorator(request, *args, **kwargs):
            if "email" not in request.session.keys():
                return func(request, *args, **kwargs)
            else:
                return redirect(redirect_url)
        return decorator
    return accepter


def login_required(redirect_url):
    def accepter(func):
        @wraps(func)
        def decorator(request, *args, **kwargs):
            if "email" in request.session.keys():
                return func(request, *args, **kwargs)
            else:
                return redirect(redirect_url)
        return decorator
    return accepter
