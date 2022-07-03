from morse3 import Morse as morse
from PIL import Image
# .は_1個+空白1個
CODE_TO_SIGNAL = {'.':'_ ','-':'___ ',' ':'  '}
IS_SIGNAL_ON   = {'_':True,'_':True, ' ':False}
morse_message =  morse('Hello.').stringToMorse()
time_codes = ''.join([CODE_TO_SIGNAL[m] for m in morse_message])
signals = [ IS_SIGNAL_ON[c] for c in time_codes]
print(morse_message); print(time_codes)

w=600
h=1200
IMAGE = {True :Image.new('RGB',(w,h),(255,255,255)),
         False:Image.new('RGB',(w,h),(0,0,0))}
images = [IMAGE[s] for s in signals]
images[0].save( 'message.gif',save_all=True,
  append_images=images[1:],optimize=True,duration=100,loop=1)
