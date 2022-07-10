import time
import datetime
from typing import List


class Trainee:

    def __init__(self, string, create=False):
        """
            string:
            "SID,last_submit,000000000000000 / 111111111111111"
        """
        if create:
            info_list = string.split(",")
            self.id = info_list[0]
            self.last_submit = info_list[1]
            self.result = [False for x in info_list[2]]
            self.score_list = [14, 14, 14, 14, 14, 14, 4, 4, 4, 4, 1, 1, 1, 1, 1]
        else:
            info_list = string.split(",")
            self.id = info_list[0]
            self.last_submit = int(info_list[1])
            self.result = [bool(int(x)) for x in info_list[2]]
            self.score_list = [14, 14, 14, 14, 14, 14, 4, 4, 4, 4, 1, 1, 1, 1, 1]

    def get_score(self):
        return sum([(result * self.score_list[idx] if result else 0) for (idx, result) in enumerate(self.result)])

    def get_html(self, bg_color: str):
        return f"""<tr style="background-color: {bg_color}">
            <td class="student-id">{self.id}</td>
            <td class="total-score">{self.get_score()}</td>
            <td class="last-submit">{datetime.datetime.fromtimestamp(self.last_submit).strftime('%m/%d %H:%M')}</td>
            {"".join(
            [
                f'''<td class="{"mark" if x else "unmark"}">{
                self.score_list[idx] if x else ""
                }</td>''' for idx, x in enumerate(self.result)
            ]
        )}
        </tr>"""

    def get_string(self):
        return f"""{self.id},{int(self.last_submit)},{"".join("1" if x else "0" for x in self.result)}"""

    def __lt__(self, other):
        self_score = self.get_score()
        other_score = other.get_score()

        if self_score != other_score:
            return self_score < other_score

        return self.last_submit > other.last_submit

    def submit_result(self, result):
        answer_list = [
            "SAST2022{FinallyOver}",
            "SAST2022{CraYon}",
            "SAST2022{WeatherReport}",
            "SAST2022{ThereCanBeNoTurningBack}",
            "SAST2022{IsItDDR4}",
            "SAST2022{UFindMe}",
            "SAST2022{ISmellAConspiracy}",
            "SAST2022{HelloTUNA!}",
            "SAST2022{WakeUp}",
            "SAST2022{H0meLessOne}",
            "SAST2022{Metaverse}",
            "SAST2022{NetSecEngineer}",
            "SAST2022{DocReader}",
            "SAST2022{DataAnalyst}",
            "SAST2022{KawaiiNana}",
        ]
        answer_dict = {k: v for v, k in enumerate(answer_list)}

        self.last_submit = int(time.time())
        if result in answer_dict.keys():
            idx = answer_dict[result]
            self.result[idx] = True
            return self.score_list[idx]
        else:
            return 0

def read_trainee_database():
    with open("data.txt", 'r+') as file:
        raw = file.read().strip()
    if len(raw):
        return [Trainee(x) for x in raw.split('\n')]
    else:
        return []

def write_trainee_database(list: List[Trainee]):
    result_str = "\n".join([x.get_string() for x in list])
    with open("data.txt", 'w+') as file:
        file.write(result_str)

def submit_result(req_dict):

    sid = req_dict.get("sid")
    flag = req_dict.get("flag")

    # Surely it's bad performance :(
    trainee_list = read_trainee_database()

    filtered_trainee_list = [(idx, x) for (idx, x) in enumerate(trainee_list) if x.id == sid]
    if len(filtered_trainee_list) == 0:
        trainee_list.append(Trainee(f"{sid},0,000000000000000"))
    idx = -1 if len(filtered_trainee_list) == 0 else filtered_trainee_list[0][0]

    ret = trainee_list[idx].submit_result(flag)
    write_trainee_database(trainee_list)
    return ret