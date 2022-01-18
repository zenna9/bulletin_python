#<views.>================
from django.shortcuts import render, get_object_or_404, redirect
from bbs.models import Board
def b_list(request):
    posts = Board.objects.all().order_by('-id')
    context = { 'my_posts' : posts}
    return render(request, 'bbs/list.html', context)

def b_detail(request, board_id):
    post = get_object_or_404(Board, pk=board_id)
    context = { 'my_post' : post}
    return render(request, 'bbs/detail.html', context)

def likeclick(request, board_id):
    post = get_object_or_404(Board, pk=board_id)
    selected_vote = post.board_set.get(pk=board_id)
    selected_vote.b_comment_count +=1
    selected_vote.save()

def b_create(request):
    return render(request, 'bbs/create.html')

def b_create_process(request):
    board = Board() #클래스에 빈 객체를 만드는 명령어 Board()
    board.b_title = request.POST['b_title']
    board.b_author = request.POST['b_author']
    board.b_content = request.POST['b_content']
    board.save() #사용자가 입력한 글을 데이터에 쑤셔넣게 만듦

    return redirect('bbs:b_list')

