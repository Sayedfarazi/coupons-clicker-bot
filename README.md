
# Coupons Clicker Bot

This script automates the process of logging into the BJ's website and clipping available coupons using Selenium and Python. The bot mimics human behavior to add coupons to a user's profile.

<sub> **This project is developed for educational purposes only. Read the [disclaimer](#disclaimer) before use.** </sub>

![Watch the video](/media/CouponBot.gif)

## Features

- **Automated Login**: Logs into the BJ's website using credentials securely stored in a `secrets.json` file.
- **Coupon Clipping**: Finds and clips all available coupons on the website automatically.

## Requirements

- Python 3.7 or later
- `undetected-chromedriver`
- `selenium`
- `certifi`

## Setup

1. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Create a `secrets.json` file in the project directory with your login credentials:
   ```json
   {
       "email": "your-email@example.com",
       "pass": "your-password"
   }
   ```

3. Run the script:
   ```bash
   python bjs.py
   ```

## File Structure

- **`bjs.py`**: Main automation script
- **`secrets.json`**: Stores login credentials securely
- **`requirements.txt`**: Python dependencies

## How It Works

1. **Login**:
   - Navigates to the website's login page.
   - Automatically inputs email and password.
   - Handles login errors and exits if credentials are incorrect.

2. **Coupon Clipping**:
   - Navigates to the coupons page.
   - Finds and clips all available coupons.
   - Logs progress to the console for transparency.

3. **Completion**:
   - Closes the browser after finishing the process.

## Notes

- Ensure valid credentials are saved in the `secrets.json` file before running the script.
- The script uses `undetected-chromedriver` to reduce the chances of bot detection.
- The script is intentionally slowed down to mimic human engagement and reduce stress on servers.

## Disclaimer

This script is intended for educational use only. Automating interactions with websites may violate their terms of service. **The author assumes no responsibility for misuse of this code.**



##### License: 

[MIT License](LICENSE)
