from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404, redirect
from Muser.models import SignUp, TRENDINGSong ,Artist,ArtistSong,Album,PopularSong,MarathiSong,TamilSong

def header(request):
    return render(request,'header.html')
def login(request):
    return render(request,'login.html')
def homepage(request):
    T = TRENDINGSong.objects.all()
    P = PopularSong.objects.all()
    M = MarathiSong.objects.all()
    Ta = TamilSong.objects.all()
    artist = Artist.objects.all()
    album =Album.objects.all()

    trending = None 
    popular=None
    marathi=None
    
    song_id=request.GET.get('id')
    p_id=request.GET.get('p_id')
    m_id=request.GET.get('m_id')
    if(p_id):
        popular=PopularSong.objects.filter(Song_Id=p_id)
    elif(song_id):
         trending=TRENDINGSong.objects.filter(Song_Id=song_id)
    elif(m_id):
        marathi=MarathiSong.objects.filter(Song_Id=m_id)
    else:
        trending:None 
    data={
        't':T,
        'p':P,
        'm':M,
        'ta':Ta,
        'a':artist,
        'a1':album,
        't_length': len(T),
        'p_length': len(T)+len(P),
        'trending':trending,
        'popular':popular,
        'marathi':marathi
        }
    return render(request, 'homepage.html',data)

def mysignup(request):
    if(request.method=='POST'):
        user=request.POST['user']
        pass1=request.POST['pass']
        print(user, pass1)
        s1=SignUp.objects.filter(Username=user).exists()
        if(s1):
            return HttpResponseRedirect('/error/')
        else:
            pass
        s1=SignUp(Username=user,password=pass1)
        s1.save()

        s2=SignUp.objects.filter(Username=user).first()
        if(s2):
            request.session['logged_in']=True
            request.session['user_id'] = s2.id
        return HttpResponseRedirect('/')
    return render(request,'signup.html')

def mylogin(request):
    if(request.method=='POST'):
        us=request.POST['user']
        ps=request.POST['pass']
        s1=SignUp.objects.filter(Username=us,password=ps).first()
        if(s1):
            request.session['logged_in']=True
            request.session['user_id'] = s1.id
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/errorlogin')
    return render(request,'login.html')

def profile(request):
    user_id = request.session.get('user_id')
    s1 = SignUp.objects.filter(id=user_id)
    data={
        'details':s1
    }
    return render(request,'profile.html',data)
def logout(request):
    request.session.flush()
    return HttpResponseRedirect('/')

def EditProfile(request):
    user_id = request.session.get('user_id')
    user = SignUp.objects.filter(id=user_id)
    data={
            'details':user
        }
    if(request.method=='POST'):
        user=request.POST['username']
        email=request.POST['email']
        phone=request.POST['phone']
        profile = request.FILES.get('profile')
        s1=SignUp.objects.get(Username=user)
        s1.email=email
        s1.phone=phone

        if profile:
            s1.profile = profile
        s1.save()
        return HttpResponseRedirect('/profile')
    return render(request,'profileEdit.html',data)
def error(request):
    return render(request,'signuperror.html')

def errorlogin(request):
    return render(request,'loginerror.html')


def TrendingDetail(request):
    
    return render(request,'TrendingDetails.html')

def PopularDetail(request, song_id):
    popular= PopularSong.objects.filter(Song_Id=song_id)
    data={
        'popular':popular,
    }
    return render(request, 'PopularDetails.html',data)

def MarathiDetail(request, song_id):
    marathi= MarathiSong.objects.filter(Song_Id=song_id)
    data={
        'marathi':marathi,
    }
    return render(request, 'MarathiDetails.html',data)

def TamilDetail(request, song_id):
    tamil = TamilSong.objects.filter(Song_Id=song_id)
    data={
        'tamil':tamil
    }
    return render(request, 'TemilDetails.html',data)

def artist_Details(request,artist_id):
    artist = Artist.objects.get(id=artist_id)
    songs = artist.songs.all()
    data={
        'a':artist,
        's':songs,
    }
    return render(request,'Artist.html',data) 


def album_Details(request,album_id):
    album = Album.objects.get(id=album_id)
    songs = album.songs.all()
    A={
        'a1':album,
        's1':songs,
    }
    return render(request,'Album.html',A) 

def mymain(request):
    return render(request,'main.html')
def AboutUs(request):
    return render(request,'AboutUs.html')
def Premium(request):
    return render(request,'Premium.html')
def Help(request):
    return render(request,'help.html')