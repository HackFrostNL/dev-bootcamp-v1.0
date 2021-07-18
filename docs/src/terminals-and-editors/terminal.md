# Quick Terminal Overview

Almost every operating system is equipped with a command-line interface or 'terminal', AKA Command Prompt on Windows. Terminals allow you to send commands to your computer to do various things like file management, installing applications, or controlling system configurations. In a nutSHELL, almost anything you can do with your mouse and keyboard can be done using commands.

-   Terminal = text input/output environment
-   Shell = command line interpreter

## Why command-line?

### 1. Things can get done quicker

Okay hear me out, lets say you have a directory full of mixed type files and you want to delete all the .png files but keep the rest; how long will that take you to do using your mouse and keyboard?
Your answer doesn't matter, because this is how fast it is using a command:

```sh
rm *.png
```

### 2. You're in full control

Command-line allows you to be in full control of your system. Things like configuring system settings, killing and starting tasks, managing services and quick installation of packages and applications can all be done efficiently and less error prone through command-line.

### 3. You look like a hacker using Terminal

Yes.
![](https://i.ytimg.com/vi/qbWqXKN3m3c/maxresdefault.jpg)

## Useful Commands

-   `ls` — List directory contents
    -   e.g. `ls -a` will list all files and folders including hidden ones
-   `echo` — Prints text to the terminal window
    -   e.g. `echo hello` will print 'hello' in next line
-   `touch` — Creates a file
    -   e.g. `touch app.py` will create a python app file in current directory
-   `mkdir` — Create a directory
    -   e.g. `mkdir projects` creates a folder 'projects' in current directory
-   `cd` — Change directory
    -   e.g. After creating the 'projects' folder, you can enter it with `cd projects`
-   `man` — Print manual or get help for a
    command
    -   e.g. `man mkdir` will open the manual of how to use the `mkdir` command
-   `pwd` — Print working directory
-   `clear` — Clear your terminal window
-   `rm` — Removes file
    -   e.g. `rm app.py` removes the app file you made

###### Aliases

You can create your own custom commands based on existing commands, for example:

```sh
alias c = “clear”
```

By running the above command you have created an alias for the command `clear` to be also recognized by typing the character `c`; hence if you type `c` in the next line, your terminal screen wil be cleared.
