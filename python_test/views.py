from django.db.models import Q
from django.db import IntegrityError
from django.shortcuts import render
from django.views import View
from python_test.forms import AddClientForm, SearchClientForm

from python_test.models import Client


class MainPage(View):
    def get(self, request):
        all_clients = Client.objects.all()
        ctx = {"all_clients": all_clients}
        return render(request, "main_page.html", ctx)


class ShowClientDetails(View):
    def get(self, request, id):
        client = Client.objects.get(pk=id)
        ctx = {"client": client}
        return render(request, "show_user_details.html", ctx)


class AddClient(View):
    def get(self, request):
        form = AddClientForm()
        ctx = {"form": form}
        return render(request, "add_new_client.html", ctx)

    def post(self, request):
        form = AddClientForm(request.POST)
        if form.is_valid():
            client_name = form.cleaned_data["client_name"]
            email = form.cleaned_data["email"]
            phone = form.cleaned_data["phone"]
            contact_name = form.cleaned_data["contact_name"]
            street = form.cleaned_data["street"]
            house_number = form.cleaned_data["house_number"]
            suburb = form.cleaned_data["suburb"]
            post_code = form.cleaned_data["post_code"]
            state = form.cleaned_data["state"]
            try:
                Client.objects.create(
                    client_name=client_name,
                    email=email,
                    phone=phone,
                    contact_name=contact_name,
                    street=street,
                    house_number=house_number,
                    suburb=suburb,
                    post_code=post_code,
                    state=state
                )
            except IntegrityError:
                ctx = {"form": form, "error": "This client name already exists in the database!"}
                return render(request, "add_new_client.html", ctx)

            msg = "New Client Created!"
            ctx = {"form": form, "msg": msg}
            return render(request, "add_new_client.html", ctx)
        else:
            ctx = {"form": form}
        return render(request, "add_new_client.html", ctx)


class ModifyClient(View):
    def get(self, request, id):
        client_to_modify = Client.objects.get(pk=id)
        form = AddClientForm(initial={"client_name": client_to_modify.client_name,
                                      "email": client_to_modify.email,
                                      "phone": client_to_modify.phone,
                                      "contact_name": client_to_modify.contact_name,
                                      "street": client_to_modify.street,
                                      "house_number": client_to_modify.house_number,
                                      "suburb": client_to_modify.suburb,
                                      "post_code": client_to_modify.post_code,
                                      "state": client_to_modify.state,
                                      })
        ctx = {"form": form, "client": client_to_modify}
        return render(request, "modify_client.html", ctx)

    def post(self, request, id):
        form = AddClientForm(request.POST)
        client_to_modify = Client.objects.get(pk=id)
        if form.is_valid():
            client_name = form.cleaned_data["client_name"]
            email = form.cleaned_data["email"]
            phone = form.cleaned_data["phone"]
            contact_name = form.cleaned_data["contact_name"]
            street = form.cleaned_data["street"]
            house_number = form.cleaned_data["house_number"]
            suburb = form.cleaned_data["suburb"]
            post_code = form.cleaned_data["post_code"]
            state = form.cleaned_data["state"]
            try:
                Client.objects.filter(pk=id).update(
                    client_name=client_name,
                    email=email,
                    phone=phone,
                    contact_name=contact_name,
                    street=street,
                    house_number=house_number,
                    suburb=suburb,
                    post_code=post_code,
                    state=state,
                )
            except IntegrityError:
                ctx = {"form": form, "client": client_to_modify,
                       "error": "This client name already exists in the database!"}
                return render(request, "modify_client.html", ctx)

            msg = "Data Modified!!"
            ctx = {"msg": msg, "client": client_to_modify}
            return render(request, "modify_client.html", ctx)
        else:
            ctx = {"form": form, "client": client_to_modify}
            return render(request, "modify_client.html", ctx)


class DeleteClient(View):
    def get(self, request, id):
        client_to_delete = Client.objects.get(pk=id)
        client_to_delete.delete()
        ctx = {"msg": " Client Deleted!"}
        return render(request, "standard_msg_page.html", ctx)


class SearchClient(View):
    def get(self, request):
        form = SearchClientForm()
        ctx = {"form": form}
        return render(request, "search_client.html", ctx)

    def post(self, request):
        form = SearchClientForm(request.POST)
        if form.is_valid():
            client_name = form.cleaned_data["client_name"]
            email = form.cleaned_data["email"]
            phone = form.cleaned_data["phone"]
            suburb = form.cleaned_data["suburb"]
            sorting = int(form.cleaned_data["sorting"])
            order = int(form.cleaned_data["order"])

            if sorting == 1 and order == 1:
                sort_order = 'client_name'
            elif sorting == 1 and order == 2:
                sort_order = '-client_name'
            elif sorting == 2 and order == 1:
                sort_order = 'suburb'
            elif sorting == 2 and order == 2:
                sort_order = '-suburb'
            elif sorting == 3 and order == 1:
                sort_order = 'email'
            elif sorting == 3 and order == 2:
                sort_order = '-email'
            elif sorting == 4 and order == 1:
                sort_order = 'phone'
            elif sorting == 4 and order == 2:
                sort_order = '-phone'
            else:
                sort_order = 'id'

            results = Client.objects.filter(
                Q(client_name__contains=client_name) & Q(email__contains=email) &
                Q(phone__contains=phone) & Q(suburb__contains=suburb)).order_by(sort_order)

            ctx = {"form": form, "reults": results}
            return render(request, "search_client.html", ctx)
        else:
            ctx = {"form": form}
            return render(request, "search_client.html", ctx)
