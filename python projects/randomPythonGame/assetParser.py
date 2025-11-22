import gui, json

with open("user.json", "r") as data:
    usrData = json.load(data) 

credits = usrData['credits']
manpower = usrData['manpower']

countryButton = gui.Button(780, 0, 150, 60, "Country", gui.SemiDarkBG, gui.LightBG)
techButton = gui.Button(930, 0, 150, 60, "Tech", gui.SemiDarkBG, gui.LightBG)
diplomaticButton = gui.Button(1080, 0, 200, 60, "Diplomacy", gui.SemiDarkBG, gui.LightBG)
topbanner = gui.Banner(0,0, 1280, 60, gui.DarkBG)
bottomBanner = gui.Banner(0,620, 800,150, gui.DarkBG)
creditsText = gui.TextEl(0,0, 200,60, "Credits: ", credits)
mpText = gui.TextEl(200,0, 200,60, "Manpower: ", manpower)


# Unit create buttons
