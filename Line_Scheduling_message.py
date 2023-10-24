import os
import time
import logging

from schedule import every, repeat, run_pending
from py_topping.general_use import lazy_LINE
from os.path import join, dirname
from dotenv import load_dotenv
from datetime import datetime

date_time = datetime.today().strftime("%d-%m-%y %H:%M:%S")
time_time = datetime.today().strftime("%H:%M")


class open:
    def env_file():
        path = join(dirname(__file__), ".env")
        load_dotenv(path)
        key = os.environ.get("YOUR_ENV_FILE_TO_STORE_CREDENTIALS_OR_BEARER")
        return key

    def doc(obj):
        logging.basicConfig(level=logging.INFO, filename="main.log")

        def wrapper():
            start_time = time.time()
            update_docstring = obj.__doc__.format(date_time)
            line = lazy_LINE(token=open.env_file())
            line = line.send(update_docstring)
            end_time = time.time()
            logging.info(
                f"{obj.__name__}, date: {date_time}, time: {time_time} UTC+7, start: {start_time:.2f} seconds, end: {end_time:.2f} seconds, duration: {end_time - start_time:.2f} seconds, description: {update_docstring}, event: {KeyboardInterrupt}"
            )
            return line

        return wrapper

    # change the time when you want to run the programs using the schedule decorators
    # @repeat(every().days.at('08:00'))
    @repeat(every(3).seconds)
    @doc
    def string(self):
        """
        today date is : {0}
        """
        return self.string.__doc__

    @repeat(every(3).seconds)
    @doc
    def length(self):
        """
        the current date is : {0}
        """
        return self.length.__doc__

    @repeat(every(3).seconds)
    @doc
    def time_is(self):
        """
        the current time is : {0}
        """
        return self.time_is.__doc__

    def run(self):
        while True:
            run_pending()
            time.sleep(0)


if __name__ == "__main__":
    schedule = open()
    schedule.run()
