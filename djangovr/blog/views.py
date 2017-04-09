from django.shortcuts import render

# Create your views here.
def my_memoUI(request):
    return render(request, 'blog/my_memoUI.html', {})
