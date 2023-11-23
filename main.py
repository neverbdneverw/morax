import flet as ft

from flet_route import Routing, path
from views import *
from controllers import *
from model import *

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
    
    repository = Repository()

    HomeController(page, repository, home_page)
    AddDialogController(page, repository, home_page)
    ItemInfoDialogController(page, repository, home_page)
    AddReceivableDialogController(page, repository, home_page)
    AccountSettingsDialogsController(page, repository, home_page)
    ReceivableInfoDialogController(page, repository, home_page)
    OpeningController(page, opening_page)
    OnboardingController(page, repository, onboarding_page)
    LoginController(page, repository, login_page)
    SignupController(page, repository, signup_page)
    ForgotController(page, repository, forgot_password_page)
    ConfirmEmailController(page, repository, confirm_email_page)

if __name__ == "__main__":
    ft.app(target=main)