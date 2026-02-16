import requests

from django.shortcuts import render, redirect
from django.views import generic
from django.http import JsonResponse

from .forms import ContactForm

BASE_URL = "https://jsonplaceholder.typicode.com"


class HomeView(generic.TemplateView):
    template_name = 'myapp/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        response = requests.get(f"{BASE_URL}/posts")
        context['posts'] = response.json()[:5]  
        return context


class ItemListView(generic.TemplateView):
    template_name = 'myapp/item_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        response = requests.get(f"{BASE_URL}/posts")
        context['items'] = response.json()
        return context


class ItemDetailView(generic.TemplateView):
    template_name = 'myapp/item_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        response = requests.get(f"{BASE_URL}/posts/{pk}")
        context['item'] = response.json()
        return context

class ItemCreateView(generic.TemplateView):
    template_name = 'myapp/not_available.html'

class ItemUpdateView(generic.TemplateView):
    template_name = 'myapp/not_available.html'

class ItemDeleteView(generic.TemplateView):
    template_name = 'myapp/not_available.html'


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return redirect('myapp:home')
    else:
        form = ContactForm()
    return render(request, 'myapp/contact.html', {'form': form})


def api_items(request):
    response = requests.get(f"{BASE_URL}/posts")
    return JsonResponse(response.json(), safe=False)


