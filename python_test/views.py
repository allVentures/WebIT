from django.shortcuts import render
from django.views import View

from python_test.models import Client


class MainPage(View):
    def get(self, request):
        all_clients = Client.objects.all()
        for cl in all_clients:
            print(cl.id)

        ctx = {"all_clients": all_clients}
        return render(request, "main_page.html", ctx)
