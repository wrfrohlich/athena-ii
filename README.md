# ATHENA I - Version II

## 0 - Prepare the System

`sudo su`

`passwd`

`sed -i.bkp 's|#PermitRootLogin prohibit-password|PermitRootLogin yes|i' /etc/ssh/sshd_config`



## 1 - Startup Commands:

### 1.1 - Install:

- Install system:

`sudo bash athena-ii/build.sh`

or

`unzip athena-i.zip && rm -rf athena-i.zip && sudo bash athena-ii/build.sh`


### 1.2 - Bluetooth:

`sudo bluetoothctl`

- `scan on`
  
- `pair xx:xx:xx:xx:xx:xx`


### 1.3 - Crontab:

`crontab -e`

- `1`
	
- `#crontab`



## 3 - Useful Commands:

### 3.1 - Basic Commands:

- Access database:

`sqlite3 /home/athena/ftp/files/athena-ii/athena-i.db`

- Start Manually the **Processing**

`sudo python3 /etc/athena-ii/models/receive.py`


### 3.1 - Advanced Commands:

- Remove ATHENA I:

`sudo bash /etc/athena-ii/remove.sh`

- Remove database

`rm -rf /home/athena/ftp/files/athena-ii/athena-i.db`