import argparse # click

parser = argparse.ArgumentParser() # Сущность для обработки параметров
parser.add_argument("echo", help="This echo args. Will printed in StdOut") # (required arg) Программа будет споосбна принимать 1 параметр. Внетрунее имя его - echo
args = parser.parse_args() # В этот момент происходит считывание параметров CLI
#args -> Namespace - аналог словаря
print(args)
print("Value of echo:", args.echo)