# 깔끔한 파이썬 단단한 백엔드

책 "깔끔한 파이썬 단단한 백엔드"를 공부하며 작성한 미니 트위터 서버 앱입니다.

사용 라이브러리

    Server : Flask
    Database : Mysql
        ORM : Sqlalchemy
    Test : pytest
</br>
어플리케이션 계층 : View / Service / Model

    View        :   클라이언트로부터 들어오는 요청에 맞는 작업을 연결해주는(라우팅) 뷰 계층
    Service     :   각 요청에 맞는 작업들을 정의하는 서비스 계층
    Model       :   실질적으로 데이터베이스와 통신하며 데이터를 가져오고 입력하는 모델 계층
</br>
API 종류

    GET /ping                               :   서버 health check
    POST /sign-up                           :   회원가입
    POST /login                             :   로그인
    POST /follow                            :   팔로우
    POST /unfollow                          :   언팔로우
    POST /tweet                             :   tweet 등록
    GET /timeline                           :   내 타임라인
    GET /timeline/<int:user_id>             :   특정 유저의 타임라인
    POST /profile-picture                   :   프로필 이미지 업로드
    GET /profile-picture/<int:user_id>      :   특정 유저의 프로필 이미지 url 받기
</br>
간략한 설명

    ./
        app.py                  :   Flask 서버 app을 생성
        setup.py                :   app.py에서 생성한 app을 구동
        config.py               :   DB 통신에 필요한 설정 기록

        view/
            __init__.py         :   라우팅 처리
        
        service/
            __init__.py         :   service 패키지 내 클래스 명시
            user_service.py     :   user와 관련된 요청을 처리하는 컨트롤러 클래스
            tweet_service.py    :   tweet과 관련된 요청을 처리하는 컨트롤러 클래스

        model/
            __init__.py         :   model 패키지 내 클래스 명시
            user_dao.py         :   user와 관련된 데이터를 처리하는 데이터 접근 클래스
            tweet_dao.py        :   tweet과 관련된 데이터를 처리하는 데이터 접근 클래스

        test/
            test_view.py        :   view의 각 기능 테스트
            test_service.py     :   service의 각 기능 테스트
            test_model.py       :   model의 각 기능 테스트