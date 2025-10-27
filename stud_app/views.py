from django.shortcuts import render
from stud_app.models import StudentModel

from django.views.generic import View

# Create your views here.

# create student 

class CreateStudView(View):

    def get(self,request):

        return render(request,"create_stud.html")
    
    def post(self,request):

        print(request.POST)

        StudentModel.objects.create(name = request.POST.get('username'),
                                    email = request.POST.get('email'),
                                     course = request.POST.get('course'),
                                     age = request.POST.get('age')
                                    )

        return render(request,"create_stud.html")


# read student

class ReadView(View):

    def get(self,request):

        data = StudentModel.objects.all()

        return render(request,"list_stud.html",{'data':data})
    

# update view

class UpdateView(View):

    def get(self,request):

        data = StudentModel.objects.get(id = 3)

        return render(request,"update.html",{'data':data})
    

# deleteview

class DeleteView(View):
     
     def get(self,request):
          
          data = StudentModel.objects.get(id=1)

          data.delete()

          return render(request,"create_stud.html")
          


         
