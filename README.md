
Backend für die todo app https://www.frontendmentor.io/challenges/todo-app-Su1_KokOW.

Aufgewendete Zeit: xxh xxmin

- [Funktionalitäten](#funktionalitäten)
  - [Mögliche Erweiterungen](#mögliche-erweiterungen)
- [Repository Übersicht](#repository-übersicht)
- [Start und Testen der API](#start-und-testen-der-api)
  - [Vorbedingungen](#vorbedingungen)
  - [Starten der API](#starten-der-api)
  - [Testen der API](#testen-der-api)

# Funktionalitäten
Folgende Funktionalitäten soll die API bieten. 
* Erstellen eines TODOs, beinhaltet:
    * Text
    * Status (active, complete)
* Abrufen eines TODOs mit ID
* Abrufen aller TODOs
* Bearbeiten eines TODOs
* Löschen eines TODOs

Die umgesetzten Funktionalitäten sind **fett** markiert.

## Mögliche Erweiterungen
* Erstellen von mehreren Listen 
    * Erweitern des Endpoints mit einer ListenId
    * Erstellen einer Liste
* GET mit filtern nach Status z.B. ?status=completed

# Repository Übersicht
- Im Ordner  ``./docs`` befindet sich die Postman Collection als Beschreibung der API. Diese kann auch zum Testen verwendet werden.
- Im Ordner  ``./src`` befindet sich der Source Code der Applikation.
  - Die Python Flask API befindet sich im Ordner ``./src/api``.
  - Aktuell wird keine DB verwendet, diese kann aber einfach über das Interface angebunden werden. Das Dockerfile dafür würde im ``./src/db`` platziert werden.
  - Das Docker-Compose File befindet sich unter ``./src/docker-compose.yml``.

# Start und Testen der API
## Vorbedingungen
- Installation von Docker: https://docs.docker.com/get-docker/
## Starten der API

Die API wird via Docker Container gestartet.
- ``cd ./src``
- ``docker-compose up``

Die API läuft nun unter localhost:5001

## Testen der API
-  Öffnen der Postman Collection von ``./docs``
-  Erstellen einer Notiz mit POST ``/notes``.
   - Gibt Id zurück
- Holen aller Notizen mit GET ``/notes``.
- Holen der erstellten Notiz mit GET ``/notes/{id}``.
- Bearbeiten der Notiz mit PUT ``/notes/{id}``.