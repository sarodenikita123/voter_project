from django.shortcuts import render, redirect
from .forms import VoterForm
from .models import Voter
from django.http import HttpResponse


def handler404(request, exception):
    return render(request, 'crud_app/error.html', status=404)


def create_view(request):
    template_name = "crud_app/create.html"
    form = VoterForm()
    if request.method == "POST":
        form = VoterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Register successfully!!!!")
    context = {"form": form}
    return render(request, template_name, context)


def show_view(request):
    template_name = "crud_app/show.html"
    obj = Voter.objects.all()
    form = VoterForm()
    context = {"obj": obj}
    return render(request, template_name, context)


def details(request, pk):
    template_name = "crud_app/details.html"
    obj = Voter.objects.get(id=pk)
    form = VoterForm(instance=obj)
    context = {"obj": obj}
    return render(request, template_name, context)


def update_view(request, pk):
    template_name = "crud_app/create.html"
    obj = Voter.objects.get(id=pk)
    form = VoterForm(instance=obj)
    if request.method == 'POST':
        form = VoterForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("show_url")
    context = {"form": form}
    return render(request, template_name, context)


def delete_view(request, pk):
    template_name = "crud_app/confirm.html"
    obj = Voter.objects.get(id=pk)
    form = VoterForm(instance=obj)
    if request.method == "POST":
        obj.delete()
        return redirect("show_url")
    return render(request, template_name)


