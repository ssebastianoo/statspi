from flask import Flask, render_template
import datetime, psutil, platform, os

class Stats:
    def __init__(self):
        self.launchtime = datetime.datetime.now()

    def uptime(self):
        "get raspberry uptime"

        uptime = datetime.datetime.now() - self.launchtime
        hours, x = divmod(int(uptime.total_seconds()), 3600)
        minutes, seconds = divmod(x, 60)
        days, hours = divmod(hours, 24)

        uptime = {
            "days": days,
            "hours": hours,
            "minutes": minutes,
            "seconds": seconds
        }

        return uptime

    def temperature(self):
        temp = os.popen("vcgencmd measure_temp").readline()
        return (temp.replace("temp=",""))

    def get_stats(self):
        "get all raspberry stats"

        stats = {
            "uptime": self.uptime(),
            "memory": f"{psutil.virtual_memory()[2]}%",
            "cpu": f"{psutil.cpu_percent()}%",
            "node": platform.node(),
            "system": platform.system(),
            "machine": platform.machine(),
            "architecture": f"{platform.architecture()[1]} {platform.architecture()[0]}",
            "temperature": self.temperature()
        }      
        
        return stats

app = Flask(__name__)
stats = Stats()

@app.route("/")
def index():
    rasp_info = stats.get_stats()
    stats_str = ""

    for stat in rasp_info:
        stats_str += f"{stat}: {rasp_info[stat]}<br>"

    return render_template("index.html", stats = rasp_info)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)