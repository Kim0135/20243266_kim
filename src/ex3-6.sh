#!/bin/sh
echo "폴더 이름을 입력하세요:"
read folder
if [ ! -d "$folder" ]; then
    mkdir "$folder"
    echo "$folder 폴더를 생성했습니다."
fi
cd "$folder"
for i in {1..5}; do
    touch "file$i.txt"
done
tar -czf files.tar.gz *.txt
mkdir extracted
tar -xzf files.tar.gz -C extracted
