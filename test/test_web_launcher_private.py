from src.web_launcher_private import WebLauncher
import unittest
from unittest.mock import patch

class WebLauncherPrivateTest(unittest.TestCase):

    def test_open_user_website_exit_response(self):
        with patch.object(WebLauncher, '_WebLauncher__prompt_user') as prompt_user_mock,\
             patch.object(WebLauncher, '_WebLauncher__launch_browser') as launch_browser_mock:
            prompt_user_mock.return_value = 'exit'
            web_launcher = WebLauncher()
            web_launcher.open_user_website()
            launch_browser_mock.assert_not_called()

    def test_open_user_website_url_response(self):
        with patch.object(WebLauncher, '_WebLauncher__prompt_user') as prompt_user_mock,\
             patch.object(WebLauncher, '_WebLauncher__launch_browser') as launch_browser_mock:
            prompt_user_mock.return_value = 'https://google.com'
            web_launcher = WebLauncher()
            web_launcher.open_user_website()
            launch_browser_mock.assert_called_once_with('https://google.com')
