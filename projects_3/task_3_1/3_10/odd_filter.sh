#!/bin/bash
for i in {1..20}; do
  if [ $((i % 2)) -eq 0 ]; then
    continue
  fi
  if [ "$i" -eq 15 ]; then
    echo "Найдено число 15, прекращаю работу."
    break
  fi
  echo "Нечетное число: $i"
done

echo "Работа завершена."

