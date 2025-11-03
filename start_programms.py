"""
Author: Samuel B.
description: this is to start programms that are listed in a json file properly
Version: 1.0
"""

import os
import platform
import subprocess
import tkinter
import webbrowser

import json


class OpenProgramms():
    def update(self):
        dir_list = os.listdir("json")
        self.modes = []
        self.files = []
        for mode in dir_list:
            if mode.endswith(".json"):
                self.files.append(mode)
                self.modes.append(mode.replace(".json", ""))

    def __init__(self):
        self.file = None
        self.mode = None
        self.modes = None
        self.files = None
        self.os = platform.system()
        self.update()  # creates variables

    def setup(self, mode):
        self.mode = mode
        self.file = "json/" + mode + ".json"

    def check_for_mode(self):
        if not os.path.exists(self.file):
            print(f'You idiot "{self.mode}" isn\'t a supported mode!')
        return os.path.exists(self.file)

    def start_programms(self):
        with open(self.file) as json_file:
            json_object = json.load(json_file)
            json_file.close()
        for item in json_object:
            if item == "webbrowser":
                lst = json_object[item].split(';')
                print(lst)
                for i in lst:
                    webbrowser.open(i)
            elif os.path.exists(json_object[item]):
                if (self.os.lower() == "windows"):
                    os.startfile(json_object[item])
                else:
                    subprocess.Popen(json_object[item])


class OpenProgrammsTkinter():
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("Start Programms")
        self.logic_class = OpenProgramms()

    def _items_selected(self, event):
        # get all selected indices
        selected_mode = self.listbox.get(self.listbox.curselection()[0])
        self.logic_class.setup(selected_mode)
        self.logic_class.start_programms()
        self.root.quit()

    def _setup(self):
        var = tkinter.Variable(value=self.logic_class.modes)
        self.listbox = tkinter.Listbox(self.root, listvariable=var, height=15, width=50, selectmode=tkinter.SINGLE,
                                       justify="center")
        self.listbox.pack()
        self.listbox.bind('<Double-1>', self._items_selected)

    def run(self):
        self._setup()
        self.root.mainloop()
            - type: custom-api
              title: Minecraft
              url: https://api.mcstatus.io/v2/status/java/${MC_SERVER_URL}
              cache: 30s
              template: |
                <div style="display:flex; align-items:center; gap:12px;">
                  <div style="width:40px; height:40px; flex-shrink:0;  border-radius:4px; display:flex; justify-content:center; align-items:center; overflow:hidden;">
                    {{ if .JSON.Bool "online" }}
                      <img src="{{ .JSON.String "icon" | safeURL }}" width="64" height="64" style="object-fit:contain;">
                    {{ else }}
                      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" style="width:32px; height:32px; opacity:0.5;">
                        <path fill-rule="evenodd" d="M1 5.25A2.25 2.25 0 0 1 3.25 3h13.5A2.25 2.25 0 0 1 19 5.25v9.5A2.25 2.25 0 0 1 16.75 17H3.25A2.25 2.25 0 0 1 1 14.75v-9.5Zm1.5 5.81v3.69c0 .414.336.75.75.75h13.5a.75.75 0 0 0 .75-.75v-2.69l-2.22-2.219a.75.75 0 0 0-1.06 0l-1.91 1.909.47.47a.75.75 0 1 1-1.06 1.06L6.53 8.091a.75.75 0 0 0-1.06 0l-2.97 2.97ZM12 7a1 1 0 1 1-2 0 1 1 0 0 1 2 0Z" clip-rule="evenodd" />
                      </svg>
                    {{ end }}
                  </div>

                  <div style="flex-grow:1; min-width:0;">
                    <a class="size-h4 block text-truncate color-highlight">
                      {{ .JSON.String "host" }}
                      {{ if .JSON.Bool "online" }}
                      <span
                        style="width: 8px; height: 8px; border-radius: 50%; background-color: var(--color-positive); display: inline-block; vertical-align: middle;"
                        data-popover-type="text"
                        data-popover-text="Online"
                      ></span>
                      {{ else }}
                      <span
                        style="width: 8px; height: 8px; border-radius: 50%; background-color: var(--color-negative); display: inline-block; vertical-align: middle;"
                        data-popover-type="text"
                        data-popover-text="Offline"
                      ></span>
                      {{ end }}
                    </a>

                    <ul class="list-horizontal-text">
                      <li>
                        {{ if .JSON.Bool "online" }}
                        <span>{{ .JSON.String "version.name_clean" }}</span>
                        {{ else }}
                        <span>Offline</span>
                        {{ end }}
                      </li>
                      {{ if .JSON.Bool "online" }}
                      <li data-popover-type="html">
                        <div data-popover-html>
                          {{ range .JSON.Array "players.list" }}{{ .String "name_clean" }}<br>{{ end }}
                        </div>
                        <p style="display:inline-flex;align-items:center;">
                          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="size-6" style="height:1em;vertical-align:middle;margin-right:0.5em;">
                            <path fill-rule="evenodd" d="M7.5 6a4.5 4.5 0 1 1 9 0 4.5 4.5 0 0 1-9 0ZM3.751 20.105a8.25 8.25 0 0 1 16.498 0 .75.75 0 0 1-.437.695A18.683 18.683 0 0 1 12 22.5c-2.786 0-5.433-.608-7.812-1.7a.75.75 0 0 1-.437-.695Z" clip-rule="evenodd" />
                          </svg>
                          {{ .JSON.Int "players.online" | formatNumber }}/{{ .JSON.Int "players.max" | formatNumber }} players
                        </p>
                      </li>
                      {{ else }}
                      <li>
                        <p style="display:inline-flex;align-items:center;">
                          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" class="size-6" style="height:1em;vertical-align:middle;margin-right:0.5em;opacity:0.5;">
                            <path fill-rule="evenodd" d="M7.5 6a4.5 4.5 0 1 1 9 0 4.5 4.5 0 0 1-9 0ZM3.751 20.105a8.25 8.25 0 0 1 16.498 0 .75.75 0 0 1-.437.695A18.683 18.683 0 0 1 12 22.5c-2.786 0-5.433-.608-7.812-1.7a.75.75 0 0 1-.437-.695Z" clip-rule="evenodd" />
                          </svg>
                          0 players
                        </p>
                      </li>
                      {{ end }}
                    </ul>
                  </div>
                </div>