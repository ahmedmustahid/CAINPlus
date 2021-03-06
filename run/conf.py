#!/usr/bin/python
from util import SetParameterValues
# Setting 

# number of jobs per submit.
nEventPerSubmit = 10 
nTotalEvents = 100

inconf = "templates/beam_250.i"

#integer = [i for i in range(20003)]
#odd = [str(n) for n in integer[3::2]]

# Set parameter name and its values (array).
# Use SetParameterValues("NAME",[X1,X2,X3,...]) for each parameter.
# Add SetParameterValues to scandata (array) as many as you want.
scandata = [
#    SetParameterValues("SigxFactor", ["3.0"]),
    SetParameterValues("SigxFactor", ["1.0"]),
    #SetParameterValues("SigxFactor", ["0.8", "1.0", "1.2", "1.4"]),
    #SetParameterValues("SigxFactor", ["0.2", "0.4", "0.6", "0.8", "1.0", "1.2", "1.4", "1.6", "1.8", "2.0", "2.2", "2.4", "2.6", "2.8"]),
    #SetParameterValues("SigyFactor", ["0.2", "0.4", "0.6", "0.8", "1.0", "1.2", "1.4", "1.6", "1.8", "2.0", "2.2", "2.4", "2.6", "2.8"]),
#    SetParameterValues("SigyFactor", ["0.2", "0.4", "0.6", "0.8", "1.0", "1.2", "1.4", "1.6", "1.8", "2.0", "2.2", "2.4", "2.6", "2.8", "3.0", "3.2", "3.4", "3.6", "3.8"]),
#    SetParameterValues("SigyFactor", ["0.2"]),
#    SetParameterValues("SigyFactor", ["1.2", "1.4"]),
#    SetParameterValues("SigyFactor", ["2.2", "2.4", "2.6", "2.8", "3.0"]),
#    SetParameterValues("SigyFactor", ["3.2", "3.4", "3.6", "3.8"]),
#    SetParameterValues("SigyFactor", ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10"]),
#    SetParameterValues("SigyFactor", ["0.8"]),
#    SetParameterValues("DeltayFactor", ["0.0", "0.1", "0.2", "0.3", "0.4", "0.5"]),
    #SetParameterValues("Rand", odd)
	   ]
