FROM  --platform=linux/amd64d python:3-slim

ENV CHROME_DRIVER_DIR=/usr/local/bin

RUN apt-get -y update && apt-get install -y unzip curl gnupg git

# install google chrome
RUN curl https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
RUN apt-get -y update && apt-get install -y google-chrome-stable \
  && google-chrome --version

# install chromedriver
RUN CHROMEDRIVER_LATEST_RELEASE=$(curl -sS https://chromedriver.storage.googleapis.com/LATEST_RELEASE) \
  && curl -o /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/${CHROMEDRIVER_LATEST_RELEASE}/chromedriver_linux64.zip \
  && unzip /tmp/chromedriver.zip chromedriver -d "${CHROME_DRIVER_DIR}" \
  && rm /tmp/chromedriver.zip \
  && "${CHROME_DRIVER_DIR}/chromedriver" --version

# set display port to avoid crash and dbus env to avoid hanging
ENV DISPLAY=:99
ENV DBUS_SESSION_BUS_ADDRESS=/dev/null

COPY requirements.txt /tmp/

RUN cd /tmp \
    && pip install --upgrade pip \
    && pip install -r requirements.txt \
    && timeout --foreground --verbose 10  python3 selenium-smoke-test.py --chrome_driver_path  "${CHROME_DRIVER_DIR}/chromedriver" --google_chrome_path "$(which google-chrome-stable)"

RUN mkdir /code
WORKDIR /code
