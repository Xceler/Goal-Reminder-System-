import datetime
import schedule 
import time 
from plyer import notification 

def get_user_info():
    print("Goal Reminder System")
    name = input("Enter your name:")
    goal = input("What is your curren goal: ")
    struggle = input("What is your biggest struggle: ")
    previous_emotion = input("How were you feeling previously:")
    return name, goal, struggle, previous_emotion 


def send_noti(goal):
    noti_title = 'Goal Reminder'
    noti_message = f"Don't forget your goal: {goal}"
    noti_timeout = 10

    notification.notify(
        title = noti_title,
        message = noti_message,
        timeout = noti_timeout
    )


def check_online():
    return True

def remind_user(name, goal, struggle, previous_emotion):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Hello {name} ! Here'a reminder at {current_time}")
    print(f"Your goals : {goal}")
    print(f"I feel your struggle : {struggle}")
    print(f"Your Last emotion is {previous_emotion}")
    print("Stay Focused!")
    send_noti(goal)

def schedule_reminders(name, goal, struggle, previous_emotion):
    schedule.every(30).seconds.do(remind_user, name, goal, struggle, previous_emotion)
    while check_online():
        schedule.run_pending()
        time.sleep(1)
    

def main():
    name, goal, struggle, previous_emotion = get_user_info()
    schedule_reminders(name, goal, struggle, previous_emotion)

if __name__ == '__main__':
    main()





























































































































































































































































































































































































































































































