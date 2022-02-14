from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from .models import *
import datetime
from django.db.models import Q

# Create your views here.
def cart_count(request):
    user = User.objects.get(id=request.user.id)
    mem = Member.objects.get(user=user)
    cart = Cart.objects.filter(member=mem)
    count=0
    for i in cart:
        count+=1
    return count

def Home(request):
    return render(request, 'carousel.html')


def About(request):
    return render(request, 'about.html')


def Contact(request):
    return render(request, 'contact.html')


def Login_User(request):
    error = ""
    if request.method == "POST":
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        sign = ""
        if user:
            try:
                sign = Member.objects.get(user=user)
            except:
                pass
            if sign:
                login(request, user)
                error = "pat"
            else:
                stat = Status.objects.get(status="Accept")
                pure=False
                try:
                    pure = Trainer.objects.get(status=stat,user=user)
                except:
                    pass
                if pure:
                    login(request, user)
                    error = "pat1"
                else:
                    error="notmember"

        else:
            error="not"
    d = {'error': error}
    return render(request, 'login.html', d)


def Login_Admin(request):
    error = ""
    if request.method == "POST":
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        if user:
            login(request, user)
            error = "res"
        else:
            error = "not"

    d = {'error': error}
    return render(request, 'loginadmin.html', d)

def Signup_User(request):
    error = False
    if request.method == 'POST':
        f = request.POST['fname']
        l = request.POST['lname']
        u = request.POST['uname']
        e = request.POST['email']
        p = request.POST['pwd']
        con = request.POST['contact']
        add = request.POST['address']
        d1 = request.POST['doj']
        d2 = request.POST['dob']
        h = request.POST['height']
        w = request.POST['weight']
        i = request.FILES['image']
        user = User.objects.create_user(email=e, username=u, password=p, first_name=f,last_name=l)
        sign = Member.objects.create(user=user,contact=con,address=add, height=h,weight=w,doj=d1,dob=d2,image=i)
        error = True
    d = {'error':error}
    return render(request,'signup.html',d)

def Signup_Trainer(request):
    error = False
    if request.method == 'POST':
        f = request.POST['fname']
        l = request.POST['lname']
        u = request.POST['uname']
        e = request.POST['email']
        p = request.POST['pwd']
        con = request.POST['contact']
        add = request.POST['address']
        d1 = request.POST['doj']
        d2 = request.POST['dob']
        i = request.FILES['image']
        user = User.objects.create_user(email=e, username=u, password=p, first_name=f, last_name=l)
        statu = Status.objects.get(status="pending")
        sign = Trainer.objects.create(status=statu,user=user, contact=con, address=add, doj=d1, dob=d2, image=i)
        error = True
    d = {'error':error}
    return render(request,'signup_trainer.html',d)

def Edit_Trainer(request,pid):
    trainer = Trainer.objects.get(id=pid)
    error = False
    if request.method == 'POST':
        f = request.POST['fname']
        l = request.POST['lname']
        u = request.POST['uname']
        e = request.POST['email']
        con = request.POST['contact']
        add = request.POST['address']
        d2 = request.POST['dob']
        if d2:
            try:
                trainer.dob = d2
                trainer.save()
            except:
                pass
        try:
            i = request.FILES['image']
            trainer.image=i
            trainer.save()
        except:
            pass
        trainer.user.last_name=l
        trainer.user.first_name=f
        trainer.user.email=e
        trainer.address=add
        trainer.contact=con
        trainer.user.save()
        trainer.save()
        error = True
    d = {'error':error,'trainer':trainer}
    return render(request,'edit_trainer.html',d)

def Change_status(request,pid):
    data=0
    user = User.objects.get(username=request.user.username)
    error = ""
    try:
        data = Member.objects.get(user=user)
        if data:
            error = "pat"
    except:
        data = Trainer.objects.get(user=user)
    terror = False
    pro1 = Trainer.objects.get(id=pid)
    if request.method == "POST":
        stat = request.POST['stat']
        sta = Status.objects.get(status=stat)
        pro1.status=sta
        pro1.save()
        terror=True
    d = {'pro':pro1,'error':error,'terror':terror,'data':data}
    return render(request,'status.html',d)

def Change_status1(request,pid):
    data=0
    user = User.objects.get(username=request.user.username)
    error = ""
    try:
        data = Member.objects.get(user=user)
        if data:
            error = "pat"
    except:
        data = Trainer.objects.get(user=user)
    terror = False
    pro1 = Booking.objects.get(id=pid)
    if request.method == "POST":
        stat = request.POST['stat']
        sta = Status.objects.get(status=stat)
        pro1.status=sta
        pro1.save()
        terror=True
    d = {'pro':pro1,'error':error,'terror':terror,'data':data}
    return render(request,'status1.html',d)


def Edit_Member(request,pid):
    trainer = Member.objects.get(id=pid)
    error = False
    if request.method == 'POST':
        f = request.POST['fname']
        l = request.POST['lname']
        u = request.POST['uname']
        e = request.POST['email']
        con = request.POST['contact']
        add = request.POST['address']
        d2 = request.POST['dob']
        w = request.POST['weight']
        h = request.POST['height']
        if d2:
            try:
                trainer.dob = d2
                trainer.save()
            except:
                pass
        try:
            i = request.FILES['image']
            trainer.image=i
            trainer.save()
        except:
            pass
        trainer.user.last_name=l
        trainer.user.first_name=f
        trainer.user.email=e
        trainer.address=add
        trainer.height=h
        trainer.weight=w
        trainer.contact=con
        trainer.user.save()
        trainer.save()
        error = True
    d = {'error':error,'trainer':trainer}
    return render(request,'edit_member.html',d)

def delete_trainer(request,pid):
    trainer=Trainer.objects.get(id=pid)
    trainer.delete()
    return redirect('all_trainer')

def delete_member(request,pid):
    trainer=Member.objects.get(id=pid)
    trainer.delete()
    return redirect('all_member')

def Admin_Home(request):
    total_mem = 0
    total_prod = 0
    total_tra = 0
    total_ord = 0
    order = Booking.objects.all()
    prod = Product.objects.all()
    tra = Trainer.objects.all()
    mem = Member.objects.all()
    for i in mem:
        total_mem+=1
    for i in order:
        total_ord+=1
    for i in tra:
        total_tra+=1
    for i in prod:
        total_prod+=1
    d = {'total_prod':total_prod,'total_tra':total_tra,'total_ord':total_ord,'total_mem':total_mem}
    return render(request,'admin_home.html',d)

def User_Home(request):
    count = cart_count(request)
    sign = 0
    user=User.objects.get(username=request.user.username)
    error=""
    try:
        sign = Member.objects.get(user=user)
        if sign:
            error = "pat"
    except:
        pass
    d = {'error':error,'count':count}
    return render(request,'dashboard.html',d)

def Trainer_Home(request):
    sign = 0
    user = User.objects.get(username=request.user.username)
    error=""
    try:
        sign = Member.objects.get(user=user)
        if sign:
            error = "pat"
    except:
        pass
    d = {'error': error}
    return render(request,'dashboard.html',d)

def View_Package(request):
    package = Package.objects.all()
    d = {'package':package}
    return render(request,'view_package.html',d)

def View_Product(request):
    package = Product.objects.all()
    d = {'package':package}
    return render(request,'view_product.html',d)

def View_New_Trainer(request):
    status = Status.objects.get(status="pending")
    package = Trainer.objects.filter(status = status)
    d = {'package':package}
    return render(request,'new_trainer.html',d)

def View_All_Trainer(request):
    package = Trainer.objects.all()
    d = {'package':package}
    return render(request,'all_trainer.html',d)

def View_All_Member(request):
    package = Member.objects.all()
    d = {'package':package}
    return render(request,'all_member.html',d)

def View_All_Batch(request):
    package = Batch.objects.all()
    d = {'package':package}
    return render(request,'view_all_batch.html',d)

def Edit_Batch(request,pid):
    package = Batch.objects.get(id=pid)
    error = False
    if request.method == "POST":
        n = request.POST['name']
        p = request.POST['timing']
        package.name = n
        package.timing = p
        package.save()
        error = True
    d = {'error':error,'package':package}
    return render(request,'edit_batch.html',d)

def delete_batch(request,pid):
    package = Batch.objects.get(id=pid)
    package.delete()
    return render('view_all_batch')

def View_Tips(request):
    package = Tips.objects.all()
    d = {'package':package}
    return render(request,'view_tips.html',d)

def delete_tips(request,pid):
    package = Tips.objects.get(id=pid)
    package.delete()
    return redirect('view_tips')

def View_Order(request):
    book = Booking.objects.all()
    d = {'book':book}
    return render(request,'view_order.html',d)

def delete_order(request,pid):
    book = Booking.objects.get(id=pid)
    book.delete()
    return redirect('view_order')

def Activity1(request):
    count = cart_count(request)
    sign = 0
    user = User.objects.get(username=request.user.username)
    error = ""
    try:
        sign = Member.objects.get(user=user)
        if sign:
            error = "pat"
    except:
        pass
    package = TrainerActivity.objects.all()
    d = {'act':package,'error':error,'count':count}
    return render(request,'activity.html',d)

def join_batch(request,pid):
    count = cart_count(request)
    sign = 0
    user = User.objects.get(username=request.user.username)
    error = ""
    terror=""
    try:
        sign = Member.objects.get(user=user)
        if sign:
            error = "pat"
    except:
        pass
    package = TrainerActivity.objects.get(id=pid)
    member = Member.objects.get(user=user)
    if request.method == "POST":
        train = ""
        try:
            train = BatchMember.objects.get(trainer_activity=package,member=member)
        except:
            pass
        if train:
            terror="already"
        else:
            my_batch= BatchMember.objects.create(trainer_activity=package,member=member)
            terror = "create"
    d = {'act':package,'error':error,'terror':terror,'count':count}
    return render(request,'join_batch.html',d)

def View_Order_Detail(request,pid,bid):
    product = Product.objects.all()
    book = Booking.objects.get(booking_id=pid, id=bid)
    total = 0
    num1 = 0
    user1 = book.member.user.username
    li = book.booking_id.split('.')
    li2 = []
    for j in li:
        if user1 != j:
            li2.append(int(j))
    d = {'book1':li2,'product':product,'total1':book}
    return render(request,'view_order_detail.html',d)

def View_Attendance(request):
    sign = 0
    user = User.objects.get(username=request.user.username)
    error = ""
    try:
        sign = Member.objects.get(user=user)
        if sign:
            error = "pat"
    except:
        pass
    package = Member.objects.all()
    d = {'package':package,'error':error}
    return render(request,'view_attendance.html',d)

def My_Order(request):
    count = cart_count(request)
    sign = 0
    user = User.objects.get(username=request.user.username)
    error = ""
    try:
        sign = Member.objects.get(user=user)
        if sign:
            error = "pat"
    except:
        pass
    mem = Member.objects.get(user=user)
    book = Booking.objects.filter(member=mem)
    d = {'error':error,'count':count,'book':book}
    return render(request,'my_order.html',d)

def View_Attendance_Detail(request,pid):
    sign = 0
    user = User.objects.get(username=request.user.username)
    error = ""
    try:
        sign = Member.objects.get(user=user)
        if sign:
            error = "pat"
    except:
        pass
    member = Member.objects.get(id=pid)
    package = Attendance.objects.filter(member=member)
    d = {'package':package,'member':member,'error':error}
    return render(request,'view_attendance_detail.html',d)

def View_Attendance1(request):
    count = cart_count(request)
    sign = 0
    user = User.objects.get(username=request.user.username)
    error = ""
    try:
        sign = Member.objects.get(user=user)
        if sign:
            error = "pat"
    except:
        pass
    user = User.objects.get(id=request.user.id)
    member = Member.objects.get(user=user)
    package = Attendance.objects.filter(member=member)
    d = {'package':package,'member':member,'error':error,'count':count}
    return render(request,'view_attendace1.html',d)

def all_memeber1(request):
    sign = 0
    user = User.objects.get(username=request.user.username)
    error = ""
    try:
        sign = Member.objects.get(user=user)
        if sign:
            error = "pat"
    except:
        pass
    member = Member.objects.all()
    d = {'member':member,'error':error}
    return render(request,'all_member1.html',d)

def search_member(request,pid):
    sign = 0
    user = User.objects.get(username=request.user.username)
    error = ""
    try:
        sign = Member.objects.get(user=user)
        if sign:
            error = "pat"
    except:
        pass
    alpha = Alpha.objects.all()
    pro=0
    if pid=="0":
        pro = User.objects.all()
    else:
        pro = User.objects.all().order_by("username").filter(Q(username__startswith=pid)|Q(username__startswith=pid.upper()))
    member = Member.objects.all()
    d = {'member':member,'pro':pro,'alpha':alpha,'error':error}
    return render(request,'search_member.html',d)

def view_member_detail(request,pid):
    sign = 0
    user = User.objects.get(username=request.user.username)
    error = ""
    try:
        sign = Member.objects.get(user=user)
        if sign:
            error = "pat"
    except:
        pass
    user1 = User.objects.get(id=pid)
    try:
        pro = Member.objects.get(user=user1)
        u = "member"
    except:
        pro = Trainer.objects.get(user=user1)
        u = "trainer"
    d = {'pro':pro,'error':error,'u':u}
    return render(request,'view_member_detail.html',d)

def profile(request):
    sign = 0
    user = User.objects.get(username=request.user.username)
    error = ""
    try:
        sign = Member.objects.get(user=user)
        if sign:
            error = "pat"
    except:
        pass
    user = User.objects.get(id=request.user.id)
    u=""
    count=""
    try:
        pro = Member.objects.get(user=user)
        count = cart_count(request)
        u = "member"
    except:
        pro = Trainer.objects.get(user=user)
        u = "trainer"
    d = {'pro':pro,'error':error,"u":u,'count':count}
    return render(request,'profile.html',d)

def admin_profile(request):
    sign = 0
    user = User.objects.get(username=request.user.username)
    error = ""
    try:
        sign = Member.objects.get(user=user)
        if sign:
            error = "pat"
    except:
        pass
    user = User.objects.get(id=request.user.id)
    u=""
    try:
        pro = Member.objects.get(user=user)
        u = "member"
    except:
        pro = Trainer.objects.get(user=user)
        u = "trainer"
    d = {'pro':pro,'error':error,"u":u}
    return render(request,'admin_profile.html',d)

def my_batch(request):
    count = cart_count(request)
    sign = 0
    user = User.objects.get(username=request.user.username)
    error = ""
    try:
        sign = Member.objects.get(user=user)
        if sign:
            error = "pat"
    except:
        pass
    user = User.objects.get(id=request.user.id)
    member = Member.objects.get(user=user)
    batch = BatchMember.objects.filter(member=member)
    d = {'batch':batch,'error':error,'count':count}
    return render(request,'my_batch.html',d)

def trainr(request):
    count = cart_count(request)
    sign = 0
    user = User.objects.get(username=request.user.username)
    error = ""
    try:
        sign = Member.objects.get(user=user)
        if sign:
            error = "pat"
    except:
        pass
    trainer = Trainer.objects.all()
    d = {'trainer':trainer,'error':error,'count':count}
    return render(request,'trainr.html',d)

def tips(request):
    count = cart_count(request)
    sign = 0
    user = User.objects.get(username=request.user.username)
    error = ""
    try:
        sign = Member.objects.get(user=user)
        if sign:
            error = "pat"
    except:
        pass
    tips = Tips.objects.all()
    d = {'tips':tips,'error':error,'count':count}
    return render(request,'tips.html',d)

def View_diet(request):
    sign = 0
    user = User.objects.get(username=request.user.username)
    error = ""
    try:
        sign = Member.objects.get(user=user)
        if sign:
            error = "pat"
    except:
        pass
    diet = DietPlan.objects.all()
    d = {'diet':diet,'error':error}
    return render(request,'view_diet.html',d)

def View_diet1(request):
    sign = 0
    user = User.objects.get(username=request.user.username)
    error = ""
    try:
        sign = Member.objects.get(user=user)
        if sign:
            error = "pat"
    except:
        pass
    diet = DietPlan.objects.all()
    d = {'diet':diet,'error':error}
    return render(request,'view_diet1.html',d)

def product1(request):
    count = cart_count(request)
    sign = 0
    user = User.objects.get(username=request.user.username)
    error = ""
    try:
        sign = Member.objects.get(user=user)
        if sign:
            error = "pat"
    except:
        pass
    pro = Product.objects.all()
    d = {'pro':pro,'error':error,'count':count}
    return render(request,'product1.html',d)

def view_all_activity(request):
    package = TrainerActivity.objects.all()
    d = {'package':package}
    return render(request,'view_all_activity.html',d)

def delete_all_activity(request,pid):
    package = TrainerActivity.objects.get(id=pid)
    package.delete()
    return redirect('view_all_activity')

def view_activity(request):
    package = Activity.objects.all()
    d = {'package':package}
    return render(request,'view_activity.html',d)

def my_activity(request):
    user = User.objects.get(id = request.user.id)
    train = Trainer.objects.get(user=user)
    package = TrainerActivity.objects.filter(trainer=train)
    d = {'package':package}
    return render(request,'my_activity.html',d)

def add_package(request):
    error = False
    if request.method == "POST":
        n = request.POST['name']
        p = request.POST['price']
        i = request.FILES['image']
        Package.objects.create(name=n,price=p,image=i)
        error = True
    d = {'error':error}
    return render(request,'add_package.html',d)

def edit_package(request,pid):
    package = Package.objects.get(id=pid)
    error = False
    if request.method == "POST":
        n = request.POST['name']
        p = request.POST['price']
        try:
            i = request.FILES['image']
            package.image = i
            package.save()
        except:
            pass
        package.name = n
        package.price = p
        package.save()
        error = True
    d = {'error':error,'package':package}
    return render(request,'edit_package.html',d)

def delete_package(request,pid):
    package = Package.objects.get(id=pid)
    package.delete()
    return redirect('view_package')

def add_diet(request):
    error = False
    if request.method == "POST":
        m = request.POST['meal']
        t = request.POST['time']
        w = request.POST['eat']
        DietPlan.objects.create(meal=m,timing=t,what_to_eat=w)
        error = True
    d = {'error':error}
    return render(request,'add_diet.html',d)

def edit_diet(request,pid):
    diet = DietPlan.objects.get(id=pid)
    error = False
    if request.method == "POST":
        m = request.POST['meal']
        t = request.POST['time']
        if t:
            try:
                diet.timing = t
                diet.save()
            except:
                pass
        w = request.POST['eat']
        diet.meal = m
        diet.what_to_eat = w
        diet.save()
        error = True
    d = {'error':error,'diet':diet}
    return render(request,'edit_diet.html',d)

def delete_diet(request,pid):
    diet = DietPlan.objects.get(id=pid)
    diet.delete()
    return redirect('view_diet')

def add_attendance(request,pid):
    trainer = TrainerActivity.objects.get(id=pid)
    error = False
    member1 = Member.objects.all()
    if request.method == "POST":
        n = request.POST['name']
        d = request.POST['date']
        a = request.POST['attend']
        user = User.objects.get(username=n)
        member = Member.objects.get(user=user)
        Attendance.objects.create(trainer_activity=trainer,member=member,attend=a,dot=d)
        error = True
    d = {'error':error,'member1':member1}
    return render(request,'attendance.html',d)

def add_trainer_activity(request):
    batch = Batch.objects.all()
    trainer = Trainer.objects.all()
    activity = Activity.objects.all()
    error = False
    if request.method == "POST":
        n = request.POST['activity']
        p = request.POST['trainer']
        t = request.POST['timing']
        d = request.POST['day']
        act = Activity.objects.get(name=n)
        user = User.objects.get(username=p)
        train = Trainer.objects.get(user=user)
        TrainerActivity.objects.create(activity=act,trainer=train,timing=t,day1=d)
        error = True
    d = {'error':error,'batch':batch,'trainer':trainer,'activity':activity}
    return render(request,'add_trainer_activity.html',d)


def Add_Activity(request):
    error = False
    if request.method == "POST":
        n = request.POST['name']
        p = request.FILES['image']
        Activity.objects.create(name=n,image=p)
        error = True
    d = {'error':error}
    return render(request,'add_activity.html',d)

def Edit_Activity(request,pid):
    act = Activity.objects.get(id=pid)
    error = False
    if request.method == "POST":
        n = request.POST['name']
        try:
            p = request.FILES['image']
            act.image=p
            act.save()
        except:
            pass
        act.name = n
        act.save()
        error = True
    d = {'error':error,'act':act}
    return render(request,'edit_activity.html',d)

def delete_activity(request,pid):
    act = Activity.objects.get(id=pid)
    act.delete()
    return redirect('view_activity')

def Add_Batch(request):
    error = False
    if request.method == "POST":
        n = request.POST['name']
        p = request.POST['timing']
        Batch.objects.create(name=n,timing=p)
        error = True
    d = {'error':error}
    return render(request,'add_batch.html',d)

def Add_Tips(request):
    error = False
    if request.method == "POST":
        n = request.POST['title']
        p = request.POST['desc']
        Tips.objects.create(title=n,desc=p)
        error = True
    d = {'error':error}
    return render(request,'add_tips.html',d)


def Add_Product(request):
    error = False
    if request.method == "POST":
        n = request.POST['name']
        p = request.POST['price']
        i = request.FILES['image']
        Product.objects.create(name=n,price=p,image=i)
        error = True
    d = {'error':error}
    return render(request,'add_prod.html',d)

def Edit_Product(request,pid):
    prod = Product.objects.get(id=pid)
    error = False
    if request.method == "POST":
        n = request.POST['name']
        p = request.POST['price']
        try:
            i = request.FILES['image']
            prod.image = i
            prod.save()
        except:
            pass
        prod.name = n
        prod.price = p
        prod.save()
        error = True
    d = {'error':error,'prod':prod}
    return render(request,'edit_product.html',d)

def delete_product(request,pid):
    prod = Product.objects.get(id=pid)
    prod.delete()
    return redirect('view_product')

def Logout(request):
    logout(request)
    return redirect('home')

def Add_Cart(request,pid):
    if not request.user.is_authenticated:
        return redirect('login')
    count = cart_count(request)
    if request.method=="POST":
        user = User.objects.get(id=request.user.id)
        profile = Member.objects.get(user=user)
        product = Product.objects.get(id=pid)
        Cart.objects.create(member=profile, product=product)
        return redirect('cart')

def view_cart(request):
    count = cart_count(request)
    sign = 0
    user = User.objects.get(username=request.user.username)
    error = ""
    try:
        sign = Member.objects.get(user=user)
        if sign:
            error = "pat"
    except:
        pass
    user = User.objects.get(id=request.user.id)
    profile = Member.objects.get(user=user)
    cart =  Cart.objects.filter(member=profile).all()
    total=0
    num1=0
    book_id=request.user.username
    message1="Here ! No Any Product"
    for i in cart:
        total+=int(i.product.price)
        num1+=1
        book_id = book_id+"."+str(i.product.id)
    d = {'count':count,'error':error,'profile':profile,'cart':cart,'total':total,'num1':num1,'book':book_id,'message':message1}
    return render(request,'cart.html',d)


def remove_cart(request,pid):
    if not request.user.is_authenticated:
        return redirect('login_user')
    cart = Cart.objects.get(id=pid)
    cart.delete()
    return redirect('cart')

def Booking_order(request, pid):
    count = cart_count(request)
    sign = 0
    user = User.objects.get(username=request.user.username)
    error = ""
    try:
        sign = Member.objects.get(user=user)
        if sign:
            error = "pat"
    except:
        pass
    data1 = User.objects.get(id=request.user.id)
    data = Member.objects.filter(user=data1).first()
    cart = Cart.objects.filter(member=data).all()
    total = 0
    num1=0
    for i in cart:
        total+=int(i.product.price)
    user1 = data1.username
    li = pid.split('.')
    li2 = []
    for j in li:
        if user1 != j:
            li2.append(int(j))
            num1+=1
    date1 = datetime.date.today()
    if request.method == "POST":
        d = request.POST['date1']
        c = request.POST['name']
        ad = request.POST['add']
        e = request.POST['email']
        con = request.POST['contact']
        b = request.POST['book_id']
        t = request.POST['total']
        user = User.objects.get(username=c)
        profile = Member.objects.get(user=user)
        status = Status.objects.get(status="pending")
        book1 = Booking.objects.create(member=profile, book_date=d,booking_id=b,total=t,quantity=num1,status=status)
        cart2 = Cart.objects.filter(member=profile).all()
        cart2.delete()
        return redirect('thanks_message')
    d = {'count':count,'error':error,'data': data, 'data1': data1, 'book_id': pid, 'date1': date1,'total':total,'num1':num1}
    return render(request, 'booking.html', d)

def booking_detail(request,pid,bid):
    count = cart_count(request)
    sign = 0
    user = User.objects.get(username=request.user.username)
    error = ""
    try:
        sign = Member.objects.get(user=user)
        if sign:
            error = "pat"
    except:
        pass
    user = User.objects.get(id=request.user.id)
    profile = Member.objects.get(user=user)
    cart =  Cart.objects.filter(member=profile).all()
    product = Product.objects.all()
    book = Booking.objects.get(booking_id=pid, id=bid)
    total=0
    num1=0
    user1 = user.username
    li = book.booking_id.split('.')
    li2=[]
    for j in li:
        if user1!= j :
            li2.append(int(j))
    for i in cart:
        total+=int(i.product.price)
        num1+=1
    d = {'count':count,'error':error,'profile':profile,'cart':cart,'total':total,'num1':num1,'book':li2,'product':product,'total':book}
    return render(request,'booking_detail.html',d)

def thanks_message(request):
    count = cart_count(request)
    sign = 0
    user = User.objects.get(username=request.user.username)
    error = ""
    try:
        sign = Member.objects.get(user=user)
        if sign:
            error = "pat"
    except:
        pass
    d = {'error':error,'count':count}
    return render(request,'thanks_message.html',d)

def Change_Password(request):

    sign = 0
    user = User.objects.get(username=request.user.username)
    error = ""
    count=""
    try:
        sign = Member.objects.get(user=user)
        count = cart_count(request)
        if sign:
            error = "pat"
    except:
        pass
    terror = ""
    if request.method=="POST":
        n = request.POST['pwd1']
        c = request.POST['pwd2']
        o = request.POST['pwd3']
        if c == n:
            u = User.objects.get(username__exact=request.user.username)
            u.set_password(n)
            u.save()
            terror = "yes"
        else:
            terror = "not"
    d = {'error':error,'terror':terror,'count':count}
    return render(request,'change_password.html',d)

def Edit_Profile(request):

    sign = 0
    user = User.objects.get(username=request.user.username)
    error = ""
    count = ""
    try:
        sign = Member.objects.get(user=user)
        count = cart_count(request)
        if sign:
            error = "pat"
    except:
        pass
    user1 = User.objects.get(id=request.user.id)
    pro=""
    try:
        pro = Member.objects.get(user=user)
    except:
        pro = Trainer.objects.get(user=user)
    terror = False
    if request.method == 'POST':
        f = request.POST['fname']
        l = request.POST['lname']
        u = request.POST['uname']
        try:
            i = request.FILES['image']
            pro.image=i
            pro.save()
        except:
            pass
        ad = request.POST['address']
        e = request.POST['email']
        con = request.POST['contact']
        pro.address = ad
        pro.contact=con
        user1.first_name = f
        user1.last_name = l
        user1.email = e
        user1.save()
        pro.save()
        terror = True
    d = {'terror':terror,'error':error,'pro':pro,'count':count}
    return render(request, 'edit_profile.html',d)
