# Epaper-Untis
Untis API Mircoservice

## Endpoints
### Get /health
Gibt den aktuellen Status des Mircoservices wieder

**Resp**
```json
{
  "status": "green"
}
```

### Get /untis
Gibt die Stunden für einen Raum zurück

**Para**

|Name|Typ|Beschreibung|
|-----|----|----------|
|room|str|Raumname 2.311|

GET /untis?room=2.311

**Resp**
```json
{
    {
        "date": "2024-01-01",
        "start_time": "0810",
        "end_time": "1130",
        "klasse": "BGT 23X",
        "teacher": "Muster",
        "classroom": "2.311",
        "subject": "binf",
        "code": "",
        "anzahl": 4
  }
}
```
gibt room_changed mit, wenn Raum geändert wurde

**Response 400** – Room nicht angegeben
```json
{ "status": "yellow", "error": "room fehlt" }
```

**Response 404** – Keine Stunden gefunden
```json
{ "status": "red" }
```
