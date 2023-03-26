# WPA3Auto-Authentication-with-Selenium

This project is aimed at automating the process of authentication for WPA3 networks using Selenium. The project uses Python programming language and Selenium WebDriver to control the browser and perform authentication.

Note:For now, please note that this project only works on Mac devices and requires the installation of the macchanger program.

Project Features:

Supports automatic authentication for WPA3 networks.
Uses Selenium WebDriver to control the browser.
Provides a simple and easy-to-use interface.
Supports multiple browsers such as Chrome, Firefox, Safari, and Edge.
Can be easily integrated with other Python projects.

Requirements:

Python 3.x
Selenium WebDriver
ChromeDriver (for Chrome browser)
GeckoDriver (for Firefox browser)
SafariDriver (for Safari browser)
EdgeDriver (for Edge browser)

## Installation

### Clone the repository

```bash
git clone https://github.com/MuhammetBurakGolec/WPA3Auto-Authentication-with-Selenium.git
```

### Install the required packages

```bash
cd wpa3-auto-authentication
pip install -r requirements.txt
```

### Download and install the required drivers for your browser

ChromeDriver: https://sites.google.com/a/chromium.org/chromedriver/downloads
<br>
GeckoDriver: https://github.com/mozilla/geckodriver/releases
<br>
SafariDriver: https://webkit.org/blog/6900/webdriver-support-in-safari-10/
<br>
EdgeDriver: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/

## Usage

Modify the .env file with your network SSID, username, and password.

### Run the script

```bash
./auth.sh <ssid>
```

### File Structure

```bash
├── auth.sh
├── README.md
├── requirements.txt
├── src
│   ├── selenium_auth.py
│   ├── chromedriver (executable)
│   └── .env
└── .gitignore
```

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, please create an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
