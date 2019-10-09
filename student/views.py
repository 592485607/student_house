from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import StudentForm
from .models import Student

from django.views import View
# Create your views here.
"""函数式实现"""
""" 1
def index(request):
    words = "World"
    return render(request, 'index.html', context={'words':words})
"""
""" 2
def index(request):
    students = Student.objects.all()
    print(students)
    return render(request, 'index.html', context={'students':students})
"""
""" 3
def index(request):
    # students = Student.objects.all()
    # 使用Model层封装的方法获取数据
    students = Student.get_all()
    print(students)
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            # form.cleaned_data对象，是form根据字段类型对用户提交的数据做完转换之后的结果
            cleaned_data = form.cleaned_data
            students = Student()
            students.name = cleaned_data['name']
            students.sex = cleaned_data['sex']
            students.email = cleaned_data['email']
            students.profession = cleaned_data['profession']
            students.qq = cleaned_data['qq']
            students.phone = cleaned_data['phone']
            form.save()
            # 使用reverse方法，我们在urls.py中定义index时，声明name='index',故这里可以通过reverse拿到对应的URL.
            return HttpResponseRedirect(reverse('index'))
    else:
        form = StudentForm()
    context = {
        'students':students,
        'form':form,
    }
    return render(request,'index.html',context=context)
"""
"""类方式实现 """
class IndexView(View):
    template_name = 'index.html'

    def get_context(self):
        students = Student.get_all()
        context = { 'students':students,}
        return context

    def get(self,request):
        context = self.get_context()
        form = StudentForm()
        context.update({'form':form})
        return render(request,self.template_name,context=context)

    def post(self,request):
        form = StudentForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
        context = self.get_context()
        context.update({'form': form})
        return render(request, self.template_name, context=context)
