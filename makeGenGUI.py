# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    makeGenGUI.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mdupuis <mdupuis@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/03/09 19:03:29 by mdupuis           #+#    #+#              #
#    Updated: 2022/07/06 09:50:19 by mdupuis          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import os, glob, platform
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from os import path

# Create Window
root = Tk()
root.title("Makefile Generator")
if platform.system() == 'Linux':
    root.geometry("500x600")
elif platform.system() == 'Windows': 
    root.geometry("550x655")
else:
    root.geometry("430x600")
root.resizable(False, False)
root.config(bg='#4065A4')

# Create Title:
title = Label(root, text="Makefile Generator", font=("Terminal", 24, "bold"), bg='#eeeeee', fg='black', border=4,
              relief='ridge', padx=10, pady=10, width=20)
title.grid(row=0, columnspan=2, pady=10, padx=10)

# Create Frame:
frame = Frame(root, bg='#eeeeee', border=4, relief='ridge', padx=10, pady=10)
frame.grid(row=1, columnspan=2, padx=10, pady=10)


# call function:
def disable_libft_entry():
    entry_libft.delete(0, END)
    entry_libft.configure(state='disabled')
    entry_libft_a.delete(0, END)
    entry_libft_a.configure(state='disabled')


def enable_libft_entry():
    entry_libft.configure(state='normal')
    entry_libft_a.configure(state='normal')


def disable_mlx_entry():
    entry_mlx.delete(0, END)
    entry_mlx.configure(state='disabled')
    entry_mlx_a.delete(0, END)
    entry_mlx_a.configure(state='disabled')


def enable_mlx_entry():
    entry_mlx.configure(state='normal')
    entry_mlx_a.configure(state='normal')


def disable_both():
    disable_mlx_entry()
    disable_libft_entry()
    
    
def enable_both():
    enable_libft_entry()
    enable_mlx_entry()
    

def disable_bonus_entry():
    entry_bin_bonus.delete(0, END)
    entry_bin_bonus.configure(state='disabled')
    entry_src_bonus.delete(0, END)
    entry_src_bonus.configure(state='disabled')
    entry_inc_bonus.delete(0, END)
    entry_inc_bonus.configure(state='disabled')


def enable_bonus_entry():
    entry_bin_bonus.configure(state='normal')
    entry_src_bonus.configure(state='normal')
    entry_inc_bonus.configure(state='normal')


def reset():
    entry_mlx.delete(0, END)
    entry_mlx_a.delete(0, END)
    entry_libft.delete(0, END)
    entry_libft_a.delete(0, END)
    entry_bin.delete(0, END)
    entry_src.delete(0, END)
    entry_inc.delete(0, END)
    entry_bin_bonus.delete(0, END)
    entry_src_bonus.delete(0, END)
    entry_inc_bonus.delete(0, END)
    entry_project_path.delete(0, END)


def quit_after_generate():
    messagebox.showinfo('Success', 'Makefile generated successfully!\nPlease check the folder you selected.\n\nThank '
                                   'you for using this app!\nThanks to mqueguin for the original idea.')
    root.destroy()


def exit_app():
    msgbox = messagebox.askquestion('Exit App', 'Really Quit?', icon='error')
    if msgbox == 'yes':
        root.destroy()
    else:
        messagebox.showinfo('Welcome Back', 'Welcome back to the App')


# Radio Buttons -------------------------------------------------------------------------------------------------------:
# Select language:
language = StringVar()
language.set(None)
Label(frame, text="Language:\t\t", bg='#eeeeee', fg='black', font=("Calibri", 12, "bold")).grid(row=0, column=0,
                                                                                                sticky=W)
Radiobutton(frame, text="C", variable=language, value="C", bg='#eeeeee', font=('Calibri', 12),
            command=enable_both).grid(row=0, column=1,
                                                                                                    sticky=W)
Radiobutton(frame, text="C++", variable=language, value="C++", bg='#eeeeee', font=('Calibri', 12),
            command=disable_both).grid(row=0, column=1,
                                                                                                        sticky=E)
# Libft:
libft = StringVar()
libft.set("y")
Label(frame, text="Libft:\t\t\t", bg='#eeeeee', fg='black', font=("Calibri", 12, "bold")).grid(row=1, column=0,
                                                                                               sticky=W)
Radiobutton(frame, text="Yes", variable=libft, value="y", bg='#eeeeee', font=('Calibri', 12),
            command=enable_libft_entry).grid(row=1, column=1, sticky=W)
Radiobutton(frame, text="No", variable=libft, value="n", bg='#eeeeee', font=('Calibri', 12),
            command=disable_libft_entry).grid(row=1, column=1, sticky=E, padx=10)
# Minilibx:
mlx = StringVar()
mlx.set("y")
Label(frame, text="Minilibx:\t\t", bg='#eeeeee', fg='black', font=("Calibri", 12, "bold")).grid(row=2, column=0,
                                                                                                sticky=W)
Radiobutton(frame, text="Yes", variable=mlx, value="y", bg='#eeeeee', font=('Calibri', 12),
            command=enable_mlx_entry).grid(row=2, column=1, sticky=W)
Radiobutton(frame, text="No", variable=mlx, value="n", bg='#eeeeee', font=('Calibri', 12),
            command=disable_mlx_entry).grid(row=2, column=1, sticky=E, padx=10)
# Bonus:
bonus = StringVar()
bonus.set("y")
Label(frame, text="Bonus:\t\t\t", bg='#eeeeee', fg='black', font=("Calibri", 12, "bold")).grid(row=3, column=0,
                                                                                               sticky=W)
Radiobutton(frame, text="Yes", variable=bonus, value="y", bg='#eeeeee', font=('Calibri', 12),
            command=enable_bonus_entry).grid(row=3, column=1, sticky=W)
Radiobutton(frame, text="No", variable=bonus, value="n", bg='#eeeeee', font=('Calibri', 12),
            command=disable_bonus_entry).grid(row=3, column=1, sticky=E, padx=10)
# Entries -------------------------------------------------------------------------------------------------------------:
# Name of binary:
entry_bin = StringVar(root, value="ex: minishell")
Label(frame, text="Binary name:\t", bg='#eeeeee', fg='black', font=("Calibri", 12, "bold")).grid(row=4, column=0,
                                                                                                 sticky=W)
entry_bin = Entry(frame, textvariable=entry_bin, bg='white', fg='black', font=('Helvetica', 12))
entry_bin.grid(row=4, column=1, sticky=W)

# Path of sources:
entry_src = StringVar(root, value="ex: src")
Label(frame, text="Sources path:\t", bg='#eeeeee', fg='black', font=("Calibri", 12, "bold")).grid(row=5, column=0,
                                                                                                  sticky=W)
entry_src = Entry(frame, textvariable=entry_src, bg='white', fg='black', font=('Helvetica', 12))
entry_src.grid(row=5, column=1, sticky=W)

# Path of includes:
entry_inc = StringVar(root, value="ex: includes")
Label(frame, text="Includes path:\t", bg='#eeeeee', fg='black', font=("Calibri", 12, "bold")).grid(row=6, column=0,
                                                                                                   sticky=W)
entry_inc = Entry(frame, textvariable=entry_inc, bg='white', fg='black', font=('Helvetica', 12))
entry_inc.grid(row=6, column=1, sticky=W)

# Path of libft:
entry_libft = StringVar(root, value="ex: libft")
Label(frame, text="Path to libft:\t\t", bg='#eeeeee', fg='black', font=("Calibri", 12, "bold")).grid(row=7, column=0,
                                                                                                     sticky=W)
entry_libft = Entry(frame, textvariable=entry_libft, bg='white', fg='black', font=('Helvetica', 12),
                    disabledbackground='grey')
entry_libft.grid(row=7, column=1, sticky=W)

# Path of libft.a:
entry_libft_a = StringVar()
entry_libft_a.set("ex: libft/libft.a")
Label(frame, text="Path to libft.a:\t\t", bg='#eeeeee', fg='black', font=("Calibri", 12, "bold")).grid(row=8, column=0,
                                                                                                       sticky=W)
entry_libft_a = Entry(frame, textvariable=entry_libft_a, bg='white', fg='black', font=('Helvetica', 12),
                      disabledbackground='grey')
entry_libft_a.grid(row=8, column=1, sticky=W)

# Path of minilibx:
entry_mlx = StringVar()
entry_mlx.set("ex: minilibx")
Label(frame, text="Path to minilibX:\t", bg='#eeeeee', fg='black', font=("Calibri", 12, "bold")).grid(row=9, column=0,
                                                                                                      sticky=W)
entry_mlx = Entry(frame, textvariable=entry_mlx, bg='white', fg='black', font=('Helvetica', 12),
                  disabledbackground='grey')
entry_mlx.grid(row=9, column=1, sticky=W)

# Path of minilibx.a:
entry_mlx_a = StringVar()
entry_mlx_a.set("ex: minilibx/minilibx.a")
Label(frame, text="Path to minilibX.a:\t", bg='#eeeeee', fg='black', font=("Calibri", 12, "bold")).grid(row=10,
                                                                                                        column=0,
                                                                                                        sticky=W)
entry_mlx_a = Entry(frame, textvariable=entry_mlx_a, bg='white', fg='black', font=('Helvetica', 12),
                    disabledbackground='grey')
entry_mlx_a.grid(row=10, column=1, sticky=W)

# Name of binary (bonus):
entry_bin_bonus = StringVar()
entry_bin_bonus.set("ex: minishell_bonus")
Label(frame, text="Binary name (bonus):\t", bg='#eeeeee', fg='black', font=("Calibri", 12, "bold")).grid(row=11,
                                                                                                         column=0,
                                                                                                         sticky=W)
entry_bin_bonus = Entry(frame, textvariable=entry_bin_bonus, bg='white', fg='black', font=('Helvetica', 12),
                        disabledbackground='grey')
entry_bin_bonus.grid(row=11, column=1, sticky=W)

# Path of sources (bonus):
entry_src_bonus = StringVar()
entry_src_bonus.set("ex: src_bonus")
Label(frame, text="Sources path (bonus):\t", bg='#eeeeee', fg='black', font=("Calibri", 12, "bold")).grid(row=12,
                                                                                                          column=0,
                                                                                                          sticky=W)
entry_src_bonus = Entry(frame, textvariable=entry_src_bonus, bg='white', fg='black', font=('Helvetica', 12),
                        disabledbackground='grey')
entry_src_bonus.grid(row=12, column=1, sticky=W)

# Path of includes (bonus):
entry_inc_bonus = StringVar()
entry_inc_bonus.set("ex: includes_bonus")
Label(frame, text="Includes path (bonus):\t", bg='#eeeeee', fg='black', font=("Calibri", 12, "bold")).grid(row=13,
                                                                                                           column=0,
                                                                                                           sticky=W)
entry_inc_bonus = Entry(frame, textvariable=entry_inc_bonus, bg='white', fg='black', font=('Helvetica', 12),
                        disabledbackground='grey')
entry_inc_bonus.grid(row=13, column=1, sticky=W)

# Absolute path to project:
entry_project_path = StringVar()
entry_project_path.set("ex: /mnt/nfs/homes/login/cub3d/")
Label(frame, text="Absolute path to your project:\t", bg='#eeeeee', fg='black', font=("Calibri", 12, "bold")).grid(row=14,
                                                                                                          column=0,
                                                                                                          sticky=W)
entry_project_path = Entry(frame, textvariable=entry_project_path, bg='white', fg='black', font=('Helvetica', 12),
                        disabledbackground='grey')
entry_project_path.grid(row=14, column=1, sticky=W)
Label(frame, text="(pwd in your project's root directory and paste here.)", bg='#eeeeee', fg='black', font=("Calibri", 8, "bold")).grid(row=15, column=0, sticky=NW)


def list_files(list):
    breaker = 5
    i = 0
    srcs = ""
    for file in list:
        if i == breaker and i != len(list):
            if platform.system() == "Windows":
                srcs = srcs + file.rsplit("\\")[-1] + " \\\n\t\t\t\t"
            else:
                srcs = srcs + file.rsplit("/")[-1] + " \\\n\t\t\t\t"
            i = 0   
        else:
            if platform.system() == 'Windows':
                srcs += file.rsplit("\\")[-1] + " "
            else:
                srcs += file.rsplit("/")[-1] + " "
            i += 1
    return srcs


def list_includes(list, inc_entry):
    includes = ""
    for file in list:
        if platform.system() == 'Windows':
            includes += inc_entry + "/" + file.rsplit("\\")[-1] + " \\\n\t\t\t\t"
        else:
            includes += inc_entry + "/" + file.rsplit("/")[-1] + " \\\n\t\t\t\t"
    # delete last backslash
    includes = includes[:-6]
    return includes
            

def generate():
    """
    Generate the Makefile
    """
    # Get the values of the radio buttons:
    if language.get() == "C":
        lang = "C"
    elif language.get() == "C++":
        lang = "C++"
    else:
        messagebox.showwarning("Error", "Please select a language")
        return
    # Get the values of the entries:
    name = entry_bin.get()
    src = entry_src.get()
    inc = entry_inc.get()
    if name == "" or src == "" or inc == "":
        messagebox.showwarning("Error", "Please fill all the entries")
        return
    if libft.get() == "y":
        libft_ok = entry_libft.get()
        libft_a = entry_libft_a.get()
        if libft_ok == "" or libft_a == "":
            messagebox.showwarning("Error", "Please fill all the entries")
            return
    if mlx.get() == "y":
        mlx_ok = entry_mlx.get()
        mlx_a = entry_mlx_a.get()
        if mlx_ok == "" or mlx_a == "":
            messagebox.showwarning("Error", "Please fill all the entries")
            return
    if bonus.get() == "y":
        bin_bonus = entry_bin_bonus.get()
        src_bonus = entry_src_bonus.get()
        inc_bonus = entry_inc_bonus.get()
        if bin_bonus == "" or src_bonus == "" or inc_bonus == "":
            messagebox.showwarning("Error", "Please fill all the entries")
            return
    absolute_path = entry_project_path.get()
    if absolute_path == "":
        messagebox.showwarning("Error", "Please fill the absolute path entry.\n(pwd in your project's root directory and paste here.)")
        return
    elif not path.exists(absolute_path):
        messagebox.showwarning("Error", "Directory does not exist\n(pwd in your project's root directory and paste here.)")
        return
    # Get the list of files:
    #listOfFiles = glob.glob(absolute_path + src + "/**/*.py", recursive=True)
    if lang == "C":
        listOfFiles = glob.glob(absolute_path + "/" + src + "/**/*.c", recursive=True)
        srcs = list_files(listOfFiles)
        listOfIncludes = glob.glob(absolute_path + "/" + inc + "/**/*.h", recursive=True)
        includes = list_includes(listOfIncludes, inc)
        if bonus.get() == "y":
            listOfFilesBonus = glob.glob(absolute_path + "/" + src_bonus + "/**/*.c", recursive=True)
            srcs_bonus = list_files(listOfFilesBonus)
            listOfIncludesBonus = glob.glob(absolute_path + "/" + inc_bonus + "/**/*.h", recursive=True)
            includes_bonus = list_includes(listOfIncludesBonus, inc_bonus)
    elif lang == "C++":
        listOfFiles = glob.glob(absolute_path + "/**/*.cpp", recursive=True)
        srcs = list_files(listOfFiles)
        listOfIncludes = glob.glob(absolute_path + "/**/*.hpp", recursive=True)
        includes = list_includes(listOfIncludes, inc)
        if bonus.get() == "y":
            listOfFilesBonus = glob.glob(absolute_path + "/" + src_bonus + "/**/*.cpp", recursive=True)
            srcs_bonus = list_files(listOfFilesBonus)
            listOfIncludesBonus = glob.glob(absolute_path + "/" + inc_bonus + "/**/*.hpp", recursive=True)
            includes_bonus = list_includes(listOfIncludesBonus, inc_bonus)
    # Create the Makefile:
    f = filedialog.asksaveasfile(title="Save as...", initialdir=absolute_path, mode="w")
    if f is None:
        return
    f.write("\nNAME\t\t\t=\t" + name)
    if bonus.get() == "y":
        f.write("\n\nNAME_BONUS\t\t=\t" + bin_bonus)
    if lang == "C":
        f.write("\n\nCC\t\t\t=\tgcc")
    else:
        f.write("\n\nCXX\t\t\t\t=\tc++")
    f.write("\n\nSRC_DIR\t\t\t=\t$(shell find " + src + " -type d)\n")
    if bonus.get() == "y":
        f.write("\nSRC_BONUS_DIR\t=\t$(shell find " + src_bonus + " -type d)\n")
    if libft.get() == "y":
        f.write("\nLIBFT\t\t\t=\t./" + libft_ok)
        f.write("\nLIBFT_A\t\t\t=\t./" + libft_a)
    if mlx.get() == "y":
        f.write("\nMLX\t\t\t\t=\t./" + mlx_ok)
        f.write("\nMLX_A\t\t\t=\t./" + mlx_a)
    f.write("\nOBJ_DIR\t\t\t=\t.obj")
    if bonus.get() == "y":
        f.write("\n\nOBJ_BONUS_DIR\t=\t.obj_bonus")
    if lang == "C":
        f.write("\n\nvpath %.c $(foreach dir, $(SRC_DIR), $(dir):)")
    else:
        f.write("\n\nvpath %.cpp $(foreach dir, $(SRC_DIR), $(dir):)")
    if bonus.get() == "y":
        if lang == "C":
            f.write("\nvpath %.c $(foreach dir, $(SRC_BONUS_DIR), $(dir):)")
        else:
            f.write("\nvpath %.cpp $(foreach dir, $(SRC_BONUS_DIR), $(dir):)")
    f.write("\n\n# library -----------------------------------------------------------")
    f.write("\n\nSRC\t\t\t=\t" + srcs + "\n\n")
    if bonus.get() == "y":
        f.write("SRC_BONUS\t=\t" + srcs_bonus +"\n\n")
    f.write("INC\t\t\t=\t" + includes + "\n\n")
    if bonus.get() == "y":
        f.write("INC_BONUS\t\t=\t" + includes_bonus + "\n\n")
    if language.get() == "C":
        f.write("OBJ\t\t\t=\t$(addprefix $(OBJ_DIR)/, $(SRC:%.c=%.o))\n\n")
    else:
        f.write("OBJ\t\t\t=\t$(addprefix $(OBJ_DIR)/, $(SRC:%.cpp=%.o))\n\n")
    if bonus.get() == "y":
        if language.get() == "C":
            f.write("OBJ_BONUS\t\t=\t$(addprefix $(OBJ_BONUS_DIR)/, $(SRC_BONUS:%.c=%.o))\n\n")
        else:
            f.write("OBJ_BONUS\t\t=\t$(addprefix $(OBJ_BONUS_DIR)/, $(SRC_BONUS:%.cpp=%.o))\n\n")
    f.write("# Compilation flags -------------------------------------------------\n\n")
    if lang == "C":
        f.write("CFLAGS\t\t\t=\t-Wall -Wextra -Werror\n")
    else:
        f.write("CPPFLAGS\t\t\t=\t-Wall -Wextra -Werror -std=c++98\n")
    if libft.get() == "y" and mlx.get() == "n":
        f.write("IFLAGS\t\t=	-I " + inc + "/ -I " + libft_ok + "/includes -I /usr/include\n")
    elif mlx.get() == "y" and libft.get() == "y":
        f.write("IFLAGS\t\t=	-I " + inc + "/ -I " + libft_ok + "/includes -I " + mlx_ok + " -I /usr/include\n")
    elif mlx.get() == "y" and libft.get() == "n":
        f.write("IFLAGS\t\t=	-I " + inc + "/ -I " + mlx_ok + " -I /usr/include\n")
    else:
        f.write("IFLAGS	\t\t=	-I " + inc + "/ -I /usr/include\n")
    if bonus.get() == "y":
        if libft.get() == "y" and mlx.get() == "n":
            f.write("IFLAGS_B\t\t=	-I " + inc_bonus + "/ -I " + libft_ok + "/includes -I /usr/include\n")
        elif mlx.get() == "y" and libft.get() == "y":
            f.write(
                "IFLAGS_B\t\t=	-I " + inc_bonus + "/ -I " + libft_ok + "/includes -I " + mlx_ok + " -I /usr/include\n")
        elif mlx.get() == "y" and libft.get() == "n":
            f.write("IFLAGS_B\t\t=	-I " + inc_bonus + "/ -I " + mlx_ok + " -I /usr/include\n")
        else:
            f.write("IFLAGS_B\t\t=	-I " + inc_bonus + "/ -I /usr/include\n")
    if mlx.get() == "y":
        f.write("LFLAGS\t\t\t=	-lmlx -lm -lX11 -lXext\n")
    f.write("""
# Colors ------------------------------------------------------------\n
_GREY	=	$'\\e[30m
_RED	=	$'\\e[31m
_GREEN	=	$'\\e[32m
_YELLOW	=	$'\\e[33m
_BLUE	=	$'\\e[34m
_PURPLE	=	$'\\e[35m
_CYAN	=	$'\\e[36m
_WHITE	=	$'\\e[37m\n\n""")
    f.write("# main part ---------------------------------------------------------\n")
    if lang == "C":
        f.write("""
$(OBJ_DIR)/%.o : %.c $(INC)
\t\t@echo "Compiling $(_YELLOW)$@$(_WHITE) ... \\c"
\t\t@mkdir -p $(OBJ_DIR)
\t\t@$(CC) $(CFLAGS) $(IFLAGS) -c $< -o $@
\t\t@echo \"$(_GREEN)DONE$(_WHITE)\"\n\n""")
        if bonus.get() == "y":
            f.write("""
$(OBJ_BONUS_DIR)/%.o : %.c $(INC_BONUS) 
\t\t@echo "Compiling $(_YELLOW)$@$(_WHITE) ... \\c"
\t\t@mkdir -p $(OBJ_BONUS_DIR)
\t\t@$(CC) $(CFLAGS) $(IFLAGS_B) -c $< -o $@
\t\t@echo \"$(_GREEN)DONE$(_WHITE)\"\n\n""")
    if lang == "C++":
        f.write("""
$(OBJ_DIR)/%.o : %.cpp $(INC)
\t\t@echo "Compiling $(_YELLOW)$@$(_WHITE) ... \\c"
\t\t@mkdir -p $(OBJ_DIR)
\t\t@$(CXX) $(CPPFLAGS) $(IFLAGS) -c $< -o $@
\t\t@echo \"$(_GREEN)DONE$(_WHITE)\"\n\n""")
        if bonus.get() == "y":
            f.write("""
$(OBJ_BONUS_DIR)/%.o : %.cpp $(INC_BONUS) 
\t\t@echo "Compiling $(_YELLOW)$@$(_WHITE) ... \\c"
\t\t@mkdir -p $(OBJ_BONUS_DIR)
\t\t@$(CXX) $(CPPFLAGS) $(IFLAGS_B) -c $< -o $@
\t\t@echo \"$(_GREEN)DONE$(_WHITE)\"\n\n""")

    if libft.get() == "y" and mlx.get() == "y":
        f.write("all: $(LIBFT_A) $(MLX_A) $(NAME)\n")
    elif libft.get() == "y" and mlx.get() == "n":
        f.write("all: $(LIBFT_A) $(NAME)\n")
    elif libft.get() == "n" and mlx.get() == "y":
        f.write("all: $(MLX_A) $(NAME)\n")
    else:
        f.write("all: $(NAME)\n")
    if libft.get() == "y":
        f.write("""
$(LIBFT_A):
\t\t@make -C $(LIBFT)\n""")
    if mlx.get() == "y":
        f.write("""
$(MLX_A):
\t\t@make -C $(MLX)\n""")
    if bonus.get() == "y":
        if libft.get() == "y" and mlx.get() == "y":
            f.write("\nbonus: $(LIBFT_A) $(MLX_A) $(NAME_BONUS)\n")
        elif libft.get() == "y" and mlx.get() == "n":
            f.write("\nbonus: $(LIBFT_A) $(NAME_BONUS)\n")
        elif libft.get() == "n" and mlx.get() == "y":
            f.write("\nbonus: $(MLX_A) $(NAME_BONUS)\n")
        else:
            f.write("\nbonus: $(NAME_BONUS)\n")
    f.write("""
$(NAME): $(OBJ)
\t\t@echo "-----\\nCreating Binary File $(_YELLOW)$@$(_WHITE) ... \\c\"""")
    if lang == "C++":
        f.write("\n\t\t$(CXX) $(CPPFLAGS) $(OBJ) $(IFLAGS) -o $(NAME)")
    if lang == "C":
        if libft.get() == "y" and mlx.get() == "y":
            f.write("\n\t\t$(CC) $(CFLAGS) $(OBJ) $(IFLAGS) $(LIBFT_A) -L $(MLX) $(LFLAGS) -o $(NAME)")
        elif libft.get() == "y" and mlx.get() == "n":
            f.write("\n\t\t$(CC) $(CFLAGS) $(OBJ) $(IFLAGS) $(LIBFT_A) -o $(NAME)")
        elif libft.get() == "n" and mlx.get() == "y":
            f.write("\n\t\t$(CC) $(CFLAGS) $(OBJ) $(IFLAGS) -L $MLX) $(LFLAGS) -o $(NAME)")
        else:
            f.write("\n\t\t$(CC) $(CFLAGS) $(OBJ) $(IFLAGS) -o $(NAME)")
    f.write("\n\t\t@echo \"$(_GREEN)DONE$(_WHITE)\\n-----\"\n")
    if bonus.get() == "y":
        f.write("""
$(NAME_BONUS): $(OBJ_BONUS)
\t\t@echo "-----\\nCreating Binary File $(_YELLOW)$@$(_WHITE) ... \\c\"""")
        if lang == "C++":
             f.write("\n\t\t$(CXX) $(CPPFLAGS) $(OBJ_BONUS) $(IFLAGS_B) -o $(NAME_BONUS)")
        if lang == "C":
            if libft.get() == "y" and mlx.get() == "y":
                f.write("\n\t\t$(CC) $(CFLAGS) $(OBJ_BONUS) $(IFLAGS_B) $(LIBFT_A) -L $(MLX) $(LFLAGS) -o $(NAME_BONUS)")
            elif libft.get() == "y" and mlx.get() == "n":
                f.write("\n\t\t$(CC) $(CFLAGS) $(OBJ_BONUS) $(IFLAGS_B) $LIBFT_A) -o $(NAME_BONUS)")
            elif libft.get() == "n" and mlx.get() == "y":
                f.write("\n\t\t$(CC) $(CFLAGS) $(OBJ_BONUS) $(IFLAGS_B) -L $(MLX) $(LFLAGS) -o $(NAME_BONUS)")
            else:
                f.write("\n\t\t$(CC) $(CFLAGS) $(OBJ_BONUS) $(IFLAGS_B) -o $(NAME_BONUS)")
        f.write("\n\t\t@echo \"$(_GREEN)DONE$(_WHITE)\\n-----\"\n")
    f.write("""
clean:
\t\t@echo "$(_WHITE)Deleting Objects Directory $(_YELLOW)$(OBJ_DIR)$(_WHITE) ... \\c"
\t\t@rm -rf $(OBJ_DIR) $(OBJ_DIR_BONUS)\n""")
    if libft.get() == "y":
        f.write("\t\t@make clean -C $(LIBFT)\n")
    if mlx.get() == "y":
        f.write("\t\t@make clean -C $(MLX)\n")
    f.write("\t\t@echo \"$(_GREEN)DONE$(_WHITE)\\n-----\"\n")
    f.write("""
fclean: clean
\t\t@echo "$(_WHITE)Deleting Binary File $(_YELLOW)$(NAME)$(_WHITE) ... \\c"
\t\t@rm -f $(NAME) $(NAME_BONUS)
\t\t@echo "$(_GREEN)DONE$(_WHITE)\\n-----\"\n""")
    f.write("\nre:\t\tfclean all\n\n")
    f.write(".PHONY:\t\tall bonus clean fclean re\n")
    f.close()
    quit_after_generate()


# Buttons -------------------------------------------------------------------------------------------------------------:
# Reset:
Button(frame, text="Reset", bg='#eeeeee', fg='black', font=("Calibri", 12, "bold"), relief='ridge', borderwidth=4,
       command=reset).grid(row=15, column=0,
                           sticky=W, pady=20)
# Generate:
Button(frame, text="Generate", bg='#eeeeee', fg='black', font=("Calibri", 12, "bold"), command=generate).grid(row=15,
                                                                                                              column=1,
                                                                                                              sticky=E,
                                                                                                              pady=20)
# Quit:
Button(root, text="Quit", bg='#4065A4', fg='white', font=("Calibri", 12, "bold"), command=exit_app).grid(row=3,
                                                                                                         column=0,
                                                                                                         sticky=S,
                                                                                                         pady=10,
                                                                                                         columnspan=2)

# Run Window
root.mainloop()

# End of File
