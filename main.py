# Name: Dalton Riley ID: 001511378

import csv
from hashtable import HashTable
from package import Package
from truck import Truck
import datetime

hash_table = HashTable()
truck_1 = Truck(1)
truck_2 = Truck(2)
truck_3 = Truck(3)


# This function iterates through the package csv file and creates package objects with the data.
# Then it inserts the new package into the hashtable.
# Complexity: O(N)
def load_package_list(filename):
    with open(filename) as packages:
        package_data = csv.reader(packages)
        for package in package_data:
            package_id = int(package[0])
            address = package[1]
            city = package[2]
            state = package[3]
            zipcode = package[4]
            deadline = package[5]
            weight = package[6]
            note = package[7]

            package = Package(package_id, address, city, state, zipcode, deadline, weight, note)

            hash_table.insert(package_id, package)


# Function is called and package hashtable is populated.
load_package_list('WGUPS Package File.csv')

# This variable is a two dimensional array that holds the distance table.
distance_list = [
    [0.0],
    [7.2, 0.0],
    [3.8, 7.1, 0.0],
    [11.0, 6.4, 9.2, 0.0],
    [2.2, 6.0, 4.4, 5.6, 0.0],
    [3.5, 4.8, 2.8, 6.9, 1.9, 0.0],
    [10.9, 1.6, 8.6, 8.6, 7.9, 6.3, 0.0],
    [8.6, 2.8, 6.3, 4.0, 5.1, 4.3, 4.0, 0.0],
    [7.6, 4.8, 5.3, 11.1, 7.5, 4.5, 4.2, 7.7, 0.0],
    [2.8, 6.3, 1.6, 7.3, 2.6, 1.5, 8.0, 9.3, 4.8, 0.0],
    [6.4, 7.3, 10.4, 1.0, 6.5, 8.7, 8.6, 4.6, 11.9, 9.4, 0.0],
    [3.2, 5.3, 3.0, 6.4, 1.5, 0.8, 6.9, 4.8, 4.7, 1.1, 7.3, 0.0],
    [7.6, 4.8, 5.3, 11.1, 7.5, 4.5, 4.2, 7.7, 0.6, 5.1, 12.0, 4.7, 0.0],
    [5.2, 3.0, 6.5, 3.9, 3.2, 3.9, 4.2, 1.6, 7.6, 4.6, 4.9, 3.5, 7.3, 0.0],
    [4.4, 4.6, 5.6, 4.3, 2.4, 3.0, 8.0, 3.3, 7.8, 3.7, 5.2, 2.6, 7.8, 1.3, 0.0],
    [3.7, 4.5, 5.8, 4.4, 2.7, 3.8, 5.8, 3.4, 6.6, 4.0, 5.4, 2.9, 6.6, 1.5, 0.6, 0.0],
    [7.6, 7.4, 5.7, 7.2, 1.4, 5.7, 7.2, 3.1, 7.2, 6.7, 8.1, 6.3, 7.2, 4.0, 6.4, 5.6, 0.0],
    [2.0, 6.0, 4.1, 5.3, 0.5, 1.9, 7.7, 5.1, 5.9, 2.3, 6.2, 1.2, 5.9, 3.2, 2.4, 1.6, 7.1, 0.0],
    [3.6, 5.0, 3.6, 6.0, 1.7, 1.1, 6.6, 4.6, 5.4, 1.8, 6.9, 1.0, 5.4, 3.0, 2.2, 1.7, 6.1, 1.6, 0.0],
    [6.5, 4.8, 4.3, 10.6, 6.5, 3.5, 3.2, 6.7, 1.0, 4.1, 11.5, 3.7, 1.0, 6.9, 6.8, 6.4, 7.2, 4.9, 4.4, 0.0],
    [1.9, 9.5, 3.3, 5.9, 3.2, 4.9, 11.2, 8.1, 8.5, 3.8, 6.9, 4.1, 8.5, 6.2, 5.3, 4.9, 10.6, 3.0, 4.6, 7.5, 0.0],
    [3.4, 10.9, 5.0, 7.4, 5.2, 6.9, 12.7, 10.4, 10.3, 5.8, 8.3, 6.2, 10.3, 8.2, 7.4, 6.9, 12.0, 5.0, 6.6, 9.3, 2.0,
     0.0],
    [2.4, 8.3, 6.1, 4.7, 2.5, 4.2, 10.0, 7.8, 7.8, 4.3, 4.1, 3.4, 7.8, 5.5, 4.6, 4.2, 9.4, 2.3, 3.9, 6.8, 2.9, 4.4,
     0.0],
    [6.4, 6.9, 9.7, 0.6, 6.0, 9.0, 8.2, 4.2, 11.5, 7.8, 0.4, 6.9, 11.5, 4.4, 4.8, 5.6, 7.5, 5.5, 6.5, 11.4, 6.4, 7.9,
     4.5, 0.0],
    [2.4, 10.0, 6.1, 6.4, 4.2, 5.9, 11.7, 9.5, 9.5, 4.8, 4.9, 5.2, 9.5, 7.2, 6.3, 5.9, 11.1, 4.0, 5.6, 8.5, 2.8, 3.4,
     1.7, 5.4, 0.0],
    [5.0, 4.4, 2.8, 10.1, 5.4, 3.5, 5.1, 6.2, 2.8, 3.2, 11.0, 3.7, 2.8, 6.4, 6.5, 5.7, 6.2, 5.1, 4.3, 1.8, 6.0, 7.9,
     6.8, 10.6, 7.0, 0.0],
    [3.6, 13.0, 7.4, 10.1, 5.5, 7.2, 14.2, 10.7, 14.1, 6.0, 6.8, 6.4, 14.1, 10.5, 8.8, 8.4, 13.6, 5.2, 6.9, 13.1, 4.1,
     4.7, 3.1, 7.8, 1.3, 8.3, 0.0]
]

# This variable is a list of all the addresses to be delivered to.
address_list = [
    "HUB",
    " 1060 Dalton Ave S (84104)",
    " 1330 2100 S (84106)",
    " 1488 4800 S (84123)",
    " 177 W Price Ave(84115)",
    " 195 W Oakland Ave (84115)",
    " 2010 W 500 S (84104)",
    " 2300 Parkway Blvd (84119)",
    " 233 Canyon Rd (84103)",
    " 2530 S 500 E (84106)",
    " 2600 Taylorsville Blvd (84118)",
    " 2835 Main St (84115)",
    " 300 State St (84103)",
    " 3060 Lester St (84119)",
    " 3148 S 1100 W (84119)",
    " 3365 S 900 W (84119)",
    " 3575 W Valley Central Station bus Loop (84119)",
    " 3595 Main St (84115)",
    " 380 W 2880 S (84115)",
    " 410 S State St (84111)",
    " 4300 S 1300 E (84117)",
    " 4580 S 2300 E (84117)",
    " 5025 State St (84107)",
    " 5100 South 2700 West (84118)",
    " 5383 South 900 East #104 (84117)",
    " 600 E 900 South (84105)",
    " 6351 South 900 East (84121)"
]


# This function takes an address and loops through the address list. If the address is found
# it returns the address's index.
# Complexity: O(1)
def get_address(address):
    for i, a in enumerate(address_list):
        if address in a:
            return i


# This function takes two addresses as parameters and calls the get_address function to convert them to their indexes.
# It then uses those indexes to find the value within the distance_list.
# Complexity: O(1)
def get_distance(address1, address2):
    try:
        return distance_list[get_address(address1)][get_address(address2)]
    except IndexError:
        return distance_list[get_address(address2)][get_address(address1)]


# This function loops through a truck's package addresses and compares the distance from the current
# location. If the distance is shorter than the current shortest distance we replace the value of the shortest_distance
# variable and record the address. At the end it returns the closest address, distance from current address, and
# the package id associated with that address.
# Complexity: O(N)
def min_distance(truck_packages, current_address):
    shortest_distance = 25
    closest_address = None
    closest_id = None
    for package in truck_packages:
        next_address = package.address
        distance_check = get_distance(current_address, next_address)
        if distance_check <= shortest_distance:
            shortest_distance = distance_check
            closest_address = next_address
            closest_id = package.package_id

    return closest_address, shortest_distance, closest_id


# datetime variables to check if package has been delivered on time
nine_datetime = datetime.timedelta(hours=9, minutes=00, seconds=00)
ten_thirty_datetime = datetime.timedelta(hours=10, minutes=30, seconds=00)
five_datetime = datetime.timedelta(hours=17, minutes=00, seconds=00)


# This function takes a truck object and start time as parameters. It then uses the min_distance function to loop
# the truck's packages. The closest package address is chosen, the miles to the address and time spent are recorded
# and the package status and delivery time are updated. It then removes the package from the truck. It returns the total
# amount of miles travelled delivering all packages on the truck.
# Complexity: O(N^2)
def deliver_packages(truck, start_time):
    h, m, s = start_time.split(":")
    time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
    current_address = "HUB"
    miles = 0
    for i in truck.packages[:]:
        visited_address, distance, package_id = min_distance(truck.packages, current_address)
        delivered_package = hash_table.search(package_id)
        delivered_package.time_loaded = time
        miles = miles + distance
        delivery_time = (distance / 18) * 60
        time_elapsed = datetime.timedelta(minutes=delivery_time)
        time = time + time_elapsed
        delivered_package.time_delivered = time
        delivered_package.status = "delivered"
        if delivered_package.deadline == "EOD" and time < five_datetime:
            delivered_package.on_time = "on time"
        elif delivered_package.deadline == "9:00 AM" and time < nine_datetime:
            delivered_package.on_time = "on time"
        elif delivered_package.deadline == "10:30 AM" and time < ten_thirty_datetime:
            delivered_package.on_time = "on time"
        current_address = visited_address
        truck.packages.remove(delivered_package)
        # print(str(delivered_package.package_id) + " delivered at " + str(time) + " to " + delivered_package.address)

    return miles


# This function returns the truck to the hub from the last address and returns the miles travelled.
# Complexity: O(1)
def return_to_hub(truck):
    current_location = truck.current_location
    hub = "HUB"
    distance = get_distance(current_location, hub)
    return distance


# This function sets the package status' on a truck to en route
# Complexity: O(1)
def set_en_route(truck):
    for package in truck.packages:
        package.status = 'en route'


# Loading first round of packages manually, based on constraints.
truck_1.packages = [hash_table.search(13), hash_table.search(15), hash_table.search(19)]

set_en_route(truck_1)

truck_2.packages = [hash_table.search(3), hash_table.search(18), hash_table.search(36), hash_table.search(38),
                    hash_table.search(2), hash_table.search(4), hash_table.search(5), hash_table.search(6),
                    hash_table.search(14), hash_table.search(16), hash_table.search(25), hash_table.search(39),
                    hash_table.search(21), hash_table.search(22), hash_table.search(31), hash_table.search(34)
                    ]

set_en_route(truck_2)

# first round of packages for each truck have been delivered and total miles has been recorded in variables.
t1 = deliver_packages(truck_1, '08:00:00')
t2 = deliver_packages(truck_2, '09:05:00')

# Truck 1 returns to hub for the rest of the packages. Distance travelled is stored in variable.
t3 = return_to_hub(truck_1)

truck_1.packages = [hash_table.search(1), hash_table.search(35), hash_table.search(33), hash_table.search(32),
                    hash_table.search(7), hash_table.search(8), hash_table.search(10), hash_table.search(11),
                    hash_table.search(12), hash_table.search(20), hash_table.search(29), hash_table.search(30),
                    hash_table.search(37), hash_table.search(40), hash_table.search(17)
                    ]

set_en_route(truck_1)

t4 = deliver_packages(truck_1, '9:45:00')

t5 = return_to_hub(truck_2)

truck_2.packages = [hash_table.search(9), hash_table.search(26), hash_table.search(27),
                    hash_table.search(28), hash_table.search(23), hash_table.search(24)]

set_en_route(truck_2)

t6 = deliver_packages(truck_2, "11:45:00")

total_distance = t1 + t2 + t3 + t4 + t5 + t6

# Start of the user interface
# Complexity: O(N)
print("WGUPS Routing System")
print("Total distance travelled was " + str(total_distance))

user_input = input("Type 1 to see status of all packages. Type 2 to see status of one package. Type q to quit.")

if user_input == "q":
    exit()

elif user_input == "1":
    user_time = input("Enter a time in hh:mm:ss format.")
    hour, minute, second = user_time.split(":")
    entered_time = datetime.timedelta(hours=int(hour), minutes=int(minute), seconds=int(second))
    for x in range(1, 41):
        check_package = hash_table.search(x)
        if entered_time >= check_package.time_delivered:
            print("Package " + str(check_package.package_id) + " was delivered at " +
                  str(check_package.time_delivered) + ". " + check_package.on_time)
        elif check_package.time_delivered > entered_time >= check_package.time_loaded:
            print("Package " + str(check_package.package_id) + " is en route. ")
        elif check_package.time_delivered > entered_time < check_package.time_loaded:
            print("Package " + str(check_package.package_id) + " is at the hub. ")


elif user_input == "2":
    user_time = input("Enter a time in hh:mm:ss format.")
    package_num = input("Enter package number.")
    hour, minute, second = user_time.split(":")
    entered_time = datetime.timedelta(hours=int(hour), minutes=int(minute), seconds=int(second))
    for x in range(1, 41):
        if hash_table.search(x).package_id is package_num:
            user_package = hash_table.search(x)
            if entered_time >= user_package.time_delivered:
                print("Package " + str(user_package.package_id) + " was delivered at " +
                      str(user_package.time_delivered) + ". " + user_package.on_time)
            elif user_package.time_delivered > entered_time >= user_package.time_loaded:
                print("Package " + str(user_package.package_id) + " is en route. ")
            elif user_package.time_delivered > entered_time < user_package.time_loaded:
                print("Package " + str(user_package.package_id) + " is at the hub. ")
