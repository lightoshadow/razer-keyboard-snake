# Razer Keyboard Snake

A Python implementation of the classic Snake game that runs directly on your Razer keyboard's RGB lighting.

![game gif](images/snake.gif)

The snake appears as green lights moving across your keyboard, while the fruit glows red. Each time you eat fruit, your snake grows longer

## Requirements

- **Hardware**: Razer keyboard with RGB lighting (tested on Razer Ornata Chroma)
- **OS**: Linux (required for OpenRazer drivers)
- **Python**: 3.6 or higher
- **Dependencies**:
  - [OpenRazer drivers](https://openrazer.github.io/)
  - Python curses library (usually pre-installed on Linux)

## Installation

### 1. Install OpenRazer Drivers

Follow the [official OpenRazer installation guide](https://openrazer.github.io/#download) for your Linux distribution.

### 2. Clone the Repository

```bash
git clone https://github.com/yourusername/razer-keyboard-snake.git
cd razer-keyboard-snake
```

### 4. Add User to plugdev Group

```bash
sudo gpasswd -a $USER plugdev
```

**Note**: You'll need to log out and back in for group changes to take effect.

## Usage

Run the game with:

```bash
python main.py
```

### Controls

- **Arrow Keys**: Move the snake (↑ ↓ ← →)
- **Delete Key**: Quit the game

## Compatibility

**Tested on:**
- ✅ Razer Ornata Chroma

**Should work on any Razer keyboard with:**
- RGB matrix support
- OpenRazer driver compatibility

[Check OpenRazer device support list](https://openrazer.github.io/#devices)

## Troubleshooting

### Game won't start
- Ensure OpenRazer daemon is running: `systemctl --user status openrazer-daemon`
- Check that your user is in the `plugdev` group: `groups $USER`
- Verify your keyboard is detected: `razer-cli -ls`

### Keyboard not responding
- Try restarting the OpenRazer daemon: `systemctl --user restart openrazer-daemon`
- Reconnect your keyboard

### Permission errors
- Make sure you've logged out and back in after adding yourself to `plugdev` group

## Credits

Built with [OpenRazer](https://openrazer.github.io/) - an open-source driver suite for Razer devices.

## Disclaimer

This project is not affiliated with or endorsed by Razer Inc. Use at your own risk.
