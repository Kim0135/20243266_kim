#!/bin/sh
echo "몸무게(kg)를 입력하세요:"
read weight
echo "신장(m)를 입력하세요:"
read height
bmi=$(echo "$weight / ($height * $height)" | bc -l)
if [ $(echo "$bmi >= 18.5" | bc) -eq 1 ] && [ $(echo "$bmi < 23" | bc) -eq 1 ]; then
    echo "정상 체중입니다."
else
    echo "정상 체중이 아닙니다."
fi
