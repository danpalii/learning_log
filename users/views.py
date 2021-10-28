from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """Registrarea unui user nou"""
    if request.method != 'POST':
        #Arata forma goala de registrare
        form = UserCreationForm()
    else:
        #Prelucrarea unei forme pline
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            #Intrarea si redirectionarea pe pagina home
            login(request, new_user)
            return redirect('learning_logs:index')

    #Afisarea unei forme goale sau incorecta
    context = {'form': form}
    return render(request, 'registration/register.html', context)
