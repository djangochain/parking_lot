# Problem Statement

I own a parking lot that can hold up to 'n' cars at any given point in time. Each slot is given a number starting at 1 increasing with increasing distance from the entry point in steps of one. I want to create an automated ticketing system that allows my customers to use my parking lot without human intervention.

When a car enters my parking lot, I want to have a ticket issued to the driver. The ticket issuing process includes us documenting the registration number (number plate) and the colour of the car and allocating an available parking slot to the car before actually handing over a ticket to the driver (we assume that our customers are nice enough to always park in the slots allocated to them). The customer should be allocated a parking slot which is nearest to the entry. At the exit the customer returns the ticket which then marks the slot they were using as being available.

Due to government regulation, the system should provide me with the ability to find out:

● Registration numbers of all cars of a particular colour.

● Slot number in which a car with a given registration number is parked.

● Slot numbers of all slots where a car of a particular colour is parked.

We interact with the system via a simple set of commands which produce a specific output. Please take a look at the example below, which includes all the commands you need to support - they're self explanatory. The system should allow input in two ways. Just to clarify, the same codebase should support both modes of input - we don't want two distinct submissions.

1) It should provide us with an interactive command prompt based shell where commands can be typed in

2) It should accept a filename as a parameter at the command prompt and read the commands from that file

## Installation


```bash
brew install python3 ## for mac
sudo apt-get install python3 ## for Ubuntu
```
Run ./bin/setup to check python3 is already in the system or not

## Usage

```python
python3 source/parking_lot.py ## to provide input from the prompt command line
python3 source/parking_lot.py file_inputs.txt ## to run cases from file
python3 -m unittest discover source ## to run the test case
```

```bash
./bin/parkin_lot ## to run parking lot with command prompt input

./bin/parkin_lot file_inputs.txt ##to run cases from file

./bin/run_functional_tests ## to run the test cases
```

## STDOUT
For the test case

```
Created a parking lot with 6 slots
.Allocated slot number: 1
.KA-12-FF-2017
.1
.1
.Slot number 1 is free
.
----------------------------------------------------------------------
Ran 6 tests in 0.001s

OK
```

For the file input

```
Created a parking lot with 6 slots
Allocated slot number: 1
Allocated slot number: 2
Allocated slot number: 3
Allocated slot number: 4
Allocated slot number: 5
Allocated slot number: 6
Slot number 4 is free
Slot No.	Registration No	Colour
1	KA-01-HH-1234	White
2	KA-01-HH-9999	White
3	KA-01-BB-0001	Black
5	KA-01-HH-2701	Blue
6	KA-01-HH-3141	Black
Allocated slot number: 4
Sorry, parking lot is full
KA-01-HH-1234, KA-01-HH-9999, KA-01-P-333
1, 2, 4
6
Not found
Happy Parking see you soon

```

For Command Prompt STDIN
```
> Enter command: park KA-01-HH-1234 White
> Parking Lot is not created yet

> Enter command: create_parking_lot 3
> Created a parking lot with 3 slots

> Enter command: park KA-01-HH-1234 White
> Allocated slot number: 1

> Enter command: status
> Slot No.	Registration No	Colour
> 1	 KA-01-HH-1234	 White

> Enter command: park KA-01-HH-1234 White
> Car with registration number KA-01-HH-1234 is already in the parking

> Enter command: park KA-01-HH-9999 White
> Allocated slot number: 2

> Enter command: status
> Slot No.	Registration No	Colour
> 1	KA-01-HH-1234	White
> 2	KA-01-HH-9999	White

> Enter command: park KA-01-HH-2701 Blue
> Allocated slot number: 3

> Enter command: park KA-01-HH-3141 Black
> Sorry, parking lot is full

> Enter command: leave 4
> Sorry, this slot number does not exist in parking lot.

> Enter command: leave 3
> Slot number 3 is free

> Enter command: status     
> Slot No.	Registration No	Colour
> 1	KA-01-HH-1234	White
> 2	KA-01-HH-9999	White

> Enter command: empty_slots
> 3

> Enter command: park KA-01-HH-3141 Black
> Allocated slot number: 3

> Enter command: status
> Slot No.	Registration No	Colour
> 1	KA-01-HH-1234	White
> 2	KA-01-HH-9999	White
> 3	KA-01-HH-3141	Black

> Enter command: registration_numbers_for_cars_with_colour White
> KA-01-HH-1234, KA-01-HH-9999

> Enter command: slot_numbers_for_cars_with_colour White
> 1, 2

> Enter command: slot_number_for_registration_number KA-01-HH-1234
> 1

> Enter command: slot_number_for_registration_number MH-04-AY-1111
> Not found

> Enter command: exit
> Happy Parking see you soon

```

Please make sure to update tests as appropriate.

## Author
Sahdev Garg