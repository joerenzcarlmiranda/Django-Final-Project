from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        # Set default dropdown label for degree
        self.fields['degree'].empty_label = "Select Degree"
        # Make middle name optional
        self.fields['mname'].required = False
