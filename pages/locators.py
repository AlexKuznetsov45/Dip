from selenium.webdriver.common.by import By

# Общая группа локаторов
COMMON = {
    "search_field": (By.NAME, "kp_query"),  # Поле поиска
}

# Локаторы для главной страницы
MAIN_PAGE = {
    "new_film_link": (  # Новое местоположение карточки фильма
        By.CSS_SELECTOR,
        ("#__next > div.styles_root__goB3B > div.styles_middleContainer__vJjLN." +
         "styles_baseContainer__bGRTT > div.styles_mainContainer__59YLl > div." +
         "styles_contentSlot__h_lSN > main > div:nth-child(3) > div > div > div." +
         "styles_upper__j8BIs > div.styles_main__Y8zDm > a")
    ),
    "submit_button": (  # Кнопка "Найти"
        By.CSS_SELECTOR,
        ("#__next > div.styles_root__nRLZC > div.styles_root__BJH2_." +
         "styles_headerContainer__f7XqC > header > div > div." +
         "styles_mainContainer__faOVn.styles_hasSidebar__rU_E2 > div." +
         "styles_searchFormContainerWide__3taA3.styles_searchFormContainer__GyAL5 > div > form > " +
         "div > div > button")
    ),
    # Кнопка "Фильтры"
    "filters_button": (By.CSS_SELECTOR, "a.styles_advancedSearch__uwvnd"),
    "filter_section": (By.ID, "formSearchMain"),  # Раздел с фильтрами
    # Верхняя область результатов поиска
    "results_top_text": (By.CLASS_NAME, "search_results_topText"),
    # Контейнер результатов поиска
    "search_results_container": (By.CLASS_NAME, "search_results"),
    # Старое местонахождение фильма
    "first_search_result": (By.ID, "suggest-item-film-301"),
    "tickets_menu": (  # Меню "Билеты в кино"
        By.CSS_SELECTOR,
        ("#__next > div.styles_root__nRLZC > div.styles_root__BJH2_." +
         "styles_headerContainer__f7XqC > header > div > div." +
         "styles_mainContainer__faOVn.styles_hasSidebar__rU_E2 > div." +
         "styles_featureMenuContainerCompact__EOSwA.styles_featureMenuContainer__KbrzA > nav > " +
         "a:nth-child(2)")
    ),
    "buy_ticket_button": (  # Кнопка "Купить билет"
        By.CSS_SELECTOR,
        ("#__next > div.styles_root__vsmL9.styles_wideRoot__JrXG9 > div." +
         "styles_wideContentContainer__lu_K3 > main > div.styles_root__B1q5W." +
         "styles_rootDark__L1f7i.styles_root__axj8R > div.styles_root__UtArQ > div > div." +
         "styles_column__r2MWX.styles_md_17__FaWtp.styles_lg_21__YjFTk.styles_column__5dEFP > div > div > " +
         "div:nth-child(1) > div." +
         "styles_column__r2MWX.styles_md_11__UdIH_.styles_lg_15__Ai53P > div > div." +
         "styles_root__6T3Aa > div > div > div:nth-child(2) > a")
    ),
    "city_select": (  # Поле выбора города
        By.CSS_SELECTOR,
        ("body > div.app-container.app-container_app-theme_light > div > div." +
         "app__content.app__content_app-width_wide.app__content_app-theme_light > div." +
         "app__page.app__page_app-theme_light > div > main > div.film-header > div." +
         "page-content-topline > div.page-content-topline__right > div")
    ),
    # Родительский элемент выпадающего списка
    "dropdown_list": (By.CSS_SELECTOR, '.kinopoisk-header-suggest-group'),
    # Блок с надписью "Возможно, вы искали"
    "possible_titles_block": (By.CSS_SELECTOR, '.styles_title__irLOv'),
}

# Локаторы для страницы фильма
MOVIE_PAGE = {
    # Заголовок фильма
    "movie_title": (By.XPATH, "//span[@data-tid='75209b22']"),
    "movie_rating": (  # Рейтинг фильма
        By.XPATH,
        ("//span[@class='styles_ratingKpTop__84afd' and @data-tid='939058a8']")
    ),
}
