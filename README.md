# IPSUM List Port Scans

This repository contains the output of port scans against the suspicious and/or malicious IP addresses from this repository, "https://github.com/stamparm/ipsum/tree/master". 


# Setup

```
git clone https://github.com/c2links/ipsum_port_scan.git
```

# Run
The purpose of this repository is to provide the scan results to others to use as they see fit, as such, there is nothign for users to 'run'.

The output is generated using the shell commands below which 
1. Download / normalize the IP addresses from IPSUM
2. Perform a port scan on IP addresses for the folowing ports
    - 80,443,81,443,3000,3001,10010,32768,49152-49157,50000,8443,8080,4782,1234,12345,5000,2222,3333
3. Upload results to this repository

## Commands
```
cd ipsum_port_scan
python3 ipsum_port_scan.py
masscan -oJ out/ipsum_port_scan.json -p80,443,81,443,3000,3001,10010,32768,49152-49157,50000,8443,8080 -iL in/ipaddress.txt --max-rate 1000
git add --all .
git commit -m "ipsum_port_update"
git push git@github.com:c2links/ipsum_port_scan.git

```
<b>Depending on your system, you may have to run the script at a root / system level in order for Masscan to work. </b>

# Output

Results are automatically sent to the <i>'out'</i> folder, and overwrite the file, <i>'ipsum_port_scan.json'</i>. A sample output is below.

```
[
{   "ip": "213.66.75.226",   "timestamp": "1706215401", "ports": [ {"port": 443, "proto": "tcp", "status": "open", "reason": "syn-ack", "ttl": 52} ] }
,
{   "ip": "159.223.96.213",   "timestamp": "1706215401", "ports": [ {"port": 80, "proto": "tcp", "status": "open", "reason": "syn-ack", "ttl": 57} ] }
...
{   "ip": "173.234.226.34",   "timestamp": "1706215401", "ports": [ {"port": 8080, "proto": "tcp", "status": "open", "reason": "syn-ack", "ttl": 51} ] }
]

```




