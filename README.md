# WhatTODO
---
## 요약

**Make Your Own TODO list**
-  Django 프레임워크 기반의 TODO 작성 웹 서비스
- 간편히 할 일을 추가하고 이를 쉽게 관리할수 있게 복잡하지 않은 구성이 특징

---
## How To Build

리눅스 기반의 OS에서의 설치 및 실행 방법은 아래와 같습니다.

**개발환경 및 툴**
- Python 3.7.0
- IDE : JetBrains PyCharm

**배포 환경**
- OS : Debian 9.4

### Build 방법

**패키지 정보 업데이트**
> sudo apt-get update

**Python 3.7설치**
1. Prerequisiteis
>$ sudo apt-get install build-essential checkinstall
>
>$ sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev \
>
>        libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev

2. Download Python 3.7
> $ cd /usr/src
> 
> $ sudo wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tgz
> 
> $ sudo tar xzf Python-3.7.0.tgz

3. Complie Python Source
> $ cd Python-3.7.0
> 
> $ sudo ./configure --enable-optimizations
> 
> $ sudo make altinstall

4. Setting Environments variable
> $ vi ~/.bashrc
> 
> export PYTHON_HOME=${APP_HOME}/src/Python/python
> 
> export PATH=${PYTHON_HOME}/bin:$PATH

**서버 환경 구성**
1. Pip3 install
> $ sudo apt-get install python3-pip

2. Virtual Environment install
> $ sudo apt-get install python3-venv

3. Clone code in proper directory
ex)
> $ cd /srv
> 
> $ git clone https://github.com/Jincy7/WhatTODO.git

4. Setting Virtual Environment
> $ python3 -m venv venv
> 
> $ source venv/bin/activate
> 
> $ sudo pip3 install -r requirements.txt

5. Django Setting and Start Server
> $ sudo python3 manage.py makemigrations
> 
> $ sudo python3 manage.py migrate
> 
> $ sudo python3 manage.py runserver

