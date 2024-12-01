import tkinter
from tkinter import *
from tkinter import PhotoImage
import configparser
import os
import subprocess
import sys
import os
from os.path import expanduser
from PIL import Image, ImageTk

section = ""
option = ""
value = ""

home = expanduser("~")
path = '/launcher_data'


settings_path = 'Resources/config.ini'

app_icon_path = 'Contents/placeholder.gif'
launch_path = 'app_launcher/demo/random'
launch_sym_path = 'Resources/run.sh'




is_value = ""

#unused
downloads = home + '/Downloads/app_launcher'
documents = home + '/Documents/app_launcher'
desktop = home + '/Desktop/app_launcher'
#

def quote_replacer(str):
    str = str.replace('"', '')
    return str


def quote_adder(value):
    return '"' + value + '"'


def editor(section, option, value):
    config_fullscreen = configparser.ConfigParser()
    config_fullscreen.read(settings_path)
    config_fullscreen.set(section, option, value)
    with open(settings_path, 'w') as configfile:
        config_fullscreen.write(configfile)


def reader():
    global is_value
    config_read = configparser.ConfigParser()
    config_read.read(settings_path)
    is_value = config_read['DISPLAY']['fullscreen']
    return is_value


def read_data(_file):
    if os.path.isfile(_file):
        with open(_file, 'r') as file_data:
            data = file_data.readlines()
            return data
    else:
        f = open("fullscreen.txt", "w")
        f.write("true")
        f.close


class AppLauncher:
    def __init__(self, root, app_path):
        self.root = root
        self.app_path = app_path

        self.path_init()

        self.bg = ImageTk.PhotoImage(Image.open(app_icon_path))

        self.ui_set()


        is_on = True

    def path_init(self):
        home = expanduser("~")
        self.path = home + '/launcher_data'

        self.build1 = self.path + '/Resources/part1.sh'
        self.build2 = self.path + '/Resources/part2.sh'

        self.settings_path = self.path + '/Resources/settings.ini' #WIP

        self.app_icon_path = self.path + '/Contents/placeholder.gif'

        self.launch_path = self.path + '/app_launcher/demo/'
        self.launch_sym_path = self.path + '/Resources/run.sh'

    def ui_set(self):
        self.root.geometry("800x600")
        self.root.title("App Launcher Template")

        self.myLabel = Label(self.root, image=self.bg)
        self.myLabel.place(x=0, y=0, relwidth=1, relheight=1)

        self.QuickSettings = Label(root, text='Quick Settings', font=('Times New Roman', 23), fg='white',
                                   bg='Hot Pink')
        self.QuickSettings.pack(pady=15)

        self.SetXButton = Button(self.root, text="Set Window Width ", command=self.resX)

        self.SetYButton = Button(self.root, text="Set Window Height ", command=self.resY)
        self.SetFullscreen = Button(self.root, text="Fullscreen Toggle", command=self.fullscreen_toggle)

        self.res_x = Entry(root)
        self.res_x.pack(pady=5)

        self.SetXButton.pack(pady=5)

        self.res_y = Entry(root)
        self.res_y.pack(pady=5)

        self.SetYButton.pack(pady=10)

        self.SetFullscreen.pack(pady=18)

        self.AdvSetting = Label(root, text='Advanced Settings', font=('Times New Roman', 23), fg='white',
                                bg='Red')
        self.AdvSetting.pack(pady=15)

        self.MoreDispSett = Button(root, text="Advanced Display Settings", command=self.AdvSett)
        self.MoreDispSett.pack()
        self.AudioSett = Button(root, text="Advanced Audio Settings", command=self.AudioSett)
        self.AudioSett.pack()

        self.LaunchLabel = Label(root, text='Launch', font=('Times New Roman', 23), fg='white',
                                bg='Green')
        self.LaunchLabel.pack(pady=15)





        self.LaunchButton = Button(self.root, text="Launch", padx=100, pady=50, command=self.AppLaunchTime)
        self.LaunchButton.pack()

    def AdvSett(self):
        MoreSettings(self.root)

    def AudioSett(self):
        AudioSett(self.root)

    def reader(self):
        global is_value
        config_read = configparser.ConfigParser()
        config_read.read(settings_path)
        is_value = config_read['DISPLAY']['fullscreen']
        return is_value

    def AppLaunchTime(self):
        self.LaunchButton.config(fg='red', text="You launched the app.\n\n (Check Terminal for Output)")
        subprocess.run(['bash', self.launch_sym_path])



    def resX(self):
        global value
        value = str('"') + str(self.res_x.get()) + str('"')
        editor('DISPLAY', 'window_X', value)
        self.SetXButton.config(text='Width Set! :)', fg='green')

    def resY(self):
        global value
        value = str('"') + str(self.res_y.get()) + str('"')
        editor('DISPLAY', 'window_Y', value)
        self.SetYButton.config(text='Height Set! :)', fg='green')

    def On_Checker(self):
        global is_on
        self.reader()
        if is_value == '"false"':
            is_on = False
            self.SetFullscreen.config(text="Fullscreen is: OFF")

        else:
            is_on = True
            self.SetFullscreen.config(text="Fullscreen is: ON")

    def fullscreen_toggle(self):
        global is_on
        self.On_Checker()



        if is_on is True:

            value = str('"') + "false" + str('"')
            self.SetFullscreen.config(text="Fullscreen is OFF", fg='red')

            is_on = False
            editor('DISPLAY', 'fullscreen', value)
        else:
            value = str('"') + "true" + str('"')
            editor('DISPLAY', 'fullscreen', value)

            self.SetFullscreen.config(text="Fullscreen is ON", fg='green')
            is_on = True



class MoreSettings():
    def __init__(self, parent):
        self.newWindow = Toplevel(parent)
        self.newWindow.title("Advanced Display Settings")
        self.newWindow.geometry("400x300")
        self.ui_set()
        is_on_int = True


    def ui_set(self):

        self.internal_res = Button(self.newWindow, text="Custom Internal Value is DISABLED", command=self.internal_toggle)
        self.internal_res.pack()
        self.internal_res_x = Entry(self.newWindow)
        self.internal_res_x.pack()
        self.SetXButton = Button(self.newWindow, text="Set Internal Width ",command=self.InternalResX)  # once pressed, it goes to resX
        self.SetXButton.pack()
        self.internal_res_y = Entry(self.newWindow)
        self.internal_res_y.pack()
        self.SetYButton = Button(self.newWindow, text="Set Internal Height ",command=self.InternalResY)  # once pressed, it goes to resY
        self.SetYButton.pack()

    def reader(self):
        config_read = configparser.ConfigParser()
        config_read.read(settings_path)
        is_internal = config_read['DISPLAY']['custom_fullscreen_values']
        if is_internal == '"false"':
            self.is_on_int = False
        else:
            self.is_on_int = True
        return self.is_on_int

    def internal_toggle(self):
        self.reader()
        if self.is_on_int is True:
            value = str('"') + "false" + str('"')
            self.internal_res.config(text="Custom Fullscreen Value is DISABLED", fg='red')
            self.is_on_int = False
            self.SetXButton.config(state=DISABLED)
            self.SetYButton.config(state=DISABLED)
            #print(is_on_int)
            editor('DISPLAY', 'custom_fullscreen_values', value)

        else:
            value = str('"') + "true" + str('"')
            editor('DISPLAY', 'custom_fullscreen_values', value)
            self.internal_res.config(text="Custom Fullscreen Value is ENABLED", fg='green')
            self.is_on_int = True
            self.SetXButton.config(state=NORMAL)
            self.SetYButton.config(state=NORMAL)
            #print(is_on_int)

    def InternalResX(self):
        value = str('"') + str(self.internal_res_x.get()) + str('"')  # gets the res as (ex: 1920 --> "1920")
        editor('DISPLAY', 'fullscreen_X', value)
        self.SetXButton.config(text='Fullscreen Width Set! :)', fg='green')


    def InternalResY(self):
        value = str('"') + str(self.internal_res_y.get()) + str('"')  # gets the res as (ex: 1920 --> "1920")
        editor('DISPLAY', 'fullscreen_Y', value)
        self.SetYButton.config(text='Fullscreen Height Set! :)', fg='green')


class AudioSett:
    def __init__(self,parent):
        self.newWindowAudio = Toplevel(parent)
        self.newWindowAudio.title("Advanced Audio Settings")
        self.newWindowAudio.geometry("300x300")


        self.ui_init()

    def ui_init(self):
        self.Sound_Vol = Label(self.newWindowAudio, text="Sound Volume is: ", fg='white', bg='grey')
        self.Sound_Vol.pack()
        self.Sound_Up = Scale(self.newWindowAudio, from_=0.000000, to=100, orient=HORIZONTAL, command=self.pass_val)
        self.Sound_Up.pack()

        self.Music_Vol = Label(self.newWindowAudio, text="Music Volume is: ", fg='white', bg='grey')
        self.Music_Up = Scale(self.newWindowAudio, from_=0.000000, to=100, orient=HORIZONTAL,
                              command=self.pass_music_val)
        self.Music_Vol.pack()
        self.Music_Up.pack()

        self.Jingle_Vol = Label(self.newWindowAudio, text="Jingle Volume is: ", fg='white', bg='grey')
        self.Jingle_Up = Scale(self.newWindowAudio, from_=0.000000, to=100, orient=HORIZONTAL,
                               command=self.pass_jingle_val)
        self.Jingle_Vol.pack()
        self.Jingle_Up.pack()

        self.Overall_Vol = Label(self.newWindowAudio, text="Overall Volume is: ", fg='white', bg='grey')
        self.Overall_Up = Scale(self.newWindowAudio, from_=0.000000, to=100, orient=HORIZONTAL,
                                command=self.pass_overall_val)
        self.Overall_Vol.pack()
        self.Overall_Up.pack()

    def pass_val(self, value):
        self.sound_val_config(value)
        self.Sound_Vol.config(text="Sound Volume is: {}%".format(value))

    def pass_music_val(self, value):
        self.music_val_config(value)
        self.Music_Vol.config(text="Music Volume is: {}%".format(value))

    def pass_jingle_val(self, value):
        self.jingle_val_config(value)
        self.Jingle_Vol.config(text="Jingle Volume is: {}%".format(value))

    def pass_overall_val(self, value):
        self.overall_val_config(value)
        self.Overall_Vol.config(text="Overall Volume is: {}%".format(value))

    def sound_val_config(self, value):
        val = int(value) / 100
        val_2 = round(val, 6)
        val_3 = '{:.6f}'.format(val_2)
        val_4 = quote_adder(val_3)
        editor('AUDIO', 'sound_volume', val_4)
        return val_3

    def overall_val_config(self, value):
        val = int(value) / 100
        val_2 = round(val, 6)
        val_3 = '{:.6f}'.format(val_2)
        val_4 = quote_adder(val_3)
        editor('AUDIO', 'overall_volume', val_4)
        return val_3

    def music_val_config(self, value):
        val = int(value) / 100
        val_2 = round(val, 6)
        val_3 = '{:.6f}'.format(val_2)
        val_4 = quote_adder(val_3)
        editor('AUDIO', 'music_volume', val_4)
        return val_3

    def jingle_val_config(self, value):
        val = int(value) / 100
        val_2 = round(val, 6)
        val_3 = '{:.6f}'.format(val_2)
        val_4 = quote_adder(val_3)
        editor('AUDIO', 'jingle_volume', val_4)
        return val_3

    def Overal_Volume(self):
        config_read = configparser.ConfigParser()
        config_read.read(settings_path)
        is_value = config_read['AUDIO']['overall_volume']
        is_value = quote_replacer(is_value)
        int_val = int(float(is_value)) * 100
        return int_val


if __name__ == "__main__":
    root = Tk()
    app_launcher = AppLauncher(root, app_icon_path)
    root.mainloop()
