import flet as ft

from flet_route import Routing, path
from views.opening_page import OpeningPage
from views.login_page import LoginPage
from views.signup_page import SignupPage
from views.forgot_password_page import ForgotPasswordPage
from views.confirm_email_page import ConfirmEmailPage
from views.home_page import HomePage
from views.onboarding_page import OnboardingPage

from controllers.opening_controller import OpeningController
from controllers.login_controller import LoginController
from controllers.signup_controller import SignupController
from controllers.forgot_controller import ForgotController
from controllers.confirm_email_controller import ConfirmEmailController
from controllers.home_controller import HomeController
from controllers.add_dialog_controller import AddDialogController
from controllers.item_info_dialog_controller import ItemInfoDialogController
from controllers.add_receivable_dialog_controller import AddReceivableDialogController
from controllers.onboarding_page_controller import OnboardingController
from controllers.account_settings_dialogs_controller import AccountSettingsDialogsController

from controllers.Database import Database

def main(page: ft.Page):
    page.window_width = 1024
    page.window_height = 768
    page.theme_mode = ft.ThemeMode.LIGHT
    page.title = "Morax"
    
    confirm_email_page = ConfirmEmailPage()
    opening_page = OpeningPage()
    signup_page = SignupPage()
    login_page = LoginPage()
    forgot_password_page = ForgotPasswordPage()
    onboarding_page = OnboardingPage()
    
    home_page = HomePage()
    
    app_routes = [
        path(url="/", clear=True, view=opening_page.get_view),
        path(url="/login", clear=True, view=login_page.get_view),
        path(url="/signup", clear=True, view=signup_page.get_view), 
        path(url="/forgot_password", clear=True, view=forgot_password_page.get_view),
        path(url="/confirm_email", clear=True, view=confirm_email_page.get_view),
        path(url="/home", clear=True, view=home_page.get_view),
        path(url="/onboarding", clear=False, view=onboarding_page.get_view)
    ]
    
    Routing(page = page, app_routes = app_routes)
    page.go(page.route)
    
    # page.client_storage.clear()
    
    database = Database()

    HomeController(page, database, home_page)
    AddDialogController(page, database, home_page)
    ItemInfoDialogController(page, database, home_page)
    AddReceivableDialogController(page, database, home_page)
    AccountSettingsDialogsController(page, database, home_page)
    OpeningController(page, database, opening_page)
    OnboardingController(page, database, onboarding_page)
    LoginController(page, database, login_page)
    SignupController(page, database, signup_page)
    ForgotController(page, database, forgot_password_page)
    ConfirmEmailController(page, database, confirm_email_page)

if __name__ == "__main__":
    ft.app(target=main)