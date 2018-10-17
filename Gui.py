#!/usr/bin/env python3
from argparse import Namespace
from glob import glob
import json
import random
import os
import shutil
from tkinter import Checkbutton, OptionMenu, Toplevel, LabelFrame, PhotoImage, Tk, LEFT, RIGHT, BOTTOM, TOP, StringVar, IntVar, Frame, Label, W, E, X, Entry, Spinbox, Button, filedialog, messagebox, ttk
from urllib.parse import urlparse
from urllib.request import urlopen

from GuiUtils import ToolTips, set_icon, BackgroundTaskProgress
from Main import main, __version__ as ESVersion
from Utils import is_bundled, local_path, output_path, open_file

def settings_to_guivars(settings, guivars):
    for info in setting_infos:
        name = info.name
        if name not in guivars:
            continue
        guivar = guivars[name]
        value = settings.__dict__[name]
        # checkbox
        if info.type == bool:
            guivar.set( int(value) )
        # dropdown/radiobox
        if info.type == str:
            if value is None:
                guivar.set( "" )
            else:
                if info.gui_params and 'options' in info.gui_params:
                    if 'Custom Color' in info.gui_params['options'] and re.match(r'^[A-Fa-f0-9]{6}$', value):
                        guivar.set('Custom (#' + value + ')')
                    else:
                        for gui_text,gui_value in info.gui_params['options'].items():
                            if gui_value == value:
                                guivar.set( gui_text )
                else:
                    guivar.set( value )
        # text field for a number...
        if info.type == int:
            if value is None:
                guivar.set( str(1) )
            else:
                guivar.set( str(value) )

def guivars_to_settings(guivars):
    result = {}
    for info in setting_infos:
        name = info.name
        if name not in guivars:
            result[name] = None
            continue
        guivar = guivars[name]
        # checkbox
        if info.type == bool:
            result[name] = bool(guivar.get())
        # dropdown/radiobox
        if info.type == str:
            # set guivar to hexcode if custom color
            if re.match(r'^Custom \(#[A-Fa-f0-9]{6}\)$', guivar.get()):
                result[name] = re.findall(r'[A-Fa-f0-9]{6}', guivar.get())[0]
            elif info.gui_params and 'options' in info.gui_params:
                result[name] = info.gui_params['options'][guivar.get()]
            else:
                result[name] = guivar.get()
        # text field for a number...
        if info.type == int:
            result[name] = int( guivar.get() )
    if result['seed'] == "":
        result['seed'] = None
    if result['count'] == 1:
        result['count'] = None

    return Settings(result)

def guiMain(settings=None):
    frames = {}

    mainWindow = Tk()
    mainWindow.wm_title("MM Randomizer")
    mainWindow.resizable(False, False)

    set_icon(mainWindow)

    notebook = ttk.Notebook(mainWindow)
    randomizerWindow = ttk.Frame(notebook)
    adjustWindow = ttk.Frame(notebook)
    customWindow = ttk.Frame(notebook)
    notebook.add(randomizerWindow, text='Randomize')
    notebook.pack()

    # Shared Controls

    farBottomFrame = Frame(mainWindow)

    # hierarchy
    ############

    #Rules Tab
    frames['open']   = LabelFrame(frames['rules_tab'], text='Open',   labelanchor=NW)
    frames['world']  = LabelFrame(frames['rules_tab'], text='World',   labelanchor=NW)
    frames['logic']  = LabelFrame(frames['rules_tab'], text='Shuffle',  labelanchor=NW)

    # Logic tab
    frames['rewards'] = LabelFrame(frames['logic_tab'], text='Remove Specific Locations', labelanchor=NW)
    frames['tricks']  = LabelFrame(frames['logic_tab'], text='Specific expected tricks', labelanchor=NW)

    #Other Tab
    frames['convenience'] = LabelFrame(frames['other_tab'], text='Speed Ups', labelanchor=NW)
    frames['other']       = LabelFrame(frames['other_tab'], text='Misc',      labelanchor=NW)

    #Aesthetics tab
    frames['cosmetics'] = LabelFrame(frames['aesthetic_tab'], text='General', labelanchor=NW)
    frames['tuniccolor'] = LabelFrame(frames['aesthetic_tab_left'], text='Tunic Color', labelanchor=NW)
    frames['navicolor']  = LabelFrame(frames['aesthetic_tab_right'], text='Navi Color',  labelanchor=NW)
    frames['lowhp']      = LabelFrame(frames['aesthetic_tab_left'], text='Low HP SFX',  labelanchor=NW)
    frames['navihint']   = LabelFrame(frames['aesthetic_tab_right'], text='Navi SFX', labelanchor=NW)


    # shared
    settingsFrame = Frame(mainWindow)
    settings_string_var = StringVar()
    settingsEntry = Entry(settingsFrame, textvariable=settings_string_var, width=25)

    def show_settings(event=None):
        settings = guivars_to_settings(guivars)
        settings_string_var.set( settings.get_settings_string() )

        # Update any dependencies
        for info in setting_infos:
            if info.gui_params and 'dependency' in info.gui_params:
                dep_met = info.gui_params['dependency'](guivars)

                if widgets[info.name].winfo_class() == 'Frame':
                    for child in widgets[info.name].winfo_children():
                        if child.winfo_class() == 'TCombobox':
                            child.configure(state= 'readonly' if dep_met else 'disabled')
                        else:
                            child.configure(state= 'normal' if dep_met else 'disabled')

                        if child.winfo_class() == 'Scale':
                            child.configure(fg='Black'if dep_met else 'Grey')
                else:
                    if widgets[info.name].winfo_class() == 'TCombobox':
                        widgets[info.name].configure(state= 'readonly' if dep_met else 'disabled')
                    else:
                        widgets[info.name].configure(state= 'normal' if dep_met else 'disabled')

                    if widgets[info.name].winfo_class() == 'Scale':
                        widgets[info.name].configure(fg='Black'if dep_met else 'Grey')


            if info.name in guivars and guivars[info.name].get() == 'Custom Color':
                color = askcolor()
                if color == (None, None):
                    color = ((0,0,0),'#000000')
                guivars[info.name].set('Custom (' + color[1] + ')')

    def show_settings_special(event=None):
        if guivars['logic_tricks'].get():
            widgets['logic_man_on_roof'].select()
            widgets['logic_child_deadhand'].select()
            widgets['logic_dc_jump'].select()
            widgets['logic_windmill_poh'].select()
            widgets['logic_crater_bean_poh_with_hovers'].select()
            widgets['logic_zora_with_cucco'].select()
            widgets['logic_fewer_tunic_requirements'].select()
        else:
            widgets['logic_man_on_roof'].deselect()
            widgets['logic_child_deadhand'].deselect()
            widgets['logic_dc_jump'].deselect()
            widgets['logic_windmill_poh'].deselect()
            widgets['logic_crater_bean_poh_with_hovers'].deselect()
            widgets['logic_zora_with_cucco'].deselect()
            widgets['logic_fewer_tunic_requirements'].deselect()
        settings = guivars_to_settings(guivars)
        settings_string_var.set( settings.get_settings_string() )



    def import_settings(event=None):
        try:
            settings = guivars_to_settings(guivars)
            text = settings_string_var.get().upper()
            settings.seed = guivars['seed'].get()
            settings.update_with_settings_string(text)
            settings_to_guivars(settings, guivars)
        except Exception as e:
            messagebox.showerror(title="Error", message="Invalid settings string")

    label = Label(settingsFrame, text="Settings String")
    importSettingsButton = Button(settingsFrame, text='Import Settings String', command=import_settings)
    label.pack(side=LEFT, anchor=W, padx=5)
    settingsEntry.pack(side=LEFT, anchor=W)
    importSettingsButton.pack(side=LEFT, anchor=W, padx=5)



    fileDialogFrame = Frame(frames['rom_tab'])

    romDialogFrame = Frame(fileDialogFrame)
    baseRomLabel = Label(romDialogFrame, text='Base ROM')
    guivars['rom'] = StringVar(value='ZOOTDEC.z64')
    romEntry = Entry(romDialogFrame, textvariable=guivars['rom'], width=40)

    def RomSelect():
        rom = filedialog.askopenfilename(filetypes=[("ROM Files", (".z64", ".n64")), ("All Files", "*")])
        if rom != '':
            guivars['rom'].set(rom)
    romSelectButton = Button(romDialogFrame, text='Select ROM', command=RomSelect, width=10)

    baseRomLabel.pack(side=LEFT, padx=(38,0))
    romEntry.pack(side=LEFT, padx=3)
    romSelectButton.pack(side=LEFT)

    romDialogFrame.pack()

    fileDialogFrame.pack(side=TOP, anchor=W, padx=5, pady=(5,1))

    def open_output():
        open_file(output_path(''))

    def output_dir_select():
        rom = filedialog.askdirectory(initialdir = default_output_path(guivars['output_dir'].get()))
        if rom != '':
            guivars['output_dir'].set(rom)

    openOutputButton = Button(farBottomFrame, text='Open Output Directory', command=open_output)

    if os.path.exists(local_path('README.html')):
        def open_readme():
            open_file(local_path('README.html'))
        openReadmeButton = Button(farBottomFrame, text='Open Documentation', command=open_readme)
        openReadmeButton.pack(side=LEFT)

    farBottomFrame.pack(side=BOTTOM, fill=X, padx=5, pady=5)

    # randomizer controls

    topFrame = Frame(randomizerWindow)
    rightHalfFrame = Frame(topFrame)
    checkBoxFrame = Frame(rightHalfFrame)

    createSpoilerVar = IntVar()
    createSpoilerCheckbutton = Checkbutton(checkBoxFrame, text="Create Spoiler Log", variable=createSpoilerVar)
    suppressRomVar = IntVar()
    suppressRomCheckbutton = Checkbutton(checkBoxFrame, text="Do not create patched Rom", variable=suppressRomVar)
    compressRomVar = IntVar()
    compressRomCheckbutton = Checkbutton(checkBoxFrame, text="Compress patched Rom", variable=compressRomVar)
    openForestVar = IntVar()
    openForestCheckbutton = Checkbutton(checkBoxFrame, text="Open Forest", variable=openForestVar)
    openDoorVar = IntVar()
    openDoorCheckbutton = Checkbutton(checkBoxFrame, text="Open Door of Time", variable=openDoorVar)
    dungeonItemsVar = IntVar()
    dungeonItemsCheckbutton = Checkbutton(checkBoxFrame, text="Place Dungeon Items (Compasses/Maps)", onvalue=0, offvalue=1, variable=dungeonItemsVar)
    beatableOnlyVar = IntVar()
    beatableOnlyCheckbutton = Checkbutton(checkBoxFrame, text="Only ensure seed is beatable, not all items must be reachable", variable=beatableOnlyVar)
    hintsVar = IntVar()
    hintsCheckbutton = Checkbutton(checkBoxFrame, text="Gossip Stone Hints with Stone of Agony", variable=hintsVar)

    createSpoilerCheckbutton.pack(expand=True, anchor=W)
    suppressRomCheckbutton.pack(expand=True, anchor=W)
    compressRomCheckbutton.pack(expand=True, anchor=W)
    openForestCheckbutton.pack(expand=True, anchor=W)
    openDoorCheckbutton.pack(expand=True, anchor=W)
    dungeonItemsCheckbutton.pack(expand=True, anchor=W)
    beatableOnlyCheckbutton.pack(expand=True, anchor=W)
    hintsCheckbutton.pack(expand=True, anchor=W)

    fileDialogFrame = Frame(rightHalfFrame)

    romDialogFrame = Frame(fileDialogFrame)
    baseRomLabel = Label(romDialogFrame, text='Base Rom')
    romVar = StringVar()
    romEntry = Entry(romDialogFrame, textvariable=romVar)

    def RomSelect():
        rom = filedialog.askopenfilename(filetypes=[("Rom Files", (".z64", ".n64")), ("All Files", "*")])
        romVar.set(rom)
    romSelectButton = Button(romDialogFrame, text='Select Rom', command=RomSelect)

    baseRomLabel.pack(side=LEFT)
    romEntry.pack(side=LEFT)
    romSelectButton.pack(side=LEFT)

    romDialogFrame.pack()

    checkBoxFrame.pack()
    fileDialogFrame.pack()

    drowDownFrame = Frame(topFrame)


    bridgeFrame = Frame(drowDownFrame)
    bridgeVar = StringVar()
    bridgeVar.set('medallions')
    bridgeOptionMenu = OptionMenu(bridgeFrame, bridgeVar, 'medallions', 'vanilla', 'dungeons', 'open')
    bridgeOptionMenu.pack(side=RIGHT)
    bridgeLabel = Label(bridgeFrame, text='Rainbow Bridge Requirement')
    bridgeLabel.pack(side=LEFT)

    bridgeFrame.pack(expand=True, anchor=E)

    bottomFrame = Frame(randomizerWindow)

    seedLabel = Label(bottomFrame, text='Seed #')
    seedVar = StringVar()
    seedEntry = Entry(bottomFrame, textvariable=seedVar)
    countLabel = Label(bottomFrame, text='Count')
    countVar = StringVar()
    countSpinbox = Spinbox(bottomFrame, from_=1, to=100, textvariable=countVar)


    notebook.pack(fill=BOTH, expand=True, padx=5, pady=5)

    multiworldFrame = LabelFrame(frames['rom_tab'], text='Multi-World Generation')
    countLabel = Label(multiworldFrame, wraplength=350, justify=LEFT, text='This is used for co-op generations. Increasing Player Count will drastically increase the generation time. For more information see:')
    hyperLabel = Label(multiworldFrame, wraplength=350, justify=LEFT, text='https://github.com/TestRunnerSRL/bizhawk-co-op', fg='blue', cursor='hand2')
    hyperLabel.bind("<Button-1>", lambda event: webbrowser.open_new(r"https://github.com/TestRunnerSRL/bizhawk-co-op"))
    countLabel.pack(side=TOP, anchor=W, padx=5, pady=0)
    hyperLabel.pack(side=TOP, anchor=W, padx=5, pady=0)


    worldCountFrame = Frame(multiworldFrame)
    countLabel = Label(worldCountFrame, text='Player Count')
    guivars['world_count'] = StringVar()
    countSpinbox = Spinbox(worldCountFrame, from_=1, to=100, textvariable=guivars['world_count'], width=3)

    countLabel.pack(side=LEFT)
    countSpinbox.pack(side=LEFT, padx=2)
    worldCountFrame.pack(side=LEFT, anchor=N, padx=10, pady=(1,5))

    playerNumFrame = Frame(multiworldFrame)
    countLabel = Label(playerNumFrame, text='Player ID')
    guivars['player_num'] = StringVar()
    countSpinbox = Spinbox(playerNumFrame, from_=1, to=100, textvariable=guivars['player_num'], width=3)

    countLabel.pack(side=LEFT)
    countSpinbox.pack(side=LEFT, padx=2)
    playerNumFrame.pack(side=LEFT, anchor=N, padx=10, pady=(1,5))
    multiworldFrame.pack(side=TOP, anchor=W, padx=5, pady=(1,1))


    # didn't refactor the rest, sorry


    # create the option menu

    settingsFrame.pack(fill=BOTH, anchor=W, padx=5, pady=(10,0))

    def multiple_run(settings, window):
        orig_seed = settings.seed
        for i in range(settings.count):
            settings.update_seed(orig_seed + '-' + str(i))
            window.update_title("Generating Seed...%d/%d" % (i+1, settings.count))
            main(settings, window)

    def generateRom():
        guiargs = Namespace
        guiargs.seed = int(seedVar.get()) if seedVar.get() else None
        guiargs.count = int(countVar.get()) if countVar.get() != '1' else None
        guiargs.bridge = bridgeVar.get()
        guiargs.create_spoiler = bool(createSpoilerVar.get())
        guiargs.suppress_rom = bool(suppressRomVar.get())
        guiargs.compress_rom = bool(compressRomVar.get())
        guiargs.open_forest = bool(openForestVar.get())
        guiargs.open_door_of_time = bool(openDoorVar.get())
        guiargs.nodungeonitems = bool(dungeonItemsVar.get())
        guiargs.beatableonly = bool(beatableOnlyVar.get())
        guiargs.hints = bool(hintsVar.get())
        guiargs.rom = romVar.get()
        try:
            if guiargs.count is not None:
                seed = guiargs.seed
                for _ in range(guiargs.count):
                    main(seed=seed, args=guiargs)
                    seed = random.randint(0, 999999999)
            else:
                main(seed=guiargs.seed, args=guiargs)
        except Exception as e:
            messagebox.showerror(title="Error while creating seed", message=str(e))
        else:
            messagebox.showinfo(title="Success", message="Rom patched successfully")

    generateButton = Button(bottomFrame, text='Generate Patched Rom', command=generateRom)

    seedLabel.pack(side=LEFT)
    seedEntry.pack(side=LEFT)
    countLabel.pack(side=LEFT, padx=(5, 0))
    countSpinbox.pack(side=LEFT)
    generateButton.pack(side=LEFT, padx=(5, 0))

    openOutputButton.pack(side=RIGHT)

    drowDownFrame.pack(side=LEFT)
    rightHalfFrame.pack(side=RIGHT)
    topFrame.pack(side=TOP)
    bottomFrame.pack(side=BOTTOM)

    if args is not None:
        # load values from commandline args
        createSpoilerVar.set(int(args.create_spoiler))
        suppressRomVar.set(int(args.suppress_rom))
        compressRomVar.set(int(args.compress_rom))
        if args.nodungeonitems:
            dungeonItemsVar.set(int(not args.nodungeonitems))
        openForestVar.set(int(args.open_forest))
        openDoorVar.set(int(args.open_door_of_time))
        beatableOnlyVar.set(int(args.beatableonly))
        hintsVar.set(int(args.hints))
        if args.count:
            countVar.set(str(args.count))
        if args.seed:
            seedVar.set(str(args.seed))
        bridgeVar.set(args.bridge)
        romVar.set(args.rom)

    mainWindow.mainloop()

if __name__ == '__main__':
    guiMain()
