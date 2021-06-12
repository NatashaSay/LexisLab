from lexisDB.models import *
from textblob import TextBlob
from datetime import datetime


def get_themes():
    return Theme.objects.all()

def get_profile(pk):
    return Profile.objects.get(id=pk)    

def get_theme(pk):
    return Theme.objects.get(id=pk)

def get_words(pk):
    return Word.objects.filter(theme=get_theme(pk))

def get_word(key, pk):
    return Word.objects.get(queue_value=key, theme=get_theme(pk))

def get_word_by_id(word_id):
    return Word.objects.get(id=word_id)


def get_translation(text):
    blob = TextBlob(text)
    language = blob.detect_language()
    if language == 'uk':
        return blob.translate(to='de').string
    elif language == 'de':
        return blob.translate(to='uk').string
    return 'Language is not recognized'


def get_word_count(theme):
    return Word.objects.filter(theme=get_theme(theme)).count()


def create_card(profile_id, word_id):
    card = Card()
    card.created = datetime.now
    card.profile = get_profile(profile_id)
    card.word = get_word_by_id(word_id)
    card.save()
    print('add card')


def get_theme_by_word(pk):
    word = Word.objects.get(id=pk)
    return word.theme.id

def get_queue_by_id(word_id):
    return Word.objects.get(id=word_id).queue_value

def get_cards_by_user(user_id):
    
    return Card.objects.filter(profile=user_id)


def delete_card_by_id(pk):
    Card.objects.filter(id=pk).delete()

def get_words_by_user(user_id):
    cards = Card.objects.filter(profile=user_id)
    context = []
    for item in cards:
        word = Word.objects.get(id=item.word_id)
        context.append(word)
        print(word.content)
    
    return context
    