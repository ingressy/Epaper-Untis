from env import loadenv

def main():
    #load env from docker in class "env"
    try:
        env = loadenv()
    except EnvironmentError as e:
        print(f"Environment Error: {e}")
        return

if __name__ == '__main__':
    main()