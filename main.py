from models import TrafficData
from utils import select_directory


def main():
    directory = select_directory()
    if not directory:
        print("Выбор директории отменен")
        return

    print(f"Файлов в директории: {TrafficData.count_files(directory)}")

    traffic_data = TrafficData.from_csv('data.csv')
    if not traffic_data:
        return

    print("\nОтсортировано по времени начала:")
    for item in traffic_data.sort_by_string_field('start_time'):
        print(item)

    print("\nОтсортировано по количеству проехавших автомобилей:")
    for item in traffic_data.sort_by_numeric_field('passed_cars'):
        print(item)

    try:
        threshold = int(input("\nВведите пороговое значение для авто в ожидании: "))
    except ValueError:
        print("Некорректный ввод")
        return

    print(f"\nДанные с ожиданием > {threshold}:")
    for item in traffic_data.filter_by_criterion('waiting_cars', threshold):
        print(item)

    print("\nРезультат работы генератора:")
    for item in traffic_data.filter_generator('waiting_cars', threshold):
        print(item)

    if input("\nДобавить новую запись? (д/н): ").lower() == 'д':
        traffic_data.add_new_record_interactive()
        traffic_data.to_csv('data.csv')


if __name__ == "__main__":
    main()