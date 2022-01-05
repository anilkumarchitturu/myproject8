from django.shortcuts import render
from django.views import View

# Create your views here.
class GetInput(View):
    def get(self,request):
        return render(request,'getinput.html')
class PostInput(View):
    def get(self, request):
        return render(request, 'posinput.html')
class Output(View):
    def get(self,request):
        try:
            x = (request.GET["t1"])
            y = int(request.GET["t2"])
            ope = request.GET["t3"]
            data = ""
            if ope == "add":
                z = int(x) + int(y)
                data = "The sum is:" + str(z)
            elif ope == "sub":
                z = int(x) - int(y)
                data = "The sub is:" + str(z)
            elif ope == "mul":
                z = int(x) * int(y)
                data = "The mul is:" + str(z)
            elif ope == "div":
                z = int(x) / int(y)
                data = "The div is:" + str(z)
            con_dic = {"res": data}
            return render(request, 'display.html', con_dic)
        except(ValueError):
            return render(request, 'getinput.html')
    def post(self,request):
        try:
            x = (request.POST["t1"])
            y = int(request.POST["t2"])
            ope = request.POST["t3"]
            data = ""
            if ope == "add":
                z = int(x) + int(y)
                data = "The sum is:" + str(z)
            elif ope == "sub":
                z = int(x) - int(y)
                data = "The sub is:" + str(z)
            elif ope == "mul":
                z = int(x) * int(y)
                data = "The mul is:" + str(z)
            elif ope == "div":
                z = int(x) / int(y)
                data = "The div is:" + str(z)
            con_dic = {"res": data}
            return render(request, 'display.html', con_dic)
        except(ValueError):
            return render(request, 'postinput.html')



