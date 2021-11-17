## sed명령어
하이퍼레저 패브릭을 하다보면 쉘 스크립트를 수정해야 할 일들이 꽤나 많다. 그 중에 하나가 정식의 CA 서버를 건너뛰고 certificate 를 생성해 주는 부분인데 이 때에 sed 명령어를 사용하는 스크립트들이 굉장히 많다.

- 사용법
파일 내용을 수정할 때 사용한다. cat과 파이프라인을 통해서 할 수도 있지만 꽤 손이 많이 가는 작업이기 때문에 sed를 이용하여 간단하게 수정 할 수 있다. sed 명령어는 ed 명령어와 grep 명령어(필터링 기능)의 일부 기능을 합친 것이라고 한다.(sedStream EDitor의 약자이다)


**활용**
- test.txt

abcde
fgh
231


**abcde 문자열을 숫자로 바꾸기**
sed 's/abcde/12321/' test.txt

**출력**
>12321
>fgh
>231

파일을 확인해보면 내용은 변하지 않은채 쉘에 출력만 해줄뿐이다.  -i 옵션을 사용해야지 출력이 아닌 실제 파일에 수정사항을 반영할 수 있다.



sed -i 's/abcde/12321/' test.txt

ubuntu나 centos같은 리눅스에서 사용한다면 별다른 출력과 에러 없이 제대로 동작하는 것을 볼 수 있다. 하지만 macOS를 사용하고 있다면 undefined label과 같은 에러가 발생하는데 이는 macOS에서 사용하는 sed가 다른 리눅스에서 사용중인 sed와는 다르기 때문이다.
 macOS의 경우 man을 통해서 명령어를 살펴보면 맨 윗줄에서 아래와 같은 결과를 볼 수 있다.



- sed 매뉴얼 출력
man sed

**결과**
>SED(1)                    BSD General Commands Manual                   SED(1)

BSD 계열의 소프트웨어라는 의미이다. 하지만 ubuntu나 centos에서 똑같이 테스트하게 되면 다른 결과를 볼 수 있다.



** sed 매뉴얼 출력**
man sed

**또는 그냥 입력**
sed

**결과**
>GNU sed home page: <https://www.gnu.org/software/sed/>.
>General help using GNU software: <https://www.gnu.org/gethelp/>.


우분투의 sed는 GNU sed라는 것을 알 수 있다.다시 정리하자면 BSD와 GNU 소프트웨어의 차이로 인해서 발생한 에러라는 것이다 macOS에서 GNU sed를 사용하려면 아래와 같은 작업을 해주면 된다.


- mac에서 GNU's sed 설치
--with-default-names 옵션은 기존의 sed이름으로 gnu-sed를 사용하겠다는 의미*
brew install gnu-sed --with-default-names

------------------------------------------------------------------


awk 명령어
- 의미:데이터를 조작하고 리포트를 생성하기 위해 사용하는 언어이다리눅스에서 사용하는 awk는 GNU 버전의 gawk로 심볼릭 링크되어 있다 간단한 연산자를 명령라인에서 사용할 수 있으며, 큰 프로그램을 위해 사용될 수 있다 awk는 데이터를 조작할 수 있기 때문에 쉘 스크립트에서 사용되는 필수 툴이며, 작은 데이터베이스를 관리하기  위해서도 필수이다. Alfred Aho, Peter Weinberger, Brian Kernighan 3명이 만들었는데 이들의 이름 이니셜을 가져와서 awk라고 부른다


- awk 프로그래밍 형식
awk 명령어를 입력한 다음, 작은따옴표로 둘러싸인 패턴이나 액션을 입력하고 마지막엔 입력 파일 이름. 파일 이름을 지정하지 않으면 키보드 입력에 의한 표준 입력을 받음. 그리고 awk는 입력된 라인들의 데이터들을 공백 또는 탭을 기준으로 분리해 $1부터 시작하는 각각의 필드 변수로 분리해 인식


awk 'pattern' filename
awk '{action}' filename
awk 'pattern {action}' filename


awk 동작원리
1. awk는 파일 또는 파이프를 통해 입력 라인을 얻어와 $0라는 내부 변수에 라인을 입력. 각 라인은 레코드라고 부르고, newline에 의해 구분
2. 라인은 공백을 기준으로 각각의 필드나 단어로 나뉜다. 필드는 $1부터 시작. 많게는 100개 이상의 필드를 저장할 수 있음
3. 내장 변수인 FS라고 부르는 필드 분리자가 공백을 할당받는다. 필드가 콜론이나 대시와 같은 문자에 의해 분리되면 새로운 필드 분리자로 FS의 값을 변경할 수 있다
4. awk는 화면에 필드를 출력할 때 print 함수를 사용
5. 콤마는 출력필즈 분리자(OFS)와 매핑되어 있으며 공백을 할당받음


- OFMT 변수
숫자를 출력할 때 숫자 포맷 제어할 경우 사용. 간단히 printf를 사용할 수도 있지만, OFMT를 지정할 수 있음.
default는 %.6g로 소수점 6자리
$ awk 'BEGIN{OFMT="%.2f"; print 1.23412, 15E-3}'
1.23 0.01

- printf 함수
포매팅된 깔끔한 출력을 할 경우 사용 newline을 제공하지 않기 때문에 newline이 요구되면 \n을 사용해야함
c : 문자, d : 10진수, f : 실수, x : 16진수


- awk -f 옵션
awk 액션과 명령이 파일에 작성되어 있다면 -f 옵션을 사용 awk -f [awk 명령파일] [awk 명령을 적용할 텍스트 파일


**레코드와 필드**
- 레코드
awk는 입력 데이터를 볼 수 없지만 포맷 또는 구조는 볼 수 있다. 레코드라고 불리는 각 라인은 newline으로 분리
NR 변수 : 각 레코드들의 번호는 awk의 빌트인 변수 NR에 저장된다. 레코드가 저장된 다음 NR의 값은 하나씩 증가한다

- 필드: 각 레코드는 디폴트로 공백이나 탭으로 분리된 필드라는 워드로 구성된다. NF에 필드의 수를 유지하며 라인당 100개의 필드를 가질 수 있다

- 필드 분리자
빌트인 변수 FS는 입력 필드 분리자의 값을 가지고 있음. default는 공백과 탭.
FS 값을 변경하기 위해선 -F을 사용하며 -F 다음에 오는 문자가 새로운 필드 분리자가 됨

- awk와 정규표현식
정규표현식은 슬래시로 둘러싸인 문자들로 구성된 패턴

match 연산자(~) : 표현식과 매칭되는 것이 있는지 검사하는 연산자

POSIX 문자 클래스

  $ awk '/[[:lower:]]+g[[:space:]]+[[:digit:]]' awkfile2
  > Hong KilgDong	3324	5/11/96	50354



**비교 표현식**
어떤 상태가 참일때만 액션이 수행

- 조건 표현식
표현식을 검사하기 위해 ?와 :를 사용. if/else가 하는 역할과 같은 결과를 의미
  $ awk '{max={$1 > $2) ? $1 : $2; print max}' filename
  if $1 > $2:
      max = $1
  else:
      max = $2

- 산술 연산자: 계산을 통해 필터링 가능

- 논리 연산자
	&& : AND 연산
	|| : OR 연산
	! : NOT 연산
  $ awk '$3 > $5 && $3 <= 100' filename



**awk 변수**
BEGIN 패턴
awk가 입력 파일의 라인들을 처리하기 이전에 실행되며 액션 블록 앞에 놓임 입력 파일 없이 테스트할 수 있고, 빌트인 내장 변수(OFS, RS, FS)들의 값을 변경할 경우 사용

- END 패턴
어떤 입력 라인과도 매칭되지 않고, 입력 모든 라인이 처리된 후 실행됨
BEGIN만 사용할 경우엔 아규먼트 파일명을 적지 않아도 되지만 END 블록을 사용할 경우엔 반드시 아규먼트  파일을 적어야 함
  $ awk '/Tom/{count++}END{print "Tom was found " count " times."}' awkfile5



 **awk 리다이렉션**
awk결과를 리눅스 파일로 리다이렉션할 경우 쉘 리다이렉션 연산자를 사용 파일명은 큰따옴표로 둘러쌰아 함
심볼이 사용될 때 파일이 오픈되고 잘려짐
  $ awk -F: '$4 >= 60000 {print $1, $2 > "new_file"}' awkfile5

- getline 함수
표준 입력, 파이프, 현재 처리되고 있는 파일로부터 입력을 읽기 위해 사용. 입력의 다음 라인을 가져와
NF, NR, FNR 빌트인 변수를 설정
레코드가 검색되면 1을 리턴하고, 파일의 끝이면 0을 리턴. 에러가 발생하면 -1을 리턴
  $ awk 'BEGIN{ "date " | getline d; split(d, year) ; print year[6]}'
   2009
  $ awk 'BEGIN{while (getline < "/etc/passwd" > 0)lc++; print lc}' filename

- awk 파이프
awk 프로그램에서 파이프를 오픈하고 또다른 파이프를 오픈하기 전에 기존 파이프는 닫아주어야 한다.
파이프 심볼의 오른쪽 명령은 큰따옴표(““)로 둘러싸야 한다
  $ awk '{print $1, $2 | "sort-r"}' cars
END블록에 close를 사용해 파이프를 꼭 닫아줘야 함
  $ awk '{print $1, $2 | "sort -r"} END{close("sort -r")}' cars
