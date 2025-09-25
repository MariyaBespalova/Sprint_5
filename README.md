Файл data.py - собраны все основные URL для тестирования.

Файл locators.py - локаторы, которые были использованы при проведении тестирования.

Файл conftest.py содержит фикстуры.

Файл test_registration - покрывает тестами регистрацию:
    - def test_registration_exists - проверка успешной регистрации
    - def test_incorrect_password  - тестирование регистрации с невалидным паролем

Файл test_login_in_to_website - покрывает тестами вход на сайт различными способами
    - def test_sing_in_to_account_button - вход на сайт по кнопке "Войти в аккаунт"
    - def test_log_in_to_personal_account - вход через личный кабинет
    - def test_log_in_to_register_form - вход через форму регистрации
    - def test_log_to_in_password_recovery - вход через форму восстановления пароля

Файл test_conversion - покрывает тестами переходы между страницами
    - def test_conversion_to_constructor - переход из личного кабинета в конструктор
    - def test_click_to_logotip - переход по клику на логотип Stellar Burgers

Файл test_go_to_section - покрывает тестами переходы между разделами конструктора 
    - def test_go_to_sauses - переход в раздел соусы
    - def test_go_to_toppings - переход в раздел начинки

Файл test_log_out_of_account - тестирует выход из аккаунта
    - def test_log_out_of_account
