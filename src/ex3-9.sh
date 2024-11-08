#!/bin/sh
echo "검색할 이름을 입력하세요:"
read name
grep "$name" DB.txt || echo "해당 이름의 정보가 없습니다."
