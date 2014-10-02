Viikkoharjoitus 2: Datastore
----------------------------

Datastore on App Enginen tarjoama tietokanta.
Sitä voi Python- App Engine -sovelluksesta käyttää ndb-kirjaston avulla.
Ndb-kirjastoon ja Datastoreen yleensäkin voi tutustua vaikka tästä linkistä:

https://cloud.google.com/appengine/docs/python/ndb/

Myös tästä videosta voi olla iloa Datastoren ymmärtämisessä:

https://www.youtube.com/watch?v=fQazhzcC-rg

## Tehtävä: luo eläinten ravintoketjutietokanta
1. Kloonaa itsellesi tämä git-repositorio. Se sisältää App Engine web-sovelluksen, jossa voi lisätä eläimiä sekä eläimille saaliseläimiä. Vain eläimien tallennus tietokantaan ja haku tietokannasta on toteuttamatta.
2. Toteuta ravintoketjusovelluksen Datastore-yhteys ndb-kirjaston avulla.
3. Lisäksi voit miettiä seuraavia kysymyksiä
    - Onko toteutuksesi vahvasti konsistentti (*strongly consistent*) - eli oletko varma, että haku palauttaa kaikki hakua ennen tallennetut tiedot?
    - Miten hakisit tietyn eläimen saalistajat - eli sellaiset eläimet, joiden saaliseläimenä X on?
