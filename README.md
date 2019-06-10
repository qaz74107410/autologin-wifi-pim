# Auto login PIM wifi

Auto login PIM wifi is a mini Python program for one click to login PIM ( Panyapiwat Institute of Management ) wifi.

## Installation

Require [python](https://www.python.org/downloads/) to be installed.


Use the package manager [pip](https://pip.pypa.io/en/stable/) to install aditional package.

```bash
$ pip install -r requirements.txt
```
or

```bash
$ pip install selenium
```

## Config

Edit your username and password wifi in config.py file.

config.py

```python
# user : password

my_username = "YOUR_USERNAME"
my_password = "YOUR_PASSWORD"
```

Example

```python
# user : password

my_username = "komsannip"
my_password = "pimpassword"
```

Make sure you keep this file in safe place.

## Usage

run main.py regularly with double click or  

```bash
$ python main.py
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
