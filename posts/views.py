from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from posts.models import Post
from datetime import datetime
from django.http import HttpResponse, JsonResponse


# Create your views here.
class Index(ListView):
    template_name = 'index.html'

    # context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Post.objects.order_by('-publication_date')[:5]


def create(request):
    return render(request, 'create.html')


def store(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['title']
        result = Post.objects.create(
            title=title,
            content=content,
            author=request.user
            # title=request.POST['email'],
        )
        return redirect('posts:detail', result.id)


class Detail(DetailView):
    template_name = 'detail.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(deleted_date__isnull=True)


def delete(request, pk):
    if request.method == 'DELETE':
        post = Post.objects.get(id=pk)
        post.deleted_date = datetime.now()
        post.save()
        return JsonResponse(post)
