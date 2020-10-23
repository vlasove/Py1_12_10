import argparse
# Убрать строковые .split() -> переписать через re.split()

parser = argparse.ArgumentParser()
parser.add_argument("-in", "--input", help="path to input file")
parser.add_argument("-out", "--output", help="path to outputfile")
args = parser.parse_args()

mails_list = []

if args.input is None:
    # Аргумент не был передан и нужно запросить у пользователя данные
    # из потока ввода
    mails_input = input("Enter mail. Sep by commas and space:")
    mails_list = mails_input.split(", ")
else:
    # Аргумент был передан
    try:
        with open(args.input, "r") as fhand:
            mails_input = fhand.read()
            mails_list = mails_input.split(', ')
    except FileNotFoundError as f_err:
        print("File not found. Trye again with right path to file!")

host_answer = []

if mails_list[0] != '':
    # Переберем все элементы списка , снимем доменные хостинги и сформируем вывод
    hosts_list = []
    for mail in mails_list:
        # alice@yandex.ru
        hosting = mail.split('@')[-1].split('.')[0] #['alice', 'yandex.ru'][-1] -> ['yandex', 'ru']
        hosts_list.append(hosting)
    # Отобразим только уникальные имена хостов
    host_answer = list(set(hosts_list))

    if args.output is None:
        print("Unique email aress:", ", ".join(host_answer))
    else:
        with open(args.output, "w") as fhand:
            fhand.write("Unique email aress: " + ", ".join(host_answer))
    

else:
    print("Email adress list is empty!")
