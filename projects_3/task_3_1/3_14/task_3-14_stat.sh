#!/bin/bash

sum=$(awk '{sum += $2} END {print sum}' students.txt)
echo "Сумма всех оценок: $sum"

average=$(awk '{sum += $2; n++} END {print sum/n}' students.txt)
echo "Средняя оценка: $average"

max=$(awk 'NR==1{max=$2} $2>max{max=$2} END{print max}' students.txt)
echo "Максимальная оценка: $max"
