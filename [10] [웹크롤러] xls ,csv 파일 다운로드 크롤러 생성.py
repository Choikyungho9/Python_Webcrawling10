#!/usr/bin/env python
# coding: utf-8

# In[1]:


#예제 :파일 다운로드용 크롤러 만들기 - xls 와 csv 형식 다운로드
 
print("=" *100)
print(" 예제: 파일 다운로드용 크롤러 만들기 - xls 와 csv 형식 다운로드")
print("=" *100)
 
#Step 1. 필요한 모듈과 라이브러리를 로딩합니다.
from bs4 import BeautifulSoup
from selenium import webdriver
 
import time
import os


# In[2]:


#Step 2. 사용자에게 주소를 입력 받습니다.
url_addr = input('1. 파일 다운로드 할 웹페이지 주소를 입력하세요: ')
 
f_dir=input('2.파일이 저장될 경로만 쓰세요(예: C:\\data_science_202007\\notebook\\data\\ ) : ')
 
if  os.path.isdir(f_dir) : #존재하는 경로인지 확인
    print('입력하신 경로가 존재하여  %s 폴더에 저장하겠습니다' %f_dir)
else : #존재하지 않으면 폴더 생성       
    os.makedirs(f_dir)
    print('입력하신 경로가 존재하지 않아 %s 폴더를 생성했습니다' %f_dir)
    
choice = input(''' 1.전체      2.KOSPI     3.KOSDAQ   
3. 위 번호 중 조회할 시장 번호를 선택하세요:  ''')
 
f_choice = input(''' 1.xls 형식으로 저장하기      2.csv 형식으로 저장하기  
4. 위 번호 중 저장할 파일 형식의 번호를 선택하세요:  ''')
 
print("\n")
print("요청하신 데이터를 수집 중이오니 잠시만 기다려 주세요~~^^")


# In[3]:


#Step 3. 크롬 드라이버를 사용해서 웹 브라우저를 실행합니다.
s_time = time.time( )
 
options = webdriver.ChromeOptions()
 
path = "C:\\data_science_202007\\datadown\\chromedriver.exe"
driver = webdriver.Chrome(path,options=options)
 
#다운로드 될 파일의 저장폴더지정,
##propmt 창이 뜨지 않는다.
#pdf형식이 다운로드되면 브라우저에서 보이지 않고 무조건 다운로드된다.
options.add_experimental_option("prefs", {
      "download.default_directory": f_dir,
      "download.prompt_for_download": False,
      "plugins.always_open_pdf_externally": True 
})
 
#크롬 드라이버는 악의적인 행동을 예방하기 위해 소프트웨어가 컴퓨터에서 파일을 다운로드 하지 못하도록 한다.
#이를 해결하기 위해 크롬 커맨드라인에 다운로드를 허용하는 명령을 추가해야 한다.(
 
driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': f_dir}}
command_result = driver.execute("send_command", params)
 
driver.get(url_addr)
time.sleep(10)


# In[4]:


#※ chrome driver로 열린 브라우저의 개발자 도구에서 id를 새롭게 복사해온다
#Step 4. 전체 / KOSPI / KOSDAQ  라디오 버튼 선택 후 조회 버튼 누르기
if choice == '1' :
    radio = driver.find_element_by_id("gubuna87ff679a2f3e71d9181a67b7542122c")
    radio.click()
    driver.find_element_by_id("btnidc81e728d9d4c2f636f067f89cc14862c").click() #검색버튼
elif choice == '2' :
    radio = driver.find_element_by_id("gubun1a87ff679a2f3e71d9181a67b7542122c")
    radio.click()
    driver.find_element_by_id("btnidc81e728d9d4c2f636f067f89cc14862c").click()#검색버튼
elif choice =='3' :
    radio = driver.find_element_by_id("gubun2a87ff679a2f3e71d9181a67b7542122c")
    radio.click() 
    driver.find_element_by_id("btnidc81e728d9d4c2f636f067f89cc14862c").click()#검색버튼
else :
    print('번호를 다시 확인해 주세요')


# In[5]:


#※ chrome driver로 열린 브라우저의 개발자 도구에서 xpath를 새롭게 복사해온다
#Step 5. xls 형태와 csv 형태의 파일로 다운로드 받기
if f_choice == '1' :
    driver.find_element_by_xpath("""//*[@id="e4da3b7fbbce2345d7772b0674a318d5"]/button[3]""").click()
elif choice == '2' :
    driver.find_element_by_xpath("""//*[@id="e4da3b7fbbce2345d7772b0674a318d5"]/button[4]""").click()
    
time.sleep(10)
 
e_time = time.time( )
t_time = e_time - s_time
 
#Step 6. 요약 정보 보여주기
print("=" *100)
print("총 소요시간은 %s 초 입니다 " %round(t_time,1))
print("파일이 저장된 폴더명 : %s " %f_dir)
print("=" *100)
 
driver.close( )


# In[ ]:




