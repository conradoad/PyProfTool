import time


class PyProfTool:

    def __init__(self):
        self.enabled = True
        self.prof_points = {}

    def start_point(self, name):
        if not self.enabled:
            return

        if name not in self.prof_points:
            self.prof_points[name] = {}
            self.prof_points[name]["times"] = 0
            self.prof_points[name]["time_acc"] = 0
            self.prof_points[name]["running"] = False
            self.prof_points[name]["start_ts"] = 0
            self.prof_points[name]["end_ts"] = 0
            self.prof_points[name]["time_max"] = 0
            self.prof_points[name]["time_min"] = 0
            self.prof_points[name]["time_mean"] = 0

        if self.prof_points[name]["running"]:
            raise TypeError('Não foi encontrado um end_point para o script "' + name +
                            '" ou não está corretamente posicionado na iteração')

        self.prof_points[name]["running"] = True
        self.prof_points[name]["start_ts"] = time.time()
        return

    def end_point(self, name):
        ts = time.time()

        if not self.enabled:
            return

        if name not in self.prof_points:
            raise TypeError('Não foi encontrado o script "' + name + '". Pode estar faltando um start_point.')

        if not self.prof_points[name]["running"]:
            raise TypeError('Não foi encontrado um start_point para o script "' + name +
                            '" ou não está corretamente posicionado na iteração')

        self.prof_points[name]["end_ts"] = ts
        delta_time = ts - self.prof_points[name]["start_ts"]
        self.prof_points[name]["time_acc"] = self.prof_points[name]["time_acc"] + delta_time
        if self.prof_points[name]["time_max"] < delta_time:
            self.prof_points[name]["time_max"] = delta_time

        if self.prof_points[name]["time_min"] == 0:
            self.prof_points[name]["time_min"] = delta_time
        else:
            if self.prof_points[name]["time_min"] > delta_time:
                self.prof_points[name]["time_min"] = delta_time

        times = self.prof_points[name]["times"] + 1
        self.prof_points[name]["times"] = times
        self.prof_points[name]["time_mean"] = self.prof_points[name]["time_acc"] / times

        self.prof_points[name]["running"] = False

    def enable(self):
        self.enabled = True

    def disable(self):
        self.enabled = False
