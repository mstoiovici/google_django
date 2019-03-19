from django.shortcuts import render
from django.utils import timezone
from .models import Post, Item, ShoppingItem
from .forms import PostForm
from django.shortcuts import redirect

# Create your views here.


def item_list(request):
    posts= Post.objects.filter(published_date__lte=timezone.now()).order_by("published_date")
    items=Item.objects.order_by("created_date")
    shoppingItems=ShoppingItem.objects.order_by("created")
    return render(request, 'blog/item_list.html', {"posts":posts, "items":items, "shoppingItems":shoppingItems})



#this one is not working - i get the form but I can't link it to the database
"""
def item_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            item=form.save(commit=False)

            item.author = request.user
            """
            #post.created_date = timezone.now()
            """
            item.save()
            msg="something"
            #at least I'm getting here, cause I get stuck with an error because of this variable msg="something"
            return redirect( 'item_list', {"msg":msg})
        else:
            msg="Print message if doesn't work"
            return render( request, 'blog/item_edit.html', {'form': form, "msg":msg})


    else:
        form= PostForm()
    return render(request, 'blog/item_edit.html', {'form': form})
"""


#this one is working to add blogs
"""
def item_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('item_list')
    else:
        form = PostForm()
    return render(request, 'blog/item_edit.html', {'form': form})
"""

def item_new(request):
    if request.method == "POST":
        if "taskAdd" in request.POST:
            title = request.POST["description"]
            date = str(request.POST["date"])
