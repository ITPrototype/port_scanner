import socket
import argparse
import concurrent.futures

def scan_port(target_host, port):
    try:
        with socket.create_connection((target_host, port), timeout=1):
            print(f"[+] {port} da ochiq port✅")
    except (socket.timeout, socket.error):
        pass

def scan_ports(target_host, start_port, end_port, max_threads=10):
    print(f"[*] {target_host}dagi portlar skanerlanmoqda")

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
        port_range = range(int(start_port), int(end_port) + 1)
        futures = [executor.submit(scan_port, target_host, port) for port in port_range]

        # Wait for all threads to finish
        concurrent.futures.wait(futures)

def main():
    parser = argparse.ArgumentParser(description="Port skanner.")
    parser.add_argument("-u", dest="url", required=True, help="IP address.")
    parser.add_argument("-s", dest="start", required=True, help="Port start")
    parser.add_argument("-e", dest="end", required=True, help="Port end")
    parser.add_argument("--threads", dest="threads", type=int, default=10, help="threads soni (default: 10).")
    
    args = parser.parse_args()
    scan_ports(args.url, args.start, args.end, args.threads)

if __name__ == '__main__':
    main()
