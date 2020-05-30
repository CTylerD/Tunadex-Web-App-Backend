#!/bin/bash

export AUTH0_DOMAIN = 'fsndctd.auth0.com'
export ID = 'Zoc9u7K16ZxVQs6pfwBpVe26Ou5XLrSi'
export ALGORITHMS = ['RS256']
export API_AUDIENCE = 'tunadex'
export AUTH0_CLIENT_SECRET = 'SsuHNdwLxK954-T2GcZpyAm5xX0GmIQxcGuW3CZskgrSSfWr7h_yCc24d9CHhLAa'
export DATABASE_URL = ('postgresql://wdspwndlbhdcvj:d09f9e19edf9fb71d9879d37bd'
                      'e38c70415ba6a65a58dd695d3a7e075c2d1617@ec2-35-171-31-3'
                      '3.compute-1.amazonaws.com:5432/d3ib0ohrcrh0lh')

export TEACHER_TOKEN='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlFUaERNVVpFTmtWQk0wSTBNRGRFTnpSRU56Y3dNMFl3UXpRM09UaEdSamN5TnpkRVJUa3lSZyJ9.eyJpc3MiOiJodHRwczovL2ZzbmRjdGQuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlNmRmZTlkMTA4ODViMGNhNmE5YzYwYyIsImF1ZCI6InR1bmFkZXgiLCJpYXQiOjE1OTA4NjQyNzksImV4cCI6MTU5MDk1MDY3OSwiYXpwIjoiV0pzQTdSc0dDbEZoOTV4ZG1JMFE3UjJ5SXk3OFFISGYiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTpzZXRsaXN0IiwiZGVsZXRlOnR1bmVzIiwiZ2V0OnNldGxpc3QiLCJnZXQ6dHVuZXMiLCJwYXRjaDpzZXRsaXN0IiwicGF0Y2g6dHVuZXMiLCJwb3N0OnNldGxpc3QiLCJwb3N0OnR1bmVzIl19.KReJOWxzzRawoYm52sRr69TdwQFwn97Jeo_C0DdHhHsg4ha22Ak-FHLoIrIYUy5gp2YxQaQ69gxQOjmnoSlY4_hwfZjSfEXdzcU3WjhGD94G3t2LbuH1E1uBcZU7acw2Dp2naE0IscMqEdmncSxBRd1Dsle6rawkz_vEKISo-EqYTdD-YeWSusouEEeVZx8sRxh7PAdUXfIG533bZEdSUTxf52vtmI5ZsRnYLQzhqdwzM8fdtCtVcj7lUXKvzBTAxt-hwMlLptaiE1Nw4xzGAUigxuGiFkY4vY30TOE3h8rjCcErQH8-r1W1EYZioq6b7sgLqWxdTkJ61x5paDFlHA'

teacher_auth_header = {
    'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlFUaERNVVpFTmtWQk0wSTBNRGRFTnpSRU56Y3dNMFl3UXpRM09UaEdSamN5TnpkRVJUa3lSZyJ9.eyJpc3MiOiJodHRwczovL2ZzbmRjdGQuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlNmRmZTlkMTA4ODViMGNhNmE5YzYwYyIsImF1ZCI6InR1bmFkZXgiLCJpYXQiOjE1OTA4NjQyNzksImV4cCI6MTU5MDk1MDY3OSwiYXpwIjoiV0pzQTdSc0dDbEZoOTV4ZG1JMFE3UjJ5SXk3OFFISGYiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTpzZXRsaXN0IiwiZGVsZXRlOnR1bmVzIiwiZ2V0OnNldGxpc3QiLCJnZXQ6dHVuZXMiLCJwYXRjaDpzZXRsaXN0IiwicGF0Y2g6dHVuZXMiLCJwb3N0OnNldGxpc3QiLCJwb3N0OnR1bmVzIl19.KReJOWxzzRawoYm52sRr69TdwQFwn97Jeo_C0DdHhHsg4ha22Ak-FHLoIrIYUy5gp2YxQaQ69gxQOjmnoSlY4_hwfZjSfEXdzcU3WjhGD94G3t2LbuH1E1uBcZU7acw2Dp2naE0IscMqEdmncSxBRd1Dsle6rawkz_vEKISo-EqYTdD-YeWSusouEEeVZx8sRxh7PAdUXfIG533bZEdSUTxf52vtmI5ZsRnYLQzhqdwzM8fdtCtVcj7lUXKvzBTAxt-hwMlLptaiE1Nw4xzGAUigxuGiFkY4vY30TOE3h8rjCcErQH8-r1W1EYZioq6b7sgLqWxdTkJ61x5paDFlHA'
}

student_auth_header = {
    'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlFUaERNVVpFTmtWQk0wSTBNRGRFTnpSRU56Y3dNMFl3UXpRM09UaEdSamN5TnpkRVJUa3lSZyJ9.eyJpc3MiOiJodHRwczovL2ZzbmRjdGQuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlYzZlYzE0ZDY2ZTFjMGJmNDUzMGM4ZSIsImF1ZCI6InR1bmFkZXgiLCJpYXQiOjE1OTA4NjQxODEsImV4cCI6MTU5MDk1MDU4MSwiYXpwIjoiV0pzQTdSc0dDbEZoOTV4ZG1JMFE3UjJ5SXk3OFFISGYiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDpzZXRsaXN0IiwiZ2V0OnR1bmVzIl19.hijClFAtRnd6jrM7xSTDhFWvllgYjnCj11YExK-PQzWclpTLr4VwM3Ixxy58oiwZdoXjw5Pw1TN4U_2xoKQRSFX7KiXL9q4M9EzgSOGy2jFWa3_z_3Lj1EHed0NQq-9Z2av84VJj9mf67jN2z_62qHZVHtePFqUI8mjCHfW9ZYVkKgnd3u2mi_n1hxDpms_DB6fA1DCLPI5JfOJwMgsUyNiKs4igFnD4xs_CTIA5mWiqOB1cUklE0m0uHc9-LSlJ5TM03WJ99bRFtfhPv0mIOw9BKotWAldZugyAobSAyD2BTp8jq2_Dr1CEeq5abSNHraQgfXbqTLvRi_HN_ZzpNA'
}