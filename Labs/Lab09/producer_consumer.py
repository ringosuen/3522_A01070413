import city_processor
import threading
import time
import logging


class CityOverheadTimeQueue:
    def __init__(self):
        self.data_queue = []

    def put(self, overhead_time: city_processor.CityOverheadTimes) -> None:
        """
        Responsible for adding to the queue. Accepts
        a overhead_time parameter and appends it to the data_queue list.
        :param overhead_time:
        """
        self.data_queue.append(overhead_time)

    def get(self) -> city_processor.CityOverheadTimes:
        """
        Responsible for removing an element from a Queue.
        Remember it's FIFO. Each call to this method
        returns the element at index 0 and deletes it from the list.
        :return:
        """
        return self.data_queue.pop(0)

    def __len__(self):
        """
        Returns the length of the data_queue.
        :return:
        """
        return len(self.data_queue)


class ProducerThread(threading.Thread):
    def __init__(self, cities: list, queue: CityOverheadTimeQueue):
        super().__init__()
        self.cities = cities
        self.queue = queue

    def run(self) -> None:
        counter = 0
        for city in self.cities:

            self.queue.put(
                city_processor.ISSDataRequest.get_overhead_pass(city))
            counter += 1
            if counter % 5 == 0:
                time.sleep(5)


class ConsumerThread(threading.Thread):
    def __init__(self, queue: CityOverheadTimeQueue):
        super().__init__()
        self.queue = queue
        self.data_incoming = True

    def run(self) -> None:
        if len(self.queue) is 0:
            print("length is 0")
            time.sleep(0.75)
        while self.data_incoming or len(self.queue) > 0:
            print(self.queue.get())
            time.sleep(0.5)


def main():
    excel_file = city_processor.CityDatabase("city_locations_test.xlsx")
    city_time_queue = CityOverheadTimeQueue()
    database = excel_file.city_db

    x = ProducerThread(database, city_time_queue)
    y = ProducerThread(database, city_time_queue)
    x.start()
    # y.start()
    # y.join()
    #
    z = ConsumerThread(city_time_queue)
    z.start()

    # test = CityOverheadTimeQueue()
    # test_object = city_processor.City("TEST", 10, 20)
    # test1 = city_processor.ISSDataRequest.get_overhead_pass(test_object)
    # test.put(test1)
    # for item in test.data_queue:
    #     print(item)
    # print(len(test.data_queue))
    # test.get()
    # print(len(test.data_queue))


if __name__ == '__main__':
    main()
