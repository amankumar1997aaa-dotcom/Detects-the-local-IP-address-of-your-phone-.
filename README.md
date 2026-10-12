# Phone IP Detector

A tiny Python script that detects the local IP address of your phone's (or any device's) active network interface.

## How it works

It opens a UDP socket and "connects" to `8.8.8.8` (Google Public DNS). No data is actually sent, but the operating system picks the active network interface, and the script reads the local IP from that socket.

## Requirements

- Python 3.x
- No external libraries (uses only the built-in `socket` module)

## Usage

```bash
python get_phone_ip.py
```

Works on Termux, Pydroid 3, and desktop Python.

## Example output

```
========================================
      IP DETECTION ENGINE (MOBILE)
========================================

[i] Detecting your phone's IP address...

[+] SUCCESS!
--> Your Phone's Active IP: 192.168.1.23

========================================
```

## Note

This shows your **local (private) IP** on the current network, not your public internet IP.

## License

MIT
