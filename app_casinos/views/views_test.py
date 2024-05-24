import json
from django.http import HttpRequest, JsonResponse


def get_data(request: HttpRequest):
    if request.method == 'POST':
        try:
            json_data = json.loads(request.body)
            print(f"\nJson Data Client: {json_data}")
            # Делаем что-то с полученными данными, например, сохраняем их в базу данных или обрабатываем как-то ещё.

            # Возвращаем ответ в формате JSON
            return JsonResponse({'success': True, 'message': 'Данные успешно получены и обработаны'})
        except json.JSONDecodeError as e:
            # Возвращаем ошибку, если JSON не удалось распарсить
            return JsonResponse(
                {'success': False, 'error': 'Ошибка при разборе JSON данных: {}'.format(str(e))}, status=400)
    else:
        # Если метод запроса не POST, возвращаем ошибку "Метод не разрешен"
        return JsonResponse({'success': False, 'error': 'Метод не разрешен'}, status=405)


