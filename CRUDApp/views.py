from email.mime import message
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from django.shortcuts import redirect, render
from .models import User_Data, Note
# Create your views here.

def index(request):
    if 'user_email' in request.session:
        notes = Note.objects.filter(user_email=request.session['user_email'])
        return render(request, 'index.html', {'notes':notes})
    else:
        return render(request, 'index.html')

def signUp(request):
    if 'user_name' in request.session:
        return redirect('Home')
    else:
        return render(request, 'signup.html')

def handleSignUp(request):
    userExists = True
    if request.method == 'POST':
        user_name = request.POST['name']
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        password = request.POST['pass']
        h_pass = make_password(password)

        try:
            findUser = User_Data.objects.get(user_email=email)
            userExists = False
        except:
            pass

        if userExists is False:
            messages.warning(request, 'User email already exists...')
            return redirect('signUp')
        else:
            newUser = User_Data(user_email=email, user_name=user_name, first_name=fname, last_name=lname, password=h_pass)
            newUser.save()
            messages.success(request, 'Your Accound is created Succesfully, Now you can login!')
            return redirect('Home')
    else:
        return redirect('Home')

def handleLogin(request):
    if request.method == 'POST':
        login_email = request.POST['login_email']
        login_pass = request.POST['login_pass']

        try:
            user = User_Data.objects.get(user_email=login_email)
            if(check_password(login_pass, user.password)):
                messages.success(request, 'You have Succesfully LoggedIn')
                request.session['user_name'] = user.user_name
                request.session['user_email'] = user.user_email
                return redirect('Home')
            else:
                messages.error(request, 'Wrong Password')
                return redirect('Home')
        except Exception as e:
            messages.warning(request, 'Email does not exist')
            return redirect('Home')
    else:
        return redirect('Home')

def handleLogOut(request):
    if 'user_name' in request.session:
        del request.session['user_name']
        del request.session['user_email']
        messages.success(request, 'You have successfully logged out!')
        return redirect('Home')
    else:
        return redirect('Home')

def addNote(request):
    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['desc']
        note = Note(note_title=title, note_desc=desc, user_email=request.session['user_email'])
        note.save()
        messages.success(request, 'Your note is added Successfully!')
        return redirect('Home')
    else:
        return redirect('Home')

def userNote(request, note_id):
    if 'user_name' in request.session:
        note = Note.objects.filter(note_id=note_id)
        user_email = None
        for key in note:
            user_email = key.user_email
        if(user_email == request.session['user_email']):
            return render(request, 'note.html', {'note':note})
        else:
            return redirect('Home')
    else:
        return redirect('Home')
    
def deleteNote(request, note_id):
    note = Note.objects.filter(note_id= note_id)
    note.delete()
    messages.success(request, 'Your Note has been deleted Successfully')
    return redirect('Home')

def editNote(request, note_id):
    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['desc']
        note = Note.objects.get(note_id=note_id)
        note.note_title = title
        note.note_desc = desc
        note.save()
        messages.success(request, 'Note updated Successfully!')
        return redirect(f"/note/{note_id}")
    else:
        return redirect(f'/note/{note_id}')

def searchNote(request):
    query = request.GET['search']
    noteTitle = Note.objects.filter(note_title__icontains=query)
    noteDesc = Note.objects.filter(note_desc__icontains=query)
    note = noteTitle.union(noteDesc)
    if len(note) == 0:
        messages.warning(request, 'Sorry No any Notes available for this Search')
        return redirect('Home')
    return render(request, 'search.html', {'notes':note, 'query':query})