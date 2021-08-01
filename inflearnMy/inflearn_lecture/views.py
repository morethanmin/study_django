from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import lecture as lectureModel, comment as commentModel
# Create your views here.
def home_list(request) :
  lectures = lectureModel.objects.filter(category="hot")
  return render(request, 'inflearn_lecture/home_list.html', { 'lectures': lectures })

def lecture_list(request) :
  hot_lectures = lectureModel.objects.filter(category="hot")
  all_lectures = lectureModel.objects.filter()
  return render(request, 'inflearn_lecture/lecture_list.html', { 'all_lectures': all_lectures, 'hot_lectures': hot_lectures })

def signin(request) :
  if request.method =='POST':
    email = request.POST['email']
    password = request.POST['password']

    user = auth.authenticate(request, username=email, password=password)
    if user is None:
      return redirect('/signup')
    else:
      auth.login(request,user)
      return redirect('/')
  return render(request, 'inflearn_lecture/signin.html')

def signup(request) :
  if request.method =='POST':
    email = request.POST['email']
    password = request.POST['password']

    User.objects.create_user(username=email, password=password)
    return redirect('/')
  return render(request, 'inflearn_lecture/signup.html')


def signout(request) :
  auth.logout(request)
  return redirect('/')


def lecture_detail(request, pk) :
  lecture = get_object_or_404(lectureModel, pk = pk)
  comments = commentModel.objects.filter(lecture=lecture)

  print(request.user.id)
  if request.method == 'POST' :
    commentModel.objects.create(lecture = lecture, author = request.user, text = request.POST['text'])
    return redirect('/lecture_list/' + str(pk))

  return render(request, 'inflearn_lecture/lecture_detail.html', {'lecture': lecture, 'comments': comments})