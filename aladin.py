#-*- coding: utf-8 -*-
import urllib
from bs4 import BeautifulSoup

baseUrl="http://off.aladin.co.kr/usedstore/wsearchresult.aspx?"

def safeunicode(s):
    try:
        return s.encode('latin-1').decode('cp949').encode('utf8')
    except UnicodeEncodeError:
        return s.encode('utf8')

def getUsedbookUrl(offCode, searchWord):
	return baseUrl + urllib.urlencode({"OffCode":offCode, "SearchWord":searchWord.encode('cp949')})

def getUsedbookHtml(offCode, searchWord):
	page = urllib.urlopen(getUsedbookUrl(offCode, searchWord))
	soup = BeautifulSoup(page)
	try:
		searchResult = soup.find("div", {"id": "Search3_Result"})
		[s.extract() for s in searchResult('script')]
		searchResult = safeunicode(searchResult)
	except:
		searchResult = ""

	if searchResult != "":
		print searchWord.encode('utf8')+" found in "+ offCode +"<br />"
		print searchResult.replace("wproduct.aspx?", "wproduct.aspx?OffCode="+offCode+"&")
	else:
		print "<!--"+searchWord.encode('utf8')+" not found in "+ offCode +"-->"
		#http://www.aladin.co.kr/search/wsearchresult.aspx?SearchTarget=All&SearchWord=

offStores = [
	{"name":"​강남점​", "offCode":"gangnam"},
	{"name":"​건대점​", "offCode":"geondae"},
	{"name":"​광주점​", "offCode":"gwangju"},
	{"name":"​노원점​", "offCode":"nowon"},
	{"name":"​대구점​", "offCode":"daegu"},
	{"name":"​대학로점​", "offCode":"daehakro"},
	{"name":"​부산점​", "offCode":"busan"},
	{"name":"​부천점​", "offCode":"bucheon"},
	{"name":"​대전점​", "offCode":"daejeon"},
	{"name":"​분당점​", "offCode":"bundang"},
	{"name":"​산본점​", "offCode":"sanbon"},
	{"name":"​수원점​", "offCode":"suwon"},
	{"name":"​신림점​", "offCode":"sillim"},
	{"name":"​신촌점​", "offCode":"sinchon"},
	{"name":"​울산점​", "offCode":"ulsan"},
	{"name":"​일산점​", "offCode":"ilsan"},
	{"name":"​전주점​", "offCode":"jeonju"},
	{"name":"​종로점​", "offCode":"jongno"},
	{"name":"​청주점​", "offCode":"cheongju"}
]

offStores = [
	{"name":"​대전점​", "offCode":"daejeon"},
	{"name":"​분당점​", "offCode":"bundang"},
	{"name":"​강남점​", "offCode":"gangnam"}
]

#bookList from http://www.ac2.kr/reading
#bookList can be author, title, ISBN
bookList = [
	u"익스트림 프로그래밍​", 
	u"스크럼과 XP​​", 
	u"리틀 벳​​", 
	u"어댑트​​", 
	u"영속 성장 기업의 비밀 6​​", 
	u"린 소프트웨어 개발​​", 
	u"린 소프트웨어 개발의 적용​​", 
	u"역발상 마케팅​​", 
	u"그룹 지니어스​​", 
	u"완벽한 컨설팅​​", 
	u"컨설팅의 비밀​​", 
	u"성공하는 컨설팅의 7요소​​", 
	u"성과향상을 위한 코칭 리더십​​", 
	u"조직 변화의 긍정 혁명​​", 
	u"성공한 CEO는 단순하게 해결한다​​", 
	u"해결을 위한 면접​​", 
	u"해결중심 단기코칭​​", 
	u"동기강화상담 기술훈련 실무자 워크북​​", 
	u"탤런트 코드: 재능을 지배하는 세 가지 법칙​​", 
	u"실용주의 사고와 학습​​", 
	u"침묵으로 가르치기: 학생이 스스로 생각하고 배우는 핀켈 교수의 새로운 교육법​​", 
	u"이너 게임​​", 
	u"이너골프로 10타 줄이기​​", 
	u"공부와 열정​​", 
	u"학습은 어떻게 이루어지나​​", 
	u"어떻게 공부할 것인가​​", 
	u"사티어 모델​​", 
	u"기업을 죽이고 살리는 리더간의 갈등관리​​", 
	u"사티어의 빙산의사 소통방법​​"
]

bookList = [
	"8991268102",	#u"익스트림 프로그래밍​"
	"8991268609",	#u"스크럼과 XP​​"
	"8992717253",	#u"리틀 벳​​"
	"8901133342",	#u"어댑트​​"
	"8950934787",	#u"영속 성장 기업의 비밀 6​​"
	"8991268099",	#u"린 소프트웨어 개발​​"
	"8995856475",	#u"린 소프트웨어 개발의 적용​​"
	"8919204624",	#u"역발상 마케팅​​"
	"8992759061",	#u"그룹 지니어스​​"
	"8991268293",	#u"완벽한 컨설팅​​"
	"8991268005",	#u"컨설팅의 비밀​​"
	"8995213469",	#u"성공하는 컨설팅의 7요소​​"
	"8934926783",	#u"성과향상을 위한 코칭 리더십​​"
	"8996248800",	#u"조직 변화의 긍정 혁명​​"
	"8990994136",	#u"성공한 CEO는 단순하게 해결한다​​"
	"8958320702",	#u"해결을 위한 면접​​"
	"895832905X",	#u"해결중심 단기코칭​​"
	"8991633870",	#u"동기강화상담 기술훈련 실무자 워크북​​"
	"8901096412",	#u"탤런트 코드: 재능을 지배하는 세 가지 법칙​​"
	"8992939361",	#u"실용주의 사고와 학습​​"
	"8963702685",	#u"침묵으로 가르치기: 학생이 스스로 생각하고 배우는 핀켈 교수의 새로운 교육법​​"
	"8995540214",	#u"이너 게임​​"
	"8984821233",	#u"이너골프로 10타 줄이기​​"
	"8937487314",	#u"공부와 열정​​"
	"8958324406",	#u"학습은 어떻게 이루어지나​​"
	"8937834863",	#u"어떻게 공부할 것인가​​"
	"8995162805",	#u"사티어 모델​​"
	"8960770906",	#u"기업을 죽이고 살리는 리더간의 갈등관리​​"
	"8991567258",	#u"사티어의 빙산의사 소통방법​​"
	u"존 가트맨",	
	"899610485X",	#u"비폭력 대화​​"
	"8974424371",	#u"불의 화법​​"
	"8993322171",	#u"가장 듣고 싶은 한마디 Yes!​​"
	"8934962402",	#u"결정적 순간의 대화​​"
	"8934932171",	#u"결정적 순간의 대면​​"
	"8950921839",	#u"탈권위 리더십​​"
	"8950949156",	#u"설득의 심리학​​"
	"8950905620",	#u"대화의 심리학​​"
	"8947529125",	#u"원하는 것이 있다면 감정을 흔들어라​​"
	"8991989101",	#u"Yes를 이끌어내는 협상법​​"
	"8901091682",	#u"당신이 회사에서 보지 못하는 90%의 진실​​"
	"8966260667",	#u"대체 뭐가 문제야​​"
	"8957820728",	#u"증거경영​​"
	"8992124295",	#u"헤일로 이펙트​​"
	"8996724831",	#u"전진의 법칙​​"
	"8995540265",	#u"성과주의의 혁신​​"
	"8975608670",	#u"회사를 살리는 성과경영​​"
	"8934950323",	#u"인플루엔서​​"
	"8901106981",	#u"스위치​​"
	"8901093154",	#u"넛지​​"
	"8925545934",	#u"긍정적 이탈​​"
	"896263063X",	#u"의지력의 재발견​​"
	"8901145278",	#u"스토리​​"
	"8952766016",	#u"왜 나는 항상 결심만 할까​​"
	"8950936585",	#u"어떻게 바꿀 것인가​​"
	"890115059X",	#u"습관의 힘​​"
	"8950927683",	#u"이기는 결정의 제1원칙​​"
	"8962600323",	#u"제7의 감각​​"
	"8959520055",	#u"의사결정의 가이드맵​​"
	"8947528684",	#u"인튜이션​​"
	"8998199041",	#u"대가의 조언​​"
	"895090473X",	#u"스마트 초이스​​"
	"8995845759",	#u"성격의 탄생​"
	"8989566576",	#u"강점이 독이 되는 리더십 함정​​"
	"8935210056",	#u"지그재그​​"
	"899672484X",	#u"티밍: 조직이 학습하고 혁신하는 스마트한 방법​​"
	"8970857648"	#u"성공적인 팀의 5가지 조건​​"
]

'''
bookList = [
	"8991268102",	#u"익스트림 프로그래밍​"
	"8991268609",	#u"스크럼과 XP​​"
	"8992717253"	#u"리틀 벳​​"
]
'''

for book in bookList:
	print "<!--"+book.encode('utf8')+"-->"
	print "<div><h1>"+book.encode('utf8')+"</h1>"
	for offCode in offStores:
		getUsedbookHtml(offCode["offCode"], book)
	print "</div>"