def status_updates(code, *args):
    if code == 'params_invalid':
        print()
    elif code == 'params valid':
        print(f'SUCCESS! Parameter {args[0]} is valid!')
    elif code == 'component_failure':
        print()
    elif code == 'component_false':
        print()
    elif code == 'component-successful':
        print()
    elif code == 'static_mac_found':
        print()
    elif code == 'static_mac_not_found-on-device':
        print()
    elif code == 'db_query_failure':
        print()
    elif code == 'retrieved-device_list':
        print()
    elif code == 'handle-success':
        print()
    elif code == 'handle-failure':
        print()
    elif code == 'worker-failure':
        print()
    elif code == 'static-mac-not-found-done':
        print()
    elif code == 'failed-connections':
        print()
    elif code == 'successful-connections':
        print()

param = 'myParam'
x = status_updates('params valid', param)

########################################################################################

class StatusUpdates:
    
    def params_invalid(self):
        print()
    def params_valid(self, param):
        print(f'SUCCESS! Parameter {param} is valid!')
    def component_failure(self):
        print()
    def component_false(self):
        print()
    def component_successful(self):
        print()
    def static_mac_found(self):
        print()
    def static_mac_not_found_on_device(self):
        print()
    def db_query_failure(self):
        print()
    def retrieved_device_list(self):
        print()
    def handle_success(self):
        print()
    def handle_failure(self):
        print()
    def worker_failure(self):
        print()
    def static_mac_not_found_done(self):
        print()
    def failed_connections(self):
        print()
    def successful_connections(self):
        print()

param = 'MYPARAM'
new_class = StatusUpdates()
new_class.params_valid(param)

# Dictionary Mapping for Switch case in Python
def monday():
    return "monday"
def tuesday():
    return "tuesday"
def wednesday():
    return "wednesday"
def thursday():
    return "thursday"
def friday():
    return "friday"
def saturday():
    return "saturday"
def sunday():
    return "sunday"
def default():
    return "Incorrect day"

switcher = {
    1: monday,
    2: tuesday,
    3: wednesday,
    4: thursday,
    5: friday,
    6: saturday,
    7: sunday
    }

def switch(dayOfWeek):
    return switcher.get(dayOfWeek, default)()

print(switch(3))
print(switch(5))


# # Using Python classes
# class PythonSwitch:
#     def day(self, dayOfWeek):

#         default = "Incorrect day"

#         return getattr(self, 'case_' + str(dayOfWeek), lambda: default)()

#     def case_1(self):
#         return "monday"
#     def case_2(self):
#         return "tuesday"
#     def case_3(self):
#         return "wednesday"
#     def case_4(self):
#        return "thursday"
#     def case_5(self):
#         return "friday"
#     def case_7(self):
#         return "saturday"
#     def case_6(self):
#         return "sunday"
        
# my_switch = PythonSwitch()

# print (my_switch.day(1))
# print (my_switch.day(3))


# def zero():
#         return 'zero'
# def one():
#         return 'one'
# def indirect(i):
#         switcher={
#                 0:zero,
#                 1:one,
#                 2:lambda:'two'
#                 }
#         func=switcher.get(i,lambda :'Invalid')
#         return func()
# indirect(4)


# if __name__ == "__main__":
#     # Executed when file is run directly
#     # python3 /home/runner/Notebook/how-to/switch_case.py

#     my_name = 'Daniel'
#     if my_name == 'Daniel':
        # select_option(7)
