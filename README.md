**Гайд**

1. В терминале: pip3 install bs4
2. Запустить main.py
3. Результат выводится в консоль в виде мапы, ключ - преподаватель, значение - список статей.

**Кратко о работе**

1. Парсится страница https://kpfu.ru/main_page?p_sub=7860&p_id=10857&p_order=0
2. Собираются все ссылки на преподавателей
3. На странице преподавателя ищем ссылку на статьи
4. Парсим страницу со статьями преподавателя и добавляем в мапу
5. Все шаги выполняем для всех страниц https://kpfu.ru/main_page?p_sub=7860&p_id=10857&p_order=0, меняя параметр p_order