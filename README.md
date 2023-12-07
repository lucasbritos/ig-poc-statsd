# POC: Using statsd with Django

## Compose services

* web: Minimal Django application on port 8000 http://localhost:8000/helloworld/
* telegraf: Simulates a local agent, listening port UDP 8125 for statsd
* influxdb & grafana: Monitoring stack http://localhost:3000 **(This could be replaced by New Relic, Datadog, Cloudwatch etc)**


## Metrics collected:

* Custom gauge metric on /helloworld/:  web/eapp/views.py
```
stats.gauge("parameter", n , tags={'view':'hello_world'})
```
* Request statistic, class StatsdMiddleware, web/eapp/middleware.py

```
stats_tags={
    'stage': settings.STAGE,
    'method': request.method,
    'user_agent': request.META['HTTP_USER_AGENT'],
    "status_code": response.status_code
    }
stats.timing('request', enlapsed, tags=stats_tags)

```

## Steps:

1. ```docker-compose up -d```
2. Load InfluxDB datasource to grafana: http://influxdb:8086
3. Load Grafana dashboards JSONs in grafana/dashboards folder
4. Run traffic generator to have some metrics on dashboards:

```
./generate_traffic.sh
```
