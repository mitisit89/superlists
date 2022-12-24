from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from lists.models import Item


def home_page(
    request: HttpRequest,
) -> HttpResponse:
    if request.method == "POST":
        Item.objects.create(text=request.POST["item_text"])
        return redirect("/lists/the-one-and-only-list-in-the-world/")
    return render(request, "home.html")


def view_list(request: HttpRequest) -> HttpResponse:
    items = Item.objects.all()
    return render(request, "list.html", {"items": items})
