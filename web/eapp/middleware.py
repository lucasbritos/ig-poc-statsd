from django.conf import settings
import statsd
import time
stats = statsd.StatsClient(settings.STATSD_HOST, settings.STATSD_PORT)


class StatsdMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        _time_ti = time.perf_counter()

        response = self.get_response(request)

        _time_tf = time.perf_counter()
        enlapsed = _time_tf - _time_ti
        stats_tags={
            'stage': settings.STAGE,
            'method': request.method,
            'user_agent': request.META['HTTP_USER_AGENT'],
            "status_code": response.status_code
            }
        stats.timing('request', enlapsed, tags=stats_tags)

        return response
