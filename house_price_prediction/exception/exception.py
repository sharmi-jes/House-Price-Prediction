import os
import sys
import logging
from house_price_prediction.logging.logging import logging


logging.info("create the exception class")
class HousePriceException(Exception):
    def __init__(self,error_message,error_detail:sys):
        self.error_message=error_message
        _,_,exc_tb=error_detail.exc_info()

        logging.info("error detail exc info return two param s->file no and filename")

        self.filename=exc_tb.tb_frame.f_code.co_filename
        self.lineno=exc_tb.tb_lineno
    
    logging.info("retunr error in str object function")
    def __str__(self):
       return f"Error occurred in Python script [{self.filename}] at line number [{self.lineno}] with error message: [{self.error_message}]"


if __name__=="__main__":
    try:
        a=1/0
        print("Zero division error")
    except Exception as e:
        raise HousePriceException(e,sys)