import os

import streamlit as st


def main():
    st.title("Harry Potter Fanfics Analytics")

    data_path = "data/images"
    with st.expander(
            "Гипотеза 1: Популярность фанфиков (измеряемая количеством избранных, подписчиков и обзоров) со временем возросла"
    ):
        st.image(os.path.join(data_path, "H1/опубликованные фанфики.png"))
        st.image(os.path.join(data_path, "H1/средние показатели.png"),
                 caption="Использовались библиотеки matplotlib.pyplot и seaborn")

    with st.expander("Гипотеза 2: Более длинные фанфики более популярны"):
        st.image(os.path.join(data_path, "H2/зависимость между количеством слов и лайками.png"),
                 caption="Использовались библиотеки numpy и statsmodels.api")
        st.image(os.path.join(data_path, "H2/зависимость между количеством слов и подписчиками.png"))
        st.image(os.path.join(data_path, "H2/матрица корелляций слов, лайков и подписчиков.png"),
                 caption="Использовались библиотеки matplotlib.pyplot и seaborn")

    with st.expander("Гипотеза 3: Определенные персонажи и пары более популярны, чем другие."):
        st.image(os.path.join(data_path, "H3/топ 25 популярных пейрингов.png"),
                 caption="Использовались библиотеки networkx, matplotlib.pyplot, Counter, combinations, LinearSegmentedColormap")

    with st.expander("Гипотеза 4: Рейтинг фанфиков влияет на их популярность."):
        st.image(os.path.join(data_path, "H4/популярность разных рейтингов по годам.png"))
        rating = st.selectbox("Выберите рейтинг", ["K", "K+", "T"])
        st.image(os.path.join(data_path, f"H4/рейтинги/{rating}.png"))

    with st.expander("Гипотеза 5: Жанр фанфиков влияет на их популярность."):
        st.text("Без графиков")

    with st.expander(
            "Гипотеза 6: Наличие определенных ключевых слов в названии коррелирует с более высокой популярностью (лайки)."
    ):
        st.image(os.path.join(data_path, "H6/облако слов в названиях фф.png"),
                 caption="Использовались библиотеки re, WordCloud, matplotlib.pyplot")

    with st.expander("Предсказательная модель"):
        st.image(os.path.join(data_path, "H7/влияние параметров на предсказание модели.png"))


if __name__ == "__main__":
    main()
