#!/bin/sh
echo "이름을 입력하세요:"
read name
echo "생일 또는 전화번호를 입력하세요:"
read info
echo "$name: $info" >> DB.txt
echo "정보가 DB에 추가되었습니다."
