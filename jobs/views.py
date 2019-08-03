from django.shortcuts import render

from .models import Job

def home(request):
    jobs = Job.objects
    my_pr1 = "35才の実務未経験プログラマーです。"
    my_pr2 = "DjangoでのWeb開発やってます。転職希望です。"
    # my_pr3 = "転職希望です。"
    product_pr = "下記サイトはDjangoで開発したWebアプリの一覧です。よろしければクリックしてください。"
    params = {
        'jobs':jobs,
        'my_pr1':my_pr1,
        'my_pr2':my_pr2,
        # 'my_pr3':my_pr3,
        'product_pr':product_pr,
    }
    return render(request, 'jobs/home.html', params)
