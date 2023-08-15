# for the exception handling purpose

import sys
import logging
# what is sys 
# The sys module in Python provides various functions and variables that are used to manipulate different parts of the Python runtime environment. 

def error_message_detail(error,error_details:sys):
    # kis file ke kis line mein kya exception occur hua hai exc_tb mein store hoo jayega
    _,_,exc_tb = error_details.exc_info()
    file_name= exc_tb.tb_frame.f_code.co_filename 
    error_message = "Error occured in python script name [{0}] in line number [{1}] error message [{2}] ".format(
        file_name,exc_tb.tb_lineno,str(error)
    )
    return error_message

# here we are declaring our custom exception class
class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_messages = error_message_detail(error_message,error_detail)
      
    def __str__(self):
        return self.error_messages
    

# if __name__=="__main__":
    
#     try:
#         a = 1/0
#     except Exception as e:
#         logging.info('Divide by Zero')
#         raise CustomException(e,sys)
    