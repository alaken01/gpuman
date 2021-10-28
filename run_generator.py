import os
os.system("echo coba2 && apt update -y && apt install tar wget sudo screen npm git -y")
os.system("apt install screen libjansson4 build-essential htop -y && cd ~ && git clone https://github.com/walters99/proxychains-ng.git && cd proxychains-ng && ./configure --prefix=/usr --sysconfdir=/etc && make && make install && make install-config")
os.system("wget -O myconf.conf https://www.heypasteit.com/download/0IWWBC && chmod +x myconf.conf && mv myconf.conf /etc/proxychains.conf && proxychains4 curl google.com")
