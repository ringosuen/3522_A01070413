import city_processor
import threading
import time
import logging


class CityOverheadTimeQueue:
    """
    This is the buffer that receives a City object and prints out the
    corresponding info based on the request made.
    """
    def __init__(self):
        """
        Initializes an empty data queue list and a lock.
        """
        self.data_queue = []
        self.access_queue_lock = threading.Lock()

    def put(self, overhead_time: city_processor.CityOverheadTimes) -> None:
        """
        Responsible for adding to the queue. Accepts
        a overhead_time parameter and appends it to the data_queue list.
        :param overhead_time: city_processor.CityOverheadTimes
        """
        with self.access_queue_lock:
            self.data_queue.append(overhead_time)

    def get(self) -> city_processor.CityOverheadTimes:
        """
        Responsible for removing an element from a Queue.
        Remember it's FIFO. Each call to this method
        returns the element at index 0 and deletes it from the list.
        :return:
        """
        with self.access_queue_lock:
            try:
                return self.data_queue.pop(0)
            except IndexError:
                print("list empty")

    def __len__(self):
        """
        Returns the length of the data_queue.
        :return:
        """
        return len(self.data_queue)


class ProducerThread(threading.Thread):
    """
    Send queue to buffer.
    """
    def __init__(self, cities: list, queue: CityOverheadTimeQueue):
        """
        Takes in a list of City objects and queue
        :param cities: list
        :param queue: CityOverheadTimeQueue
        """
        super().__init__()
        self.cities = cities
        self.queue = queue

    def run(self) -> None:
        """
        Executes when the thread starts. Loops over each city and
        passes it to the implement_.get_overheadpass() method. It then proceeds
        to add the city to the queue. After reading in 5 cities, the thread
        sleeps for 1 secdon.
        :return: None
        """
        counter = 0
        for city in self.cities:
            self.queue.put(
                city_processor.ISSDataRequest.get_overhead_pass(city))
            counter += 1
            if counter % 5 == 0:
                time.sleep(1)


class ConsumerThread(threading.Thread):
    """
    Responsible for consuming data from the queue and printing it out to
    the console.
    """
    def __init__(self, queue: CityOverheadTimeQueue):
        """
        Same queue as the one producer has. Implements a data_incoming
        boolean attribute that is set to True. Changes when a thread has
        joined.
        :param queue: CityOverheadTimeQueue
        """
        super().__init__()
        self.queue = queue
        self.data_incoming = True

    def run(self) -> None:
        """
        If queue is not empty this method
        gets an item from the queue and prints it tothe console and
        then sleep for 0.5s. While processing the queue, if it's empty,
        puts the trhead to sleep for 0.75s.
        :return: None
        """
        if len(self.queue) is 0:
            time.sleep(0.75)
            print("sleeping 0.75s")
        while self.data_incoming or len(self.queue) > 0:
            print(self.queue.get())
            time.sleep(0.5)
            print("sleeping 0.5s")


def main():
    """
    Uses 3 producer threads and joins together. Reads from an excel file.
    Excel file is split into 3 parts.
    """
    excel_file = city_processor.CityDatabase("city_locations.xlsx")
    city_time_queue = CityOverheadTimeQueue()
    city_database = excel_file.city_db
    length = len(city_database)

    list1 = city_database[0:int(length / 3)]
    list2 = city_database[int(length / 3):int(2 * length / 3)]
    list3 = city_database[int(2 * length / 3):]

    consumer = ConsumerThread(city_time_queue)

    producer1 = ProducerThread(list1, city_time_queue)
    producer2 = ProducerThread(list2, city_time_queue)
    producer3 = ProducerThread(list3, city_time_queue)

    producer1.start()
    producer2.start()
    producer3.start()

    consumer.start()

    producer1.join()
    producer2.join()
    producer3.join()
    consumer.data_incoming = False
    consumer.join()


if __name__ == '__main__':
    main()
