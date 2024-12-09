import platform, os, sys
import time, re
from colorama import Fore, Back, Style
import urllib.request as urec
import subprocess

def ask_yes_no(question):
    while True:
        answer = input(f"{question} [Y/N]: ").strip().lower()
        if answer in ['y', 'yes']:
            return True
        elif answer in ['n', 'no']:
            return False
        else:
            print("Por favor, responde con 'Y' o 'N'.")




class main:
    def __init__(self):
        self.system = self.osDetector()
        self.connection = self.check_connection()
        self.permittedOS = self.test(self)

    @staticmethod
    def check_connection():
        url=[]
        try:
            urec.urlopen("https://www.github.com")
            return True
        except:
            return False

    @staticmethod
    def osDetector():
        system_operation = platform.system()
        
        if "PREFIX" in os.environ and os.path.exists("/data/data/com.termux"):
            return "Termux"
        elif system_operation == "Linux":
            if "ANDROID_ARGUMENT" in os.environ:
                return "Android"
            else:
                return "Linux"
        elif system_operation == "Windows":
            return "Windows"
        elif system_operation == "Darwin":
            return "Mac"
        else:
            return "Unknown"

    @staticmethod
    def test(self):
        system=self.system
        connection=self.connection
        notAllowed=["a","Windows","Darwin","Android","Unknown"]
        permittedSystem=["Linux", "Termux"]
        if system in notAllowed:
            return False
        elif system in permittedSystem:
            if connection == True:
#                print(Fore.GREEN + "[*]", Fore.RESET + "The device has internet access.")
                return True
            else:
                return "No internet access"

    def launcher(self):
        permittedOS = self.permittedOS
        dvc=False
        if permittedOS == True:
            dvc=True
            try:
                while dvc:
                    option = {0: "00", 1: "01", 2: "02", 3: "03", 4: "04", 5: "05", 6: "06"}
                    subprocess.run("clear", shell=True)
                    print(f"{Fore.GREEN}Multi-Tool CLI{Style.RESET_ALL}")
                    print(f"{Fore.WHITE}[01]. {Fore.CYAN}Gestión de Archivos{Style.RESET_ALL}")
                    print(f"{Fore.WHITE}[02]. {Fore.CYAN}Monitoreo del Sistema{Style.RESET_ALL}")
                    print(f"{Fore.WHITE}[03]. {Fore.CYAN}Descarga de Contenido{Style.RESET_ALL}")
                    print(f"{Fore.WHITE}[04]. {Fore.CYAN}Automatización de Tareas{Style.RESET_ALL}")
                    print(f"{Fore.WHITE}[05]. {Fore.CYAN}Seguridad y Privacidad{Style.RESET_ALL}")
                    print(f"{Fore.WHITE}[00]. {Fore.RED}Salir{Style.RESET_ALL}")
                    put=input("> ")

                    # Validar la entrada
                    if put.isdigit() and int(put) in option:
                        # Si la opción es 0, salir del programa
                        if put == "0" or option[0]:
                            subprocess.run("clear", shell=True)
                            print(Fore.GREEN + "\n[*]", Fore.RESET + "Programme stopped.")
                            sys.exit()
                    elif put.strip() == "":
                        print(Fore.YELLOW + "[!]", Fore.RESET + "No input detected. Please select an option.")
                        time.sleep(0.5)
                    elif re.fullmatch(r'^\s*$', put):
                        print(Fore.YELLOW + "[!]", Fore.RESET + "Only spaces detected. Please select an option.")
                        time.sleep(0.5)
                    elif not re.fullmatch(r'^\d+$', put):
                        print(Fore.YELLOW + "[!]", Fore.RESET + "Invalid characters or symbols detected. Please enter a valid option.")
                        time.sleep(1)
                    else:
                        # Mostrar mensaje de error si la opción no es válida
                        print(Fore.RED + "[!]", Fore.RESET + "Invalid option.")
                        time.sleep(1.5)
            except KeyboardInterrupt:
                subprocess.run("clear", shell=True)
                print(Fore.GREEN + "\n[*]", Fore.RESET + "Programme stopped.")
                sys.exit()
        elif permittedOS == False:
            print(Fore.RED + "[!]", Fore.RESET + "Your system is not compatible.")
            sys.exit()
        elif permittedOS == "No internet access":
            # Todavía no hay un launcher programado para "sin conexión a internet".
            print(Fore.RED + "[!]", Fore.RESET + "Your device does not have internet access.")
            sys.exit()

if __name__ == "__main__":
    apps=main()
    apps.launcher()