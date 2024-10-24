# В классе декораторе в инит передаётся функция,
# в __call__ происходит проверка, а также либо вызов результирующей функции, либо вызов другой нужной функции


class HandlerGET:
    def __init__(self, func):
        self.func = func

    def __call__(self, request, *args, **kwargs):
        m = request.get('method', 'GET')
        if m == 'GET':
            return self.get(self.func, request)
        return None

    def get(self, func, request, *args, **kwargs):
        return f"GET: {func(request)}"

@HandlerGET
def contact(request):
    return "Сергей Балакирев"

contact({"method": "GET", "url": "contact.html"})