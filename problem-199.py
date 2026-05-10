#Rate Limiter Example

import time

# store user request timestamps
user_requests = []

# limit settings
LIMIT = 5        # max requests
TIME_WINDOW = 10 # seconds

def rate_limiter():

    current_time = time.time()

    # remove old requests
    while user_requests and current_time - user_requests[0] > TIME_WINDOW:
        user_requests.pop(0)

    # check limit
    if len(user_requests) < LIMIT:
        user_requests.append(current_time)
        return True
    else:
        return False

# simulate requests
for i in range(10):

    if rate_limiter():
        print(f"Request {i+1}: Allowed")
    else:
        print(f"Request {i+1}: Blocked (Rate Limit Exceeded)")

    time.sleep(1)

'''
output:-

Request 1: Allowed
Request 2: Allowed
Request 3: Allowed
Request 4: Allowed
Request 5: Allowed
Request 6: Blocked (Rate Limit Exceeded)
Request 7: Blocked (Rate Limit Exceeded)
Request 8: Allowed
Request 9: Allowed
Request 10: Allowed
'''