import sys

from flask_script import Manager  # manager 인스턴스를 만들어 커맨드를 관리
from app import create_app
from flask_twisted import Twisted
from twisted.python import log

if __name__ == "__main__":
    app = create_app()
    twisted = Twisted(app)
    log.startLogging(sys.stdout)

    # 어플리케이션 객체를 생성했다면 해당 객체 아래에 logger라는 인스턴스에 접근할 수 있다.
    # 이는 파이썬 logging 모듈 내의 Logger 객체의 인스턴스이다.
    # app.logger.debug/warning/error
    app.logger.info(f"Running the app...")

    manager = Manager(app)
    manager.run()