import requests
from argparse import ArgumentParser

if __name__ == "__main__":
    parser = ArgumentParser(description="A program that helps you submit your flags.")
    parser.add_argument("student_id", type=str, help="Student ID.")
    parser.add_argument("flag", type=str, help="Flag string you found.")
    args = parser.parse_args()

    sid = args.student_id
    flag = args.flag

    if len(sid) != 10 or int(sid) % 10000 > 5000 or int(sid[:4]) < 2018 or int(sid[:4]) > 2022:
        print("[Submit] Bad Student ID...")
        print("[Submit] Example: 2020010951")

    elif len(flag) < 10 or flag[:len("SAST2022{")] != "SAST2022{" or flag[-1] != "}":
        print("[Submit] Bad Flag string...")
        print("[Submit] Example: SAST2022{xxxxxxxx}")

    else:
        res = requests.post("http://121.5.165.232:12000/", json={
            "sid": sid,
            "flag": flag
        })

        result = res.json()['result']

        if result == 0:
            print(f"[Submit] Wrong Answer: {flag}")
        else:
            print(f"[Submit] Accepted: {flag} ({result} p.t.s)")
