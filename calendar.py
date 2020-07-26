"""
Sample Input
------------
person1_working_hours ['9:00', '17:00']
person1_booked_slots  [['9:00', '10:00'], ['12:00', '12:30'], ['13:00', '14:30']]

person2_working_hours ['8:00', '20:00']
person2_booked_slots  [['9:30', '10:00'], ['12:30', '13:00'], ['14:00', '15:30'], ['15:30', '16:00']]

slot_duration         30

Sample Output
-------------
available_slots      [['10:00', '12:00'], ['16:00', '17:00']]
"""


def compare_times(time1, time2):
    hour1, minute1 = time1.split(':')
    hour2, minute2 = time2.split(':')

    time1_in_minute = int(hour1) * 60 + int(minute1)
    time2_in_minute = int(hour2) * 60 + int(minute2)

    if time1_in_minute < time2_in_minute:
        return -1
    elif time1_in_minute > time2_in_minute:
        return 1
    else:
        return 0


def min_time(time1, time2):
    hour1, minute1 = time1.split(':')
    hour2, minute2 = time2.split(':')

    time1_in_minute = int(hour1) * 60 + int(minute1)
    time2_in_minute = int(hour2) * 60 + int(minute2)

    return time1 if time1_in_minute < time2_in_minute else time2


def max_time(time1, time2):
    hour1, minute1 = time1.split(':')
    hour2, minute2 = time2.split(':')

    time1_in_minute = int(hour1) * 60 + int(minute1)
    time2_in_minute = int(hour2) * 60 + int(minute2)

    return time1 if time1_in_minute > time2_in_minute else time2


def duration_in_minute(time1, time2):
    hour1, minute1 = time1.split(':')
    hour2, minute2 = time2.split(':')

    time1_in_minute = int(hour1) * 60 + int(minute1)
    time2_in_minute = int(hour2) * 60 + int(minute2)

    return time2_in_minute - time1_in_minute


def merge_booked_slots(person1_booked_slots, person2_booked_slots):
    merged_booked_slots = []
    counter1 = counter2 = 0

    while counter1 < len(person1_booked_slots) or counter2 < len(person2_booked_slots):
        # print(merged_booked_slots)
        # print(person1_booked_slots[counter1], person2_booked_slots[counter2])
        merged_booked_slots.append([min_time(person1_booked_slots[counter1][0], person2_booked_slots[counter2][0]),
                                    max_time(person1_booked_slots[counter1][1], person2_booked_slots[counter2][1])])

        counter1 += 1
        counter2 += 1

        if counter1 >= len(person1_booked_slots):
            merged_booked_slots.append(*person2_booked_slots[counter2:])
            break

        if counter2 >= len(person2_booked_slots):
            merged_booked_slots.append(*person1_booked_slots[counter1:])
            break

    return merged_booked_slots


def adjust_merged_booked_slots_for_working_hours(person1_working_hours, person2_working_hours, available_slots_of_both_person, merged_booked_slots_of_both_person):
    common_working_hours = [max_time(person1_working_hours[0], person2_working_hours[0]),
                            min_time(person1_working_hours[1], person2_working_hours[1])]
    # print('common working hours:\t', common_working_hours)

    if compare_times(common_working_hours[0], merged_booked_slots_of_both_person[0][0]) == -1:
        available_slots_of_both_person.insert(0, [common_working_hours[0], merged_booked_slots_of_both_person[0][0]])

    if compare_times(merged_booked_slots_of_both_person[len(merged_booked_slots_of_both_person) - 1][1], common_working_hours[1]) == -1:
        available_slots_of_both_person.append([merged_booked_slots_of_both_person[len(merged_booked_slots_of_both_person) - 1][1], common_working_hours[1]])

    return available_slots_of_both_person


def available_calender_slot(slots):
    available_slots = []

    for i in range(len(slots) - 1):
        if compare_times(slots[i][1], slots[i + 1][0]) < 0:
            available_slots.append([slots[i][1], slots[i + 1][0]])

    return available_slots


def check_valid_slots_for_duration(adjusted_available_slots, slot_duration):
    available_slots = []

    for adjusted_available_slot in adjusted_available_slots:
        if duration_in_minute(adjusted_available_slot[0], adjusted_available_slot[1]) >= slot_duration:
            available_slots.append(adjusted_available_slot)

    return available_slots


if __name__ == '__main__':
    person1_working_hours = ['7:00', '17:00']
    person1_booked_slots = [['9:00', '10:00'], ['12:00', '12:30'], ['13:00', '14:30']]

    person2_working_hours = ['6:00', '20:00']
    person2_booked_slots = [['9:30', '10:00'], ['12:30', '13:00'], ['14:00', '15:30'], ['15:30', '16:00']]

    slot_duration = 30

    print('person1, working hours:\t', person1_working_hours)
    print('person1, booked hours:\t', person1_booked_slots)
    print('person2, working hours:\t', person2_working_hours)
    print('person2, booked hours:\t', person2_booked_slots)
    print('slot duration:\t', slot_duration)
    print()

    merged_booked_slots_of_both_person = merge_booked_slots(person1_booked_slots, person2_booked_slots)
    # print('merged booked slots:\t', merged_booked_slots_of_both_person)
    available_slots_of_both_person = available_calender_slot(merged_booked_slots_of_both_person)
    # print('available slots:\t\t', available_slots_of_both_person)

    adjusted_available_slots = adjust_merged_booked_slots_for_working_hours(person1_working_hours, person2_working_hours, available_slots_of_both_person, merged_booked_slots_of_both_person)
    # print('adjusted available slots:\t', adjusted_available_slots)
    final_available_slots = check_valid_slots_for_duration(adjusted_available_slots, slot_duration)
    print('available slots:\t', final_available_slots)
