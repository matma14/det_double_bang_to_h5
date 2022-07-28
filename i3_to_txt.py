# python3

from icecube import icetray,dataio,dataclasses, simclasses, recclasses
import os

os.mkdir('/home/mandia/transfer_data/txt')
os.mkdir('/home/mandia/transfer_data/txt/not_important')
f = dataio.I3File('/home/mandia/transfer_data/Det_00_11_00357.i3.zst')
frame = f.pop_daq()
pulse = frame['MCPESeriesMap_withNoise_weighted']
nop = frame['I3Photons']

bad_words = 'Weight', 'Wavelength', 'ModuleKey', 'ParticleID', 'Group Vel.', 'Azimuth', 'Zenith', 'OMKey', 'Source', 'I3MCPulse'


with open('./txt/not_important/pulse.txt', 'a+') as f:
    for line in pulse:
        f.write(str(line))
        f.write('\n')
with open('./txt/not_important/nop.txt', 'a+') as f:
    for line in nop:
        f.write(str(line))
        f.write('\n')

with open('./txt/not_important/pulse.txt', 'r+') as f:
    for line in pulse:
        f.write(str(line))
        f.write('\n')
with open('./txt/not_important/nop.txt', 'r+') as f:
    for line in nop:
        f.write(str(line))
        f.write('\n')

in_pulse = open('./txt/not_important/pulse.txt', 'a+')
in_nop = open('./txt/not_important/nop.txt', 'a+')

new_pulse = open('./txt/not_important/new_pulse.txt', 'a+')
new_nop = open('./txt/not_important/new_nop.txt', 'a+')

charge = open('./txt/charge.txt', 'a+')
time = open('./txt/time.txt', 'a+')
time_nop = open('./txt/time_nop.txt', 'a+')
position = open('./txt/position.txt', 'a+')

in_pulse = open('./txt/not_important/pulse.txt', 'r+')
in_nop = open('./txt/not_important/nop.txt', 'r+')

new_pulse = open('./txt/not_important/new_pulse.txt', 'r+')
new_nop = open('./txt/not_important/new_nop.txt', 'r+')

charge = open('./txt/charge.txt', 'r+')
time = open('./txt/time.txt', 'r+')
time_nop = open('./txt/time_nop.txt', 'r+')
position = open('./txt/position.txt', 'r+')



for line in in_pulse :
     if not any(bad_word in line for bad_word in bad_words):
            new_pulse.write(line)

for line in in_nop :
     if not any(bad_word in line for bad_word in bad_words):
            new_nop.write(line)

for line in new_pulse :
     if 'Charge' not in line:
            time.write(line)
            # time.replace ('\n', ',')
     if 'Time' not in line:
            charge.write(line)
            # charge.replace ('\n', ',')
for line in new_nop :
     if 'Position' not in line:
            time_nop.write(line)
            # time_nop.replace ('\n', ',')
     if 'Time' not in line:
            position.write(line)
            # position.replace ('\n', ',')


in_pulse = open('./txt/not_important/pulse.txt', 'r+')
in_nop = open('./txt/not_important/nop.txt', 'r+')

new_pulse = open('./txt/not_important/new_pulse.txt', 'r+')
new_nop = open('./txt/not_important/new_nop.txt', 'r+')

charge = open('./txt/charge.txt', 'r+')
time = open('./txt/time.txt', 'r+')
time_nop = open('./txt/time_nop.txt', 'r+')
position = open('./txt/position.txt', 'r+')



for line in in_pulse :
     if not any(bad_word in line for bad_word in bad_words):
            new_pulse.write(line)

for line in in_nop :
     if not any(bad_word in line for bad_word in bad_words):
            new_nop.write(line)

for line in new_pulse :
     if 'Charge' not in line:
            time.write(line)
            # time.replace ('\n', ',')
     if 'Time' not in line:
            charge.write(line)
            # charge.replace ('\n', ',')
for line in new_nop :
     if 'Position' not in line:
            time_nop.write(line)
            # time_nop.replace ('\n', ',')
     if 'Time' not in line:
            position.write(line)
            # position.replace ('\n', ',')           



  


