import time
from pathlib import Path

import pytest
import requests
from pushnotifier.PushNotifier import PushNotifier
from pushnotifier.exceptions import DeviceNotFoundError


IMAGE_PATH = Path(__file__).parent / "img" / "tux-small.png"

# Run with: pytest --user u --password p --package p --token t
# Show console output with: pytest -s


@pytest.fixture
def pushnotifier(request):
    print("Setup credentials for tests")
    user = request.config.getoption("--user")
    password = request.config.getoption("--password")
    token = request.config.getoption("--token")
    package = request.config.getoption("--package")
    assert user is not None
    assert password is not None
    assert token is not None
    assert package is not None
    yield PushNotifier(user, password, package, token)


@pytest.fixture(autouse=False)
def slow_down_tests():
    yield
    time.sleep(0.1)


class TestPushNotifier:
    def test_connection(self):
        try:
            r = requests.get("https://www.google.com", timeout=5.0)
            assert r.status_code == 200
        except:
            assert False

    @pytest.mark.skip(reason="Not implemented yet")
    def test_login_200(self, pushnotifier):
        pass

    @pytest.mark.skip(reason="Not implemented yet")
    def test_login_404(self, pushnotifier):
        pass

    @pytest.mark.skip(reason="Not implemented yet")
    def test_login_403(self, pushnotifier):
        pass

    def test_refresh_token(self, pushnotifier):
        old_token = pushnotifier.app_token
        new_token = pushnotifier.refresh_token()
        assert type(new_token) == str
        assert pushnotifier.app_token == new_token  # check if method sets app token
        assert old_token != new_token  # check if a new token is generated

    def test_get_all_devices(self, pushnotifier):
        devices = pushnotifier.get_all_devices()
        assert len(devices) > 0
        for device in devices:  # check length of device ID's
            assert len(device) == 4

    def test_send_text_200(self, pushnotifier):
        pushnotifier.send_text("test_send_text_200")

    def test_send_text_404(self, pushnotifier):
        with pytest.raises(DeviceNotFoundError):
            pushnotifier.send_text("test_send_text_400", devices=["ABCD"])

    def test_send_url0_200(self, pushnotifier):
        pushnotifier.send_url("https://test-send-url-200.com")

    def test_send_url_404(self, pushnotifier):
        with pytest.raises(DeviceNotFoundError):
            pushnotifier.send_url("https://test-send-url-404.com", devices=["ABCD"])

    def test_send_notification_200(self, pushnotifier):
        pushnotifier.send_notification(
            "test_send_notification_200", "https://test-send-notification-200.com"
        )

    def test_send_notification_404(self, pushnotifier):
        with pytest.raises(DeviceNotFoundError):
            pushnotifier.send_notification(
                "test_send_notification_404",
                "https://test-send-notification-404.com",
                devices=["ABCD"],
            )

    def test_send_image_200(self, pushnotifier):
        pushnotifier.send_image(str(IMAGE_PATH))

    @pytest.mark.skip("Not implemented yet")
    def test_send_image_413(self, pushnotifier):
        pass

    def test_send_image_404(self, pushnotifier):
        with pytest.raises(DeviceNotFoundError):
            pushnotifier.send_image(str(IMAGE_PATH), devices=["ABCD"])
