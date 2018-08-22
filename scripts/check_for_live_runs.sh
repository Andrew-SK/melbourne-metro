curl 'http://timetableapi.ptv.vic.gov.au/v3/runs/route/9?devid=1000679&signature=3058750FECD5ED3207B4A07BEEF193F53703EB7A' | json_pp | rg 'vehicle_(descriptor|position)' | rg -v 'null'

