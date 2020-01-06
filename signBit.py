# this code was necessary to debug an openCV issue
# before being able to run analysis on a colored or uncolored image
# I had to determine the sign and bit types so I could run the correct analysis

import numpy as np

def signType(markers, name):

    print( "%s has shape %s" % (name, str(markers.shape) ) )
    if len(markers.shape)==1:
        if np.issubdtype(markers[0], np.dtype('int8').type):
            print( "signed 8")
        elif  np.issubdtype(markers[0], np.dtype('int16').type):
            print( "signed 16 ")
        elif np.issubdtype(markers[0], np.dtype('int32').type) :
            print( "signed 32")
        elif np.issubdtype(markers[0], np.dtype('int64').type) :
            print( "signed 64")
        elif np.issubdtype(markers[0], np.dtype('uint8').type) :
            print( "unsigned 8")
        elif  np.issubdtype(markers[0], np.dtype('uint16').type):
            print( "unsigned 16")
        elif np.issubdtype(markers[0], np.dtype('uint32').type) :
            print( "unsigned 32")
        elif np.issubdtype(markers[0], np.dtype('uint64').type) :
            print( "unsigned 64")
        else:
            print("is not signed or unsigned of 8 bit, 16 bit, 32 bit, or 64 bit types.")
    elif len(markers.shape)==2:
        if np.issubdtype(markers[0][0], np.dtype('int8').type):
            print( "signed 8")
        elif  np.issubdtype(markers[0][0], np.dtype('int16').type):
            print( "signed 16 ")
        elif np.issubdtype(markers[0][0], np.dtype('int32').type) :
            print( "signed 32")
        elif np.issubdtype(markers[0][0], np.dtype('int64').type) :
            print( "signed 64")
        elif np.issubdtype(markers[0][0], np.dtype('uint8').type) :
            print( "unsigned 8")
        elif  np.issubdtype(markers[0][0], np.dtype('uint16').type):
            print( "unsigned 16")
        elif np.issubdtype(markers[0][0], np.dtype('uint32').type) :
            print( "unsigned 32")
        elif np.issubdtype(markers[0][0], np.dtype('uint64').type) :
            print( "unsigned 64")
        else:
            print("is not signed or unsigned 8 bit, 16 bit, 32 bit, or 64 bit types.")
    elif len(markers.shape)==3:
        if np.issubdtype(markers[0][0][0], np.dtype('int8').type) :
            print( "signed 8")
        elif  np.issubdtype(markers[0][0][0], np.dtype('int16').type) :
            print( "signed 16 ")
        elif np.issubdtype(markers[0][0][0], np.dtype('int32').type) :
            print( "signed 32")
        elif np.issubdtype(markers[0][0][0], np.dtype('int64').type) :
            print( "signed 64")
        elif np.issubdtype(markers[0][0][0], np.dtype('uint8').type):
            print( "unsigned 8")
        elif  np.issubdtype(markers[0][0][0], np.dtype('uint16').type):
            print( "unsigned 16")
        elif np.issubdtype(markers[0][0][0], np.dtype('uint32').type) :
            print( "unsigned 32")
        elif np.issubdtype(markers[0][0][0], np.dtype('uint64').type) :
            print( "unsigned 64")
        else:
            print("is not signed or unsigned 8 bit, 16 bit, 32 bit, or 64 bit types.")
    else:
        print("This function is only set up to tell the sign and bit of length 1, 2, or 3. Your parameter was not any of those.")
    print("")
