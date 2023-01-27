class Package:
    # Complexity: O(1)
    def __init__(self, package_id, address, city, state, zipcode, deadline, weight, note, status="At the HUB",
                 time_delivered=None, time_loaded=None, on_time="late"):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.note = note
        self.status = status
        self.time_delivered = time_delivered
        self.time_loaded = time_loaded
        self.on_time = on_time

    # Creates a string from the package attributes.
    # Complexity O(1)
    def __str__(self):
        package_str = 'ID: ' + str(self.package_id) + \
                      '\n- Address: ' + str(self.address) + \
                      '\n- Zip: ' + str(self.zipcode) + \
                      '\n- City: ' + str(self.city) + \
                      '\n- Deadline: ' + str(self.deadline) + \
                      '\n- Weight (kg): ' + str(self.weight) + \
                      '\n- Note: ' + str(self.note) + \
                      '\n- Status: ' + str(self.status) + \
                      '\n- Time Delivered: ' + str(self.time_delivered)

        return package_str
