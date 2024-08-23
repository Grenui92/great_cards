from django.shortcuts import redirect


def class_login_required(func):
    """A decorator to check if a user is logged in before accessing
    a class-based view.
    """
    def inner(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(to='news:main')
        return func(self, request, *args, **kwargs)
    return inner


def func_login_required(func):
    """A decorator to check if a user is logged in before accessing
    a function-based view.
    """
    def inner(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(to='news:main')
        return func(request, *args, **kwargs)
    return inner
