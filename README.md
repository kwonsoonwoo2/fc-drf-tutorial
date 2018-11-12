# DRF Tutorial
 ## pipenv
 ### Installation
 #### Ubuntu Linux
 ```
pip install --user --upgrade pip
pip install --user --upgrade pipenv
```
 `vi ~/.zshrc`
 ```sh
export PATH=$HOME/bin:/usr/local/bin:$PATH
export PATH=$HOME/.local/bin:$PATH
```
 #### macOS
 ```sh
brew install pipenv
```
 ### Using
 초기화 (Python버전 지정 및 virtualenv생성)
 ```sh
pipenv --python 3.6.6
```
 패키지 설치
 ```sh
pipenv install <패키지명>
```
 virtualenv위치
 ```sh
~/.local/share/virtualenvs/<가상환경명>
```
 해당 가상환경의 Shell적용
 ```sh
pipenv shell
```
 가상환경 지우기
 ```sh
pipenv --rm
```