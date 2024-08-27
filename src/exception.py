import sys
import os 

def error_message_detail(error, error_detail:sys):
    
    _,_,exc_tb = error_detail.exc_info()

    filename = exc_tb.tb_frame.f_code.co_filename
    line_number= exc_tb.tb_lineno
    error_info= str(error)

    error_message="Error occured in file [{0}] in the line-number [{1}] and error is [{2}]".format(filename,line_number,error_info)
    
    return error_message



class SrcException(Exception):
    
    def __init__(self,error_message,error_detail:sys):

        super().__init__(error_message)
        
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
        
    def __str__(self):
        return  self.error_message
"""
In Python, the __str__() method is a special method that is used to define a human-readable string 
representation of an object. When you print an object or use str() on an object, Python will 
call the __str__() method of that object to get its string representation.

Key Points About __str__():
Readable Representation:

The purpose of __str__() is to return a string that is easy to read and understand, 
usually meant for end-users.
Automatic Invocation:

When you use print(object) or str(object), Python automatically calls object.__str__() to get 
the string to display.
Difference from __repr__():

While __str__() is meant for a human-readable output, __repr__() is meant for a more technical,
 unambiguous string representation (often for debugging). If you don’t define __str__(),
 Python will use __repr__() as a fallback.

"""