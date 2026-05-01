from typing import Any

import webuntis, datetime

start = datetime.datetime.now()
end = start + datetime.timedelta(days=5)
now = datetime.datetime.now()
time_format_date = "%Y-%m-%d"
time_format = "%H%M"
stunden = []


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
                "klasse": " ".join([k.name for k in h.klassen]),
                "teacher": " ".join([t.name for t in h.teachers]) if h.teachers else "---",
                "classroom":  " ".join([r.name for r in h.rooms]),
                "subject": " ".join([s.name for s in h.subjects]),
                "code": h.code if h.code is not None else "",
            }
        )
        return stunden
    return None




