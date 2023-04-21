from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render

from .repository import ContactRepository

contact_repository = ContactRepository()


@login_required(redirect_field_name='login')
def index(request):
    contacts = contact_repository.order_all_by("id")

    paginator = Paginator(contacts, 30)
    page = request.GET.get("page")
    contacts = paginator.get_page(page)

    return render(request, "contacts.html", {"contacts": contacts})


@login_required(redirect_field_name='login')
def contact(request, id):
    try:
        contact = contact_repository.get_by_id(id)

        if contact.disabled:
            raise Exception()
    except Exception:
        raise Http404()

    return render(request, "contact.html", {"contact": contact})


@login_required(redirect_field_name='login')
def search(request):
    term = request.GET.get("term")

    if not term:
        messages.add_message(
            request,
            messages.ERROR,
            "Search term is required"
        )

    contacts = contact_repository.search_by(term)

    paginator = Paginator(contacts, 30)
    page = request.GET.get("page")
    contacts = paginator.get_page(page)

    return render(request, "search.html", {"contacts": contacts})
