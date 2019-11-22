import city_processor
import threading
import time
import logging


class CityOverheadTimeQueue:
    def __init__(self):
        self.data_queue = []
        self.access_queue_lock = threading.Lock()

    def put(self, overhead_time: city_processor.CityOverheadTimes) -> None:
        """
        Responsible for adding to the queue. Accepts
        a overhead_time parameter and appends it to the data_queue list.
        :param overhead_time:
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
                time.sleep(1)
                print("sleeping 1s")


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
