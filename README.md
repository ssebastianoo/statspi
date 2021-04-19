# StatsPi
`statspi` is a local website that gives you info about your raspberry pi.

![statspi](https://i.imgur.com/rlpZ1LX.png)

### How to Run
open your terminal, go wherever you want and run
```
git clone https://github.com/ssebastianoo/statspi
cd statspi
python3 -m pip install flask
python3 -m pip install psutil
```
now we need to setup this to run on boots and reboots, to do this we need to edit `rc.local`
```
sudo nano /etc/rc.local
```
scroll down, and paste (on the line befor `exit 0`)
```
cd <location to folder>
sudo python3 server.py &
```
the file should look something like this:
```
#!/bin/sh -e
#
# rc.local
#
# This script is executed at the end of each multiuser runlevel.
# Make sure that the script will "exit 0" on success or any other
# value on error.
#
# In order to enable or disable this script just change the execution
# bits.
#
# By default this script does nothing.

# Print the IP address
_IP=$(hostname -I) || true
if [ "$_IP" ]; then
  printf "My IP address is %s\n" "$_IP"
fi

cd /home/pi/Desktop/codes/statspi
sudo python3 server.py &
exit 0
```
now reboot the raspberry, open the browser from any device connected to the same wifi as the raspberry and go to `raspberry ip` (like `123.456.1.234`)

### Setup Port and Host
you can edit `host` and `port` editing `config.json`

