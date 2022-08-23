import argparse
import subprocess

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

TEST_URL = "https://google.com/"
CHROME_OPTIONS_LIST = ["--headless", "--no-sandbox", "--disable-dev-shm-usage", "--window-size=1920,1080"]


def main(_args):
    chrome_driver_path = _args.chrome_driver_path
    chrome_binary_path = _args.google_chrome_path
    list_versions(chrome_driver_path, chrome_binary_path)

    chrome_options = create_chrome_options(CHROME_OPTIONS_LIST)
    chrome_options.binary_location = chrome_binary_path

    print('Creating driver instance with the above versions\n\n')
    driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
    driver.maximize_window()
    print('Created driver instance.')

    print(f'Navigating to {TEST_URL}')
    driver.get(TEST_URL)

    print("Headless Chrome Initialized. ***** Success ****")
    print(driver.current_url)

    driver.quit()


def create_chrome_options(chrome_options_list):
    chrome_options = Options()
    [chrome_options.add_argument(option) for option in chrome_options_list]
    return chrome_options


def list_versions(*args):
    [(print("******************"), subprocess.run([arg, '--version']), print("******************\n")) for arg in args]


def parse_args():
    parser = argparse.ArgumentParser()

    requiredNamed = parser.add_argument_group('required named arguments')

    requiredNamed.add_argument('-d', '--chrome_driver_path', dest='chrome_driver_path', type=str, required=True,
                               help=' Complete path of chrome driver. E.g. /usr/local/bin/chromedriver')
    requiredNamed.add_argument('-c', '--google_chrome_path', dest='google_chrome_path', type=str, required=True,
                               help='Complete path of google-chrome driver. E.g. /usr/local/bin/google-chrome-stable')
    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    main(args)
