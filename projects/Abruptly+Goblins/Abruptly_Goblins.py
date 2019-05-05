game = "Abruptly Goblins!"
gamers = []


def add_gamer(gamer, gamers_list):
    if gamer.get("name") and gamer.get("availability"):
        gamers_list.append(gamer)
    else:
        print("Gamer missing critical information")


kimberly = {'name': 'Kimberly Warner', 'availability': ['Monday', 'Tuesday', 'Friday']}
add_gamer(kimberly, gamers)

add_gamer({'name': 'Thomas Nelson', 'availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joyce Sellers', 'availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name': 'Michelle Reyes','availability': ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name': 'Stephen Adams', 'availability': ["Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, gamers)
add_gamer({'name': 'Latasha Bryan', 'availability': ["Monday", "Sunday"]}, gamers)
add_gamer({'name': 'Crystal Brewer', 'availability': ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name': 'James Barnes Jr.', 'availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name': 'Michel Trujillo', 'availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)

print(gamers)


def build_daily_frequency_table():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    values = [0, 0, 0, 0, 0, 0, 0]
    zipped_days = zip(days, values)
    days_dict = {key:value for key, value in zipped_days}
    return days_dict


count_availability = build_daily_frequency_table()

print(count_availability)


def calculate_availability(gamers_list, available_frequency):
    for gamer in gamers_list:
        for day in gamer["availability"]:
            available_frequency[day] += 1


calculate_availability(gamers, count_availability)
print(count_availability)


def find_best_night(availability_table):
    max = 0
    for key, value in availability_table.items():
        if value > max:
            best_day = key
            max = value
    return best_day


game_night = find_best_night(count_availability)

print(game_night)


def available_on_night(gamers_list, day):
    # list comprehension equivalent:
    # return [gamer for gamer in gamers_list if day in gamer['availability']]
    total_people = []
    for gamer in gamers_list:
        if day in gamer['availability']:
            if gamer not in total_people:
                total_people.append(gamer)
    return total_people


attending_game_night = available_on_night(gamers, game_night)
print(attending_game_night)

form_email = """
Dearest {name}, 

Heroes & Fantasy is proud to host {game} night!
 
We shall converge on {day_of_week} of this week,
and look forward to adventuring together!

Sincerely, 
Game Master
"""


def send_email(gamers_who_can_attend, day, game):
    for gamer in gamers_who_can_attend:
        print(form_email.format(name=gamer['name'], day_of_week=day, game=game))


send_email(attending_game_night, game_night, "Abruptly Goblins!")


unable_to_attend_best_night = [gamer for gamer in gamers if not gamer in attending_game_night]

second_night_availability = build_daily_frequency_table()
calculate_availability(unable_to_attend_best_night, second_night_availability)
second_night = find_best_night(second_night_availability)
print(second_night)

available_second_game_night = available_on_night(gamers, second_night)
send_email(available_second_game_night, second_night, "Abruptly Goblins!")

