import webuntis, datetime
from typing import Any

start = datetime.datetime.now()
end = start + datetime.timedelta(days=7)
now = datetime.datetime.now()
time_format_date = "%Y-%m-%d"
time_format = "%H%M"


def get_untis_data(env,raum :str) -> list[Any] | None:
    login = webuntis.Session(
        server=env.server,
        username=env.username,
        password=env.password,
        school=env.school,
        useragent=env.useragent,
    )
    login.login()

    #sortiert nur nach den raum
    rooms = login.rooms().filter(name=raum)

    timetable = login.timetable(room=rooms[0], start=start,end=end)
    timetable = sorted(timetable, key=lambda x: x.start)
    stunden = []

    for h in timetable:
        #spart Zeit
        #löscht alte Daten
        if h.end.date() < now.date():
            continue
        #löscht alle gelaufene Stunden
        if h.end.date() == now.date() and h.end.time() < now.time():
            continue

        stunden.append(
            {
                "date":  h.start.strftime(time_format_date),
                "start_time": h.start.strftime(time_format),
                "end_time" : h.end.strftime(time_format),
                "klasse": short_klassen([k.name for k in h.klassen]),
                "teacher": " ".join([t.name for t in h.teachers]) if h.teachers else "---",
                "classroom":  " ".join([r.name for r in h.rooms]),
                "subject": " ".join([s.name for s in h.subjects]),
                "code": h.code if h.code is not None else "",
            }
        )
    login.logout()
    return stunden

def short_klassen(klassen: list[Any]) -> list[Any]:
    #wird aus untis.py aufgerufen
    #macht BGT 24X BGT 2XX XXX 241

    #nur eine klasse
    if len(klassen) == 1:
        return klassen[0]

    #gemeinsamer präfix finden
    prefix = klassen[0]
    for k in klassen[1:]:
        while not k.startswith(prefix):
            prefix = prefix[:-1]

    #add X
    laenge = len(klassen[0])
    fehlend = laenge - len(prefix)

    return prefix + "X" *fehlend




