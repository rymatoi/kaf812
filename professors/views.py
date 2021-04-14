from django.contrib import messages
from django.forms import TextInput
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from extra_views import ModelFormSetView

from professors.models import Professors, Groups, UsersXProfessors, Students, ProfessorTypes


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
    model = Students
    template_name = "chair812/tests.html"
    fields = ['z1', 'z2', 'z3', 'z4', 'z5', 'z6', 'z7', 'z8', 'z9', 'z10', 'sum']

    def get_context_data(self, **kwargs):
        # В первую очередь получаем базовую реализацию контекста
        context = super(ReferenceFormSetView, self).get_context_data(**kwargs)
        # Добавляем новую переменную к контексту и иниуиализируем ее некоторым значением
        user_id = self.request.user.pk
        group_id = self.kwargs.get('groupid', None)
        group = Groups.objects.filter(pk=group_id).first()
        professor = UsersXProfessors.objects.filter(user_id=user_id).first()
        if self.request.user.is_superuser:
            context['professor_type'] = 1
        elif group.seminarist == professor.professor:
            context['professor_type'] = 1
        elif group.lector == professor.professor:
            context['professor_type'] = 2

        context['lector'] = group.lector
        context['seminarist'] = group.seminarist
        context['group'] = group.name

        return context

    def get_queryset(self):
        user_id = self.request.user.pk
        professor = UsersXProfessors.objects.filter(user_id=user_id).first()
        group_id = self.kwargs.get('groupid', None)
        group = Groups.objects.filter(pk=group_id).first()
        self.factory_kwargs['widgets'] = {}
        self.factory_kwargs['extra'] = 0
        if self.request.user.is_superuser:
            widgets = ['z1', 'z2', 'z3', 'z4', 'z5', 'z6', 'z7', 'z8', 'z9', 'z10']
            for widget in widgets:
                self.factory_kwargs['widgets'][widget] = TextInput(
                    attrs={'size': '1', 'id': 'input', 'onchange': 'input_changed(this);', 'max': '2', 'min': '0',
                           'type': "number"})
            self.factory_kwargs['widgets']['sum'] = TextInput(
                attrs={'size': '1'})
        elif group.seminarist == professor.professor:
            widgets = ['z1', 'z2', 'z3', 'z4', 'z5', 'z6', 'z7', 'z8', 'z9', 'z10']
            for widget in widgets:
                self.factory_kwargs['widgets'][widget] = TextInput(
                    attrs={'size': '1', 'id': 'input', 'onchange': 'input_changed(this);', 'max': '2', 'min': '0',
                           'type': "number"})
            self.factory_kwargs['widgets']['sum'] = TextInput(
                attrs={'size': '1'})
        elif group.lector == professor.professor:
            widgets = ['z1', 'z2', 'z3', 'z4', 'z5', 'z6', 'z7', 'z8', 'z9', 'z10']
            for widget in widgets:
                self.factory_kwargs['widgets'][widget] = TextInput(
                    attrs={'size': '1', 'id': 'input', 'onchange': 'input_changed(this);', 'max': '2', 'min': '0',
                           'type': "number",
                           "readonly": "True"})
            self.factory_kwargs['widgets']['sum'] = TextInput(
                attrs={'size': '1'})
        return Students.objects.filter(group_id=group_id).order_by('name')

    def get_success_url(self):
        return reverse('home')

    def formset_invalid(self, formset):
        """
        If the formset is invalid, re-render the context data with the
        data-filled formset and errors.
        """
        messages.error(self.request, "Error dummy")
        return self.render_to_response(self.get_context_data(formset=formset))


class AllGroupsListView(generic.ListView):
    model = Groups
    context_object_name = 'groups_list'
    template_name = 'chair812/groups_with_links.html'

    def get_queryset(self):
        if not self.request.user.is_superuser:
            return
        return Groups.objects.all()

    def get_context_data(self, **kwargs):
        # В первую очередь получаем базовую реализацию контекста
        context = super(AllGroupsListView, self).get_context_data(**kwargs)
        # Добавляем новую переменную к контексту и иниуиализируем ее некоторым значением
        user_id = self.request.user.pk
        professor = UsersXProfessors.objects.filter(user_id=user_id).first()
        context['professor_name'] = Professors.objects.get(pk=professor.professor_id)
        return context
