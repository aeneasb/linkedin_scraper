import re
import locale
import datetime

def time_divide(string,convert=True):
    duration = re.search("\((.*?)\)", string)

    if duration != None:
        duration = duration.group(0)
        string = string.replace(duration, "").strip()
    else:
        duration = "()"
        string = string + "––()"

    times = string.split("–")

    if convert==True:
        times = time_convert(times)

    return (times[0].strip(), times[1].strip(), duration[1:-1])

def time_convert(times):

    def minex(m):
        month_exc = ['Januar','Februar','März','April','Juni','Juli','August','Sept.','September','Oktober','Novermber','Dezmeber']
        month_tar = ['Jan','Feb','M\xe4r','Apr','Jun','Jul','Aug','Sep','Sep','Okt','Nov','Dez']
        if m in month_exc:
            return month_tar[month_exc.index(m)]
        else:
            return m[:-1]

    locale.setlocale(locale.LC_TIME, "de_DE")
    try:
        y1 = str(int(times[0].split()[0]))
        y2 = str(int(times[1].split()[0]))
        times = [y1[-2:],y2[-2:]]
    except:
        #Extract single months out of string
        m1 = times[0].split()[0]
        y1 = times[0].split()[1]

        if times[1] == 'Heute':
            m1n = minex(m1)
            d1 = datetime.datetime.strptime(m1n+' '+y1, '%b %Y').strftime('%m.%y')
            d2 = 'today'
            times = [d1,d2]
        else:
            m2 = times[1].split()[0]
            y2 = times[1].split()[1]

            m1n = minex(m1)
            m2n = minex(m2)

            d1 = datetime.datetime.strptime(m1n+' '+y1, '%b %Y').strftime('%m.%y')
            d2 = datetime.datetime.strptime(m2n+' '+y2, '%b %Y').strftime('%m.%y')

            times = [d1,d2]
    return times
