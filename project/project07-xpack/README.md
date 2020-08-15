# project07 - X-Pack

#### docker-compose.xpack.yml
- `xpack.license.self_generated.type=basic` "basic" 일부 xpack의 기능을 무료로 사용가능, trial은 30일 체험버전
- `xpack.security.enabled=true`로 하면 user/pw를 가지고 클러스터에 접근해야한다.
- kibana UI에서 Security가 활성화되고, user & role를 설정할 수 있다.
- https://www.elastic.co/guide/kr/x-pack/current/xpack-introduction.html
- https://www.elastic.co/kr/subscriptions 


```
$ curl -XGET -u elastic:changeme http://localhost:9200/_xpack/security/user?pretty
$ curl -XGET http://elastic:changeme@localhost:9200/_xpack/security/user?pretty
```
![스크린샷 2020-07-28 오전 10 43 55](https://user-images.githubusercontent.com/11022719/88609506-3e410180-d0bf-11ea-977c-007c646088b1.png)
![스크린샷 2020-07-28 오전 10 44 09](https://user-images.githubusercontent.com/11022719/88609518-46993c80-d0bf-11ea-99bd-737b16ea4c9f.png)

