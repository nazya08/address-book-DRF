import logging

from django.http import HttpResponse
from django.utils import timezone


logger = logging.getLogger(__name__)


class DDOSProtectionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.ip_access_count = {}
        self.request_window = 5 * 60  # 5 хвилин (в секундах)

    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR')
        current_time = timezone.now().timestamp()

        # Видаляємо старі записи про запити
        for ip_address, access_info in list(self.ip_access_count.items()):
            if current_time - access_info['timestamp'] > self.request_window:
                del self.ip_access_count[ip_address]

        # Оновлюємо кількість запитів для даної IP-адреси
        if ip not in self.ip_access_count:
            self.ip_access_count[ip] = {'count': 1, 'timestamp': current_time}
        else:
            self.ip_access_count[ip]['count'] += 1

        # Перевіряємо, чи кількість запитів не перевищує ліміт за часовий проміжок
        if self.ip_access_count[ip]['count'] > 100:
            logger.warning(f"Too many requests from {ip}")
            return HttpResponse("Too many requests", status=429)

        # Викликаємо наступний обробник запиту
        response = self.get_response(request)
        return response
