#!/bin/bash
echo "Создаём файлы..."
for i in {1..10}; do
    touch "test$i.txt"
    echo "Создан файл: test$i.txt"
done
echo "Все файлы созданы. Начинаю удаление в обратном порядке..."
counter=10
while [ $counter -ge 1 ]; do
    filename="test${counter}.txt"
    if [ -f "$filename" ]; then
        rm "$filename"
        echo "Удален файл: $filename"
    else
        echo "Файл $filename не найден"
    fi
    counter=$((counter - 1))
done

echo "Все файлы удалены. Работа завершена."
