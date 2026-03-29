#!/bin/bash

check_root() {
  if [ "$EUID" -ne 0 ]; then
        echo "Ошибка: Скрипт должен быть запущен от имени суперпользователя (root)."
        return 1
  else
        echo "Скрипт запущен от имени суперпользователя (root)."
        return 0
  fi
}
check_root

