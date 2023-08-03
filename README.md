# Network Scanner Skript

Dieses Skript scannt das Netzwerk auf MAC-Adressen und vergleicht sie mit einer Liste von genehmigten Adressen. Es wird eine Warnung ausgegeben, wenn unbekannte Geräte im Netzwerk gefunden werden, und es besteht die Möglichkeit, eine E-Mail-Benachrichtigung zu senden.

## Anforderungen

- Dieses Skript muss als Root-Benutzer ausgeführt werden.
- Python 3.x muss installiert sein.
- Die Bibliotheken os, shutil, nmap, sys, subprocess und datetime müssen installiert sein.

## Verwendung

Das Skript führt einen nmap-Scan des angegebenen Netzwerks durch (standardmäßig 192.168.0.1/24). Es extrahiert die IP- und MAC-Adressen und speichert sie in einer Datei.

### Schritte:

1. **Backup von alten Scans:** Wenn eine Datei von früheren Scans vorhanden ist, wird eine Sicherungskopie der Datei erstellt.
2. **Neue Datei für Scan-Ergebnisse öffnen:** Eine neue Datei für die Scan-Ergebnisse wird geöffnet und erstellt.
3. **Netzwerk scannen:** Es wird ein Netzwerkscan durchgeführt, und die Ergebnisse werden in die Datei geschrieben.
4. **MAC-Adressen lesen:** Die MAC-Adressen werden gelesen und mit einer Liste von genehmigten Adressen verglichen.
5. **Warnung bei neuen Geräten:** Wenn unbekannte Geräte gefunden werden, wird eine Warnung auf der Konsole ausgegeben.
6. **E-Mail-Benachrichtigung:** Es besteht die Möglichkeit, eine E-Mail-Benachrichtigung zu senden, wenn unbekannte Geräte gefunden werden.

## Anpassung

- Ändern Sie die IP-Range in der `nm.scan` Methode, um Ihr spezifisches Netzwerk zu scannen.
- Fügen Sie Ihre genehmigten MAC-Adressen in die `approved_macs`-Liste ein.
- Passen Sie die E-Mail-Benachrichtigungslogik an Ihre Bedürfnisse an.

## Haftungsausschluss

Die Verwendung dieses Skripts erfolgt auf eigene Gefahr. Bitte testen Sie es in einer sicheren Umgebung, bevor Sie es in der Produktion verwenden, und stellen Sie sicher, dass Sie die Berechtigung zum Scannen des Netzwerks haben.
