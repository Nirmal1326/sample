from http.server import BaseHTTPRequestHandler, HTTPServer
import os

DATA_FILE = "/data/tasks.txt"

class SimpleHandler(BaseHTTPRequestHandler):
   def do_GET(self):
       os.makedirs("/data", exist_ok=True)

       with open(DATA_FILE, "a") as f:
           f.write("Task accessed\n")

       with open(DATA_FILE, "r") as f:
           content = f.read()

       self.send_response(200)
       self.send_header("Content-type", "text/plain")
       self.end_headers()
       self.wfile.write(content.encode())

if __name__ == "__main__":
   server = HTTPServer(("0.0.0.0", 5000), SimpleHandler)
   print("Server running on port 5000...")
   server.serve_forever()

