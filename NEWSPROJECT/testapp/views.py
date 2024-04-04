from django.shortcuts import render

# Create your views here.
def news_info(request):
    return render(request,'testapp/index.html')

def movie_view(request):
    head_msg='Movie Information'
    sub_msg1='Eagle movie was nice'
    sub_msg2='NTR 30 movie will come soon'
    sub_msg3='OG will come soon'
    type='movie'
    my_dict={'head_msg':head_msg,'sub_msg1':sub_msg1,'sub_msg2':sub_msg2,'sub_msg3':sub_msg3,'type':type}
    return render(request,'testapp/news.html',my_dict)
def sports_info(request):
    head_masg = 'Sports Information'
    sub_msg1 = 'RCB women went to the final'
    sub_msg2 = 'Upcoming IPL will start March-23rd'
    sub_msg3 = 'Kabaddi Kabaddi'
    type = 'sports'
    my_dict = {'head_msg':head_masg, 'sub_msg1':sub_msg1, 'sub_msg2':sub_msg2, 'sub_msg3':sub_msg3,'type':type}
    return render(request,'testapp/news.html',my_dict)

def politics_info(request):
    head_masg = 'Politics Information'
    sub_msg1 = 'Telangana CM Revanth Reddy'
    sub_msg2 = 'Upcoming CM for Ap ???????'
    sub_msg3 = 'Paddy fields are getting dry in NALGONDA due to  water'
    type = 'politics'
    my_dict = {'head_msg':head_masg, 'sub_msg1':sub_msg1, 'sub_msg2':sub_msg2, 'sub_msg3':sub_msg3,'type':type}
    return render(request,'testapp/news.html',my_dict)
