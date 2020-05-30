curl -H "Content-Type: application/json" -H "Authorization: Bearer $TEACHER_TOKEN" https://tunadex.herokuapp.com/tunes/

curl -H "Content-Type: application/json" -H "Authorization: Bearer $TEACHER_TOKEN" https://tunadex.herokuapp.com/tunes/1/

curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer $TEACHER_TOKEN" -d '{"title": "Footprints", "composer": "Wayne Shorter", "key": "C Minor", "mastery": 5}' https://tunadex.herokuapp.com/tunes/

curl -X PATCH -H "Content-Type: application/json" -H "Authorization: Bearer $TEACHER_TOKEN" -d '{"mastery": 5}' https://tunadex.herokuapp.com/tunes/5/

curl -X DELETE -H "Content-Type: application/json" -H "Authorization: Bearer $TEACHER_TOKEN" https://tunadex-dev.herokuapp.com/tunes/2