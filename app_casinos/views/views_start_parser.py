from __future__ import annotations

# import os
import subprocess
# import sys
import threading
# from django.utils import timezone
from django.http import JsonResponse
from django.views import View

from app_casinos.models.state_program import StateProgram
# from app_casinos.Tools import toolbox


def is_program_running(name):
    try:
        state = StateProgram.objects.get(name=name)
        return state.data.get('running', False), state
    except StateProgram.DoesNotExist:
        return False, None


def set_program_state(name, running, additional_data = None) -> StateProgram:
    defaults = {'data': {'running': running, 'additional_data': additional_data} }
    state, created = StateProgram.objects.update_or_create(name=name, defaults=defaults)
    return state


def run_subprocess():
    try:
        # Определение абсолютного пути к скрипту worker.py
        # script_path = os.path.abspath('worker.py')
        script_path = '/home/pavelpc/PycharmProjects/Working_Projects/Casinoguru/pars_data/main.py'
        # Определение абсолютного пути к Интерпретатору
        # python_executable = sys.executable
        python_executable = '/home/pavelpc/PycharmProjects/Working_Projects/Casinoguru/env-python/bin/python3'

        # Запуск worker.py в отдельном процессе с параметрами для повышения производительности и безопасности
        result = subprocess.run(
            # python_executable - путь к интерпретатору Python, script_path - путь к скрипту
            [python_executable, script_path],
            capture_output=True,  # Захватывает stdout и stderr, что позволяет обрабатывать их позже
            text=True,  # Декодирует байты в строки, упрощая обработку вывода
            stdin=subprocess.DEVNULL,  # Отключает стандартный ввод для дочернего процесса
            timeout=120  # Ограничивает время выполнения процесса до 60 секунд
        )

        # Обработка результата выполнения скрипта
        if result.returncode != 0:
            # Если процесс завершился с ошибкой, выбрасываем исключение с сообщением об ошибке
            raise Exception(result.stderr.strip())
        else:
            # Если процесс завершился успешно, выводим стандартный вывод
            print(result.stdout.strip())
    except subprocess.TimeoutExpired:
        # Обработка случая, когда процесс превышает время выполнения
        raise TypeError("TimeoutExpired: The worker process timed out.")
    except Exception as e:
        # Обработка других исключений, возникших при выполнении
        raise TypeError(e)


def program_logic(name: str):
    error = None
    # Ваш код запуска программы здесь
    print(f"\nПрограмма запущена")
    try:
        set_program_state(name, True)
        run_subprocess()
        print(f"Программа завершена")
        set_program_state(name, False)
    except Exception as err:
        error = str(err)
    finally:
        state = set_program_state(name, running=False, additional_data={"program_logic_error": error})
        print(f"\nFinally State: {state.data}")


def start_program(name, state: StateProgram):
    thread = threading.Thread(target=program_logic, args=(name, ))
    thread.start()


class ParserView(View):
    name_program = 'pars_casinoguru'

    def get(self, request, *args, **kwargs):
        is_running, state = is_program_running(self.name_program)

        if not is_running:
            start_program(self.name_program, state)
            message = 'The data collection program has been started!'
        else:
            message = 'The data collection program is already running!'

        data = {
            'message': message,
            'status': 'success',
            'program_name': self.name_program,
            'is_running': is_running,
            'start_time': state.start_time if state else None
        }

        return JsonResponse(data)
