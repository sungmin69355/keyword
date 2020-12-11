from django.shortcuts import render
import requests
from bs4 import BeautifulSoup 
from selenium.webdriver.common.keys import Keys
from django.views.decorators.csrf import csrf_exempt
from .models import KeywordModel

@csrf_exempt #CSRF token missing or incorrect오류 해결
def home(request):
    return render(request, 'main.html')

@csrf_exempt #CSRF token missing or incorrect오류 해결
def result(request):
    keywordmodel = KeywordModel()
    if request.method == "POST":
        keyword = request.POST['Keyword']
    url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query={}'.format(keyword)
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    keywordarray = soup.select('div[class="tit"]')

    keyword_list =[]
    keyword_list_print = {}

    for i in range(len(keywordarray)):
        keyword_list.append(keywordarray[i].text.strip())
        keyword_list_print[i] = keywordarray[i].text.strip()

    if not keyword_list:
        print("저장 x")
    else :
        keywordmodel.keyword = keyword
        keywordmodel.keyword_list = keyword_list
        keywordmodel.save()


    return render(request, 'result.html',{'keyword_list':keyword_list_print.items(),'keyword':keyword})


