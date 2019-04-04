import sys
import time
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from .activities import MoodActivity
from .theme import Shraavani, Colors


class SplashScreen:
    def __init__(self, tk_root, imageFilename, minSplashTime=0):
        im = Image.open(imageFilename).crop((0, 300, 1400, 1000))
        im.thumbnail((500, 500), Image.ANTIALIAS)

        self._root = tk_root
        self._image = ImageTk.PhotoImage(im)
        self._splash = None
        self._minSplashTime = time.time() + minSplashTime
        self.status = None
        s = Shraavani()
        s.apply()

    def __enter__(self):
        # Remove the app window from the display
        self._root.withdraw()

        # Calculate the geometry to center the splash image
        screen_wt = self._root.winfo_screenwidth()
        screen_ht = self._root.winfo_screenheight()

        img_wt = self._image.width()
        img_ht = self._image.height()

        img_x_pos = (screen_wt / 2) - (img_wt / 2)
        img_y_pos = (screen_ht / 2) - (img_ht / 2)

        # Create the splash screen
        self._splash = tk.Toplevel(self._root)
        self._splash.overrideredirect(1)
        self._splash.geometry('+%d+%d' % (img_x_pos, img_y_pos))
        self._splash.config(background=Colors.re_prim)
        ttk.Label(self._splash, image=self._image, cursor='watch').pack()
        self.status = ttk.Label(self._splash, text="Initializing ...", style='Splash.Label')
        self.status.pack(pady=(0, 5))

        # Force Tk to draw the splash screen outside of mainloop()
        self._splash.update()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # Make sure the minimum splash time has elapsed
        time_now = time.time()
        if time_now < self._minSplashTime:
            time.sleep(self._minSplashTime - time_now)

        self._splash.destroy()
        self._root.deiconify()

    def status_update(self, msg):
        self.status['text'] = msg
        self._splash.update()


class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        title, icon = kwargs.get('title', 'Vaaya'), kwargs.get('icon', 'logo.ico')
        kwargs.pop('title', None)
        kwargs.pop('icon', None)

        tk.Tk.__init__(self, *args, **kwargs)

        if sys.platform.startswith('win'):
            tk.Tk.iconbitmap(self, default=icon)
        else:
            tk.Tk.iconbitmap(self, bitmap='@'+icon)
        tk.Tk.wm_title(self, title)

        self.frames = {}

        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def setup(self, activities):
        for F in activities:
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MoodActivity)
        self.__center()

    def __center(self):
        self.eval('tk::PlaceWindow %s center' % self.winfo_toplevel())
