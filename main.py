from env import loadenv
from untis import get_untis_data

def main():
    #load env from docker in class "env"
    try:
        env = loadenv()
    except EnvironmentError as e:
        print(f"Environment Error: {e}")
        return
    get_untis_data(env,"2.311")

if __name__ == '__main__':
    main()