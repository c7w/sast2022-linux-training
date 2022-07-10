import time
from tqdm import tqdm


def read_story():
    with open("./assets/alice.txt") as f:
        lines = f.read().split('\n')
        for k in tqdm(lines):
            tqdm.write(k)
            time.sleep(1)

if __name__ == "__main__":

    print("Hey kid, u wanna hear a story?")
    print("After it il give u a Flag!")
    print("Don't worry I will read it fast. (y/n)")

    while True:
        k = input()
        if k == "y":
            print("Really? Now I gonna start!")
            read_story()
            break
        if k == "n":
            print("Well...I'll see u next time!")
            break
