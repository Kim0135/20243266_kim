#!/bin/sh
echo "원하는 옵션을 입력하세요 (start/stop/status):"
read action
case $action in
    start)
        echo "시작합니다.";;
    stop)
        echo "중지합니다.";;
    status)
        echo "상태를 확인합니다.";;
    *)
        echo "알 수 없는 명령입니다.";;
esac
