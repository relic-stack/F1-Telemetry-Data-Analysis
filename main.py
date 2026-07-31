import fastf1

print("Before")

schedule = fastf1.get_event_schedule(2025)

print("After")
print(schedule.head(10))

session = fastf1.get_session(2021, 7, 'Q')
print(session.event)