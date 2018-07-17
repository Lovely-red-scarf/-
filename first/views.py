from django.shortcuts import render,redirect,reverse,HttpResponse
import json,datetime

from first.models import Book,Author,Publish,User

from first .form import U_ser
# Create your views here.

#定义一个装饰器  然后所有的 函数都用装饰器进行封装
def wrapper(func):
    def inner(*args,**kwargs):
        request = args[0]
        # if request.COOKIES.get('is_login'):
        if request.session.get('is_login'):

            return func(*args,**kwargs)
        else:
            return redirect(reverse('login'))

    return inner



#登陆函数  cookie
# def login(request):
#     print('11111111111111111')
#     if request.method == 'POST':
#         name = request.POST.get('user')
#         pwd = request.POST.get('pwd')
#         print(name,pwd)
#         log_obj = User.objects.filter(name = name ,pwd=pwd).first()
#         if log_obj:  #登陆成功
#             ret = redirect(reverse('index'))
#             ret.set_cookie('name',name)
#             ret.set_cookie('pwd',pwd)
#             ret.set_cookie('is_login',True)
#             ret.set_cookie('last_time',log_obj.date)
#             log_obj.date = datetime.datetime.now()
#             log_obj.save()
#
#             return ret
#     # return redirect(reverse('login'))
#     return render(request,'login.html')


@wrapper
#主界面
def index(request):
    book_list = Book.objects.all()
    publish_list = Publish.objects.all()
    author_list = Author.objects.all()


    return render(request,'index.html',locals())

@wrapper
def add_book(request):
    '''
    这是对书籍的信息进行增加的函数
    :param request:
    :return:
    '''
    book_list = Book.objects.all()
    publish_list = Publish.objects.all()
    author_list = Author.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        date = request.POST.get('date')
        publish = request.POST.get('publish')
        author = request.POST.getlist('author')
        print(author)
        book = Book.objects.create(name = name,price = price, date = date ,publish_id=publish)
        book .authors.set(author)  #给你的这个书籍对象 添加作者

        return redirect(reverse('index'))  #添加完之后就重新定向到主界面

    return render(request,'add_book.html',locals())


@wrapper
def del_book(request):  #删除函数
    deid = request.POST.get('deid')
    print(deid)
    del_book = Book.objects.filter(id = deid)  #获取你前端点击的那个id的书籍对象
    del_book.delete()
    print(111*100)
    return HttpResponse(json.dumps({'status':1}))

@wrapper
def edit_book(request ,edid):
    # print('___________________________')
    book_list = Book.objects.filter(id=edid).first()
    publish_list = Publish.objects.all()
    author_list = Author.objects.all()
    print(book_list)
    print(6666666666666)
    if request.method =='POST':
        print(2222222222)

        name = request.POST.get('name')
        price = request.POST.get('price')
        date = request.POST.get('date')
        publish = request.POST.get('publish')
        author = request.POST.getlist('author')
        # bk_bj =Book.objects.filter(id=edid).update(name=name, price=price, date=date, publish=publish)
        # bk_bj.author.set(author)
        print(3333333333333)
        book_list.name = name
        book_list.price = price
        book_list.publish_id = publish
        book_list.authors.set(author)
        book_list.save()
        return redirect(reverse('index'))
    print(55555555555555)
    return render(request,'edit_book.html',locals())


@wrapper
def logout(request): #注销
    ret = redirect(reverse('login'))
    # ret.delete_cookie('name')
    # ret.set_cookie('last_time')
    # ret.delete_cookie('pwd')
    request.session.flush()
    return ret






#这个使用session
def login_session(request):
    # print(request.POST)
    if request.method == 'POST':
        name = request.POST.get('user','')

        pwd = request.POST.get('pwd','')

        user_obj = User.objects.filter(name=name ,pwd =pwd).first()

        if user_obj:
            ret = redirect(reverse('index'))
            request.session['is_login'] = True
            request.session['name'] = name
            request.session['pwd'] = pwd
            request.session['last_time'] = str(user_obj.date)  # 你去出的是一个date兑现 但是要存起来就要用 str
            user_obj.date = datetime.datetime.now()
            user_obj.save()
            return ret
        # else:  #这一步是你输入的账号和密码不对的时候
            # return HttpResponse('您输入用户名不对')
        return redirect(reverse('hint'))
    return render(request,'login.html')




#定义一个注册用户的函数
def register(request):

    if request.method == 'POST':

        form = U_ser(request.POST)  #把前端的信息和form组件对比判断
        if form.is_valid():#正确
            name = request.POST.get('name')
            pwd = request.POST.get('pwd')
            date = request.POST.get('date')
            email = request.POST.get('email')
            User.objects.create(name = name ,pwd = pwd,date = date,email = email)

            return redirect(reverse('login'))  #注册成功就去登陆界面
        else:

            g_error = form.errors.get('__all__')  #获取所有的错误
            if g_error:
                g_error = g_error[0]
            print(locals())
            return render(request,'register.html',locals())

    form = U_ser()
    print(55555555555555)
    return render(request,'register.html',locals())



def hint(request):
    return render(request,'hint.html')


