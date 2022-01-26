import os
import sys
import shlex
import subprocess
import pyfiglet
import stdiomask
import cryptocode
from colorama import Fore
class Main:
    def __init__(self):
        self.start_program = True
        while self.start_program == True:
            self.init()
    def init(self):
        try:
            self.command_input = input("\nMetros-mde> ")
            if self.command_input.replace(" ", "") != "":
                self.command_input_split = shlex.split(self.command_input)
                try:
                    self.command()
                except IndexError:
                    self.indexeror_()
        except KeyboardInterrupt:
            self.start_program = False
            print("\t")
        except EOFError:
            pass
    def command(self):
        if (
            str(self.command_input_split[0]).lower() == "help"
            or str(self.command_input_split[0]).lower() == "/?"
            or str(self.command_input_split[0]).lower() == "?"
        ):
            print("\nAll the commands:")
            print(
                "\t• file -d, --decrypt — Decrypt the contents of the file by password."
            )
            print(
                "\t• file -e, --encrypt — Encrypt the contents of the file with a password."
            )
            print("\t• hash               — Output of encrypted text.")
            print("\t• cls, clear, clean  — Screen cleaning.")
            print("\t• exit, quit, ^C     — Exit from the program.")
            print("\t• $cmd               — Executing a console command.")
            print("\t• help, /?, ?        — Displaying a list of program commands.")
            print("Syntax:")
            print("\tfile <parameter>")
            print("\thash <filename>")
            print("\t<command> <parameter>")
            print(
                "\n{}[*]{} To display command help, enter only the name of the command.".format(
                    Fore.BLUE, Fore.WHITE
                )
            )
        if str(self.command_input_split[0]).lower() == "$cmd":
            os.system(self.command_input.replace("$cmd", ""))
        if (
            str(self.command_input_split[0]).lower() == "exit"
            or str(self.command_input_split[0]).lower() == "quit"
            or str(self.command_input_split[0]).lower() == "^c"
        ):
            self.start_program = False
        if (
            str(self.command_input_split[0]).lower() == "cls"
            or str(self.command_input_split[0]).lower() == "clear"
            or str(self.command_input_split[0]).lower() == "clean"
        ):
            try:
                subprocess.call("cls")
            except:
                subprocess.call("clear")
        if (
            str(self.command_input_split[0]).lower() == "exit"
            or str(self.command_input_split[0]).lower() == "quit"
            or str(self.command_input_split[0]).lower() == "^C"
        ):
            self.start_program = False
        if (
            str(self.command_input_split[0]).lower() == "file"
            and str(self.command_input_split[1]).lower() == "--encrypt"
            or str(self.command_input_split[1]).lower() == "-e"
        ):
            file_name = input("Metros-mde> [File name]: ")
            if file_name.replace(" ", "") != "":
                if os.path.isfile(file_name) == True:
                    password = stdiomask.getpass(
                        prompt="Metros-mde> [Password]:  ", mask="*"
                    )
                    try:
                        result_file = cryptocode.encrypt(
                            open(file_name, encoding="utf-8", errors="ignore").read(),
                            password,
                        )
                        file = open(file_name, "w+")
                        file.write(result_file)
                        file.close()
                        print("\n{}[+] Succeeded!{}".format(Fore.GREEN, Fore.WHITE))
                    except Exception as error:
                        print(error)
                elif os.path.isfile(file_name) == False:
                    print(
                        "\n{}[!] The file could not be found: {}!{}".format(
                            Fore.RED, file_name, Fore.WHITE
                        )
                    )
        if (
            str(self.command_input_split[0]).lower() == "file"
            and str(self.command_input_split[1]).lower() == "--decrypt"
            or str(self.command_input_split[1]).lower() == "-d"
        ):
            file_name = input("Metros-mde> [File name]: ")
            if file_name.replace(" ", "") != "":
                if os.path.isfile(file_name) == True:
                    password = stdiomask.getpass(
                        prompt="Metros-mde> [Password]:  ", mask="*"
                    )
                    try:
                        result_file = cryptocode.decrypt(
                            open(file_name, encoding="utf-8", errors="ignore").read(),
                            password,
                        )
                        print(result_file)
                        print(
                            "\n{}[*]{} File name: {}".format(
                                Fore.BLUE, Fore.WHITE, file_name
                            )
                        )
                    except Exception as error:
                        print(error)
                elif os.path.isfile(file_name) == False:
                    print(
                        "\n{}[!] The file could not be found: {}!{}".format(
                            Fore.RED, file_name, Fore.WHITE
                        )
                    )
        if str(self.command_input_split[0]).lower() == "hash":
            if str(self.command_input_split[0]).replace(" ", "") != "":
                file_name = str(self.command_input_split[1])
                if file_name.replace(" ", "") != "":
                    if os.path.isfile(file_name) == True:
                        password = stdiomask.getpass(
                            prompt="Metros-mde> [Password]:  ", mask="*"
                        )
                        try:
                            result_file = cryptocode.encrypt(
                                open(
                                    file_name, encoding="utf-8", errors="ignore"
                                ).read(),
                                password,
                            )
                            print(result_file)
                        except Exception as error:
                            print(error)
                    elif os.path.isfile(file_name) == False:
                        print(
                            "\n{}[!] The file could not be found: {}!{}".format(
                                Fore.RED, file_name, Fore.WHITE
                            )
                        )
    def indexeror_(self):
        if str(self.command_input_split[0]).lower() == "file":
            print("file — Command to encrypt files.")
            print("Parameters:")
            print("\t-d, --decrypt — Decrypt the contents of the file by password.")
            print("\t-e, --encrypt — Dncrypt the contents of the file with a password.")
            print("Syntax:")
            print("\tfile <parameter>")
        if str(self.command_input_split[0]).lower() == "hash":
            print("hash — Output of encrypted text.")
            print("Syntax:")
            print("\thash <filename>")
class Boot:
    def __init__(self):
        os.system("clear")
        print(Fore.BLUE + pyfiglet.figlet_format("Metros Data Encryption") + Fore.WHITE)
        print(
            "{}[*]{} Metros Data Encryption [version 1.0] 2022.".format(
                Fore.BLUE, Fore.WHITE
            )
        )
        print(
            "\n{}[*]{} Detailed information on the website: metros-software.ru".format(
                Fore.BLUE, Fore.WHITE
            )
        )
        print(
            "{}[*]{} Technical support metros:            metrostechnicalsupp0rt@gmail.com".format(
                Fore.BLUE, Fore.WHITE
            )
        )
        Main()
        print("\n{}[*]{} Completing Metros Data Encryption...\n")
if __name__ == "__main__":
    try:
        if sys.argv[1] == "--version" or sys.argv[1] == "-v":
            print(
                "{}[*]{} Metros Data Encryption [version 1.0] 2022.".format(
                    Fore.BLUE, Fore.WHITE
                )
            )
        if sys.argv[1] == "--clear":
            try:
                subprocess.call("cls")
            except:
                subprocess.call("clear")
            Boot()
    except:
        Boot()
