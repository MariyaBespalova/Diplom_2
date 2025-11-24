class Ingredients:
    BODY_WITHOUT_INGREDIENTS = { 'ingredients': []}
    BODY_INVALID_HASH_INGREDIENT = {'ingredients': ['61c0c5a71d1f82001bdaaa6c1']}

    @staticmethod
    def ingredients_body():
        bun = '61c0c5a71d1f82001bdaaa6d'
        main = '61c0c5a71d1f82001bdaaa6f'
        souse = '61c0c5a71d1f82001bdaaa72'
        return { 'ingredients': [bun, main, souse]}

class DataResponse:
    ORDER_WITHOUT_INGREDIENTS = {"success": False,"message": "Ingredient ids must be provided"}
    CREATING_REGISTERED_USER = {"success": False,"message": "User already exists"}
    CREATING_USER_WITHOUT_FILLED_FIELD = {"success": False, "message": "Email, password and name are required fields"}
    RECEIVING_ORDERS_AUTHORIZED_USER = {"success": False,"message": "You should be authorised"}
    AUTHORIZATION_WITH_INCORRECT_USERNAME_AND_PASSWORD = {"success": False,"message": "email or password are incorrect"}
    UPDATE_DATA_WITHOUT_AUTHORIZATION_USER = {"success": False,"message": "You should be authorised"}

class Data:
    USER_CREATION_DATA = [
        ("", 555555, "serega"),
        ("qatest-11@yandex.ru", "", "serega"),
        ("qatest-11@yandex.ru", 555555, "")
    ]

    EXPECTED_RESPONSE_BODY = {
        "message": "Заполните все обязательные поля",
        "code": 403,
        "type": "Bad Request"
    }
