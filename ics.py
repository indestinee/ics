import time
import pytz

tzids = pytz.all_timezones

def current_time():
    t = time.localtime(time.time())
    tz = time.tzname
    if isinstance(tz, tuple):
        tz = tz[0]
    gmt = int(time.timezone//3600)
    return {
        'start_date': '%d%02d%02d'%(t.tm_year, t.tm_mon, t.tm_mday),
        'start_time': '%02d%02d%02d'%(t.tm_hour, t.tm_min, t.tm_sec),
        'start_tz': 'Etc/GMT%s%s'%('+' if gmt >= 0 else '', gmt)
    }

my_tz = current_time()['start_tz']

def check_tz(tz):
    if tz[:3] == 'GMT':
        if len(tz) == 3:
            tz = tz + '+0'
        tz = 'Etc/' + tz
    assert tz in tzids, '{} not in tzids'.format(tz)
    return tz

def generate(start_date, start_time, end_date, end_time, summary,\
        start_tz=my_tz, end_tz=my_tz,
        description=None, location=None, url=None, **kwargs):
    start_tz = check_tz(start_tz)
    end_tz = check_tz(end_tz)
    data = '\n'.join([
        'BEGIN:VCALENDAR',
        'VERSION:2.0',
        'BEGIN:VEVENT',
        'URL:{}'.format(url),
        'DTSTART;TZID={}:{}T{}'.format(start_tz, start_date, start_time),
        'DTEND;TZID={}:{}T{}'.format(end_tz, end_date, end_time),
        'SUMMARY:{}'.format(summary),
        'LOCATION:{}'.format(location),
        'DESCRIPTION:{}'.format(description.replace('\n', ' ')),
        'END:VEVENT',
        'END:VCALENDAR',
    ])

    return data
