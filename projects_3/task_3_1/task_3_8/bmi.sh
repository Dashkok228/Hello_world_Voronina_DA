#!/bin/bash
echo "Расчёт индекса массы тела (ИМТ)"
read -p "Введите массу тела в килограммах: " weight
read -p "Введите рост в метрах: " height
bmi=$(echo "scale=0; $weight / ($height * $height)" | bc -l)
echo "Ваш индекс массы тела (ИМТ): $bmi"

