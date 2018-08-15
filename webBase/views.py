from django.shortcuts import render

def frontpage(request):
    context = { 'request': request }
    return render( request, 'frontpage.html', context )
