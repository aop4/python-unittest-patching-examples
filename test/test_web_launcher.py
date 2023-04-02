from src.web_launcher import WebLauncher
import unittest
from unittest.mock import patch

class WebLauncherTest(unittest.TestCase):
    
    @patch.object(WebLauncher, 'prompt_user')
    @patch.object(WebLauncher, 'launch_browser')
    def test_open_user_website_exit_response_patch_decorator(self, launch_browser_mock, prompt_user_mock):
        prompt_user_mock.return_value = 'exit'
        web_launcher = WebLauncher()
        web_launcher.open_user_website()
        launch_browser_mock.assert_not_called()

    @patch.object(WebLauncher, 'prompt_user')
    @patch.object(WebLauncher, 'launch_browser')
    def test_open_user_website_url_response_patch_decorator(self, launch_browser_mock, prompt_user_mock):
        prompt_user_mock.return_value = 'https://google.com'
        web_launcher = WebLauncher()
        web_launcher.open_user_website()
        launch_browser_mock.assert_called_once_with('https://google.com')

    def test_open_user_website_exit_response_using_with(self):
        with patch.object(WebLauncher, 'prompt_user') as prompt_user_mock,\
             patch.object(WebLauncher, 'launch_browser') as launch_browser_mock:
            prompt_user_mock.return_value = 'exit'
            web_launcher = WebLauncher()
            web_launcher.open_user_website()
            launch_browser_mock.assert_not_called()
    
    def test_open_user_website_url_response_using_with(self):
        with patch.object(WebLauncher, 'prompt_user') as prompt_user_mock,\
             patch.object(WebLauncher, 'launch_browser') as launch_browser_mock:
            prompt_user_mock.return_value = 'https://google.com'
            web_launcher = WebLauncher()
            web_launcher.open_user_website()
            launch_browser_mock.assert_called_once_with('https://google.com')

    def test_open_user_website_stub_built_in_methods(self):
        with patch('src.web_launcher.input') as input_mock,\
             patch('webbrowser.open') as open_mock:
            input_mock.return_value = 'https://google.com'
            web_launcher = WebLauncher()
            web_launcher.open_user_website()
            open_mock.assert_called_once_with('https://google.com')
