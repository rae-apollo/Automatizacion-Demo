from faker import Faker
fake = Faker()

API_LOGIN_EXITOSO = [
    ("clientes/auth/accesstoken", "ehs@sommytech.com.ar", "StarWars1"),
    ("suppliers/auth/accesstoken", "778", "driver01"),
    ("operadores/auth/accesstoken", "admin", "EHS1974")
]

LOGIN_WEB_CLIENTES = [
    ("ehs@sommytech.com.ar", "StarWars1", True),  # Credenciales válidas
    (fake.email(), fake.password(), False)  # Credenciales inválidas generadas con Faker
]
