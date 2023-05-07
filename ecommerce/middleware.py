from django.shortcuts import redirect


class AuthMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated and request.path in ['/cart/deliveryAddress/','/cart/']:
            request.session['next_url'] = request.path
            return redirect('login')
        elif request.user.is_authenticated and 'next_url' in request.session:
            next_url = request.session.pop('next_url')
            return redirect(next_url)
        return self.get_response(request)