from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html> 
  <body>
    <h1 allign="centre"> Device Specifications</h1>
    <h2 allign ="right">(Janani) </h2>
    <h3 allign="right">(24900080)</h3>
    <ol type="i">
        <li> Device name	DESKTOP-HGBNL1F</li>
        <li>  Processor	13th Gen Intel(R) Core(TM) i5-1334U   1.30 GHz</li>
        <li>  Installed RAM	16.0 GB (15.7 GB usable)</li>
        <li>  Device ID	2DB9535D-8827-43C0-A0AA-3DD3241218DA</li>
        <li> Product ID	00356-24767-98958-AAOEM</li>
        <li> System type- 64-bit operating system, x64-based processor</li>
        <li> Pen and Touch-No pen or touch input is available for this display </li>
    
    
    </ol>
  </body>  
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()