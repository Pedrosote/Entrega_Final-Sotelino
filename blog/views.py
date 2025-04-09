from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.shortcuts import render, redirect
from .models import Post
from django.urls import reverse_lazy
from .forms import PostForm


def miblog(request):
    busqueda = request.GET.get("busqueda", None)
    if busqueda:
        miblog = Post.objects.filter(titulo__icontains=busqueda)
    else:
        miblog = Post.objects.all()
    return render(request, "blog/miblog.html", context={"posts" : miblog})

class PostListView(ListView):
    model = Post
    template_name = "blog/miblog.html"
    context_object_name = "posts"
    
    def get_queryset(self):
        queryset = super().get_queryset()
        busqueda = self.request.GET.get("busqueda", None)
        if busqueda:
            queryset = queryset.filter(titulo__icontains=busqueda)
        return queryset

def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            if request.user.is_authenticated:
                post.autor = request.user
                post.save()
                return redirect("blog:postlist")
            else:
                form.add_error(None, "debes estar logueado para crear una publicacion")
    else:
        form = PostForm()
    return render(request, "blog/post_create.html", context = {"form": form})

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy("blog:postlist")

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.autor = self.request.user
        else:
            form.add_error(None, "debes estar logueado para crear una publicacion")
            return self.form_invalid(form)
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy("blog:postlist")


class PostDetailView(DetailView):
    model = Post

class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy("blog:postlist")