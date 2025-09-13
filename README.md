# Pili 🚀

A fun and versatile Python command-line utility that brings together system monitoring, games, text manipulation, and random entertainment - all in one lightweight script!

## ✨ Features

### 🌐 Web & Network
- **website** - Opens ayopili.com in your browser
- **weather [city]** - Get current weather for any city
- **speedtest** - Test your internet connection speed (uses `speedtest-cli` if available, else basic ping)
- **net** - Show network interfaces and their IP addresses

### 🎮 Entertainment & Games
- **hello** - Random friendly greetings
- **excuse** - Generate creative excuses via [excuse generator API](https://github.com/Piliii/excuse-gen-api)
- **secret** - Display random ASCII art
- **coinflip** - Flip a coin (Heads or Tails)
- **dice [sides] [count]** - Roll dice (default: 1d6)
- **ttt** - Play Tic-Tac-Toe (2-player or vs AI with multiple difficulties)

### ⏰ Time & Productivity
- **time** - Show current date and time
- **uptime** - Display system uptime
- **countdown [seconds]** - Start a countdown timer with beep
- **remind [minutes] [message]** - Set a reminder with notification
- **boot** - Show system boot time

### 🖥️ System Monitoring
- **cpu** - Show CPU usage, cores, and frequency
- **memory** - Display RAM usage and availability
- **disk** - Show disk usage for all partitions
- **procs [N]** - List top N processes by memory usage (default: 10)
- **top** - Show top 5 processes by CPU usage
- **kill [pid]** - Kill a process by PID
- **battery** - Show battery status if available
- **env [VAR]** - Show all environment variables or a specific one
- **user** - Show the current logged-in user

### 📝 Text Manipulation
- **zalgo [text]** - Convert text to spooky zalgo format
- **reverse [text]** - Reverse text backwards
- **mock [text]** - CoNvErT tO mOcKiNg CaSe
- **leet [text]** - Transform to 1337 sp34k
- **flip [text]** - Flip text upside down ¡ǝʞᴉl sᴉɥʇ

## 🚀 Installation

1. **Clone the repository:**
```bash
git clone https://github.com/Piliii/pili.git
cd pili
```

2. **Install dependencies:**
```bash
pip install requests psutil
```

3. **Make it globally accessible (optional):**

**On Linux/macOS:**
```bash
chmod +x pili.py
sudo cp pili.py /usr/local/bin/pili
```

**On Windows:**
Add the script directory to your PATH, or create a batch file:
```batch
@echo off
python "C:\path\to\pili.py" %*
```

## 📖 Usage

```bash
python pili.py <command> [arguments]

# Or if installed globally:
pili <command> [arguments]
```

### Examples

```bash
# Basic commands
pili hello
pili time
pili coinflip

# Weather and network
pili weather London
pili speedtest
pili net

# System info
pili cpu
pili memory
pili disk
pili uptime
pili procs 5
pili top
pili kill 1234
pili battery
pili boot
pili env
pili env PATH
pili user

# Text fun
pili zalgo "Hello World"
pili mock "this is serious"
pili leet "elite hacker"
pili reverse "desserts"
pili flip "hello"

# Games
pili dice 20 2      # Roll 2 twenty-sided dice
pili ttt            # Play Tic-Tac-Toe

# Productivity
pili countdown 300         # 5 minute timer
pili remind 25 "Take a break"  # Pomodoro reminder
```

## 🎮 Tic-Tac-Toe Game

The built-in Tic-Tac-Toe game features:
- **2-player mode** - Play with a friend
- **AI opponents** with three difficulty levels:
  - **Easy** - Random moves
  - **Medium** - Tries to win/block
  - **Expert** - Unbeatable minimax algorithm

## 🔧 Dependencies

- **Python 3.6+**
- **requests** - For API calls and web features
- **psutil** - For system monitoring
- **Standard libraries**: sys, webbrowser, random, datetime, time, os, platform, subprocess, threading

## 🌟 Optional Enhancements

- Install `speedtest-cli` for more accurate speed tests: `pip install speedtest-cli`
- On Windows, `winsound` is used for better audio notifications

## 🤝 Contributing

Feel free to contribute! Whether it's:
- Adding new commands
- Improving existing features
- Fixing bugs
- Enhancing documentation

## 📝 License

This project is open source and available under the [MIT License](LICENSE).