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

:)

# Informació important DV2
Mencionar que hem canviat la web perk la api de spotify no funcionava
Per a modul·lar millor les funcions a implementar, hem separat l'app en les 3 instàncies principals, que són molt similars.
### Creació d'instàncies
Per a la creació d'instàncies ha sigut necessari crear una classe view, és a dir, utilitzarem una classe,
juntament amb el seu template, per a generar la nostra web, enlloc de definir una funció. Aquesta classe subclasse de CreateView
ens permet crear una web amb un formulari amb les dades de l'artista.
Aquest formulari és a partir d'una classe que hem definit a
forms.py, en la qual definim el formulari per a que demani totes les dades del model Favourite_Artist excepte l'usuari,
ja que no volem que un usuari creei artistes als altres usuaris. Amb la classe de la view, definim que l'usuari que es guarda
al formulari és el mateix que fa la request. Un cop s'ha respost el formulari i s'ha creat l'objecte, a l'usuari se li
mostra una pàgina amb els detalls de l'objecte que ha creat, creada amb la classe DetailView de Django, juntament amb
links per a modificar-lo, eliminar-lo, o tornar a la llista. Les cançons, gèneres i artistes utilitzen el mateix procediment.
### Modificació d'instàncies
Un cop creada una instància, des de la seva pàgina amb els detalls es pot entrar a una pàgina per modificar-la. Utilitzant un
procés similar a la creació, però aquest cop amb UpdateView, a l'usuari se li deixa modificar el rating i la descripció de
l'objecte, però no el seu nom, o, en el cas de les cançons, tampoc el nom de l'artista. Un cop acabat o cancel·lat, es torna
a la pàgina de detalls.
### Eliminació d'instàncies
Per a l'eliminació d'instàncies, utilitzem una funció a views que rep com a paràmetre l'id de l'objecte a borrar, que simplement
eliminem de la base de dades, i redireccionem a l'usuari un altre cop a la llista. No hi pot haver problemes amb el tipus
d'objecte a borrar, ja que la url que crida a views té el tipus d'objecte a borrar.
### Tests
Aaa nose
### Ús d'una API
La nostra web utilitza la llibreria jQuery per a poder oferir a l'usuari la funció d'autocomplete en certs camps al crear
un objecte a la web. La funció pot prendre com a paràmetre source, és a dir, d'on treurà els registres que oferirà a l'usuari
quan aquest escrigui, 3 tipus diferents de valors; una llista de JavaScript, un String o una funció. La llista de JavaScript
no ens permet la flexibilitat que necessitem i la funció és massa avançada pels nostres nivells de JavaScript. Per això hem
utilitzat l'String. Aquest String ha de ser una url, de manera que si la url és http://www.exemple.com, aquest domini ha de
respondre una resposta JSON amb els resultats a mostrar quan s'hi accedeix fent http://www.exemple.com?term=busqueda. Si
a source li passem una url de la nostra web, i definim una view que obtingui les dades i les retorni amb una JsonResponse,
podem realitzar la request a la API de forma molt més senzilla.
Quan l'usuari vol crear un artista, el camp name realitza l'autocomplete, realitzant una búsqueda a una API gratuïta amb
dades musicals anomenada MusicBrainz. Aquest autocomplete no funciona gaire bé, ja que MusicBrainz sol té un mètode per buscar
i no per buscar per l'inici. Llavors si l'usuari escriu "Que" esperant a que surti "Queen", abans li sortiran grups amb noms
com Que, [.que], o Gee-Que, ja que s'assemblen més al terme de búsqueda.  
Quan l'usuari vol crear un gènere, el camp name realitza l'autocomplete, llegint d'un fitxer amb uns 1800 gèneres
musicals diferents.  
Quan l'usuari vol crear una cançó, es realitza autocomplete a 2 camps; el gènere i el nom de l'artista. El gènere és igual que
si es crea un gènere, es llegeix del fitxer. El nom de l'artista, en canvi, enlloc de fer una búsqueda a la API de MusicBrainz,
dóna prioritat als artistes que ha afegit l'artista, de manera que si l'usuari ha afegit algun artista, li sortirà abans al autocomplete.
