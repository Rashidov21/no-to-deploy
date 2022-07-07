from .models import Product, Category


def main_context(request):
    # print(dir(request.session))
    # print(type(request.session))
    # print(request.session["counter"])
    if "counter" in request.session:
        cnt = request.session["counter"] + 1
    else:
        cnt = 1
    request.session["counter"] = cnt
    # print(request.session.test_cookie_worked())
    # request.session.set_expiry()
    # py manage.py clearsessions - hamma sessiyani ochirish
    # request.session.flush() - sesiyani butunlay tozalaydi
    # request.session.set_test_cookie() - client brauzeri cookie ni support qiladimi yomio aniqlash uchun

    context = {
        'status': 200
    }
    return context
