from django.contrib import messages
from django.forms import TextInput
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from extra_views import ModelFormSetView

from professors.models import Professors, Groups, UsersXProfessors, Tests, Students, ProfessorTypes


def formula(request):
    return render(request, "chair812/formula.html")


def index(request):
    return render(request, "chair812/base.html")


class ProfessorsListView(generic.ListView):
    model = Professors
    context_object_name = 'professors_list'
    queryset = Professors.objects.all()
    template_name = 'chair812/professors.html'


class ProfessorTypesListView(generic.ListView):
    model = ProfessorTypes
    context_object_name = 'professors_type_list'
    queryset = ProfessorTypes.objects.all()
    template_name = 'chair812/professors_type.html'


class GroupsListView(generic.ListView):
    model = Groups
    context_object_name = 'groups_list'
    template_name = 'chair812/groups_with_links.html'

    def get_queryset(self):
        user_id = self.request.user.pk
        type = self.kwargs.get('typeid', None)
        professor = UsersXProfessors.objects.filter(user_id=user_id).first()
        if type == 1:
            return Groups.objects.filter(lector_id=professor.professor_id)
        elif type == 2:
            return Groups.objects.filter(seminarist_id=professor.professor_id)

    def get_context_data(self, **kwargs):
        # В первую очередь получаем базовую реализацию контекста
        context = super(GroupsListView, self).get_context_data(**kwargs)
        # Добавляем новую переменную к контексту и иниуиализируем ее некоторым значением
        user_id = self.request.user.pk
        professor = UsersXProfessors.objects.filter(user_id=user_id).first()
        context['professor_name'] = Professors.objects.get(pk=professor.professor_id)
        return context


class ReferenceFormSetView(ModelFormSetView):
    model = Tests
    template_name = "chair812/tests_lector.html"
    fields = ['z1', 'z2', 'z3', 'z4', 'z5', 'z6', 'z7', 'z8', 'z9', 'z10', 'sum']
    factory_kwargs = {
        'extra': 0,
        'widgets': {
            'z1': TextInput(attrs={'size': '1'}),
            'z2': TextInput(attrs={'size': '1'}),
            'z3': TextInput(attrs={'size': '1'}),
            'z4': TextInput(attrs={'size': '1'}),
            'z5': TextInput(attrs={'size': '1'}),
            'z6': TextInput(attrs={'size': '1'}),
            'z7': TextInput(attrs={'size': '1'}),
            'z8': TextInput(attrs={'size': '1'}),
            'z9': TextInput(attrs={'size': '1'}),
            'z10': TextInput(attrs={'size': '1'}),
            'sum': TextInput(attrs={'size': '1'}),

        }
    }

    def get_queryset(self):
        user_id = self.request.user.pk
        professor = UsersXProfessors.objects.filter(user_id=user_id).first()
        group_id = self.kwargs.get('groupid', None)
        group = Groups.objects.filter(pk=group_id).first()
        if group.seminarist == professor.professor:
            self.template_name = "chair812/tests.html"
        elif group.lector == professor.professor:
            self.template_name = "chair812/tests_lector.html"

        return Tests.objects.filter(student__group_id=group_id).all()

    def get_success_url(self):
        return reverse('home')

    def formset_invalid(self, formset):
        """
        If the formset is invalid, re-render the context data with the
        data-filled formset and errors.
        """
        messages.error(self.request, "Error dummy")
        return self.render_to_response(self.get_context_data(formset=formset))
