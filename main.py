
 getops명령어
이 파일은 실행 옵션 기능을 확인하기 위해 간단히 만든 스크립트이다. 크게 사용법, 실행 옵션 설정, 실행 옵션 확인 이렇게 세 부분으로 나뉘어 있다. 필요한 옵션을 만들 때에는 빨간색으로 표시된 부분을 주의해서 변경해야 한다

 

- 인자가 있는 실행 옵션

옵션 뒤에 ":"를 붙여줍니다. 아래 예에서는 "m" 옵션과 "u"옵션이 해당한다

 

- 인자가 없는 실행 옵션

옵션만 정의합니다. 아래 예에서는 "f", "q", "v", "d", "g", "h" 옵션이 해당한다



**사용법**

usage()
{
        echo "$0 -m MODE[,MODE,...] [-u USER -f -q -v -d -g -h]"
        echo "<options>"
        echo "    -m MODE[,MODE,...]:" 
        echo "           : MODE is 'GET' or 'SET' or 'SHOW'" 
        echo "             If MODE is GET, get Info."
        echo "             If MODE is SET, set Info."
        echo "             If MODE is SHOW, show Info"
        echo "    -u USER: user name usging logging. default is 'unknown'"
        echo "    -f     : Without waiting for a lock, force the update."
        echo "    -q     : Optional. Quiet mode"
        echo "    -v     : Optional. Verbose mode"
        echo "    -d     : Optional. print debug message"
        echo "    -g     : Optional. No logging to syslog"
        echo "    -h     : Show this message."
        echo "<exit code>"
        echo "    0: Success."
        echo "    1: Failure."
        exit 1
}

**실행 옵션 설정**
while getopts m:u:fqvdgh opts; do
        case $opts in
        m) O_MODES=$OPTARG
                ;;
        u) O_USER=$OPTARG
                ;;
        f) O_FORCE="yes"
                ;;
        q) O_QUIET="yes"
                ;;
        v) O_VERBOSE="yes"
                ;;
        d) O_DEBUG="yes"
                ;;
        g) O_SYSLOG="no"
                ;;
        h) usage
                ;;
        \?) usage
                ;;
        esac
done

**실행 옵션 확인**
echo "O_MODES=${O_MODES}"
echo "O_USER=${O_USER}"
echo "O_FORCE=${O_FORCE}"
echo "O_QUIET=${O_QUIET}"
echo "O_VERBOSE=${O_VERBOSE}"
echo "O_DEBUG=${O_DEBUG}"
echo "O_SYSLOG=${O_SYSLOG}"



**사용방법 확인**
"-h 옵션"을 이용해서 사용법을 확인한다

getopt_test.sh -h



**인자가 있는 옵션**
getopt_test.sh -m SET

getopt_test.sh -u jungfo

getopt_test.sh -m SET -u jungfo


**인자가 없는 옵션**
getopt_test.sh -f -q -v -d -g

getopt_test.sh -fqvdg

getopt_test.sh -m GET -u leo -fqvdg



