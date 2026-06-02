"""
From the given string, extract
IP
DATE
PICS
URL

Expected Output:
123.123.123.123
26/Apr/2000
wpaper.gif
http://www.jafsoft.com/asctortf/
"""
print("Input Data:")
print("-"*20)
# ---------------

input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'
print(input_data)

print("#"*40, end="\n\n")
#########################

print("Type of Input Data:")
print("-"*20)
# ---------------

print(type(input_data))

print("#"*40, end="\n\n")
#########################

print("Extract IP: 1-way")
print("-"*20)
# ---------------

# input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'
start_index = input_data.find("/pics/") # Returns index of 1st /
# start_index = start_index + len("/pics/")
# OR
start_index = start_index + 6

end_index = input_data.find("HTTP")
end_index = end_index - 1

img_1 = input_data[start_index:end_index]
print(img_1)

print("#"*40, end="\n\n")
#########################

# ---------------
# >>> # About split() method
# ---------------
# >>> # Feature-1
# >>> my_string = "WEL COME"
# >>> sp = my_string.split() # It will split by SPACE
# >>> sp
# ['WEL', 'COME']
# >>> # Feature-2
# >>> sp = my_string.split("C") # It will split by C
# >>> sp
# ['WEL ', 'OME']
# >>>
#########################

print("Extract IP: 2-way")
print("-"*20)
# ---------------

# input_data = '123.123.123.123 - - [26/Apr/2000:00:23:48 -0400] "GET /pics/wpaper.gif HTTP/1.0" 200 6248 "http://www.jafsoft.com/asctortf/" "Mozilla/4.05 (Macintosh; I; PPC)"'
sp = input_data.split()
print("Value of sp:", sp)

raw_img = sp[6]
print("raw_img:", raw_img) #  /pics/wpaper.gif

# 1-way to remove /pics/ from /pics/wpaper.gif
img_1 = raw_img[ 6 : ]

# 2-way to remove /pics/ from /pics/wpaper.gif
img_2 = raw_img.removeprefix("/pics/")

# 3-way to remove /pics/ from /pics/wpaper.gif
raw_img_sp = raw_img.split("/") # ['', 'pics, wpaper.gif]
img_3 = raw_img_sp[-1] # Take last value using negative indexes

print(img_1, img_2, img_3, sep="\n", end="\n\n")

print("#"*40, end="\n\n")
#########################
