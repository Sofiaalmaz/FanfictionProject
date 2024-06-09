# Проект Harry Potter Fanfiction Data Analysis

## Описание

Проект направлен на сбор и анализ данных о фанфиках, связанных с книгами о Гарри Поттере. Основная цель проекта —
исследовать тенденции и закономерности в создании и популярности фанфиков, а также проанализировать основные
характеристики, такие как количество страниц, количество лайков, подписчиков и отзфвов.

Представим, что вы начинающий фикрайтер и сразу хотите стать популярным, однако вы не знаете в каком жанре писать, каких
героев использовать, и насколько длинным должен быть ваш фанфик. Этот проект поможет вам в этих вопросах.

## Данные

Для анализа используются два источника данных:

1. Фанфики с 2004 по 2019 год — данные взяты с сайта Kaggle.
2. Фанфики с 2020 по 2024 год — данные получены путем скрэпинга иностранного сайта fanfiction.net.

## Описание пайплайна

1. Сбор данных:
    - Данные с 2004 по 2019 год были загружены с Kaggle.
    - Данные с 2020 по 2024 год были собраны путем скрэпинга сайта fanfiction.net.

2. Подготовка данных:
    - Функция prepare_data_part1 обрабатывает данные с 2004 по 2019 год, удаляя ненужные столбцы и приводя данные к
      нужному формату.
    - Функция prepare_data_part2 выполняет аналогичную обработку для данных с 2020 по 2024 год, включая заполнение
      пропусков и переименование столбцов.
    - Функция create_union_data объединяет оба набора данных в один.
    - Функция remove_duplicates удаляет дубликаты фанфиков.

3. Анализ данных:
    - Анализ популярных пейрингов (функция add_pairings).
    - Группировка данных по годам и расчет средних значений для избранных, подписчиков и обзоров.
    - Выявление тенденций популярности фанфиков и их параметров по годам.

4. Визуализация данных:
    - Визуализация данных осуществляется с помощью Matplotlib, Seaborn, WordCloud, для построения графиков и диаграмм.
    - Пример: построение графика изменения популярности фанфиков по годам с помощью функции sns.lineplot.

## Результаты анализа

- Выявлено, что популярность фанфиков постоянно растёт
- Для написания фанфика лучше всего использовать рейтинг Т, а жанр Romance
- Для написания фанфика лучше всего использовать комбинацию персонажей: Гарри Поттер и Северус Снейп.
- Лучше всего писать фанфик объемом 200-300 тясяч слов
- Использование ключевых популярных слов немного влияет на популярность фанфика

## Архитектура проекта

Проект имеет следующую структуру:

```

├── .gitignore
├── README.md
├── analysis/
│ ├── __init__.py
│ ├── data.py
│ ├── fanfiction_project.ipynb
│ ├── features.py
│ └── visualization.py
├── data/
│ ├── fanfiction_data.csv
│ └── hpcleanvlarge1.csv
├── parser/
│ ├── __init__.py
│ ├── main.py
│ └── processing.py
├── poetry.lock
├── pyproject.toml
└── web/
├── __init__.py
└── app.py
```

### Описание компонентов

- analysis/ - Содержит скрипты для анализа данных.
    - data.py - функции для подготовки и объединения данных.
    - features.py - функции для извлечения дополнительных признаков из данных.
    - visualization.py - функции для визуализации данных.
    - fanfiction_project.ipynb - основной ноутбук Jupyter для анализа данных.
- data/ - Содержит исходные данные.
    - fanfiction_data.csv - данные с 2020 по 2024 год.
    - hpcleanvlarge1.csv - данные с 2004 по 2019 год.
- parser/ - Содержит скрипты для сбора данных.
    - main.py - основной скрипт для запуска процесса скрэпинга.
    - processing.py - функции для обработки собранных данных.
- web/ - Содержит скрипты для веб-интерфейса.
    - app.py - основной скрипт для запуска веб-приложения.

## Использованные технологии

- Python
- Selenium для скрэпинга
- продвинутые возможности pandas (группы)
- регулярные выражения
- numpy / scipy для решения математических задач
- библиотека networkx
- сложные визуализации
- построение предсказательных моделей типа регрессий или решающих деревьев
- некоторые графики проекта размещены на streamlit для большей наглядности
- библиотеки LinearSegmentedColormap, tqdm, itertools, collections, wordcloud, sklearn.metrics, не использовавшиеся в
  ходе курса
- Matplotlib
- Seaborn
- Jupyter Notebook для удобного анализа данных
- Poetry для удобного установления зависимостей