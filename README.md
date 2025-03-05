# TONxDAO Bot

## Overview
TONxDAO is an automated script for managing accounts, performing check-ins, completing tasks, and farming operations using API-based authentication.

## Features
- Auto check-in for registered accounts
- Automated task completion
- Farming automation
- Configurable settings via `config.json`
- Runs automatically every 7 hours

## Requirements
- Python 3.x
- Required libraries: `requests`, `json`, `base64`, `time`

## Installation
1. Clone the repository or download the script.
   ```sh
   git clone https://github.com/your-repo/tonxdao-bot.git
   cd tonxdao-bot
   ```
2. Install the required dependencies.
   ```sh
   pip install -r requirements.txt
   ```
3. Set up `config.json` with the necessary parameters.
4. Create a `data.txt` file containing account credentials, each on a new line.

## Usage
Run the script with:
```sh
python tonxdao.py
```
The script will execute and wait for 7 hours before running again.

## Configuration
Modify `config.json` to enable or disable features:
```json
{
  "auto-check-in": true,
  "auto-do-task": true,
  "auto-claim-ref": false,
  "auto-farm": true
}
```

## Stopping the Script
Press `CTRL + C` to stop the script.

## License
MIT License

## Disclaimer
Use this script responsibly. The author is not responsible for any misuse.

