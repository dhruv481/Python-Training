"""
Get data from sample_data.log

then

extract
IP
DATE
URL

then

make dictionary with extracted data

then

write to my_report_2.json

Expected dictionary
my_dictionary = {
0 : ('123.123.123.123', ''26/Apr/2000', 'http://www.jafsoft.com/asctortf/'),
1 : ('123.123.123.123', ''26/Apr/2000', 'http://search.netscape.com/Computers/Data_Formats/Document/Text/RTF'),
2 : ('123.123.123.123', ''26/Apr/2000', 'http://www.jafsoft.com/asctortf/'),
3 : ('123.123.123.123', ''26/Apr/2000', 'http://www.jafsoft.com/asctortf/'),
4 : ('123.123.123.123', ''26/Apr/2000', 'http://www.jafsoft.com/asctortf/'),
5 : ('123.123.123.123', ''26/Apr/2000', 'http://www.jafsoft.com/asctortf/')
}
"""