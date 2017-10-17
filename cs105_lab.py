'''
    Some TAs are really lazy.
    Little script that I wrote to start up my labs easily
    For FAll 2017 CS105

    But it should be general enough really.

    Remember to alter some things.
'''
import webbrowser as wb
import winsound as ws
import datetime
import time
import sys
import pdb

################################################
############ things that TAs do ################
################################################

# Constants
CALM_UPDATE_TIME = 15
PANIC_UPDATE_TIME = 1
GRACE_TIME = datetime.timedelta(hours=0, minutes=9, seconds=30)
HANDIN_URL = 'https://my.cs.illinois.edu/handin/'
OPEN_LAB_URL = False
BASE_ALIGN = '\t\t'
TIME_ALIGN = '\t\t\t\t'
BLANK_LINES = '\n\n\n\n'
# TA Specific
TA_NAME = 'Haroun'
TA_MAIL = 'hhabeeb2@illinois.edu'
TA_EXTRA_MESSAGES = ['',
                     'Office hours by appointment. Drop me an email.\n',
                     'Please include \'CS105\' in email subject\n']

# Lab specific
LAB_URL = 'https://courses.engr.illinois.edu/cs105/fa2017/labs/plab6.html'
LAB_END_TIME = datetime.datetime(2017,
                                 10,  # TO CHANGE
                                 17,  # TO CHANGE
                                 19,  # TO CHANGE
                                 50,  # TO CHANGE
                                 00)


def parse_timedelta_hms(td):
    '''
        ARGS: td: timedelta object.
                  they store days and (seconds for day-fractions)
        RETURNS: hours, minutes, seconds (hms)
    '''
    h, r = divmod(td.seconds, 3600)
    h += 24 * td.days
    m, r = divmod(r, 60)
    return h, m, r


def play_alarm(n_repetitions):
    for i in range(0, n_repetitions):
        ws.Beep(440, 1000)
        ws.Beep(880, 1000)
        ws.Beep(1760, 4000)
        time.sleep(1)


def start_time(end_time, grace_time):
    '''
        ARGS:
            end_time: a datetime object for when the lab ends.
                    includes date, year, month, hours, minutes, seconds
            grace_time: a timedelta object representing how much time
                    after end_time is grace.
    '''
    def step(t):
        '''
            ARGS:
                takes timedelta object t which is time until completion.
            RETURNS:
                number of seconds to wait for
        '''
        h, m, s = parse_timedelta_hms(t)
        if (m > 0):
            return CALM_UPDATE_TIME
        else:
            return PANIC_UPDATE_TIME

    # Waiting for end time
    now = datetime.datetime.now()
    print(BASE_ALIGN, 'Remaining time: ', sep='')
    while (now < end_time):
        now = datetime.datetime.now()  # Use this to compute remaining time etc
        to_end = end_time - now
        hours, minutes, seconds = parse_timedelta_hms(to_end)
        print(TIME_ALIGN,
              hours, ' hr :',
              minutes, ' min :',
              seconds, ' sec',
              end='\r', sep='')
        time.sleep(step(to_end))

    print(BASE_ALIGN, 'TIMES UPPPPPP BEEP BEEP BEEP', sep='')
    
    print(BLANK_LINES)

    print(BASE_ALIGN, 'Handin: ', HANDIN_URL, sep='')
    #  MAKE NOISE
    play_alarm(3)

    now = datetime.datetime.now()
    end_time = end_time + grace_time
    print(BASE_ALIGN, 'GRACE TIME: ', sep='')
    while (now < end_time):
        now = datetime.datetime.now()  # Use this to compute remaining time etc
        to_end = end_time - now
        hours, minutes, seconds = parse_timedelta_hms(to_end)
        print(TIME_ALIGN,
              hours, ' hr :',
              minutes, ' min :',
              seconds, ' sec',
              end='\r', sep='')
        time.sleep(step(to_end))

    play_alarm(5)


def open_google_timer_for_haroun_tuesday():
    wb.open('https://www.google.com/search?q=set+timer+to+7%3A50pm&oq=set+timer+to+7%3A50pm&aqs=chrome..69i57.5336j0j1&sourceid=chrome&ie=UTF-8')


def open_google_timer_for_haroun_wednesday():
    wb.open('https://www.google.com/search?q=set+timer+to+3%3A20pm&oq=set+timer+to+3%3A20pm&aqs=chrome..69i57.3110j0j4&sourceid=chrome&ie=UTF-8')


print(BLANK_LINES)
print(BASE_ALIGN, 'Your lab: ', LAB_URL, sep='')
print(BLANK_LINES)
print(BASE_ALIGN, 'Handin: ', HANDIN_URL, sep='')

print(BASE_ALIGN, 'Your TA is ', TA_NAME, sep='')
print(BASE_ALIGN, 'Email ID: ', TA_MAIL, sep='')
print(BASE_ALIGN.join(TA_EXTRA_MESSAGES))

if (OPEN_LAB_URL is True):
    wb.open(LAB_URL)

start_time(LAB_END_TIME, GRACE_TIME)

################################################
############ things that YOU do ################
################################################
