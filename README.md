weShop to aplikacja stworzona na potrzeby przedmiotu "Projekt zespołowy" przez zespół:

Mykola Zhyhallo  
Dawid Morawiak  
Piotr Konarski  


Cel projektu:

Celem projektu jest stworzenie uniwersalnej aplikacji przeznaczonej głównie dla urządzeń mobilnych, ułatwiającej robienie zakupów.  
Aplikacja pozwala użytkownikowi tworzyć własną interaktywną listę zakupów, zsynchronizować ją ze zdalną bazą danych, a także udostępniać ją innym użytkownikom.  


Wykorzystane narzędzia:

Do realizacji projektu został wykorzystany język programowania Python (back-end).  
FastAPI framework umożliwił łatwą obsługę NodeJS, z pomocą którego powstał widoczny interfejs (front-end).  


Opis działania aplikacji:

Po uruchomieniu aplikacji wczytuje się pusta lista zakupów. Po wpisaniu nazwy przedmiotu w widoczne pole tekstowe i wciśnięciu przycisku "+", przedmiot ten zostaje dodany do listy zakupów. Jednocześnie lista ta jest natychmiast synchronizowana z serwerem. Aby oznaczyć przedmiot jako zakupiony lub dodany do koszyka, należy kliknąć przycisk z zieloną ikoną koszyka po prawej stronie od nazwy danego przedmiotu. Wszystkie przedmioty, zarówno te z listy, jak i te z koszyka, można w dowolnym momencie usunąć. Wystarczy kliknąć czerwony przycisk z ikoną kosza, znajdujący się po lewej stronie od nazwy danego przedmiotu. Oczywiście wszystkie te akcje również są na bieżąco aktualizowane w bazie danych, aby zachować aktualny wygląd naszej listy zakupów również po wyłączeniu i ponownym uruchomieniu aplikacji.  


Podsumowanie projektu:

Stworzona aplikacja świetnie spełnia swoje zadanie, ułatwiając wszelkiego rodzaju zakupy.  
Przy realizacji tego projektu jako zespół, mieliśmy możliwość ćwiczenia umiejętności pracy w zespole, obsługi Git Flow do organizacji pracy, oraz wykorzystywania Visual Studio Code i NodeJS do tego typu celów.  


Perspektywy dalszego rozwoju:

Istnieje masa możliwości rozwoju aplikacji weShop. Główna wizja polega na rozbudowie możliwości udostępniania własnej listy zakupów innym użytkownikom. Przykładowo dzieląc się ze znajomymi przepisem na jakieś danie, możliwe byłoby zamieszczenie linku do listy zakupów z potrzebnymi produktami. Lista dodawałaby się automatycznie do aplikacji po kliknięciu w link.  
Gdyby sieci sklepów zdecydowały się współpracować z naszą aplikacją, mogłyby one tworzyć bazę produktów, które można w ich sklepach nabyć. Pozwoliłoby to na wygenerowanie w aplikacji najoptymalniejszej trasy zakupów (aby kupić wszystkie przedmioty z listy w możliwie jak najmniejszej ilości sklepów).  
Ciekawym rozwiązaniem byłby również zaawansowany system inteligentnych powiadomień. Przypominałyby one o zrobieniu odpowiednich zakupów na przykład po wyjściu z pracy o określonej godzinie.
