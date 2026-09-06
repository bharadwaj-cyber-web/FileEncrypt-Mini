from colorama import Fore,init

init(autoreset=True)



def banner() -> None:
    """
    Display the application banner.

    Shows the title of the File Encryption Tool
    when the program starts.
    """
    print(Fore.CYAN + "=" * 45)
    print(Fore.CYAN + "      FILE ENCRYPTION TOOL")
    print(Fore.CYAN + "=" * 45)

def success(message: str) -> None:
    """
    Display a success message.

    Args:
        message: The success message to display.
    """
    print(Fore.GREEN + f"{message}")

def error(message: str) -> None:
    """
    Display an error message.

    Args:
        message: The error message to display.
    """
    print(Fore.RED + f"{message}")

def warning(message: str) -> None:
    """
    Display a warning message.

    Args:
        message: The warning message to display.
    """
    print(Fore.YELLOW + f"{message}")

def info(message: str) -> None:
    """
    Display an informational message.

    Args:
        message: The information message to display.
    """
    print(Fore.BLUE + message)