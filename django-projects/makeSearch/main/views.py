import json
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View, TemplateView, ListView, DeleteView
from django.db.models import Q


from .models import Player
from .forms import ManagerAddForm
# Create your views here.


class PlayerAddView(View):
    form_class = ManagerAddForm
    template_name = 'form_template.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            print("not valid")

        return render(request, self.template_name, {'form': form})


class IndexTemplateView(TemplateView):
    template_name = 'index.html'
    extra_context = {"help": "help from django !"}


class PlayerListView(ListView):
    model = Player
    template_name = 'index.html'
    context_object_name = 'players'
    paginate_by = 2


def searchPageView(request):
    players = Player.objects.all()

    data = {
        "players": players
    }
    return render(request, "index.html", context=data)


def resultPageView(request):
    q = request.GET.get("query")
    # print(type(q))
    if len(q) >= 3:
        # query = Player.objects.filter(name__icontains=q)
        query = Player.objects.filter(
            Q(name__icontains=q) | Q(club__name__icontains=q) | Q(
                country__name__icontains=q)
        )
        return render(request, "result.html", {"object_list": query})
    return render(request, "result.html")


@csrf_exempt
def inlineSearch(request):
    data = json.loads(request.body)
    q = data.get('q')
    res = list(Player.objects.filter(
        Q(name__icontains=q) | Q(club__name__icontains=q) | Q(
            country__name__icontains=q)
    ).values())
    # print(res)
    data = {
        "object_list": res
    }
    return JsonResponse(data)
