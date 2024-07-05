import socket
import argparse

def scan_ports(target_host, start_port, end_port):
    try:
        target_ip = socket.gethostbyname(target_host)
    except socket.gaierror:
        print(f"Error: Can\'t resolve {target_host}")
        return

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Timeout for connection attempt
        result = sock.connect_ex((target_ip, port))
        if result == 0:
            print(f"Port {port} is Open")
        sock.close()

def main():
    parser = argparse.ArgumentParser(description="Python network scanner")
    parser.add_argument("host")
    parser.add_argument("start_port", type=int)
    parser.add_argument("end_port", type=int)
    args = parser.parse_args()

    if args.start_port > args.end_port or args.start_port < 1 or args.end_port > 65535:
        print("Error: Invalid port range")
        return

    scan_ports(args.host, args.start_port, args.end_port)

if __name__ == "__main__":
    main()
