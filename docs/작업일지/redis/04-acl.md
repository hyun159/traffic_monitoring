# ACL
```
레디스 사용자 계정별로 권한 관리
```
---

# users.acl 구조
```
user <사용자명> <활성화여부> <비밀번호> <접근가능한 Key> <허용 명령어>
```

```conf
user default off

user admin on >1234! ~* +@all
```

## 접근 가능한 key 정의 방법
```
~*  전체 키
~user: *  user:로 시작하는 키만 허용
~user:* ~order:*  user 또는 order로 시작하는 키
```


## 허용 명령어 정의 방법
```
+@all
+@read
+@write
+@admin
+@dangerous

(개별 명령어)
+get
-keys
```