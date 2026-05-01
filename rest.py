from aiohttp import web

from untis import get_untis_data

async def health(request):
    return web.json_response({"status": "green"})

async def untis(request) -> None:
    data = await request.json()
    room = data.get("room")

    if room is None:
        return

    get_untis_data(room)