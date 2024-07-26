import requests
import time
import random

def read_authorizations(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def make_post_request(url, payload, headers):
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Request failed with status code: {response.status_code}")
        return None

def countdown(minutes):
    total_seconds = minutes * 60
    while total_seconds > 0:
        mins, secs = divmod(total_seconds, 60)
        time_str = f"{mins:02d}:{secs:02d}"
        print(f"Countdown: {time_str}", end='\r')
        time.sleep(1)
        total_seconds -= 1
    print()

def generate_random_user_agent():
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/125.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Safari/605.1.15",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Brave/1.23.71 Chrome/89.0.4389.114 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0"
    ]
    return random.choice(user_agents)

def tap_tap_task(authorization, user_agent):
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-GB,en;q=0.9,en-US;q=0.8",
        "Authorization": authorization,
        "Cache-Control": "no-cache",
        "Content-Type": "application/json",
        "Origin": "https://banana.carv.io",
        "Pragma": "no-cache",
        "Referer": "https://banana.carv.io/",
        "Sec-Ch-Ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Microsoft Edge\";v=\"126\", \"Microsoft Edge WebView2\";v=\"126\"",
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
        "User-Agent": user_agent,
        "X-App-Id": "carv"
    }

    do_click_url = "https://interface.carv.io/banana/do_click"
    claim_lottery_url = "https://interface.carv.io/banana/claim_lottery"

    total_clicks = 0

    for i in range(5):
        click_count = random.randint(1, 10)
        total_clicks += click_count
        payload_click = {"clickCount": click_count}
        response_click = make_post_request(do_click_url, payload_click, headers)
        if response_click:
            print(f"Tap tap task {i+1}: Click count {click_count} - Success")

    payload_claim = {"claimLotteryType": total_clicks}
    response_claim = make_post_request(claim_lottery_url, payload_claim, headers)
    if response_claim:
        print(f"Claim lottery with points {total_clicks} - Success")

def main():
    auth_file = 'data.txt'
    authorizations = read_authorizations(auth_file)
    total_accounts = len(authorizations)
    user_agents = [generate_random_user_agent() for _ in range(total_accounts)]

    print(f"Total accounts to process: {total_accounts}")

    for index, authorization in enumerate(authorizations):
        print(f"Processing account {index+1}/{total_accounts} with user agent: {user_agents[index]}...")
        tap_tap_task(authorization, user_agents[index])
        print(f"Finished processing account {index+1}/{total_accounts}.")
        time.sleep(5)

    print("All accounts processed. Starting countdown for 6 minutes before restart.")
    countdown(6)
    main()

if __name__ == "__main__":
    main()
