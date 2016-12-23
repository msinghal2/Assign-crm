from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import EmployeeInfo, Assignment, Delegation

class IndexView(generic.ListView):
    template_name = 'assign/index.html'
    context_object_name = 'emp_list'

    def get_queryset(self):
        return EmployeeInfo.objects.all()

class DetailView(generic.DetailView):
    model = EmployeeInfo
    template_name = 'assign/detail.html'

class EmpCreate(CreateView):
    model = EmployeeInfo
    # fields = ['employeeName', 'address', 'email', 'photo']
    fields = ['employeeName', 'email']

class EmpUpdate(UpdateView):
    model = EmployeeInfo
    # fields = ['employeeName', 'address', 'email', 'photo']
    fields = ['employeeName', 'email']

class EmpDelete(DeleteView):
    model = EmployeeInfo
    success_url = reverse_lazy('assign:index')

#Assignment views

class AssignIndexView(generic.ListView):
    template_name = 'assign/assignindex.html'
    context_object_name = 'assign_list'

    def get_queryset(self):
        return Assignment.objects.all()

class AssignDetailView(generic.DetailView):
    model = Assignment
    template_name = 'assign/assigndetail.html'

class AssignCreate(CreateView):
    model = Assignment
    # fields = ['employeeName', 'address', 'email', 'photo']
    fields = ['assignee', 'abuilding', 'afloor', 'aroom']

    def form_valid(self, form):
        temp = self.request.user.get_full_name()
        form.instance.assignor = temp
        building = form.cleaned_data['abuilding']
        floor = form.cleaned_data['afloor']
        room = form.cleaned_data['aroom']
        q = EmployeeInfo.objects.get(employeeName=temp)
        r = q.delegation_set.all()

        for x in r:
            ferror1 = 0
            ferror2 = 0
            if floor == x.dfloor or x.dfloor == 'all':
                ferror1=1
            if building == x.dbuilding or x.dbuilding == 'all':
                ferror2=1
            if ferror1 == 1 and ferror2 == 1:
                return super(AssignCreate, self).form_valid(form)
        form.add_error(None, 'You are not delegated to this combination of building and floor')
        return self.form_invalid(form)
        # return super(AssignCreate, self).form_valid(form)

class AssignDelete(DeleteView):
    model = Assignment
    success_url = reverse_lazy('assign:assignindex')

class AssignUpdate(UpdateView):
    model = Assignment
    fields = ['assignee', 'abuilding', 'afloor', 'aroom']

    def form_valid(self, form):
        temp = self.request.user.get_full_name()
        form.instance.assignor = temp
        building = form.cleaned_data['abuilding']
        floor = form.cleaned_data['afloor']
        room = form.cleaned_data['aroom']
        q = EmployeeInfo.objects.get(employeeName=temp)
        r = q.delegation_set.all()

        for x in r:
            ferror1 = 0
            ferror2 = 0
            if floor == x.dfloor or x.dfloor == 'all':
                ferror1 = 1
            if building == x.dbuilding or x.dbuilding == 'all':
                ferror2 = 1
            if ferror1 == 1 and ferror2 == 1:
                return super(AssignCreate, self).form_valid(form)
        form.add_error(None, 'You are not delegated to this combination of building and floor')
        return self.form_invalid(form)

#Delegation views

class DelegIndexView(generic.ListView):
    template_name = 'assign/delegindex.html'
    context_object_name = 'deleg_list'

    def get_queryset(self):
        return Delegation.objects.all()

class DelegDetailView(generic.DetailView):
    model = Delegation
    template_name = 'assign/delegdetail.html'

class DelegCreate(CreateView):
    model = Delegation
    # fields = ['employeeName', 'address', 'email', 'photo']
    fields = ['delegated', 'dbuilding', 'dfloor', 'dwing']

    def form_valid(self, form):
        temp = self.request.user.get_full_name()
        form.instance.delegator = temp
        building = form.cleaned_data['dbuilding']
        floor = form.cleaned_data['dfloor']
        wing = form.cleaned_data['dwing']
        q = EmployeeInfo.objects.get(employeeName=temp)
        r = q.delegation_set.all()

        for x in r:
            ferror1 = 0
            ferror2 = 0
            if floor == x.dfloor or x.dfloor == 'all':
                ferror1 = 1
            if building == x.dbuilding or x.dbuilding == 'all':
                ferror2 = 1
            if ferror1 == 1 and ferror2 == 1:
                return super(DelegCreate, self).form_valid(form)
        form.add_error(None, 'You are not delegated to this combination of building and floor')
        return self.form_invalid(form)
        # return super(DelegCreate, self).form_valid(form)

class DelegDelete(DeleteView):
    model = Delegation
    success_url = reverse_lazy('assign:delegindex')

class DelegUpdate(UpdateView):
    model = Delegation
    fields = ['delegated', 'dbuilding', 'dfloor', 'dwing']

    def form_valid(self, form):
        temp = self.request.user.get_full_name()
        form.instance.delegator = temp
        building = form.cleaned_data['dbuilding']
        floor = form.cleaned_data['dfloor']
        wing = form.cleaned_data['dwing']
        q = EmployeeInfo.objects.get(employeeName=temp)
        r = q.delegation_set.all()

        for x in r:
            ferror1 = 0
            ferror2 = 0
            if floor == x.dfloor or x.dfloor == 'all':
                ferror1 = 1
            if building == x.dbuilding or x.dbuilding == 'all':
                ferror2 = 1
            if ferror1 == 1 and ferror2 == 1:
                return super(DelegCreate, self).form_valid(form)
        form.add_error(None, 'You are not delegated to this combination of building and floor')
        return self.form_invalid(form)