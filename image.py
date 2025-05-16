# # name = 'python'
# #
# # if name == 'java' 'HTML' or 'CSS':
# #     print("Login successful")
# # else:
# #     print("Not valid")
#
# # n = 5
# # for i in range(n+1):
# #     for j in range(2*n-1):
# #         print(" ", end="")
# #     for j in range(i):
# #         print("*", end="")
# #     print()
#
# # a = [1, 2, 3]  #a and b point to the same list [1, 2, 3]
# # b = a,
# # a = a * 2 #multiply a list by a number, it concatenates the
# # # list with itself that number of times
# # print(b)
# #
# # from PIL import Image
# #
# # # https://t.me/LearnPython3
# #
# # in_img = 'piyush.jpg'
# # out_img = 'grayscale.jpg'
# #
# # # Open the image
# # with Image.open(in_img) as img:
# #     # Convert the image to grayscale
# #     grayscale_img = img.convert('L')
# #     # Save the grayscale image
# #     grayscale_img.save(out_img)
# # import os
# # import google.generativeai as genai
# # import tkinter as tk
# # from tkinter import scrolledtext
# #
# # # Configure the API key
# # genai.configure(api_key='AIzaSyBPaN_ah9RkuxKFe9hRUrl7Ko1-1-l1svA')
# #
# # # Create the model
# # generation_config = {
# #     "temperature": 1,
# #     "top_p": 0.95,
# #     "top_k": 64,
# #     "max_output_tokens": 8192,
# #     "response_mime_type": "text/plain",
# # }
# # safety_settings = [
# #     {
# #         "category": "HARM_CATEGORY_HARASSMENT",
# #         "threshold": "BLOCK_MEDIUM_AND_ABOVE",
# #     },
# #     {
# #         "category": "HARM_CATEGORY_HATE_SPEECH",
# #         "threshold": "BLOCK_MEDIUM_AND_ABOVE",
# #     },
# #     {
# #         "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
# #         "threshold": "BLOCK_MEDIUM_AND_ABOVE",
# #     },
# #     {
# #         "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
# #         "threshold": "BLOCK_MEDIUM_AND_ABOVE",
# #     },
# # ]
# #
# # model = genai.GenerativeModel(
# #     model_name="gemini-1.5-flash",
# #     safety_settings=safety_settings,
# #     generation_config=generation_config,
# # )
# #
# # chat_session = model.start_chat(history=[])
# #
# #
# # # Define the GUI application
# # class ChatBotApp:
# #     def _init_(self, root):
# #         self.root = root
# #         self.root.title("Generative AI Chatbot")
# #
# #         # Chat history text area
# #         self.chat_history = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, state='disabled', width=80, height=20)
# #         self.chat_history.grid(column=0, row=0, padx=10, pady=10, columnspan=2)
# #
# #         # User input entry
# #         self.user_input = tk.Entry(self.root, width=60)
# #         self.user_input.grid(column=0, row=1, padx=10, pady=10)
# #         self.user_input.bind("<Return>", self.send_message)
# #
# #         # Send button
# #         self.send_button = tk.Button(self.root, text="Send", command=self.send_message)
# #         self.send_button.grid(column=1, row=1, padx=10, pady=10)
# #
# #     def send_message(self, event=None):
# #         user_message = self.user_input.get()
# #         if user_message.strip():
# #             self.display_message("You", user_message)
# #             self.user_input.delete(0, tk.END)
# #
# #             response = chat_session.send_message(user_message)
# #             self.display_message("Bot", response.text)
# #
# #     def display_message(self, sender, message):
# #         self.chat_history.config(state='normal')
# #         self.chat_history.insert(tk.END, f"{sender}: {message}\n")
# #         self.chat_history.yview(tk.END)
# #         self.chat_history.config(state='disabled')
# #
# #
# # # Create the main window
# # root = tk.Tk()
# # app = ChatBotApp()
# # root.mainloop()
# # from tkinter import Label, Tk
# # import time
# # app_window = Tk()
# # app_window.title("Digital Clock")
# # app_window.geometry("420x150")
# # app_window.resizable(1,1)
# #
# # text_font= ("Boulder", 68, 'bold')
# # background = "#f2e750"
# # foreground= "#363529"
# # border_width = 25
# #
# # label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width)
# # label.grid(row=0, column=1)
# #
# # def digital_clock():
# #    time_live = time.strftime("%H:%M:%S")
# #    label.config(text=time_live)
# #    label.after(200, digital_clock)
# #
# # digital_clock()
# # app_window.mainloop()
# from bs4 import BeautifulSoup
# import requests
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
#
#
# def weather(city):
#     city = city.replace(" ", "+")
#     res = requests.get(
#         f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8',
#         headers=headers)
#     print("Searching in google......\n")
#     soup = BeautifulSoup(res.text, 'html.parser')
#     location = soup.select('#wob_loc')[0].getText().strip()
#     time = soup.select('#wob_dts')[0].getText().strip()
#     info = soup.select('#wob_dc')[0].getText().strip()
#     weather = soup.select('#wob_tm')[0].getText().strip()
#     print(location)
#     print(time)
#     print(info)
#     print(weather + "°C")
#
#
# print("enter the city name")
# city = input()
# city = city + " weather"
# weather(city)
# from datetime import datetime
# from playsound import playsound
# alarm_time = input("Enter the time of alarm to be set:HH:MM:SS\n")
# alarm_hour=alarm_time[0:2]
# alarm_minute=alarm_time[3:5]
# alarm_seconds=alarm_time[6:8]
# alarm_period = alarm_time[9:11].upper()
# print("Setting up alarm..")
# while True:
#     now = datetime.now()
#     current_hour = now.strftime("%I")
#     current_minute = now.strftime("%M")
#     current_seconds = now.strftime("%S")
#     current_period = now.strftime("%p")
#     if(alarm_period==current_period):
#         if(alarm_hour==current_hour):
#             if(alarm_minute==current_minute):
#                 if(alarm_seconds==current_seconds):
#                     print("Wake Up!")
#                     playsound('audio.mp3')
#                     break
# def check_guess(guess, answer):
#     global score
#     still_guessing = True
#     attempt = 0
#     while still_guessing and attempt < 3:
#         if guess.lower() == answer.lower():
#             print("Correct Answer")
#             score = score + 1
#             still_guessing = False
#         else:
#             if attempt < 2:
#                 guess = input("Sorry Wrong Answer, try again")
#             attempt = attempt + 1
#     if attempt == 3:
#         print("The Correct answer is ", answer)
#
#
# score = 0
# print("Guess the Animal")
# guess1 = input("Which bear lives at the North Pole? ")
# check_guess(guess1, "polar bear")
# guess2 = input("Which is the fastest land animal? ")
# check_guess(guess2, "Cheetah")
# guess3 = input("Which is the larget animal? ")
# check_guess(guess3, "Blue Whale")
# guess3 = input("who is the winner of IPL 2015? ")
# check_guess(guess3, "Mumbai Indians")
# print("Your Score is " + str(score))
import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Snake initial position and properties
snake_block = 10
snake_speed = 15
x1 = screen_width / 2
y1 = screen_height / 2
x1_change = 0
y1_change = 0
snake_list = []
snake_length = 1

# Food initial position and properties
foodx = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
foody = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0

# Function to draw snake
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, black, [x[0], x[1], snake_block, snake_block])

# Main game loop
game_over = False
clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -snake_block
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = snake_block
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -snake_block
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = snake_block
                x1_change = 0

    # Boundary conditions for game over
    if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
        game_over = True

    # Move the snake
    x1 += x1_change
    y1 += y1_change
    screen.fill(white)
    pygame.draw.rect(screen, green, [foodx, foody, snake_block, snake_block])
    snake_head = []
    snake_head.append(x1)
    snake_head.append(y1)
    snake_list.append(snake_head)
    if len(snake_list) > snake_length:
        del snake_list[0]

    for x in snake_list[:-1]:
        if x == snake_head:
            game_over = True

    draw_snake(snake_block, snake_list)
    pygame.display.update()

    # Check if snake has eaten food
    if x1 == foodx and y1 == foody:
        foodx = round(random.randrange(0, screen_width - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, screen_height - snake_block) / 10.0) * 10.0
        snake_length += 1

    clock.tick(snake_speed)

# Display game over message
font_style = pygame.font.SysFont(None, 50)
message = font_style.render("Game Over!", True, red)
screen.blit(message, [screen_width / 3, screen_height / 3])
pygame.display.update()
pygame.time.wait(2000)

pygame.quit()
quit()
