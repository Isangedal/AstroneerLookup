import requests

def run(version, appname):
    # Get the html from "http://www.isangedal.7m.pl/websites/version/{appname}.php"
    # This will return a new url. Go to that url and get the html.
    # That html will contain the version number.
    # If the version number is equal to "version", return "OK"
    # If the version number is LESS than "version", return "AHEAD"
    # If the version number is GREATER than "version", print "link" which is the link to download the latest version then return "OUTDATED"
    # If any other error occurs, return "ERROR"

    r = requests.get(f"http://www.isangedal.7m.pl/websites/version/{appname}.php")

    if r.status_code == 200:
        r2 = requests.get(r.text)
        text = float(r2.text)

        if r2.status_code == 200:
            if version == text:
                return "OK"
            elif version > text:
                return "AHEAD"
            else:
                return "OUTDATED"
        else:
            return "ERROR"
    else:
        return "ERROR"