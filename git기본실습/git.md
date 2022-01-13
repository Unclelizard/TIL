## git <버전변화 테스트>

>  분산 버전 관리 시스템(DVCS)

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
> Please tell me who you are. (버전기록자 식별안됨)

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

  

  

  W.D((working tree))---->staging area(index)---->repository

  a.txt----->add-------->>>>commit



git init->W.D(working tree)

git status /상태(W.D/staging area)(index)

git log/커밋된 기록(repository)



## status

```bash
$ git status


# 커밋할 변경사항들(staging area)
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        deleted:    b.txt
# 커밋을 위해 준비되지 않은 변경사항 (staging area에 없음=>working directory)
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   a.txt
#트래킹되지 않은 파일들(working directory)
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        c.txt
```

* 파일을 조작을 하는 방법이 4가지?
  * 생성 Create
  * ~~읽기 Read~~
  * 수정 Update
  * 삭제 Delete

### git에서 관리하는 파일 변경사항 상태 

* untrackted : 커밋된 적 없는 파일
* tracked
  * modified : 커밋에 비해서 수정된 경우
  * staged : 커밋 되기 전 목록(staging area)
  * commited : 커밋된 상태





## log

>  Show commit logs

```bash
$ git log
```



## 3. git 파일의 라이프 사이클

[관련 문서 - Git 기초](https://git-scm.com/book/ko/v2/%EC%8B%9C%EC%9E%91%ED%95%98%EA%B8%B0-Git-%EA%B8%B0%EC%B4%88)

[관련 문서 - Git 수정하고 저장소에 저장하기](https://git-scm.com/book/ko/v2/Git%EC%9D%98-%EA%B8%B0%EC%B4%88-%EC%88%98%EC%A0%95%ED%95%98%EA%B3%A0-%EC%A0%80%EC%9E%A5%EC%86%8C%EC%97%90-%EC%A0%80%EC%9E%A5%ED%95%98%EA%B8%B0)

![image-20220113101851253](git.assets/image-20220113101851253.png)

![image-20220113101938077](git.assets/image-20220113101938077.png)

* untracked : 커밋에 포함된 적 없는 파일
* tracked 
  * modified : 커밋에 비해서 수정된 경우
  * staged : 커밋 되기 전 목록 (Staging area)
  * commited : 커밋된 상태

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













