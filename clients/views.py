import slug as slug
from django.contrib.auth.mixins import LoginRequiredMixin  # New
from django.shortcuts import redirect, render, get_object_or_404
from django.template.context_processors import request
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic import ListView, DetailView
from pip._vendor.requests import post
from .forms import CommentForm
from .models import models
from .models import Client, Comment
from django.urls import reverse_lazy


class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    template_name = 'client_list.html'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Client.objects.all()
        else:
            return Client.objects.filter(author=self.request.user)


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client
    template_name = 'client_detail.html'
    login_url = 'login'


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    fields = ('name', 'notes', 'address', 'city', 'state', 'zipcode', 'email', 'cell_phone', 'acct_number')
    template_name = 'client_edit.html'


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    template_name = 'client_delete.html'
    success_url = reverse_lazy('client_list')


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    template_name = 'client_new.html'
    fields = ('name', 'notes', 'address', 'city', 'state', 'zipcode', 'email', 'cell_phone', 'acct_number')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# def post_detailview(request, id):
#     if request.method == 'POST':
#         cf = CommentForm(request.POST or None)
#         if cf.is_valid():
#             content = request.POST.get('content')
#             comment = Comment.objects.create(post=post, user=request.user, content=content)
#             comment.save()
#             return redirect(post.get_absolute_url())
#         else:
#             cf = CommentForm()
#
#         context = {
#             'comment_form': cf,
#         }
#         return render(request, 'client_list.html', context)


class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'

    # fields = '__all__'
    # def form_valid(self, form):
    #     form.instance.post_id = self.kwargs['pk']
    #     return super().form_valid(form)
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    success_url = reverse_lazy('client_list')
