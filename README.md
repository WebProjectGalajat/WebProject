# WebProject

## Important URLs
- https://spotipy.readthedocs.io/en/2.17.1/
- https://developer.spotify.com/documentation/general/guides/scopes/#user-top-read
- https://stmorse.github.io/journal/spotify-api.html

## Fitxers importants
- Carpeta WebProject: Repo global
- Carpeta WebProjectSpotify de fora: Projecte de django
- Carpeta WebProjectSpotify de dins: Fitxers de coses del projecte (?)
- Carpeta songlist: App de django

## Com fer deploy (HEROKU)
- *heroku login*
- Fer *git remote -v* per veure si el remot de heroku hi és, si no hi és afegirlo
- Afegir el remot de l'aplicació *git remote add heroku https://git.heroku.com/<nom_aplicacio_heroku>.git*
- Modificar el que sigui
- *git add -A*
- *git commit -m "missatge commit"*
- *git push heroku* per pujar els fitxers a Heroku, que farà un deploy automàtic


## Traduccio part del document:

Within the WebProjectSpotify directory we find the asgi.py file which is a file that defines our application path. The following file, called settings.py, is the central configuration of all Django-type projects, which has been modified to effectively run the Django application, provide end-users with a streamlined experience, and keep potential attackers under control. The urls.py file is used to update urls throughout the project. Finally we find the file wsgi.py which is the main deployment platform of Django, is the Python standard for servers and web applications.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Traduccio part del document (II):

The views.py file is the script that reveals the links of which the website is composed. Inside the document we have the urls of: main, of the shop, dashboard, and the register.
Within the directory 'webspoty' we find the file dashboard.html which implements the change of passwords therefore it is the section that redirects you.
The index.html file contains the links for the login and register buttons. In the 'registration' directory are the login html files, logout, password_change_done, password_change_form in addition to the register. These elements allow the identification, registration and modification of users on the web.
