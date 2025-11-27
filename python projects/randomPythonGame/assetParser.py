import gui, json

with open("user.json", "r") as data:
    usrData = json.load(data) 

credits = usrData['credits']
manpower = usrData['manpower']

# Buttons
countryButton = gui.Button(780, 0, 150, 60, "Country", gui.SemiDarkBG, gui.LightBG)
techButton = gui.Button(930, 0, 150, 60, "Tech", gui.SemiDarkBG, gui.LightBG)
diplomaticButton = gui.Button(1080, 0, 200, 60, "Diplomacy", gui.SemiDarkBG, gui.LightBG)

# Banners
topBanner = gui.Banner(0,0, 1280, 60, gui.DarkBG)
bottomBanner = gui.Banner(0,570, 1000,150, gui.DarkBG)

# Text Elements
creditsText = gui.TextEl(0,0, 200,60, "Credits: ", credits)
mpText = gui.TextEl(200,0, 200,60, "Manpower: ", manpower)

# Unit create buttons
infantryButton = gui.Button(200, 600, 60, 60, "I", gui.SemiDarkBG, gui.LightBG)
tankButton = gui.Button(260, 600, 60, 60, "T", gui.SemiDarkBG, gui.LightBG)
artilleryButton = gui.Button(320, 600, 60, 60, "A", gui.SemiDarkBG, gui.LightBG)
aircraftButton = gui.Button(380, 600, 60, 60, "Ac", gui.SemiDarkBG, gui.LightBG)
navalButton = gui.Button(440, 600, 60, 60, "N", gui.SemiDarkBG, gui.LightBG)


# Tech Tree Surface
techTreeSurface = gui.Banner(100, 100, 600, 470, gui.LightBG)