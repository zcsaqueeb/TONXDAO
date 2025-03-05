import sys
import base64
import requests
import json
import time

sys.dont_write_bytecode = True

from itbaarts import base
from core.token import get_token, get_centrifugo_token
from core.info import get_info
from core.task import process_check_in, process_do_task
from core.ws import process_farm

def key_bot():
    api = base64.b64decode("aHR0cDovL2l0YmFhcnRzLmNvbS9hcGkuanNvbg==").decode('utf-8')
    try:
        response = requests.get(api)
        response.raise_for_status()
        try:
            data = response.json()
            header = data['header']
            print('\033[96m' + header + '\033[0m')
        except json.JSONDecodeError:
            print('\033[96m' + response.text + '\033[0m')
    except requests.RequestException as e:
        print('\033[96m' + f"Failed to load header: {e}" + '\033[0m')

class TONxDAO:
    def __init__(self):
        self.data_file = base.file_path(file_name="data.txt")
        self.config_file = base.file_path(file_name="config.json")
        self.line = base.create_line(length=50)
        self.auto_check_in = base.get_config(self.config_file, "auto-check-in")
        self.auto_do_task = base.get_config(self.config_file, "auto-do-task")
        self.auto_claim_ref = base.get_config(self.config_file, "auto-claim-ref")
        self.auto_farm = base.get_config(self.config_file, "auto-farm")

    def main(self):
        while True:
            base.clear_terminal()
            key_bot()
            data = open(self.data_file, "r").read().splitlines()
            num_acc = len(data)
            base.log(self.line)
            base.log(f"{base.green}Number of accounts: {base.white}{num_acc}")

            for no, data in enumerate(data):
                base.log(self.line)
                base.log(f"{base.green}Account number: {base.white}{no+1}/{num_acc}")
                try:
                    token = get_token(data=data)
                    if token:
                        dao_id = get_info(token=token)
                        centrifugo_token = get_centrifugo_token(token=token)
                        
                        if self.auto_check_in:
                            base.log(f"{base.yellow}Auto Check-in: {base.green}ON")
                            process_check_in(token=token)
                        else:
                            base.log(f"{base.yellow}Auto Check-in: {base.red}OFF")
                        
                        if self.auto_do_task:
                            base.log(f"{base.yellow}Auto Do Task: {base.green}ON")
                            process_do_task(token=token)
                        else:
                            base.log(f"{base.yellow}Auto Do Task: {base.red}OFF")
                        
                        if self.auto_farm:
                            base.log(f"{base.yellow}Auto Farm: {base.green}ON")
                            process_farm(token=centrifugo_token, dao_id=dao_id)
                        else:
                            base.log(f"{base.yellow}Auto Farm: {base.red}OFF")
                        
                        get_info(token=token)
                    else:
                        base.log(f"{base.red}Token not found! Please get new query id")
                except Exception as e:
                    base.log(f"{base.red}Error: {base.white}{e}")

            print()
            wait_time = 60 * 60 * 7  # 7 hours
            base.log(f"{base.yellow}Wait for {int(wait_time/3600)} hours!")
            time.sleep(wait_time)

if __name__ == "__main__":
    try:
        txd = TONxDAO()
        txd.main()
    except KeyboardInterrupt:
        sys.exit()
