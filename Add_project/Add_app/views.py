from django.shortcuts import render

# Create your views here.


def add_number(request):
    if request.method == 'POST':
        NUM1 = int(request.POST.get('NUM1'))
        NUM2 = int(request.POST.get('NUM2'))
        res = NUM1 + NUM2

        context = {'result':res}
        return render(request, 'Add_app/add.html',context)
    return render(request, 'Add_app/add.html')

