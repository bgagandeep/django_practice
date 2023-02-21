from django.shortcuts import render
from django.views.generic import TemplateView, FormView, CreateView, ListView, DetailView, UpdateView, DeleteView
from classroom.forms import ContactForm
from django.urls import reverse_lazy
from classroom.models import Teacher

# Create your views here.
def home_view(request):
    return render(request, 'classroom/home.html', {})

class HomeView(TemplateView):
    template_name = 'classroom/home.html'

class ThankYouView(TemplateView):
    template_name = 'classroom/thank_you.html'

class TeacherCreateView(CreateView):
    template_name = 'classroom/teacher_form.html'
    model = Teacher
    fields = '__all__'
    success_url = reverse_lazy('classroom:thank_you')

class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'classroom/contact.html'
    success_url = reverse_lazy('classroom:thank_you')
    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class TeacherListView(ListView):
    model = Teacher
    queryset = Teacher.objects.order_by('first_name')
    template_name = 'classroom/teacher_list.html'
    context_object_name = 'teachers'

class TeacherDetailView(DetailView):
    model = Teacher
    template_name = 'classroom/teacher_detail.html'
    context_object_name = 'teacher'

class TeacherUpdateView(UpdateView):
    model = Teacher
    fields = '__all__'
    template_name = 'classroom/teacher_form.html'
    success_url = reverse_lazy('classroom:teacher_list')

class TeacherDeleteView(DeleteView):
    model = Teacher
    template_name = 'classroom/teacher_confirm_delete.html'
    success_url = reverse_lazy('classroom:teacher_list')