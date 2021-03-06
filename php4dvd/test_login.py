__author__ = 'agorgoma'

from model.user import User
# from selenium_fixture import app


def test_login_with_invalid_credentials(app):
    app.ensure_logout()
    app.login(User.random())
    assert app.is_not_logged_in()


def test_login(app):
    app.ensure_logout()
    app.login(User.Admin())
    assert app.is_logged_in()
