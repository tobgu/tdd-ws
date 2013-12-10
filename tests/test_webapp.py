from webapp import app


def test_it_can_serve_HTTP():
    browser = app.test_client()
    response = browser.get('/')
    assert response.status_code == 200
