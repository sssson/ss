# 2021_LIKELION_Hackathon

추가된 파일 설명

  templates 폴더 속 blog => html 모아둘 곳
  static 폴더 속 css => css 파일 모아둘 곳
 

1. 웹페이지 연결 참조 사이트  https://nachwon.github.io/django-11-static/
    1) firstapp -> view 에 들어가서 함수 생성 및 render (html파일)
    2) firstproject -> urls 에 들어가서 각 도메인에 연결
    
    주의할 점 : template 와 static 파일은 현재 경로를 settings.py 에 고정시켜 두었음! 함부로 변경하면 안됨.
    
2. html과 css 연결
    css 연결할 때 =>  <link rel="stylesheet" href="{% static 'css/basic.css' %}"> 
    css/ 를 경로에 추가해줘야함!
   
