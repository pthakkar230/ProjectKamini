import random
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-n", dest="number", action="store", help="phone number", default="0")
args = parser.parse_args()
phone_number = args.number

# Add phrases here
phrases = [
    "HEY THERE",
    "MY GIRL",
    "LOVE YOU MOM",
    "ITS ALL GOOD",
    "AYYY!"
]
file_path = os.path.realpath(__file__)
file_path = fp.split(os.path.basename(__file__))[0]
bashCommand = 'osascript {}/sendMessage.applescript {} "Greetings from Project Kamini! You have subscribed to our stuff. Message: {}. Send STOP to cancel subscription. Just kidding, that will not work."'.format(
    file_path, phone_number, random.choice(phrases)
)
os.system(bashCommand)
