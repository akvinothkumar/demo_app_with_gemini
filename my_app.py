from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse
from config import model
import markdown


class PromptFormHandler(BaseHTTPRequestHandler):
    def markdown_to_html(self, text):
        return markdown.markdown(text)

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        with open("index.html", "r") as f:
            html = f.read()
        self.wfile.write(html.encode())

    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length)
        data = urllib.parse.parse_qs(post_data.decode())
        prompt = data.get("prompt_field", [""])[0]
        response = model.generate_content(prompt).text
        html_response = self.markdown_to_html(response)
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(html_response.encode("utf-8"))


if __name__ == "__main__":
    server = HTTPServer(("localhost", 8000), PromptFormHandler)
    print("Server running at http://localhost:8000/")
    server.serve_forever()
