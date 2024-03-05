# TL;DR
Führen Sie:
```zsh
pip install -r requirements.txt
```
aus um alle verwendeten Python Bibliotheken zu installieren.

Note: `pip` ist seit Python 3.4.0 nativ bei jedem Installer für Python dabei der via https://www.python.org verfügbar ist. Daher muss dies nicht extra installiert werden. (https://peps.python.org/pep-0453/)

Führen Sie:
```zsh
python manage.py runserver
```
aus um den localen django server zustarten.

Der default port für den Django Server ist 8000 falls dort bereits eine Anwendung läuft die Sie nicht schließen wollen.
Nutzen Sie bitte:
```zsh
python manage.py runserver <port>
```
Hier bei ist `<port>` ihr Wunschport. Beachten Sie, dass im nachfolgenden nur port 8000 genutzt wird. Diesen müssen Sie dann durch ihren Port austauschen!

Nachdem dieser gestartet ist, können Sie ihren browser öffnen um sich die Seite anzugucken.

Hier zu öffnen Sie den Brower ihrer Wahl (Internet Explorer ausgenommen) unter:
`localhost:8000` oder `127.0.0.1:8000` falls ihre etc/host noch keinen eintrag besitzt.

