if __name__ == "__main__":
    for k in range(10000, 10250):
        print(f"docker stop SAST2022-{k}")
        print(f"docker rm SAST2022-{k}")
