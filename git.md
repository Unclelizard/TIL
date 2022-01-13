## git

>  분산 버전 관리 시스템(DVCS)

## 1. Git 저장소 만들기

```bash
$ git init
Initialized empty Git repository in C:/Users/wjdqh/OneDrive/Desktop/first/.git/
(master) $
```

* .git 폴더가 생성=>버전이 기록되는 저장소
  * 해당 폴더를 지우게 되면 모든 버전이 삭제되니 주의!
* (master) git bash에 

1. 작업하면
2. add하여 staging area에 모아
3. commit으로 기록



> Author identity unknown
>
>  Please tell me who you are. (버전기록자 식별안됨)

> git config --global user.email "you@example.com"
> git config --global user.name "Your Name"



> $ git config --global -l
> user.email=wjdqh3579@naver.com
> user.name=euichan



## 버전기록하기

###  'add'

```bash
$ git add 파일명
$ git add a.txt
$ git add my_folder/
$ git add a.txt b.txt

```

### commit

```bash
$ git commit -m '커밋메세지'
```

* 커밋 메세지는 항상 버전의 내용(변경사항)에 대해서 나타낼 수 있도록 기록한다.

  

  

  W.D---->staging area---->repository

  a.txt----->add-------->>>>commit



git init->W.D

git status /상태(W.D/staging area)

git log/커밋된 기록(repository)



## status

```bash
$ git status
```

### log

```bash
$ git log
```



# 원격 저장소 활용(GitHub)

## 기초 활용

### 조회

```bash
$ git remote -v
origin  https://github.com/edutak/first1.git (fetch)
origin  https://github.com/edutak/first1.git (push)
```

### 추가 

```bash
$ git remote add <원격저장소이름> <url>
$ git remote add origin https://github.com/username/repository.git
```

* `origin` : 일반적으로 많이 활용되는 원격저장소 이름

### 삭제

```bash
$ git remote rm <원격저장소이름>
$ git remote rm origin
```



## 원격 저장소 push

> Update remote refs along with associated objects (commit)

```bash
$ git push <원격저장소이름> <브랜치이름>
$ git push origin master
```



## pull

> Fetch from and integrate with another repository or a local branch

```bash
$ git pull <원격저장소이름> <브랜치이름>
$ git pull origin master
```



## 원격 저장소 clone

> Clone a repository into a new directory

```bash
$ git clone <원격저장소주소>
$ git clone https://github.com/username/repository.git
```

* 원격저장소 이름의 폴더가 생성됨.













