#!/usr/bin/env python3
import http.server, socketserver, json, datetime

PORT = 8080

# === Thresholds ===
LIMITS = {
    "BPM": (50, 100),
    "SpO2": (94, 100),
    "TempDS18B20": (35.0, 38.0),
    "TempDHT": (35.0, 38.0),
    "Humidity": (30, 60),
}

class SimpleHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get('Content-Length', 0))
        data = self.rfile.read(length).decode('utf-8')
        try:
            payload = json.loads(data)
        except:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"Invalid JSON")
            return

        # Raspberry’nin kendi zamanı
        pi_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        node_time = payload.get("Timestamp", "N/A")

        node_id = payload.get("NodeID", "Unknown")

        print(f"\n[{pi_time}] Data from {node_id}:")
        print(f"  Node timestamp: {node_time}")
        for k,v in payload.items():
            if k in ["NodeID","Timestamp"]: 
                continue
            print(f"  {k}: {v}")

        # === Check limits ===
        warnings = []
        for key,(lo,hi) in LIMITS.items():
            val = payload.get(key)
            if val is None: 
                continue
            try:
                valf = float(val)
                if valf < lo or valf > hi:
                    warnings.append(f"{key}={valf} OUT OF RANGE ({lo}-{hi})")
            except:
                pass

        if warnings:
            print("WARNINGS:")
            for w in warnings: print("   -", w)
        else:
            print("All values within normal range.")

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")

if __name__ == "__main__":
    print(f"🚀 Listening on port {PORT} for POST requests from NodeMCUs...")
    with socketserver.TCPServer(("", PORT), SimpleHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server gracefully...")
