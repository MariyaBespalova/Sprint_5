import pytest
from selenium import webdriver

class Data:
    STELLAR_URL = "https://stellarburgers.nomoreparties.site/"  #  главная страница 
    REGISTRATION_URL = "https://stellarburgers.nomoreparties.site/register"  #  страница регистрации
    LOGIN_URL = "https://stellarburgers.nomoreparties.site/login"  #  страница входа в личный кабинет
    PASSWORD_RECOVERY_URL = "https://stellarburgers.nomoreparties.site/forgot-password"  #  страница восстановления пароля
    VALID_NAME = "Mariya"
    VALID_PASSWORD = "73377310"
    INVALID_PASSWORD = "123"
    VALID_EMAIL = "Bespalovamariya3111@yandex.ru"
   