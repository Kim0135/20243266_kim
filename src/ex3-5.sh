#!/bin/sh
list_files() {
    ls $1
}
echo "디렉토리를 입력하세요:"
read dir
list_files "$dir"
