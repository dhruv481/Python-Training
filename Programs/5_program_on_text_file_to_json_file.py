"""
Get data from my_report_1.txt

then

extract
IP
DATE
URL

then

make dictionary with extracted data

then

write to my_report_4.json

Expected dictionary
my_dictionary = {
0 : {"IP": '123.123.123.123', "DATE": ''26/Apr/2000', "URL": 'http://www.jafsoft.com/asctortf/'},
1 : {"IP": '123.123.123.123', "DATE": ''26/Apr/2000', "URL": 'http://search.netscape.com/Computers/Data_Formats/Document/Text/RTF'},
2 : {"IP": '123.123.123.123', "DATE": ''26/Apr/2000', "URL": 'http://www.jafsoft.com/asctortf/'},
3 : {"IP": '123.123.123.123', "DATE": ''26/Apr/2000', "URL": 'http://www.jafsoft.com/asctortf/'},
4 : {"IP": '123.123.123.123', "DATE": ''26/Apr/2000', "URL": 'http://www.jafsoft.com/asctortf/'},
5 : {"IP": '123.123.123.123', "DATE": ''26/Apr/2000', "URL": 'http://www.jafsoft.com/asctortf/'}
}
"""