from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm
from django.core.paginator import Paginator
from django.db.models import Q
# Create your views here.

def student_list(request):
    search_query = request.GET.get('search', '')

    students = Student.objects.all()

    # 🔍 SEARCH
    if search_query:
        students = students.filter(
            Q(fname__icontains=search_query) |
            Q(mname__icontains=search_query) |
            Q(lname__icontains=search_query) |
            Q(degree__icontains=search_query)
        )

    # 📄 PAGINATION (5 students per page)
    paginator = Paginator(students, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'student_list': page_obj,
        'search_query': search_query
    }

    return render(request, "student_register/student_list.html", context)



def student_form(request):
    if request.method == "GET":
        # Show empty form
        form = StudentForm()
        return render(request, "student_register/student_form.html", {'form': form})
    else:
        # Process submitted form
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()  # Save data to database
            return redirect('/student/list')  # Redirect to list page
        else:
            # If form is invalid, show it again with errors
            return render(request, "student_register/student_form.html", {'form': form})

def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, "student_register/student_form.html", {'form': form})

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect('student_list')
