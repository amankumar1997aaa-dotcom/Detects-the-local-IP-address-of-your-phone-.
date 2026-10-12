"""
Phone IP Detector
-----------------
Detects the local IP address of the active network interface.
Works on Termux, Pydroid, and any standard Python 3 setup.
"""

import socket


def get_phone_ip():
    print("=" * 40)
    print("      IP DETECTION ENGINE (MOBILE)      ")
    print("=" * 40)
    print("\n[i] Detecting your phone's IP address...")

    try:
        # Create a standard UDP socket
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # "Connect" to an external address (Google Public DNS).
        # No data or packets are actually sent; this only forces the OS
        # to pick the active network interface.
        s.connect(("8.8.8.8", 80))

        # Extract the local IP assigned to that active interface
        phone_ip = s.getsockname()[0]
        s.close()

        print("\n[+] SUCCESS!")
        print(f"--> Your Phone's Active IP: {phone_ip}")

    except Exception as e:
        print("\n[!] ERROR: Could not detect IP address.")
        print(f"Details: {e}")

    print("\n" + "=" * 40)
    input("Tap 'Enter' or close the app to exit...")


if __name__ == "__main__":
    get_phone_ip()
