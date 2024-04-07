import pyautogui
import psutil
from platform import system

#indica el sistema operativo que se está usando
system_ = system()

def change_language():
    #pyautogui.sleep(1)
    pyautogui.keyDown('win')
    pyautogui.press('space')
    pyautogui.keyUp('win')

def get_process(platform='Windows'):
    proc_system = 'Code.exe' if platform == 'Windows' else 'code'
    process = psutil.process_iter()
    for proc in process:
        if proc.name() == proc_system:
            change_language()
            break
    else:
        change_language()

def main():
    get_process(system_)

if __name__ == '__main__':
    main()


