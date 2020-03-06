"""
This program takes user input time and converts it to
the alternatve time format. i.e. if user enters 12h formated
time, it gives the time in 24h format.

The first part takes the input and puts in in string format with str.
It checks if the user entered a 12h format by looking for "am", "pm" extension.
If it is there, the time is treated as 12h fromated and if it is not, it is
treated as 24h format.

It then takes the first two characters as integer and stores it as hour.
The hour is then checked to see if it is 12 or greater. If it is, then it is PM
else, it is AM.

The conversion is the made depending on what has been found.
"""


input_time = str(input(">>>> "))

hour = int(input_time[:2])
possible_extensions = ("Am", "aM", "AM", "am", "Pm", "pM", "PM", "pm")
if input_time.endswith(possible_extensions):  # this checks for the extension
    extension = input_time[-2:] # gets the last two characters and saves them as the extension
    if extension.lower() == "am": # checks if the lowercase version of extension is "am"
        if hour == 12: #checks if the "hour" is 12
            print(f"00{input_time[2:-2]}") # replace 12 in hour with 00 and removes the extension
        else:
            print(f"{input_time[:-2]}") # prints the time without extension
    elif extension.lower() == "pm":
        if hour < 12:
            hour += 12 # adds 12 to the hour value
        print(f"{hour}{input_time[2:-2]}") # replaces hour with the new hour value.
else:
    extension = "AM" 
    if hour >= 12:
        extension = "PM"
        hour -= 12 # subracts 12 from hour
    if ":" in input_time: # checks if input time contains any colons.
        print(f"{hour}{input_time[2:]} {extension}")
    else:
        minutes = input_time[2:4] # gets the minute value from input_time
        seconds = input_time[4:6] # gets the seconds value from input_time
        print(f"{hour}:{minutes}:{seconds} {extension}")
