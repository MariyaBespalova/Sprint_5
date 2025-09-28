from selenium.webdriver.common.by import By

class Locators:
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка входа в аккаунт на главной странице
    NAME = (By.XPATH, "//label[text()='Имя']/../input")  #  поле ввода имени при регистрации
    EMAIL = (By.XPATH, "//label[text()='Email']/../input")  # поле ввода Email для регистрации
    PASSWORD = (By.XPATH, "//input[@type='password']")  # поле ввода пароля для регистрации
    REGISTRATION_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")  # кнопка Зарегистрироваться
    PERSONAL_CABINET_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")  # кнопка Личный кабинет
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")  #  кнопка конструктор
    TEXT_ERROR_PASSWORD = (By.XPATH, "//p[text() = 'Некорректный пароль']")  #  ошибка "Некорректный пароль"

    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")  # кнопка Войти
    EMAIL_BUTTON = (By.XPATH, "//input[@name='name']")  #  поле ввода Email в личном кабинете
    PASSWORD_BUTTON = (By.XPATH, "//input[@name='Пароль']")  #  поле ввода пароля в личном кабинете
    LOGIN_REGISTRATION_PAGE = (By.XPATH, "//a[@class = 'Auth_link__1fOlj']")  #
    PASSWORD_RECOVERY_BUTTON = (By.XPATH, "//a[text() = 'Восстановить пароль]")  #  кнопка "Восстановить пароль"
    LOGIN_BUTTON_PASSWORD_RECOVERY = (By.XPATH, "//a[text() = 'Войти']")  #  кнопка "Войти"
    EXIT_BUTTON = (By.XPATH, "//button[text() = 'Выход']")  #  кнопка выход
    LOGOTIP_STELLAR = (By.XPATH, "//div[@class = 'AppHeader_header__logo__2D0X2']") #  логотип стеллар бургер

    #  локаторы раздела Конструктор
    ROLLS_HEADLINE = (By.XPATH, "//h2[text() = 'Булки']")  
    SAUCE_HEADLINE = (By.XPATH, "//span[text() = 'Соусы']")  
    TOPPINGS_HEADLINE = (By.XPATH, "//span[text() = 'Начинки']")  
    GALAXY_SAUSE = (By.XPATH, "//p[text() = 'Соус традиционный галактический']")  
    TOPPINGS_MEAT = (By.XPATH, "//p[text() = 'Мясо бессмертных моллюсков Protostomia']")
    BURGER_INGREDIENT = (By.XPATH, "//p[text() = 'Флюоресцентная булка R2-D3']")