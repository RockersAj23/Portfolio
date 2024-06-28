import webbrowser

def open_website(url):
    # Specify the path to the Edge browser executable
    edge_path = "C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe"

    # Set the path to Edge browser as the browser executable
    webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))

    # Open the specified URL in Edge browser
    webbrowser.get('edge').open(url)

if __name__ == "__main__":
    # URL of the website you want to open
    website_url = "http://127.0.0.1:5000"

    # Open the website in Edge browser
    open_website(website_url)
