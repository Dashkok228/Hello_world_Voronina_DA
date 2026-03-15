#!/bin/bash
read -p "Введите имя гена: " GENE_NAME
read -p "Введите уровень экспрессии (целое число): " EXPRESSION_LEVEL
if [ -z "$GENE_NAME" ] || ! [[ "$EXPRESSION_LEVEL" =~ ^[0-9]+$ ]]; then
  echo "Ошибка: недостаточно данных."
  exit 1
fi
echo "Экспрессия гена $GENE_NAME составляет $EXPRESSION_LEVEL единиц"

