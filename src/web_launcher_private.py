import webbrowser

class WebLauncher:
    def open_user_website(self):
        url = self.__prompt_user()
        if url.lower().strip() != 'exit':
            self.__launch_browser(url)

    def __prompt_user(self):
        return input('Enter the URL you want to visit (Type "exit" to decline): ')
    
    def __launch_browser(self, url):
        webbrowser.open(url)

if __name__ == '__main__':
    launcher = WebLauncher()
    launcher.open_user_website()
