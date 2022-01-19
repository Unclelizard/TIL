# 과제 제출 방법

> https://abit.ly/ssafy7-document 
>
> 과제 제출 가이드 참고

## 리소스 저장소 업데이트

```bash
$ git pull origin master
```

* 다운로드 된 오늘자 과제/워크샵 파일(`@hws`)을 확인 후 각자 본인의 hws 폴더로 이동

## 로컬 저장소 (hws)

### 문제 풀이

* 폴더명은 `과제일자` 로 생성
  * 예) 1/11인 경우 `0111` 

* 문제 풀이는 **마크다운 파일**로 만들어서 작성 (필요한 경우 소스코드 파일)

### 커밋

```bash
$ git status
$ git add .
$ git commit -m '___ 과제 제출'
```

### 과제 제출 (push)

```bash
$ git push origin master
```

