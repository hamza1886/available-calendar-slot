# Available Calendar Slot

Suppose two persons want to schedule a meeting. Both persons have their own office hours, while some of their calendar slots are already booked. 

Write an algorithm to find _common_ free (available) calendar slots of two persons given that availability of both persons is known and duration of meeting is known.

## Problem

Given calendar slots of two persons. Calendar slots are shown like `[<start_time>, <end_time>]`. Each such pair of `start_time` and `end_time` is considered one calendar slot.

Suppose availability of one person is from 7am to 5pm and similarly for other person, availability is from 6am to 8pm.

```python
person1_working_hours = ['9:00', '17:00']
person2_working_hours = ['8:00', '20:00']
```

Suppose some calendar slot of both persons are already booked. 

```python
person1_booked_slots = [['9:00', '10:00'], ['12:00', '12:30'], ['13:00', '14:30']]
person2_booked_slots = [['9:30', '10:00'], ['12:30', '13:00'], ['14:00', '15:30'], ['15:30', '16:00']]
``` 

Suppose they want to meet for a duration of 30 minute.

```python
slot_duration = 30
``` 

Write an algorithm that will show common available slots of both persons considering duration of meeting.

## Output

The output is a list of calendar slots which are commonly available for both persons. 

```python
available_slots = [['10:00', '12:00'], ['16:00', '17:00']]
``` 

## How to run code

The project is standalone, meaning there are no dependencies on third party modules.

```shell script
python calendar.py
```

# License

Copyright (c) 2020 Hamza Rashid

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.