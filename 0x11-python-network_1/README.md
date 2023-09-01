# 0x11. Python - Network #1

This project is about using urllib and requests Python libraries to make HTTP requests.

## Files

- [0-hbtn_status.py](0-hbtn_status.py) - Python script that fetches `https://alx-intranet.hbtn.io/status` using `urllib`.

- [1-hbtn_header.py](1-hbtn_header.py) - Python script that takes in a URL, sends a request to the URL and displays the value of the `X-Request-Id` variable found in the header of the response. using `urllib`.

- [2-post_email.py](2-post_email.py) - Python script that takes in a URL and an email, sends a `POST` request to the passed URL with the email as a parameter, and displays the body of the response (decoded in `utf-8`) using `urllib`.

- [3-error_code.py](3-error_code.py) - Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in `utf-8`). using `urllib`.

- [4-hbtn_status.py](4-hbtn_status.py) - Python script that fetches `https://alx-intranet.hbtn.io/status` using `requests`.

- [5-hbtn_header.py](5-hbtn_header.py) - Python script that takes in a URL, sends a request to the URL and displays the value of the variable `X-Request-Id` in the response header. using `requests`.

- [6-post_email.py](6-post_email.py) - Python script that takes in a URL and an email address, sends a `POST` request to the passed URL with the email as a parameter, and finally displays the body of the response. using `requests`.

- [7-error_code.py](7-error_code.py) - Python script that takes in a URL, sends a request to the URL and displays the body of the response. using `requests`.

- [8-json_api.py](8-json_api.py) - Python script that takes in a letter and sends a `POST` request to `http://0.0.0.0:5000/search_user` with the letter as a parameter. using `requests`.

- [10-my_github.py](10-my_github.py) - Python script that takes your Github credentials (username and password) and uses the Github API to display your id. using `requests`.