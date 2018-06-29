# BirthdayCountdown.py
import datetime
import turtle
import random
from alphabet import alphabet

pen = turtle.Turtle()
turtle.hideturtle()
pen.speed(0)
turtle.bgcolor('#000000')
pen.pensize(2)


def write_birthday_message(message, font_size, color, x, y, character_spacing, name):
    pen.color(color)
    message = message.upper()

    for character in message:
        if character in alphabet:
            letter = alphabet[character]
            pen.penup()
            for dot in letter:
                pen.goto(x + dot[0] * font_size, y + dot[1] * font_size)
                pen.pendown()

            x += font_size

        if character == " ":
            x += font_size
        x += character_spacing
    turtle.exitonclick()


def birthday_from_user():
    print('When is your birthday? ')
    year = int(input('Year (YYYY): '))
    month = int(input('Month (MM): '))
    day = int(input('Day (DD): '))

    bday = datetime.date(year, month, day)
    return bday

def days_between(original_date, target_date):
    current_year = datetime.date(target_date.year, original_date.month, original_date.day)
    dt = current_year - target_date
    return dt.days


def birthday_info_print(days, name):
    font_size = 30
    character_spacing = 5
    font_color = '#FFFFFF'
    message = f"Happy Birthday {name}"

    if days < 0:
        print(f"Your birthday was {-days} days ago this year")
    elif days > 0:
        print(f"Your birthday is in {days} days!")
    else:
        print('Happy birthday! Here is your personal birthday card: ')
        write_birthday_message(message, font_size, font_color, -190, 0, character_spacing, name)

def main():
    name = input("What is your name? ")
    birthday = birthday_from_user()
    today = datetime.date.today()
    number_of_days = days_between(birthday, today)
    birthday_info_print(number_of_days, name)


main()