from django.shortcuts import render

# Create your views here.

def mul_number(request):
    if request.method == 'POST':
        num1 = int(request.POST.get('num1'))
        num2 = int(request.POST.get('num2'))
        res = num1 * num2 

        context = {'result': res}
        return render(request,'mul_app/mul.html',context)
    return render(request,'mul_app/mul.html')
