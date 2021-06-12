from django.shortcuts import redirect, render
from django.http import JsonResponse
from .queries import *
from .forms import TranslateForm
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'index.html')


@login_required
def profile(request):
    
    context = {
        'profile' : get_profile(request.user.id),
    }
    
    return render(request, 'profile.html', context)


@login_required
def home(request):

    context = {
        'theme': get_themes(),
        'profile' : get_profile(request.user.id),
    }
    return render(request, 'home.html', context)


@login_required
def theme_details(request, pk):

    context = {
        'theme': get_theme(pk),
        'words': get_words(pk),
    }
    return render(request, 'theme_detail.html', context) 


@login_required
def learn_words(request, pk, key):

    word_count = get_word_count(pk)
    if word_count+1==key:
        return redirect('complete')
        
    context = {
        'word': get_word(key, pk),
        'all_words': word_count,
    }
    return render(request, 'learn_words.html', context)


@login_required
def learn_complete(request):
    return render(request, 'learn_words_complete.html')


@login_required
def translate(request):


    translation = ''
    if request.method == 'POST':
        print('translate')
        form = TranslateForm(request.POST)
        text = request.POST['Text1']
        translation = get_translation(text)
        #translation = 'Deutsch'
        return render(request, 'translate.html', {'form': form, 'text': text, 'translation': translation})


    else:
        form = TranslateForm()

    return render(request, 'translate.html', {'form': form, 'translation': translation})


@login_required
def add_card(request, pk):
    create_card(request.user.id, pk)
    theme = get_theme_by_word(pk)
   
    return redirect('learn_words', theme, get_queue_by_id(pk))
    

@login_required
def mylist(request):

    context = {
        'cards': get_cards_by_user(request.user.id),
        'words': get_words_by_user(request.user.id),
    }
    #print(context)
    if context['cards'].count()==0:
        return render(request, 'no_words.html')

    return render(request, 'mylist.html', context)


@login_required
def delete_card(request, pk):
    print('delete card')
    print(pk)
    delete_card_by_id(pk)
    return redirect('mylist')