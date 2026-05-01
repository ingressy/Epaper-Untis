from aiohttp import web

from env import loadenv
from untis import get_untis_data
from rest import health, untis

def main():
    #load env from docker in class "env"
    try:
        env = loadenv()
    except EnvironmentError as e:
        print(f"Environment Error: {e}")
        return

    #try to start rest api
    app = web.Application()
    app.router.add_get("/health",health)
    app.router.add_post("/untis", untis)

    try:
        web.run_app(app, host="0.0.0.0", port=71)
    except Exception as e:
        print(f"Error: {e}")
        return

    get_untis_data(env,"2.311")

if __name__ == '__main__':
    main()