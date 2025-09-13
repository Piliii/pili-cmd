import sys
import webbrowser
import random
from datetime import datetime, timedelta
import requests
import time
import os
import platform
import psutil
import subprocess
import threading

def open_website():
    print("🌐 Opening ayopili.com...")
    webbrowser.open("https://ayopili.com")

def say_hello():
    greetings = ["Hey there!", "Yo yo yo!", "Sup!", "Hello, world!", "Hiya!"]
    print(random.choice(greetings))

def get_excuse():
    url = "https://excuse-gen-api.vercel.app/api/excuse"
    try:
        response = requests.get(url)
        data = response.json()
        print(data.get("excuse", "No excuse found."))
    except Exception as e:
        print("Failed to fetch:", e)

def secret_art():
    ascii_arts = [
        r"""
 (\_._/)
 ( o o )
 /  O  \
 """,
        r"""
   /\_/\
  ( o.o )
   > ^ <
  """
    ]
    print(random.choice(ascii_arts))

def coinflip():
    print("🪙", random.choice(["Heads", "Tails"]))

def show_time():
    print("⏰ Current time:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

def uptime():
    if platform.system() == "Windows":
        try:
            import subprocess
            output = subprocess.check_output("net stats workstation", shell=True, text=True)
            for line in output.splitlines():
                if "Statistics since" in line:
                    print("🖥️ Uptime:", line.split("since",1)[1].strip())
        except:
            print("Failed to get uptime.")
    else:
        # Linux / MacOS
        try:
            with open("/proc/uptime") as f:
                seconds = float(f.readline().split()[0])
                hrs, rem = divmod(seconds, 3600)
                mins, secs = divmod(rem, 60)
                print(f"🖥️ Uptime: {int(hrs)}h {int(mins)}m {int(secs)}s")
        except:
            print("Failed to get uptime.")

def weather(city):
    try:
        url = f"https://wttr.in/{city}?format=3"
        response = requests.get(url)
        print(response.text)
    except Exception as e:
        print("Failed to fetch:", e)

def countdown(seconds):
    try:
        seconds = int(seconds)
        while seconds > 0:
            print(f"⏳ {seconds} seconds remaining", end="\r")
            time.sleep(1)
            seconds -= 1
        print("\n⏰ Time's up!")
        # Play a beep sound
        if platform.system() == "Windows":
            import winsound
            winsound.Beep(1000, 500)  # 1000 Hz for 0.5s
        else:
            print("\a")  # terminal bell
    except:
        print("Please provide countdown in seconds, e.g., pili countdown 10")

def show_cpu():
    try:
        cpu_percent = psutil.cpu_percent(interval=1)
        cpu_count = psutil.cpu_count()
        cpu_freq = psutil.cpu_freq()
        
        print(f"🖥️  CPU Usage: {cpu_percent}%")
        print(f"🔢 CPU Cores: {cpu_count}")
        if cpu_freq:
            print(f"⚡ CPU Freq: {cpu_freq.current:.0f} MHz")
    except Exception as e:
        print("Failed to get CPU info:", e)

def show_memory():
    try:
        memory = psutil.virtual_memory()
        
        print(f"🧠 Memory Usage: {memory.percent}%")
        print(f"📊 Total: {memory.total / (1024**3):.1f} GB")
        print(f"✅ Available: {memory.available / (1024**3):.1f} GB")
        print(f"🔴 Used: {memory.used / (1024**3):.1f} GB")
    except Exception as e:
        print("Failed to get memory info:", e)

def show_disk_usage():
    """Show disk usage for all mounted partitions."""
    try:
        partitions = psutil.disk_partitions()
        print("💽 Disk Usage:")
        for p in partitions:
            try:
                usage = psutil.disk_usage(p.mountpoint)
                print(f"  {p.device} ({p.mountpoint}): {usage.percent}% used, {usage.used // (1024**3)}GB/{usage.total // (1024**3)}GB")
            except PermissionError:
                continue
    except Exception as e:
        print("Failed to get disk usage:", e)

def list_processes(top_n=10):
    """List top N processes by memory usage."""
    try:
        processes = []
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
            processes.append(proc.info)
        processes.sort(key=lambda x: x['memory_percent'], reverse=True)
        print(f"🗂️ Top {top_n} processes by memory usage:")
        print(f"{'PID':>6} {'CPU%':>6} {'MEM%':>6} Name")
        for p in processes[:top_n]:
            print(f"{p['pid']:>6} {p['cpu_percent']:>6.1f} {p['memory_percent']:>6.1f} {p['name']}")
    except Exception as e:
        print("Failed to list processes:", e)

def kill_process():
    """Kill a process by PID."""
    if len(sys.argv) < 3:
        print("Usage: pili kill <pid>")
        return
    try:
        pid = int(sys.argv[2])
        p = psutil.Process(pid)
        p.terminate()
        print(f"🛑 Process {pid} terminated.")
    except Exception as e:
        print("Failed to kill process:", e)

def show_network_interfaces():
    """Show network interfaces and their IP addresses."""
    try:
        addrs = psutil.net_if_addrs()
        stats = psutil.net_if_stats()
        print("🌐 Network Interfaces:")
        for iface, addr_list in addrs.items():
            status = "UP" if stats[iface].isup else "DOWN"
            ips = [a.address for a in addr_list if a.family == 2]
            print(f"  {iface} [{status}]: {', '.join(ips) if ips else 'No IPv4'}")
    except Exception as e:
        print("Failed to get network interfaces:", e)

def show_battery_status():
    """Show battery status if available."""
    try:
        battery = psutil.sensors_battery()
        if battery is None:
            print("🔋 No battery found.")
            return
        plugged = "Charging" if battery.power_plugged else "Not charging"
        print(f"🔋 Battery: {battery.percent}% ({plugged})")
    except Exception as e:
        print("Failed to get battery status:", e)

def show_boot_time():
    """Show system boot time."""
    try:
        boot = datetime.fromtimestamp(psutil.boot_time())
        print("🕒 System boot time:", boot.strftime("%Y-%m-%d %H:%M:%S"))
    except Exception as e:
        print("Failed to get boot time:", e)

def show_env_vars():
    """Show all environment variables or a specific one."""
    if len(sys.argv) == 2:
        for k, v in os.environ.items():
            print(f"{k}={v}")
    else:
        key = sys.argv[2]
        print(f"{key}={os.environ.get(key, '[Not set]')}")

def show_current_user():
    """Show the current logged-in user."""
    try:
        user = os.getlogin() if hasattr(os, 'getlogin') else os.environ.get('USERNAME') or os.environ.get('USER')
        print(f"👤 Current user: {user}")
    except Exception as e:
        print("Failed to get current user:", e)

def show_top_processes():
    """Show top 5 processes by CPU usage."""
    try:
        processes = []
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
            processes.append(proc.info)
        processes.sort(key=lambda x: x['cpu_percent'], reverse=True)
        print("🔥 Top 5 processes by CPU usage:")
        print(f"{'PID':>6} {'CPU%':>6} Name")
        for p in processes[:5]:
            print(f"{p['pid']:>6} {p['cpu_percent']:>6.1f} {p['name']}")
    except Exception as e:
        print("Failed to get top processes:", e)

def speedtest():
    print("🌐 Running speed test...")
    # Note: Install speedtest-cli for accurate results: pip install speedtest-cli
    
    try:
        # Try to use speedtest-cli if available
        result = subprocess.run(['speedtest-cli', '--simple'], capture_output=True, text=True, timeout=30)
        if result.returncode == 0:
            print(result.stdout)
        else:
            # Fallback to basic ping test
            basic_speedtest()
    except:
        basic_speedtest()

def basic_speedtest():
    print("🔄 Running basic connectivity test...")
    try:
        start_time = time.time()
        response = requests.get('https://www.google.com', timeout=10)
        end_time = time.time()
        
        if response.status_code == 200:
            ping_time = (end_time - start_time) * 1000
            print(f"📶 Google ping: {ping_time:.0f}ms")
            
            if ping_time < 50:
                print("🚀 Connection: Excellent")
            elif ping_time < 100:
                print("✅ Connection: Good")
            elif ping_time < 200:
                print("⚠️  Connection: Fair")
            else:
                print("🐌 Connection: Slow")
        else:
            print("❌ Connection test failed")
    except:
        print("❌ No internet connection")

def roll_dice(sides=6, count=1):
    try:
        if len(sys.argv) > 2:
            sides = int(sys.argv[2])
        if len(sys.argv) > 3:
            count = int(sys.argv[3])
            
        rolls = [random.randint(1, sides) for _ in range(count)]
        
        print(f"🎲 Rolling {count}d{sides}:")
        if count == 1:
            print(f"Result: {rolls[0]}")
        else:
            print(f"Results: {', '.join(map(str, rolls))}")
            print(f"Total: {sum(rolls)}")
            
    except:
        print("Usage: pili dice [sides] [count]")
        print("Example: pili dice 20 2  (rolls 2 twenty-sided dice)")

def zalgo_text():
    if len(sys.argv) < 3:
        print("Usage: pili zalgo <text>")
        return
    
    text = " ".join(sys.argv[2:])

    zalgo_up = [
        '\u030d', '\u030e', '\u0304', '\u0305', '\u033f', '\u0311', '\u0306', '\u0310',
        '\u0352', '\u0357', '\u0351', '\u0307', '\u0308', '\u030a', '\u0342', '\u0343',
        '\u0344', '\u034a', '\u034b', '\u034c', '\u0303', '\u0302', '\u030c', '\u0350',
        '\u0300', '\u0301', '\u030b', '\u030f', '\u0312', '\u0313', '\u0314', '\u033d',
        '\u0309', '\u0363', '\u0364', '\u0365', '\u0366', '\u0367', '\u0368', '\u0369',
        '\u036a', '\u036b', '\u036c', '\u036d', '\u036e', '\u036f', '\u033e', '\u035b'
    ]
    
    zalgo_mid = [
        '\u0315', '\u031b', '\u0340', '\u0341', '\u0358', '\u0321', '\u0322', '\u0327',
        '\u0328', '\u0334', '\u0335', '\u0336', '\u034f', '\u035c', '\u035d', '\u035e',
        '\u035f', '\u0360', '\u0362', '\u0338', '\u0337', '\u0361', '\u0489'
    ]
    
    zalgo_down = [
        '\u0316', '\u0317', '\u0318', '\u0319', '\u031c', '\u031d', '\u031e', '\u031f',
        '\u0320', '\u0324', '\u0325', '\u0326', '\u0329', '\u032a', '\u032b', '\u032c',
        '\u032d', '\u032e', '\u032f', '\u0330', '\u0331', '\u0332', '\u0333', '\u0339',
        '\u033a', '\u033b', '\u033c', '\u0345', '\u0347', '\u0348', '\u0349', '\u034d',
        '\u034e', '\u0353', '\u0354', '\u0355', '\u0356', '\u0359', '\u035a', '\u0323'
    ]
    
    result = ""
    for char in text:
        result += char
        
        # Add random zalgo characters
        for _ in range(random.randint(0, 3)):  # 0-3 up chars
            result += random.choice(zalgo_up)
        for _ in range(random.randint(0, 2)):  # 0-2 mid chars  
            result += random.choice(zalgo_mid)
        for _ in range(random.randint(0, 3)):  # 0-3 down chars
            result += random.choice(zalgo_down)
    
    print(f"👹 Zalgo: {result}")

def reverse_text():
    if len(sys.argv) < 3:
        print("Usage: pili reverse <text>")
        return
    
    text = " ".join(sys.argv[2:])
    reversed_text = text[::-1]
    print(f"↩️  Reversed: {reversed_text}")

def mock_text():
    if len(sys.argv) < 3:
        print("Usage: pili mock <text>")
        return
    
    text = " ".join(sys.argv[2:])
    result = ""
    uppercase = False
    
    for char in text:
        if char.isalpha():
            if uppercase:
                result += char.upper()
            else:
                result += char.lower()
            uppercase = not uppercase
        else:
            result += char
    
    print(f"🤡 mOcKiNg: {result}")

def leet_text():
    if len(sys.argv) < 3:
        print("Usage: pili leet <text>")
        return
    
    text = " ".join(sys.argv[2:]).lower()
    
    leet_map = {
        'a': '4', 'e': '3', 'l': '1', 'o': '0', 's': '5', 
        't': '7', 'i': '!', 'g': '9', 'b': '6', 'z': '2'
    }
    
    result = ""
    for char in text:
        result += leet_map.get(char, char)
    
    print(f"💻 1337: {result}")

def flip_text():
    if len(sys.argv) < 3:
        print("Usage: pili flip <text>")
        return
    
    text = " ".join(sys.argv[2:])
    
    flip_map = {
        'a': 'ɐ', 'b': 'q', 'c': 'ɔ', 'd': 'p', 'e': 'ǝ', 'f': 'ɟ', 'g': 'ƃ', 
        'h': 'ɥ', 'i': 'ᴉ', 'j': 'ɾ', 'k': 'ʞ', 'l': 'l', 'm': 'ɯ', 'n': 'u', 
        'o': 'o', 'p': 'd', 'q': 'b', 'r': 'ɹ', 's': 's', 't': 'ʇ', 'u': 'n', 
        'v': 'ʌ', 'w': 'ʍ', 'x': 'x', 'y': 'ʎ', 'z': 'z',
        'A': '∀', 'B': 'ᗺ', 'C': 'Ɔ', 'D': 'ᗡ', 'E': 'Ǝ', 'F': 'ᖴ', 'G': 'פ',
        'H': 'H', 'I': 'I', 'J': 'ſ', 'K': 'ʞ', 'L': '˥', 'M': 'W', 'N': 'N',
        'O': 'O', 'P': 'Ԁ', 'Q': 'Q', 'R': 'ᴿ', 'S': 'S', 'T': '┴', 'U': '∩',
        'V': 'Λ', 'W': 'M', 'X': 'X', 'Y': '⅄', 'Z': 'Z',
        '?': '¿', '!': '¡', '.': '˙', ',': "'", "'": ',', '"': '„',
        '(': ')', ')': '(', '[': ']', ']': '[', '{': '}', '}': '{'
    }
    
    result = ""
    for char in text:
        result += flip_map.get(char, char)

    result = result[::-1]
    print(f"🙃 Flipped: {result}")

def remind_me():
    try:
        if len(sys.argv) < 3:
            print("Usage: pili remind <minutes> [message]")
            return
            
        minutes = int(sys.argv[2])
        message = "Time's up!"
        if len(sys.argv) > 3:
            message = " ".join(sys.argv[3:])
        
        def reminder():
            time.sleep(minutes * 60)
            print(f"\n{'='*50}")
            print(f"⏰ REMINDER: {message}")
            print(f"{'='*50}")
            # Multiple beeps to make it more noticeable
            for i in range(3):
                if platform.system() == "Windows":
                    try:
                        import winsound
                        winsound.Beep(800, 300)
                        time.sleep(0.2)
                    except:
                        print("\a", end="", flush=True)
                        time.sleep(0.2)
                else:
                    print("\a", end="", flush=True)
                    time.sleep(0.2)
        
        # Run reminder in background
        thread = threading.Thread(target=reminder)
        thread.daemon = True
        thread.start()
        
        reminder_time = datetime.now() + timedelta(minutes=minutes)
        print(f"⏰ Reminder set for {minutes} minute(s) from now ({reminder_time.strftime('%H:%M')})")
        print(f"💬 Message: {message}")
        print("💡 Keep this terminal open to see the reminder!")
        
    except ValueError:
        print("Please provide minutes as a number")
    except Exception as e:
        print("Failed to set reminder:", e)

def tictactoe():
    board = [" "] * 9

    def print_board():
        print("\n")
        print(f" {board[0]} | {board[1]} | {board[2]} ")
        print("---+---+---")
        print(f" {board[3]} | {board[4]} | {board[5]} ")
        print("---+---+---")
        print(f" {board[6]} | {board[7]} | {board[8]} ")
        print("\n")

    def check_win(player):
        wins = [
            [0,1,2],[3,4,5],[6,7,8],
            [0,3,6],[1,4,7],[2,5,8],
            [0,4,8],[2,4,6]
        ]
        return any(all(board[i] == player for i in line) for line in wins)

    def check_draw():
        return all(space != " " for space in board)

    def player_move(player):
        while True:
            try:
                move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
                if move < 0 or move > 8:
                    print("❌ Invalid position! Choose 1-9.")
                    continue
                if board[move] != " ":
                    print("❌ That spot is taken!")
                    continue
                board[move] = player
                break
            except ValueError:
                print("❌ Enter a number 1-9 only.")

    # --- AI logic ---
    def ai_move(difficulty):
        if difficulty == "easy":
            # Random move
            move = random.choice([i for i, x in enumerate(board) if x == " "])
            board[move] = "O"

        elif difficulty == "medium":
            # Try to win or block, else random
            for player_check in ["O", "X"]:
                for i in range(9):
                    if board[i] == " ":
                        board[i] = player_check
                        if check_win(player_check):
                            if player_check == "O":
                                return  # AI wins
                            else:
                                board[i] = "O"  # block
                                return
                        board[i] = " "
            # fallback random
            move = random.choice([i for i, x in enumerate(board) if x == " "])
            board[move] = "O"

        elif difficulty == "expert":
            # Minimax unbeatable
            def minimax(b, depth, is_max):
                if check_win("O"):
                    return 10 - depth
                if check_win("X"):
                    return depth - 10
                if check_draw():
                    return 0

                if is_max:
                    best = -float('inf')
                    for i in range(9):
                        if b[i] == " ":
                            b[i] = "O"
                            best = max(best, minimax(b, depth + 1, False))
                            b[i] = " "
                    return best
                else:
                    best = float('inf')
                    for i in range(9):
                        if b[i] == " ":
                            b[i] = "X"
                            best = min(best, minimax(b, depth + 1, True))
                            b[i] = " "
                    return best

            best_score = -float('inf')
            best_move = None
            for i in range(9):
                if board[i] == " ":
                    board[i] = "O"
                    score = minimax(board, 0, False)
                    board[i] = " "
                    if score > best_score:
                        best_score = score
                        best_move = i
            board[best_move] = "O"

    # --- Game start ---
    print("🎮 Tic-Tac-Toe! Player: X | AI: O")
    print_board()

    mode = input("Choose mode: [1] 2-player, [2] vs AI: ")
    ai_enabled = mode == "2"
    difficulty = None
    if ai_enabled:
        difficulty = input("Select AI difficulty: [easy, medium, expert]: ").lower()
        if difficulty not in ["easy", "medium", "expert"]:
            print("⚠️ Invalid difficulty! Defaulting to expert.")
            difficulty = "expert"

    player = "X"
    while True:
        if player == "X" or not ai_enabled:
            player_move(player)
        else:
            print(f"🤖 AI ({difficulty}) is thinking...")
            ai_move(difficulty)

        print_board()

        if check_win(player):
            confetti_animation("You win!" if player=='X' else "AI wins!")
            break
        if check_draw():
            print("🤝 It's a draw!")
            break

        player = "O" if player == "X" else "X"

def confetti_animation(winner_text):
    confetti_chars = ['🎉', '✨', '💥', '🌟', '🥳', '🔥']
    
    print("\n" + "="*40)
    print(f"🏆 {winner_text} 🏆")
    print("="*40 + "\n")
    
    for _ in range(10):  # number of confetti bursts
        for _ in range(5):  # number of lines per burst
            line = "".join(random.choice(confetti_chars) for _ in range(40))
            print(line)
        time.sleep(0.3)  # pause between bursts
    
    # Final winner text
    print("\n" + "="*40)
    print(f"🏆 {winner_text} 🏆")
    print("="*40 + "\n")

def mock_text():
    if len(sys.argv) < 3:
        print("Usage: pili mock <text>")
        return
    
    text = " ".join(sys.argv[2:])
    result = ""
    uppercase = False
    
    for char in text:
        if char.isalpha():
            if uppercase:
                result += char.upper()
            else:
                result += char.lower()
            uppercase = not uppercase
        else:
            result += char
    
    print(f"🤡 mOcKiNg: {result}")

# --- Main program ---
def main():
    if len(sys.argv) < 2:
        print("Usage: pili <command> [args]")
        print("\n📋 Available commands:")
        print("🌐 website, hello, excuse, secret, coinflip")
        print("⏰ time, uptime, countdown, remind")
        print("🌤️ weather, speedtest")
        print("🖥️ cpu, memory, disk, procs, kill, net, battery, boot, env, user, top")
        print("🎲 dice, ttt")
        print("📝 zalgo, reverse, mock, leet, flip")
        return

    command = sys.argv[1].lower()
    args = sys.argv[2:]

    if command == "website":
        open_website()
    elif command == "hello":
        say_hello()
    elif command == "joke":
        print("Use pili excuse or add more jokes manually!")
    elif command == "excuse":
        get_excuse()
    elif command == "time":
        show_time()
    elif command == "secret":
        secret_art()
    elif command == "coinflip":
        coinflip()
    elif command == "uptime":
        uptime()
    elif command == "weather":
        if args:
            weather(" ".join(args))
        else:
            print("Usage: pili weather <city>")
    elif command == "countdown":
        if args:
            countdown(args[0])
        else:
            print("Usage: pili countdown <seconds>")
    elif command == "cpu":
        show_cpu()
    elif command == "memory":
        show_memory()
    elif command == "disk":
        show_disk_usage()
    elif command == "procs":
        top_n = int(args[0]) if args and args[0].isdigit() else 10
        list_processes(top_n)
    elif command == "kill":
        kill_process()
    elif command == "net":
        show_network_interfaces()
    elif command == "battery":
        show_battery_status()
    elif command == "boot":
        show_boot_time()
    elif command == "env":
        show_env_vars()
    elif command == "user":
        show_current_user()
    elif command == "top":
        show_top_processes()
    elif command == "speedtest":
        speedtest()
    elif command == "dice":
        roll_dice()
    elif command == "remind":
        remind_me()
    elif command == "zalgo":
        zalgo_text()
    elif command == "reverse":
        reverse_text()
    elif command == "mock":
        mock_text()
    elif command == "leet":
        leet_text()
    elif command == "flip":
        flip_text()
    elif command == "ttt":
        tictactoe()
    else:
        print(f"❌ Unknown command: {command}")
        print("\n📋 Available commands:")
        print("🌐 website, hello, excuse, secret, coinflip")
        print("⏰ time, uptime, countdown, remind")
        print("🌤️ weather, speedtest")
        print("🖥️ cpu, memory, disk, procs, kill, net, battery, boot, env, user, top")
        print("🎲 dice, ttt")
        print("📝 zalgo, reverse, mock, leet, flip")

if __name__ == "__main__":
    main()