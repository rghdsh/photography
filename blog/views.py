from django.shortcuts import render

def blog(raquest):
    return render(raquest,'blog/blog.html')