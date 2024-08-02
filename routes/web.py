from masonite.routes import Route
from app.controllers.auth.LoginController import LoginController
from app.controllers.auth.RegisterController import RegisterController
from app.controllers.auth.PasswordResetController import PasswordResetController


ROUTES = [
    Route.get("/", LoginController.show).name("login"),
    Route.post("/", LoginController.store).name("login.store"),
    Route.get("/logout", LoginController.logout).name("logout"),
    Route.get("/register", RegisterController.show).name("login.register"),
    Route.post("/register", RegisterController.store).name("register.store"),
    Route.get("/forgotpassword", PasswordResetController.show).name("login.forgot_password"),
    Route.post("/passwordreset", PasswordResetController.show).name("password_reset.store"),
]
