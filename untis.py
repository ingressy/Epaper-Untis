import webuntis, datetime

start = datetime.datetime.now()
end = start + datetime.timedelta(days=1)


def get_untis_data(env,room :str) -> None:
    login = webuntis.Session(
        server=env.server,
        username=env.username,
        password=env.password,
        school=env.school,
        useragent=env.useragent,
    )
    login.login()

    #sortiert nur nach den raum
    rooms = login.rooms().filter(room=room)

    timetable = login.timetable(rooms=rooms[0], start=start,end=end)
    timetable = sorted(timetable, key=lambda x: x.start)

    for h in timetable:
        print(h)
