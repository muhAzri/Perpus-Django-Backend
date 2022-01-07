from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from perpus.settings import LOGIN_URL
from perpustakaan.models import *
from perpustakaan.forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from perpustakaan.resource import BookResource

def export_xls(request):
    book =BookResource()
    dataset = book.export()
    response = HttpResponse(dataset.xls, content_type='apllication/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment: filename="report_book.xls"'
    return response

def home(request):
    return HttpResponse('Halaman Home')

@login_required(login_url=LOGIN_URL)
def signup(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User Created")
            return redirect('signup')
        else:
            messages.error(request, "Error")
            return redirect('signup')
    else:
        form = UserCreationForm()
        context = {
            'form':form
        }

    return render(request, 'signup.html',context)

@login_required(login_url=LOGIN_URL)
def buku(request):
    books = Book.objects.all()

    context = {
        'books' : books
    }
    return render(request, 'buku.html', context)

@login_required(login_url=LOGIN_URL)
def hapus_buku(request, book_id):
    book = Book.objects.filter(id=book_id)
    book.delete()
    messages.success(request, "Data Berhasil Dihapus!")

    return redirect('buku')

@login_required(login_url=LOGIN_URL)
def ubah_buku(request, book_id):
    book = Book.objects.get(id=book_id)
    template = 'ubah-buku.html'
    if request.POST:
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            messages.success(request, 'Data updated')
            form.save()
            return redirect('ubah_buku', book_id=book_id)
    else :
        form = BookForm(instance=book)
        context = {
            'form':form,
            'book':book,
        }

        return render (request, template, context)

def penerbit(request):
    return HttpResponse("Halaman Penerbit")

@login_required(login_url=LOGIN_URL)
def tambah_buku(request):
    if request.POST:
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = BookForm()

            message= "Data saved"

            context = {
                'form' : form,
                'message' : message
            }

            return render(request, 'tambah-buku.html', context)

    else :
        form = BookForm()

    context = {
        'form' : form
    }

    return render(request, 'tambah-buku.html', context)