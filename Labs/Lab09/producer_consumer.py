import city_processor
from city_processor import ISSDataRequest, CityOverheadTimes, CityDatabase, \
    City

class CityOverheadTimeQueue:
    def __init__(self):
        pass

    def put(self, overhead_time: city_processor.CityOverheadTimes) -> None:
        pass

    def get(self) -> city_processor.CityOverheadTimes:
        pass

    def __len__(self):
        pass


def main():
    pass


if __name__ == '__main__':
    main()
