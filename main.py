import fastf1

print("1. Starting...")

# Pass 'French Grand Prix' instead of '7'
session = fastf1.get_session(2021, 7, 'Q', backend='fastf1')

print("2. Session object initialized!")
print("Event Name:", session.event['EventName'])
print("Session Name:", session.name)
print("Session Date:", session.date)

print("3. Done!")