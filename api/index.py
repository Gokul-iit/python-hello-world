# from http.server import BaseHTTPRequestHandler

# class handler(BaseHTTPRequestHandler):

#     def do_GET(self):
#         self.send_response(200)
#         self.send_header('Content-type','text/plain')
#         self.end_headers()
#         self.wfile.write('Hello, world!'.encode('utf-8'))
#         return

from fastapi import FastAPI
# from mangum import Mangum

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hi, this is Jerry"}

# 👇 THIS is crucial
# handler = Mangum(app)
