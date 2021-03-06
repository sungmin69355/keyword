from django.shortcuts import render,get_object_or_404
import requests
from bs4 import BeautifulSoup 
from selenium.webdriver.common.keys import Keys
from django.views.decorators.csrf import csrf_exempt
from .models import KeywordModel
from django.http import HttpResponseNotFound, Http404

@csrf_exempt #CSRF token missing or incorrect오류 해결
def home(request):
    return render(request, 'main.html')

@csrf_exempt #CSRF token missing or incorrect오류 해결
def result(request):
    try:
        keywordmodel = KeywordModel()
        if request.method == "POST":
            keyword = request.POST['Keyword']
        url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query={}'.format(keyword)
        req = requests.get(url)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')

        keywordarray = soup.select('div[class="tit"]')
        tag = soup.select('.total_tag_area span[class*=txt]')  
        notkeyword = "For you 함께 클릭한 상품 추천"
        keyword_list = {}
        tag_list ={}
        tag_overlap_list_keyword =[]

        for i in range(len(keywordarray)):
            if(notkeyword !=keywordarray[i].text.strip()):
                keyword_list[i] = keywordarray[i].text.strip()

        for i in range(len(tag)):
            tag_overlap_list_keyword.append(tag[i].text.strip())
        
        tag_list = tuple(set(tag_overlap_list_keyword))

        if not keyword_list:  
            print("저장 x")
            if not tag_list:
                print("테그저장 x")
            else:
                keywordmodel.keyword = keyword
                keywordmodel.tag_list = tag_list
                keywordmodel.save()
        else :
            keywordmodel.keyword = keyword
            keywordmodel.keyword_list = keyword_list
            if not tag_list:
                print("테그저장 x")
            else:
                keywordmodel.tag_list = tag_list
            keywordmodel.save()
    except:
        return HttpResponseNotFound("키워드를 입력하세요.")

    return render(request, 'result.html',{'keyword_list':keyword_list.items(),'keyword':keyword,'tag_list':tag_list})

def stock(reqeust):
    return render(reqeust, 'stock.html')