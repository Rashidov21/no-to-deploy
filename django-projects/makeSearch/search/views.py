from django.shortcuts import render


from django.contrib.postgres.search import SearchQuery, SearchVector

from django.db.models import Max, Avg, Count, Q

from main.models import Player
# Create your views here.


def searchMethodView(request):
    q = request.GET.get("query")
    # p = Player.objects.aggregate(Avg('age'))
    # m = Player.objects.aggregate(Max('age'))
    # print(m)
    obj = Player.objects.annotate(filter=Q(rating__lte=80))
    print(obj)
    # obj = Player.objects.annotate(search=SearchVector("name", "club__name")).filter(
    #     search=q)
    # print(obj)
    return render(request, 'search.html')


# class SearchClassView(ListView):
#     model = Player
#     template_name = 'search.html'
