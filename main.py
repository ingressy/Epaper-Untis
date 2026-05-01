from aiohttp import web

from rest import health, untis
from env import loadenv

def main():
    try:
       env = loadenv()
    except EnvironmentError as e:
        print(f"Environment Error: {e}")
        return

    #try to start rest api
    app = web.Application()
    app.router.add_get("/health",health)
    app.router.add_get("/untis", untis)

    try:
        web.run_app(app, host="0.0.0.0", port=env.port)
    except Exception as e:
        print(f"Error: {e}")
        return


if __name__ == '__main__':
    main()