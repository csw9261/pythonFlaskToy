# Python 공식 이미지를 베이스 이미지로 사용
FROM python:3.9-slim

# 작업 디렉토리 설정
WORKDIR /app

# 의존성 파일 복사
COPY requirements.txt .

# 의존성 설치
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 파일 복사
# COPY . . 명령어는 Dockerfile이 있는 현재 디렉토리(즉, Dockerfile이 위치한 프로젝트의 루트 디렉토리)에 있는 모든 파일과 폴더를 Docker 이미지 내의 현재 작업 디렉토리로 복사
COPY . .

# Gunicorn으로 애플리케이션 실행(app.py 위치를 제대로 명시해 줘야함 "app.app:app")
# docker run -it --entrypoint /bin/bash pythonflasktoyprojectdockerimage로 진입하고 
# ls 해보면 ->  Dockerfile  README.md  app  config.py  requirements.txt 이렇게 디렉토리가 나오는데 app.py는 app디렉토리 안에 들어있으니 app.app:app으로 해줘야 한다. 
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "app:app"]

