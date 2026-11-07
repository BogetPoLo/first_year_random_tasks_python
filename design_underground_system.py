class DesignUndergroundSystem:
    def __init__(self):
        self.drives = {}
        self.all_end_drives = {}


    def check_in(self, passenger_id: int | str, station: str, time: float) -> None:
        """Добавляет пассажира"""
        if passenger_id in self.drives:
            raise ValueError("Пассажир уже в поезде")
        else:
            self.drives[passenger_id] = (station, time)


    def check_out(self, passenger_id: int | str, station: str, time: float) -> None:
        """Удаляет пассажира"""
        if passenger_id not in self.drives:
            raise ValueError("Пассажира нет в поезде")
        else:
            st, ti = self.drives[passenger_id]
            if (st, station) not in self.all_end_drives:
                self.all_end_drives[(st, station)] = [[time - ti], 1]
            else:
                listt = self.all_end_drives[(st, station)]
                listt[0].append(time - ti)
                listt[1] += 1
                self.all_end_drives[(st, station)] = listt
        del self.drives[passenger_id]


    def get_average_time(self, start_station, end_station) -> float:
        """Выводит среднее значение"""
        if (start_station, end_station) not in self.all_end_drives:
            raise ValueError("Нет такого маршрута")
        value, count = self.all_end_drives[(start_station, end_station)]
        return sum(value) / count


test = DesignUndergroundSystem()
test.check_in(1, "Красногвардейская", 10.0)
test.check_out(1, "Сокол", 15.5)

test.check_in(2, "Красногвардейская", 20.4)
test.check_out(2, "Сокол", 31.3)

print(test.get_average_time("Красногвардейская", "Сокол"))

test.check_in(3, "Борисово", 20.2)
test.check_out(3, "Марьино", 31.3)

print(test.get_average_time("Борисово", "Марьино"))

# print(test.get_average_time("Борисово", "Марьино"))  # Ошибка
# test.check_out(4, "Борисово", 20.2)  # Ошибка
test.check_in(1, "Красногвардейская", 10.0)
test.check_in(1, "Красногвардейская", 10.0)  # Ошибка