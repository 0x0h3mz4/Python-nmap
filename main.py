from flask import Flask, request, redirect , render_template
import nmap

app = Flask(__name__)


@app.route("/")
def index():
    if request.method == 'POST':
        scanner = nmap.PortScanner()
        ip = request.form['ip']
        scan=request.name['scan']
        if scan == 'SYN ACK':
            print("Nmap Version: ", scanner.nmap_version())
            scanner.scan(ip, '1-1024', '-v -sS')
            print(scanner.scaninfo())
            print("Ip Status: ", scanner[ip].state())
            print(scanner[ip].all_protocols())
            print("Open Ports: ", scanner[ip]['tcp'].keys())
        elif scan == 'UDP':
            print("Nmap Version: ", scanner.nmap_version())
            scanner.scan(ip, '1-1024', '-v -sU')
            print(scanner.scaninfo())
            print("Ip Status: ", scanner[ip].state())
            print(scanner[ip].all_protocols())
            print("Open Ports: ", scanner[ip]['udp'].keys())
        elif scan == 'Comprehensive Scan':
            print("Nmap Version: ", scanner.nmap_version())
            scanner.scan(ip, '1-1024', '-v -sS -sV -sC -A -O')
            print(scanner.scaninfo())
            print("Ip Status: ", scanner[ip].state())
            print(scanner[ip].all_protocols())
            print("Open Ports: ", scanner[ip]['tcp'].keys())
        
    else:
        return render_template("form.html")
    

#     scanner = nmap.PortScanner()
#     ip = request.form['ip']
#     scan=request.name['scan']
#     if scan == 'SYN ACK':
#         print("Nmap Version: ", scanner.nmap_version())
#         scanner.scan(ip, '1-1024', '-v -sS')
#         print(scanner.scaninfo())
#         print("Ip Status: ", scanner[ip].state())
#         print(scanner[ip].all_protocols())
#         print("Open Ports: ", scanner[ip]['tcp'].keys())
#     elif scan == 'UDP':
#         print("Nmap Version: ", scanner.nmap_version())
#         scanner.scan(ip, '1-1024', '-v -sU')
#         print(scanner.scaninfo())
#         print("Ip Status: ", scanner[ip].state())
#         print(scanner[ip].all_protocols())
#         print("Open Ports: ", scanner[ip]['udp'].keys())
#     elif scan == 'Comprehensive Scan':
#         print("Nmap Version: ", scanner.nmap_version())
#         scanner.scan(ip, '1-1024', '-v -sS -sV -sC -A -O')
#         print(scanner.scaninfo())
#         print("Ip Status: ", scanner[ip].state())
#         print(scanner[ip].all_protocols())
#         print("Open Ports: ", scanner[ip]['tcp'].keys())

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)