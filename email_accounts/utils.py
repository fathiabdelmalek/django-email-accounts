from django.shortcuts import redirect, reverse


def anonymous_required(view_func):
    def wrapped(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(request.GET.get('next', reverse(request.META.get('HTTP_REFERER') if request.META.get('HTTP_REFERER') else 'home')))
        return view_func(request, *args, **kwargs)
    return wrapped
