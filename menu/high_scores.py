import pygame

PATH = "../assets/"
file_name = "high_scores.txt"
f1 = open(PATH+file_name, "r", encoding='utf-8')
s1 = f1.read()
print(s1)
f1.close()
