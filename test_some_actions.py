import os

from dotenv import load_dotenv
from selene import browser, have, be
from selene.support.shared.jquery_style import s, ss

load_dotenv()
qa_guru = os.getenv("QA_GURU")
login = os.getenv("OWN_LOGIN")
password = os.getenv("OWN_PASS")
google = os.getenv('GOOGLE')
fail_google_request = os.getenv('FAIL_SEARCH')


def test_account_login():
    browser.open(qa_guru)
    s('[name=email]').type(login)
    s('[name=password]').type(password).press_enter()
    s('.xdget-block').should(have.text('Актуальные события'))
    s('.page-header').should(have.text('Список тренингов'))

    s('[title=Профиль]').click()
    s('.subitem-link').should(be.clickable)

    ss('.subitem-link')[3].should(have.text('ВЫЙТИ')).click()
    s('#xdget172046_1').should(have.text('Войти'))

    s('[name=email]').should(be.blank).click().type('fakemail')
    s('[name=password]').should(be.blank).click().type(password)
    s('#xdget33092_1').should(have.text('Войти')).click()
    s('.btn-error').should(have.text('Неверный формат e-mail'))


def test_google_search():
    browser.open(google)
    s('[name=q]').type('yashaka/selene').press_enter()
    ss('.LC20lb')[0].should(have.text('yashaka/selene: User-oriented Web UI browser tests in')).click()
    s('.my-3').should(have.text('User-oriented Web UI browser tests in Python'))


def test_fail_google_search():
    browser.open(google)
    s('#APjFqb').should(be.clickable).type(fail_google_request).press_enter()
    browser.element('#search-result').should(have.no.text(fail_google_request))

