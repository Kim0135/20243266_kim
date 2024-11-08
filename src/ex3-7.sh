#!/bin/sh
echo "폴더 이름을 입력하세요:"
read folder
mkdir -p "$folder"
cd "$folder"
for i in {1..5}; do
    filename="file$i.txt"
    touch "$filename"
    mkdir -p "$filename-folder"
    ln -s "$(pwd)/$filename" "$(pwd)/$filename-folder/"
done
