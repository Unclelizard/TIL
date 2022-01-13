

## git 원격저장소 활용(github)



## 원격저장소 (remote repository) 추가

### 추가



```bash
$ git remote add <원격저장소이름> <url>
$ git remote add origin http://github.com/username.repository.git

```

* `origin` : 일반적으로 많이 활용되는 원격저장소이름 (변수 뒤에 주소를 받는)

### 삭제

```bash
$ git remote rm <원격저장소이름>
$ git remote rm origin
```



### 확인

```bash
$ git remote -v
origin  https://github.com/Unclelizard/first.git (fetch)
origin  https://github.com/Unclelizard/first.git (push)

```



## 원격 저장소 push

```bash
$ git push <원격저장소이름> <브랜치이름>
$ git push origin master
```



## 원격 저장소 Pull

```bash
$ git pull <원격저장소이름> <브랜치이름>
$ git pull origin master
```



## 원격 저장소 Clone

```bash
$ git clone <원격저장소주소>
$ git clone http://github.com/username/repository.git
```

* 원격저장소 이름의 폴더가 생성됨.
* 