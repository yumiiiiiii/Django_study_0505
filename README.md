# Django_study_0505

### 1.html/css
##### django는 static선언 후 따로 참고해야함!

    <link rel = "stylesheet" href="{% static 'list.css' %}/> 
    
##### 이런식으로..css파일은 firstproject파일의 static 파일안에 따로있다. settings.py에서 static 적용도 해줘야함.

    import os
        STATIC_URL = '/static/'
    STATICFILES_DIRS=(
        os.path.join(BASE_DIR,'static'),
    )


### 2. span 정렬
##### span은 div처럼 가운데 정렬이 적용이 안됨!

    display: table;
    text-align: center;
    
##### 같이 적용하면 가운데 정렬은 됨. 대신 span처럼 수평으로 이어지진 않는다.

### ___3. 하나의 template에 여러가지 views를 표현하는법___
##### 
    contexts={'posts':posts, 'M_posts':M_posts, 'D_posts':D_posts}
    return render(request, 'list.html', contexts)
##### 이런식으로 하자!
* * *
##### 참고
###### git hub에 push를 하니까 자꾸 파일이 없어지는 현상이 있었다...결국에 밤새서 다시 만들었는데 눈물 났다. 이유는 모르겠는데 앞으로는 push하기 전에 미리미리 파일을 복사해서 옮기거나 저장하는 습관을 들이자...:disappointed_relieved:

