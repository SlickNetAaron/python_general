import time
from datetime import datetime as dt
hosts_path = "/etc/hosts"
#hosts_path = r"C:\Windows\System32\drivers\etc\hosts"  # Real file, r for "row" so we don't have to escape
# hosts_path = "hosts" # Testing on a copy of hosts file

# Hours scheduled
work_start = 8
work_end = 17

redirect = "127.0.0.1"
website_list = ["facebook.com", "www.facebook.com", "hotmail.com", "www.hotmail.com",  "outlook.live.com"]

hour_now = dt.now().hour

def is_working_hours(work_start, work_end, hour_now):
    working = False
    if work_start <= hour_now < work_end:
        working = True
        return working
    else:
        working = False
        return working

assert not is_working_hours(6, 10, 4)
assert is_working_hours(6, 10, 6)
assert is_working_hours(6, 10, 8)
assert not is_working_hours(6, 10, 10)

while True:
    if is_working_hours(work_start, work_end, hour_now):
        print("is working hours")
        with open(hosts_path, 'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("is free time")
    time.sleep(5)