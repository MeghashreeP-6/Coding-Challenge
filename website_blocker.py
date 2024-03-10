#This is a real program that blocks certain distracting websites during your working hours. 
#If your current time is between working hours, that will block the websites and access them again if you reach free time.
import datetime
import time

host_path = "C:/Windows/System32/drivers/etc/hosts"
redirect = "127.0.0.1"
block_list = ["www.facebook.com"]
end_time = datetime.datetime(2024,3,11,10,00)

while True:
    if datetime.datetime.now() < end_time:
        print("Start Blocking")
        with open(host_path, "r+")as host_file:
            content = host_file.read()

            for websites in block_list:
                if websites not in content:
                    host_file.write(redirect + " " + websites + "\n")
                else:
                    pass

    else:
        with open(host_path, "r+") as host_file:
            content = host_file.readlines()
            host_file.seek(0)
            for lines in content:
                if not any (website in lines for website in block_list):
                    host_file.write(lines)
            host_file.truncate()
        time.sleep(5)
