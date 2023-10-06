from services import get_available_services, execute_requested_service
from custom_exception import InvalidOptionException

while True:
    for i in get_available_services():
        print(i)
    try:
        execute_requested_service(input("Enter valid option:"))
    except InvalidOptionException as e:
        print(e)
    finally:
        if input("Enter 9 to exit\nEnter any other number to continue\n") == '9':
            break