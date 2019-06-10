# Auto login PIM wifi

Auto login PIM wifi เป็นโปรแกรมภาษา Python เล็กสำหรับทำให้ login wifi ของ PIM ( Panyapiwat Institute of Management ) แบบอัตโนมัติโดยไม่ต้องเข้าหน้าเว็บ

## วิธีติดตั้ง

ต้องติดตั้ง [python](https://www.python.org/downloads/) ก่อน


จากนั้นใช้คำสั่ง [pip](https://pip.pypa.io/en/stable/) ในการติดตั้ง

```bash
$ pip install -r requirements.txt
```
หากไม่ได้ให้ใช้

```bash
$ pip install selenium
```

## ตั้งค่า

ตั้งค่า Username กับ Password ในไฟล์ชื่อ config.py

config.py

```python
# user : password

my_username = "YOUR_USERNAME"
my_password = "YOUR_PASSWORD"
```

ตัวอย่างการตั้งค่า

```python
# user : password

my_username = "komsannip"
my_password = "pimpassword"
```

กรุณาเก็บรักษาไฟล์ไว้ให้ดี เนื่องจากไฟล์มีรหัสผ่านสำหรับเข้า wifi

## วิธีใช้

เปิดไฟล์ชื่อ main.py โดยการดับเบิ้ลคลิกปกติ หรือพิมพ์  

```bash
$ python main.py
```

## การอนุญาติ
[MIT](https://choosealicense.com/licenses/mit/)
