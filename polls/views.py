from django.views.generic import ListView
from .models import Post

class home_page_view(ListView):
    model = Post
    template_name = 'polls/home.html'
    

