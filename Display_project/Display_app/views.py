from django.shortcuts import render

# Create your views here.

def add_number(request):
    if request.method == 'POST':
        num1 = int(request.POST.get('num1'))
        num2 = int(request.POST.get('num2'))
        res = num1 + num2
       # print(res)
        context = {'result': res}
        return render(request, 'Display_app/add.html',context)
    return render(request, 'Display_app/add.html')


