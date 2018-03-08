"""
this code converts rgb values(0 to 255) to hex values(base 16)
and also otherwise.
"""
#convert rgb to hex
def rgb_hex():
  invalid_msg="Invalid input";
  
  red=int(input("Enter a red value: "));
  if(red<0 or red>255):
    print("Enter a value between 0 and 255");
    return;
  green=int(input("Enter a green value: "));
  if(green<0 or green>255):
    print("Enter a value between 0 and 255");
    return;
  blue=int(input("Enter a blue value: "));
  if(blue<0 or blue>255):
    print("Enter a value between 0 and 255");
    return;
  val=(red<<16) +(green<<8)+blue;
 
  print("%s"% hex(val)[2:]);

#convert hex to rgb
def hex_rgb():
  hex_val=input("Enter a hex value - R|G|B :");
  if(len(hex_val)!=6):
    print("Invalid input. enter a 6 digit hex");
    return;
  else:
    hex_val=int(hex_val,16);
  
  two_hex_digits=2**8;
  
  blue=hex_val%two_hex_digits;
  hex_val=hex_val>>8;
  
  green=hex_val%two_hex_digits;
  hex_val=hex_val>>8;
  
  red=hex_val%two_hex_digits;
  
  print("red: %s green: %s blue: %s" %(red,green,blue));
  
#main convert method
def convert():
  while(True):
    option=input("Enter 1 to convert RGB to HEX. Enter 2 to convert HEX to RGB. Enter X to Exit:");
    if(option=='1'):
      print("RGB to Hex...");
      rgb_hex();
    elif(option=='2'):
      print("Hex to RGB...");
      hex_rgb();  
    elif(option=='x' or option=='X'):
      break;
    else:
      print("Error. Invalid input");
      
      
convert();
