import logging
from datetime import datetime
import requests

logging.basicConfig(filename='ipsumPortScan.log', filemode='w', level =  logging.INFO , format='%(name)s - %(levelname)s - %(message)s')

def getIPSUM():

    repo_url = 'https://github.com/stamparm/ipsum'
    branch = "master"
    file_path = 'ipsum.txt'
    raw_url = f'{repo_url.rstrip("/")}/raw/{branch}/{file_path}'
    FINAL_IPS = []
    try:
        response = requests.get(raw_url)
        response.raise_for_status()
        ipsum = response.text
        ipsumLines = ipsum.splitlines()
        for record in ipsumLines:
            if "#" not in record:
                ip=record.split("\t")
                FINAL_IPS.append(ip[0])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching file: {e}")
    return FINAL_IPS

def main():

    logging.info(f"Started at {datetime.now()}")

    IPADDRESSES = getIPSUM()
    logging.info(f"Found {len(IPADDRESSES)} IP's from the ipsum list")
    logging.info(f"Writting to in/ipaddress.txt")
    with open("in/ipaddress.txt","w") as ipFile:
        for IP in IPADDRESSES:
            ipFile.write(f'{IP}\n')
            
    logging.info(f"Finished at {datetime.now()}\n")

if __name__ == "__main__":
    main()