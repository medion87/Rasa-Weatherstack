## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## bot challenge
* bot_challenge
  - utter_iamabot

## Weather
* weather_location
  - actions.weatherapi
## interactive_story_1
* greet
    - utter_greet
* weather_location{"location": "Thailand"}
    - slot{"location": "Thailand"}
    - actions.weatherapi
* affirm
    - utter_happy
* goodbye
    - utter_goodbye

## interactive_story_2
* greet
    - utter_greet
* mood_great
    - utter_happy
* weather_location{"location": "New York"}
    - slot{"location": "New York"}
    - actions.weatherapi
* mood_great
    - utter_happy
* goodbye
    - utter_goodbye

## interactive_story_3
* weather_location{"location": "Japan"}
    - slot{"location": "Japan"}
    - actions.weatherapi
* mood_great
    - utter_happy
