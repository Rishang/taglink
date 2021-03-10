# api for scraping metadata

## api setup

Steps to setup metadata scraping api

- Install required packages

    `pip3 install -r taglink/requirements.txt`

- Start api server

    `uvicorn main:app --host 0.0.0.0 --port 8800 --reload`

- vist api docs, on your browser

    `http://0.0.0.0:8800/docs`
