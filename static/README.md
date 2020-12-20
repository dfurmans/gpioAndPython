FurmanS KendzioR 2018 !

Warte uwagi :
https://nestjs.com/
https://feathersjs.com/

0. Wszystkie tutoriale prosze szukac na http://books.goalkicker.com/

1. Technologia wiodaca : PYTHON
2. Framework : http://flask.pocoo.org/
3. GPIO : RPi.GPIO
4. MODEL ZARZEN OBSLUGI GUZIKOW : FIFO
5. MODEL komunikacji KLIENT-SERVER : na bazie WebSocket protokol
6. WIDOK  : REALIZOWANY ZA POMOCA HTML ORAZ JavaScript

=============
URUCHOMINIE APLIKACJI
=============
0. W CONSOLI  W KATALOGU GLOWNYM APLIKACJI
1. FLASK_APP=kendzioRFurmanSedzia.py flask run
2. APLIKACJA EXPONUJE 1.  ENDPOINT PO PROTOKOLE HTTP na PORCIE TCP 5000 I IP 127.0.0.1 to znaczy ze nalezy wejsc w przegladarke i wpisac
3. http://127.0.0.1:5000/ 




Lista zakupów została zrelizowana 30.01.2018 
TODO:: AKTUALIZOWAC CO ZOSTALO KUPIONE 

DNIA 30.01.2018 O GODZINIE 13 ZOSTAŁO KUPIONE:

1. SWT-05284 Arcade Push Button 3,3cm czarna obudowa - biały z podświetleniem 5,50 zł x3=16,50 zł
2. SWT-05281 Arcade Push Button 3,3cm czarna obudowa - niebieski z podświetleniem 5,50 zł x3=16,50 zł
3. RPI-05576 Raspberry Pi 3 model B WiFi Bluetooth 1GB RAM 1,2GHz 169,00 zł
4. ZAS-09707 Zasilacz microUSB 5,1V / 3A do Raspberry Pi 3/2/B+/ZeroZasilacz microUSB 5,1V / 3A do Raspberry Pi
   3/2/B+/Zero 34,90 zł
5. SPF-01630 Moduł z multiplekserem analogowo-cyfrowym 74HC4067 - SparkFun 19,90 zł
6. KAB-01450 Zestaw goldpin raster 2,54mm - mini 4,90 zł
7. NSZ-03341 Organizer Knox NO35 2,95 zł
8. KAB-01223 Przewody połączeniowe męsko-męskie 20cm - 40szt. 5,95 zł
9. KAB-01021 Przewody połączeniowe żeńsko-żeńskie 20cm - 40szt. 5,95 zł

DNIA 05.02.2018 O GODZINIE 17 ZOSTAŁO KUPIONE:

1. Karta pamięci micro SDHC UHS-I, class 10, 16GB - 39,98 zł

DNIA 05.02.2018 O GODZINIE 19 ZOSTAŁO KUPIONE:

1. Przejściówka HDMI-VGA - 25 zł
BRAKUJE:

1. Przejściówka (kupię ją, bo uważam że się przyda :D)- KUPIONA JUŻ- pomysł podłączenia maliny i sterowania zdalnie mi się podoba i go wykorzystam na 100% przy innym projekcie :-) rozważam kupno swojej maliny xD
Nie ma co wydawać kasy na przejścówkę! Można to inaczej zrobić:
a. Podlaczyc Maline pod RJ45 tak żeby można było ja w sieci widać - po prostu pod ruter podlaczyć
b. Zainstalować na Malinie ScreenServer - coś co wysyla dane eknrau przez siec - jest troche takich aplikacji po Linux
c. Zainstalowac na Widnows ScreenClient - tak zeby odebrac te dane z sieci (adres IP oraz PORT TCP) z Maliny
d. Wysiwetlić na Widnows to co jest na malinie - tym sposobem zaosszczedzi sie ne przejsciowce - ale bedzie troche konfiguracji pewie i bledow pod drodze
2. Obudowa do maliny i "guzik-box" x3
3. Cygaro zwycięstwa x2

KASA:

30.01.2018:
Produkty 276,55 zł
Wysyłka 12,90 zł
Razem 289,45 zł

05.02.2018:
Karta pamięci 39,98 zł

06.02.2018
Przejściówka HDMI-VGA 25zł

SUMA CAŁKOWITA :354,43: PLN
==============================================


GUZIOLE

Lista rzeczy do kupienia::

1. Raspberry PI - wraz z zasilaczeem Kartą SD oraz obudową 
2. Mux na GPIO dla Raspberry PI - https://www.sparkfun.com/products/9056 - wraz z potrzebnymi PINami do podpięcia RPI i guzików
3. Guziole - tak zeby mozna bylo je podlaczyc do MUX - sygnal Analog => Digital via Mux into Raspberry PI 
4. Kabel HDMI - tak zeby podłaczyć televizor

Po otrzymaniu Raspberry PI
1. Instalacja i konfiguracaja systemu operacujnego
W szczegloności :
1.1biblioteka dla GPIO dla Python lub C
https://sourceforge.net/p/raspberry-gpio-python/ 
1.2 Instalacja servera WWW 
1.3 Instalacja Bazy danych - postgreSQL
1.4. Instalacja clienta SSH - tak zeby zdalnie mozna bylo sie zalogowac na te maszyne

Po instalacji tych rzeczy należy:
1. Właściie połączyć mux do GPIO do RPI
2. Podłączyć zasilanie i RJ45 dla RPI 
3. Wystawic RPI na zewnatrz - tutaj moga być większe trudności - należy skonfigurować DDNS i klienta SSH

Po tym będzie można pod MUX podłączyć guziki i odbierać z nich sygnał z GPIO
do tego należy :

1. Napisać aplikacje w Python lub C która będzie odpowiadzielana za odbior sygnalu z guziolow via MUX
2. Zastanowaic sie jak skladowac i prezentowac odebrane dane - ostatni krok implementacji

++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Opis, cel i wymagania projektu "System punktacji pakerów"

1. Opis- Trzech sędziów w określonym czasie ocenia ćwiczenie wykonane przez zawodnika.
   Żaden z sędziów nie widzi na ekranie jaki głos oddał inny sędzia do momentu aż ostatni sędzia odda głos, wtedy to na ekranie mają pokazać się wyniki.
   System oceny jest dwupunktowy, czyli tak lub nie, co graficznie jest prezentowane na ekranie odpowiednimi kolorami -zielony TAK, czerwony NIE.
2. Cel- "Graficznie" zaprezentowane oceny jakie uzyskał zawodnik, tak aby nawet chińczyk nie znający innego słowa niż "kutak w ćeśćie" mógł zrozumieć czy przechodzi dalej.
3. Wymagania- sędzia może zmienić ocenę do momentu, aż zebrane zostaną trzy głosy, wtedy na ekranie pojawia się wynik, a oddane głosy zostają "zamrożone".
   Ekran podzielony jest na trzy pola, każde zarezerwowane jest dla jednego z trzech sędziów. Pola są np. białe, aż do momentu kiedy zostanie wyświetlony wynik, wtedy pola zmieniają kolor odpowiednio dla oddanego głosu na zielony lub czerwony.
   Wynik, pojawia się dopiero w momencie, kiedy to ostani sędzia odda głos -obojętne który z trzech. 
4. Zagwozdki- Kiedy rozpoczyna się nowa runda? 1. Po naciśnięciu innego guzika? 2. Po upływie określonego czasu od wyświetlenia guzika system ma być gotowy na kolejne oddawanie głosów?
