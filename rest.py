from aiohttp import web

from data import get_data

status = "green"

async def health(request):
    return web.json_response({"status": status})

async def untis(request) -> None:
    room = request.rel_url.query.get("room", "")
    if not room:
        status = "yellow"
        return web.json_response({"status": "yellow", "error": "Room not found"}, status=400)

    stunden = get_data(room)
    if not stunden:
        return web.json_response({"status": "red"}, status=404)

    return web.json_response(stunden)