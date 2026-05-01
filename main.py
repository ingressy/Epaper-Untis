from aiohttp import web


from data import get_data
from rest import health, untis

def main():


    #try to start rest api
    app = web.Application()
    app.router.add_get("/health",health)
    app.router.add_get("/untis", untis)

    try:
        web.run_app(app, host="0.0.0.0", port=71)
    except Exception as e:
        print(f"Error: {e}")
        return


if __name__ == '__main__':
    main()