import os
from django.core.management import execute_from_command_line
import webbrowser

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "versandplanung.settings")

def run_server():
    execute_from_command_line(["manage.py", "runserver", "--noreload"])
    
def open_browser():
    webbrowser.open_new_tab("http://localhost:8000")

if __name__ == "__main__":
    open_browser() # not ideal to open the web before the server is running but run_server is a loop
    run_server()