import webview
import socket
import ssl
import os

# URL to load
url = "https://cafe.geeks-soft.uz/"

def setup_ssl_ignore():
    """Configure environment to ignore SSL certificate errors"""
    # Disable SSL verification for Python's urllib/requests
    os.environ['PYTHONHTTPSVERIFY'] = '0'
    os.environ['CURL_CA_BUNDLE'] = ''
    os.environ['REQUESTS_CA_BUNDLE'] = ''
    
    # For CEF backend (if used)
    os.environ['CEF_PYTHON_IGNORE_SSL_ERRORS'] = '1'
    
    # Disable SSL verification globally
    ssl._create_default_https_context = ssl._create_unverified_context

def check_internet_connection():
    """Check if internet connection is available"""
    try:
        # Try to connect to a reliable host (Google DNS)
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return True
    except OSError:
        try:
            # Alternative check using Cloudflare DNS
            socket.create_connection(("1.1.1.1", 53), timeout=3)
            return True
        except OSError:
            try:
                # Try to resolve a domain name
                socket.gethostbyname("google.com")
                return True
            except socket.gaierror:
                return False

class API:
    """API class for JavaScript-Python communication"""
    def __init__(self, window):
        self.window = window
    
    def reload_page(self):
        """Reload the page by checking connection and loading URL"""
        if check_internet_connection():
            self.window.load_url(url)
            return True
        else:
            return False

if __name__ == '__main__':
    # Setup SSL certificate ignoring
    setup_ssl_ignore()
    
    # Check internet connection
    if not check_internet_connection():
        print("Error: No internet connection detected!")
        # Create a simple error page
        error_html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>No Internet Connection</title>
            <meta charset="UTF-8">
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    background-color: #f0f0f0;
                }}
                .error-container {{
                    text-align: center;
                    padding: 40px;
                    background: white;
                    border-radius: 10px;
                    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                }}
                h1 {{ color: #e74c3c; }}
                .reload-btn {{
                    margin-top: 20px;
                    padding: 12px 30px;
                    font-size: 16px;
                    background-color: #3498db;
                    color: white;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                    transition: background-color 0.3s;
                }}
                .reload-btn:hover {{
                    background-color: #2980b9;
                }}
                .reload-btn:active {{
                    transform: scale(0.98);
                }}
                .reload-btn:disabled {{
                    background-color: #95a5a6;
                    cursor: not-allowed;
                }}
            </style>
        </head>
        <body>
            <div class="error-container">
                <h1>⚠️ No Internet Connection</h1>
                <p>Please check your internet connection and try again.</p>
                <button class="reload-btn" id="reloadBtn" onclick="reloadPage()">🔄 Reload</button>
            </div>
            <script>
                async function reloadPage() {{
                    const btn = document.getElementById('reloadBtn');
                    btn.disabled = true;
                    btn.textContent = 'Checking...';
                    
                    try {{
                        // Try to navigate to the actual URL
                        window.location.href = '{url}';
                    }} catch (error) {{
                        btn.disabled = false;
                        btn.textContent = '🔄 Reload';
                    }}
                }}
            </script>
        </body>
        </html>
        """
        window = webview.create_window(
            'Cafe - Geeks Soft',
            html=error_html,
            width=1200,
            height=800,
            resizable=True,
            min_size=(800, 600),
        )
        # Create API instance for this window
        api = API(window)
    else:
        # Create webview window
        # SSL certificate errors will be ignored due to setup_ssl_ignore()
        window = webview.create_window(
            'Cafe - Geeks Soft',
            url,
            width=1024,
            height=748,
            resizable=True,
            min_size=(800, 600),
        )
        api = API(window)
    
    # Start webview with API (for future use if needed)
    webview.start(debug=False)

