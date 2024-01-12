import customtkinter as ctk
import os
from functions.navigation import go_to
from functions.create_page import (
    create_choose_course_page,
    create_select_specific_lesson_page,
    create_choose_hiragana_or_katakana_page,
    create_select_character_page,
    create_part_break_page,
    create_lesson_1_page,
    )
from functions.create_button import create_title, create_long_button
def exit_fullscreen(event=None):
    window.attributes("-fullscreen", False)

def exit_program():
    window.destroy()

def create_main_menu_page(main_menu_page, page_log, next_page):
    # Create title: Let’s learn Japanese!
    create_title(main_menu_page, "Let’s learn Japanese!", (150, 155))
    # Create button 1: Let's go!
    create_long_button(main_menu_page, "Let's go!", "normal", lambda: go_to(page_log, next_page))
    # Create button 2: Leaderboard
    create_long_button(main_menu_page,"Leaderboard","disabled", None,)
    # Create button 3: Setting
    create_long_button(main_menu_page, "Setting", "disabled", None)
    # Create button 4: Exit
    create_long_button(main_menu_page, "Exit", "normal", lambda: exit_program())

# File path
directory_path = os.path.dirname(os.path.realpath(__file__))
ui_file_path = directory_path + r"\ui"
character_ui_file_path = directory_path + r"\ui\hiragana_character"
hiragana_caligraphy_file_path = directory_path + r"\ui\hiragana_caligraphy"
hiragana_pronounce_file_path = directory_path + r"\sound\hiragana_pronounce"
katakana_caligraphy_file_path = directory_path + r"\ui\katakana_caligraphy"
katakana_pronounce_file_path = directory_path + r"\sound\katakana_pronounce"

hiragana_romanji_list = [
    "a", "i", "u", "e", "o",
    "ka", "ki", "ku", "ke", "ko",
    "sa", "shi", "su", "se", "so",
    "ta", "chi", "tsu", "te", "to",
    "na", "ni", "nu", "ne", "no",
    "ha", "hi", "fu", "he", "ho",
    "ma", "mi", "mu", "me", "mo",
    "ya", "yu", "yo", "ra", "ri",
    "ru", "re", "ro", "wa", "wo", "n",
]

hiragana_jp_list = [
    "あ", "い", "う", "え", "お",
    "か", "き", "く", "け", "こ",
    "さ", "し", "す", "せ", "そ",
    "た", "ち", "つ", "て", "と",
    "な", "に", "ぬ", "ね", "の",
    "は", "ひ", "ふ", "へ", "ほ",
    "ま", "み", "む", "め", "も",
    "や", "ゆ", "よ", "ら", "り",
    "る", "れ", "ろ", "わ", "を", "ん",
]

hiragana_character_dict = {}

for i in range(len(hiragana_romanji_list)):
    romanji_character = hiragana_romanji_list[i]
    jp_character = hiragana_jp_list[i]

    hiragana_character_dict[romanji_character] = {
        "jp_character": jp_character,
        "image_file": hiragana_caligraphy_file_path + rf"\{romanji_character}.png",
        "sound_file": hiragana_pronounce_file_path + rf"\{romanji_character}.mp3",
    }

page_log = []
select_character_list = []    
number_list = [0]
select_lesson_list = [0]
select_course_list = [0]
choose_hiragana_or_katakana_page_list = [0]

#romanji_dict = {character: character for character in hiragana_romanji_list}

ctk.set_default_color_theme(directory_path + r"\Theme\white_minimal.json")
window = ctk.CTk()
window.title = "Japanese learner helper"
window.geometry("1920x1080")
window.resizable(False, False)
window.bind("<Escape>", exit_fullscreen)
window.attributes("-fullscreen", True)

# All page
main_menu_page = ctk.CTkFrame(window)
select_course_page = ctk.CTkFrame(window)
select_specific_lesson_page = ctk.CTkFrame(window)
choose_hiragana_or_katakana_page = ctk.CTkFrame(window)
select_character_page = ctk.CTkFrame(window)
part_1_break_page = ctk.CTkFrame(window)
part_2_break_page = ctk.CTkFrame(window)
lesson_1_page_ex_1 = ctk.CTkFrame(window)
lesson_1_page_ex_2 = ctk.CTkFrame(window)
lesson_1_page_ex_3 = ctk.CTkFrame(window)
lesson_2_page_ex_1  = ctk.CTkFrame(window)
lesson_2_page_ex_2  = ctk.CTkFrame(window)
lesson_2_page_ex_3  = ctk.CTkFrame(window)
end_lesson_page = ctk.CTkFrame(window)

create_main_menu_page(main_menu_page, page_log, select_course_page)
create_choose_course_page(
    select_course_page, 
    ui_file_path, 
    page_log,
    choose_hiragana_or_katakana_page,
    select_specific_lesson_page,
)

create_select_specific_lesson_page(
    select_specific_lesson_page, 
    ui_file_path,
    page_log, 
    select_lesson_list,
    choose_hiragana_or_katakana_page,
)
create_choose_hiragana_or_katakana_page(
    choose_hiragana_or_katakana_page, 
    ui_file_path, 
    page_log,
    select_character_page,
    choose_hiragana_or_katakana_page_list,
)
create_select_character_page(
    select_character_page, 
    ui_file_path, 
    character_ui_file_path,
    main_menu_page, 
    part_1_break_page, 
    page_log,
    select_character_list,
)
create_part_break_page(
    part_1_break_page, 
    "1", 
    "writing and listening", 
    ui_file_path, 
    page_log, 
    main_menu_page, 
    lesson_1_page_ex_1,
    select_character_list,
    )

create_lesson_1_page(
    lesson_1_page_ex_1, 
    select_character_list,
    hiragana_character_dict,
    number_list, 
    hiragana_caligraphy_file_path,
    ui_file_path,
    main_menu_page, 
    page_log,
    "3",
    "1",
    hiragana_romanji_list[0],
    lesson_1_page_ex_2,
    )

create_lesson_1_page(
    lesson_1_page_ex_2, 
    select_character_list,
    hiragana_character_dict,
    number_list, 
    hiragana_caligraphy_file_path,
    ui_file_path,
    main_menu_page, 
    page_log,
    "3",
    "2",
    hiragana_romanji_list[1],
    lesson_1_page_ex_3,
    )

create_lesson_1_page(
    lesson_1_page_ex_3, 
    select_character_list,
    hiragana_character_dict,
    number_list, 
    hiragana_caligraphy_file_path,
    ui_file_path,
    main_menu_page, 
    page_log,
    "3",
    "3",
    hiragana_romanji_list[2],
    lesson_2_page_ex_1,
    )
go_to(page_log, main_menu_page)
window.mainloop()
