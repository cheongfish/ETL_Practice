# ETL_Practice
## Outline
* Extract , Transform , Load 에 관한 내용을 바탕으로 실습
* Mysql에서 추출한 데이터를 변환과정을 거치고 postgresql로 적재
* .env 파일로 민감정보 관리
* Query , ORM(SQLAlchemy)를 이용하여 적재함

### Directory
📦ETL_Practice <br>
 ┣ 📂db <br>
 ┃ ┣ 📜connector.py <br>
 ┃ ┣ 📜mysql_query.py <br>
 ┃ ┗ 📜postgresql_query.py <br>
 ┣ 📂pipeline <br>
 ┃ ┣ 📜controller.py <br>
 ┃ ┣ 📜extract.py <br>
 ┃ ┣ 📜load.py <br>
 ┃ ┗ 📜transform.py <br>
 ┣ 📜.env <br>
 ┣ 📜settings.py <br>
 ┣ 📜start.py <br>
 ┗ 📜utils.py




## Inference
* https://velog.io/@baeyuna97/SQLAlchemy-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0
* https://bramhyun.tistory.com/18
