# Royal Ride Dealership Centre Projekt


## PROJEKTIDEE
Entwicklung einer umfangreichen Konsolenanwendung in Python mit dem Namen "Royal Ride Dealership Centre", die den Benutzern die Verwaltung von Fahrzeugen für Verkauf, Kauf und Vermietung ermöglicht. Die Anwendung konzentriert sich auf die Implementierung von Funktionen in Python wie Benutzerauthentifizierung, Fahrzeugsuche und weitere. 
Die Mitarbeiter können Fahrzeuge hinzufügen, löschen, konfigurieren und auflisten. Kunden können Fahrzeuge kaufen, verkaufen, mieten und suchen. Gesten können sich registrieren bzw. anmelden. Die verfügbaren Fahrzeugtypen sind Auto, Motorrad, LKW und Boot, und die Parameter umfassen ID, Fahrzeugtyp, Marke, Modell, Preis, Jahr, Spezifikationen und Status.

## PROJEKTBESCHRIEB
Das Ziel dieses Projekts ist die Entwicklung einer umfassenden Python-Terminalanwendung für ein Autohandelszentrum, die Benutzern eine Vielzahl von Funktionen bietet, um den Kauf, Verkauf und die Miete von Fahrzeugen zu verwalten. Die Anwendung wird auf Funktionen und Logikentwicklung konzentriert sein, mit einem Schwerpunkt auf effizienten Abläufen und Benutzerinteraktion über die Befehlszeile.

Die wichtigsten Funktionen der Anwendung umfassen:
1.	Benutzerauthentifizierung und -registrierung: Benutzer können sich anmelden oder ein neues Konto erstellen, um auf die Funktionen der Anwendung zuzugreifen.
2.	Fahrzeugsuche und -browsing: Benutzer können nach Fahrzeugen suchen und alle verfügbaren Fahrzeuge durchsuchen, basierend auf die Marke.
3.	Fahrzeugkauf: Benutzer können Fahrzeuge kaufen, indem sie Details anzeigen, den Kaufprozess abschliessen und Zahlungen tätigen.
4.	Fahrzeugverkauf: Benutzer können ihre eigenen Fahrzeuge zum Verkauf anbieten, indem sie Details eingeben und das Fahrzeug in die Datenbank des Handelszentrums aufnehmen.
5.	Fahrzeugmiete: Benutzer können Fahrzeuge für Kurzzeit- oder Langzeitmiete ausleihen, indem sie Mietdetails eingeben und Reservierungen vornehmen.
6.  Die Anwendung wird auf die Entwicklung von Funktionen und die Logik hinter den verschiedenen Abläufen des Dealerships fokussiert sein.

## PROJEKTPLANUNG
1.	ZIELSETZUNG
-	Entwicklung einer Python-Konsolenanwendung zur Verwaltung von Fahrzeugen für den Verkauf, Kauf und Vermietung, mit Fokus auf Python Funktionen und SQLite Datenbank Implementierung.
2.	FUNKTIONEN

### Staff Funktionen
Add Vehicle;   
Add Staff Member;   
Delete Vehicle;   
Delete Client;   
Delete Staff Member;   
Configurate a Vehicle;   
List Vehicles;   
List Clients;   
List Staff Members;  

### Client Funktionen
Buy a Vehicle;   
Sell a Vehicle;   
Rent a Vehicle;   
Search a Vehicle;    
Browse all Vehicles;   

### Algemeine Funktionen  
Register;  
Login;


-	Benutzerauthentifizierung: Einloggen und Registrieren von Benutzern und Mitarbeiter.
-	Fahrzeugsuche: Suche nach Fahrzeugen basierend auf die Marke.
-	Fahrzeugkauf: Benutzer können Fahrzeuge kaufen, wobei verschiedene Zahlungsmethoden unterstützt werden wie Kartenzahlung oder Leasing.
-	Fahrzeugverkauf: Benutzer können ihre Fahrzeuge zum Verkauf anbieten.
-	Fahrzeugvermietung: Benutzer können Fahrzeuge für einen bestimmten Zeitraum mieten.
-	Anzeige aller verfügbaren Fahrzeuge: Benutzer können alle verfügbaren Fahrzeuge durchsuchen.

3.	PARAMETER
-	Vehicles: Car, Motorbike, Truck, Boat
-	Vehicle Parameters: ID, Vehicle Type, Brand, Model, Price, Year, Specifications, Status

4.	DATENBANKMODELL
-	User: Tabelle zur Speicherung von Mitarbeiterinformationen oder Benutzerinformationen wie Benutzername, Passwort ind Rolle.
-	Vehicle: Tabelle zur Speicherung von Fahrzeuginformationen wie ID, Typ, Marke, Modell, Preis, Jahr, Spezifikationen und Verfügbarkeit.

5.	ZEITPLAN
-	Woche 1-4: Planung des Projekts, Ablaufdiagramm, Datenbankdesign und -implementierung.
-	Woche 5-8: Implementierung der Benutzerauthentifizierung und der grundlegenden Funktionen.
-	Woche 9-12: Implementierung fortgeschrittener Funktionen.
-	Woche 13-16: Kontrolle der Funktionen, Durchführung von Tests, Fehlerbehebung und Optimierung.

6.	RESSOURCEN
-	Python-Entwicklungsumgebung.
-	SQLite-Datenbank.
-	Python-Bibliotheken für Benutzereingabe und -ausgabe.
-	Versionskontrolle (GitLab) für gute Übersicht.

7.	RISIKEN UND HERAUSFORDERUNGEN
-	Komplexe Implementierungsfunktionen wie Zahlungsabwicklung und Fahrzeugverwaltung.
-	Überprüfung und Validierung von Benutzereingaben und Datenbankoperationen.




## Prototyp
Vor dem Projektbeginn habe ich einen einfachen Python-Prototyp erstellt, um die Funktionalitäten eines Car Dealerships zu simulieren und eine Grundlage für die weitere Entwicklung zu schaffen. Der Prototyp besteht aus zwei Hauptkomponenten: der Klasse 'CarInventory' und einer Hauptklasse, die den Ablauf steuert. Zusätzlich gibt es eine „Testdaten“-Datei zum Erzeugen zufälliger automatischer Daten.

Der Code nutzt verschiedene If-Else-Bedingungen und While-True-Schleifen, um Benutzereingaben zu verarbeiten. In dieser grundlegenden Version wird zwischen zwei Benutzertypen unterschieden: User und Staff. User können Autos kaufen und verkaufen, während Staff-Mitarbeiter Autos hinzufügen, löschen, Parameter ändern und die gesamte Fahrzeugliste anzeigen lassen können. 

Dieser Prototyp diente dazu, die Grundfunktionalitäten zu testen und sicherzustellen, dass sie korrekt funktionieren, bevor komplexere Features implementiert werden.
![Alt text](Dokumentation/image.png)
![Alt text](Documentation\image-1.png)
![Alt text](Dokumentation/image-2.png)





## Implementation

Nach der Erstellung des Prototyps wurde ein strukturiertes Vorgehen implementiert, um das Projekt von einer einfachen Simulation zu einem voll funktionsfähigen Car Dealership System zu entwickeln. Hier ist der Prozess der Implementation im Detail beschrieben:

1. **Anforderungen stezen**: Zunächst wurden die spezifischen Anforderungen des Projekts klar definiert. Dazu gehörten die Funktionen, die das endgültige Programm bieten sollte, wie zum Beispiel Benutzerverwaltung, detaillierte Fahrzeugdaten, Verkaufs- und Kaufprozesse.

2. **Planung**: Basierend auf den Anforderungen wurde ein detaillierter Projektplan erstellt. Dies umfasste die Datenbankstruktur, Benutzeroberflächen und die Interaktionen zwischen verschiedenen Modulen. Eine umfangreiche Designplanung war nicht erforderlich, da sich das Programm in der Konsole befindet. 

3. **Code-Planung**: Eine detaillierte Planung des Code-Ablaufs war erforderlich, da zahlreiche Benutzerentscheidungen berücksichtigt werden mussten. Um Verwirrung zu vermeiden und eine klare Struktur zu gewährleisten, wurde der Ablauf gründlich geplant.

4. **Erweiterung der Datenstruktur**: Die Code-Struktur wurde erheblich verändert und in mehrere Dateien unterteilt, um die Organisation und Wartbarkeit zu verbessern.

5. **Datenbank-Entwicklung**: Mithilfe von SQLite wurde eine Datenbank erstellt, um eine zuverlässige und skalierbare Speicherung der Fahrzeug- und Benutzerdaten zu gewährleisten. Die Daten wurden sorgfältig strukturiert und gespeichert.

6. **Implementierung der Geschäftslogik**: Die Kernfunktionen wie Kauf, Verkauf, Hinzufügen, Löschen und Bearbeiten von Fahrzeugdaten wurden implementiert. Komplexere Geschäftsregeln und -prozesse wurden ebenfalls berücksichtigt und im Code integriert.

7. **Benutzerverwaltung**: Ein Benutzermanagementsystem wurde entwickelt, um verschiedene Benutzerrollen zu unterstützen.

8. **Testen**: Unit Tests wurden durchgeführt, um sicherzustellen, dass alle Funktionen wie vorgesehen arbeiten. 


Durch diesen strukturierten und iterativen Prozess konnte der ursprüngliche Prototyp zu einem guten und voll funktionsfähigen Dealership Center System weiterentwickelt werden.


## Testing
Es wurden zahlreiche Unit-Tests implementiert, die jeweils spezifische Funktionalitäten für Clients und Mitarbeiter überprüfen sollen.

## Video Präsentation
Im Git-Verzeichnis befindet sich ein fast siebenminütiges Video "Video Presentation", das die Abläufe des Programms detailliert erläutert. Dieses Video enthält zudem zwei Anwendungsbeispiele, die die Nutzung des Programms veranschaulichen.


## Arbeitsrapport

Jan 29, 2024
-	Projekt Anweisungen hören (40min)
-	Ideenfindung (30min)
-	Grobe Plannung (40min)
-	Entscheidung in welchen Programm ich der Projekt mache (Python)

Feb 19, 2024
-	Genaue Plannung - Ablauf der Funktionen - Consolen IN/OUTput (3h+)

Feb 26, 2024
-	Projekt in GitLab erstellen
-	Projekt Files erstellen

Mar 04, 2024
-	Ablaufdiagramm gemacht (noch nicht fertig) (2h)
-	Test code gemacht mit einfache funktionen  (3h)

Mar 11, 2024
-	Ablaufdiagramm fertig gemacht (3h)
-	Datenbank mit SQLite gemacht (1h)

Mar 18, 2024
-	Benutzer und Mitarbeiter Login und Registration gemacht (4h)
-	-> schwierigkeiten mit Datenbank speicherung (3h)

Mar 25, 2024
-	Mit Funktionen angefangen – Buy / Sell Vehicle (1h)
-	Immer noch Probleme mit Datenbank (3h)
-	Mit Dokumentation angefangen

Apr 15, 2024
-	Weiter Funktionen gemacht – Rent Vehicle (40min)
-	Datenbank Probleme (2h)
-	Funktionen Planung korigiert (30min)
-	Dokumentation - Idee, Beschreib, Planung (3h)

Apr 21, 2024
-	Dokumentation geschrieben (1h)
-	Datenbank link verbessert (3h)

May 21, 2024
-	Client Funktionen + Sample data (fast fertig)(6h)
-	Staff Funktionen (fast fertig)(4h)
-	Login / Register verbesserung (4h)

May 22, 2024
-	Datenbank verbesserung (2h)

May 27, 2024
-	Singleton in der Datenbank gemacht (2h)

Jun 03, 2024
-	Search Funktion verbesserung (1h)
-	Unit Tests (4h)

Jun 06, 2024
-	Konfigure Funktion verbesserung (30 min)
-	Pap Diagramm fertig machen (3h)

Jun 10, 2024
-	Video Produktion (6h)
-	Unit Tests (2h)

Jun 14, 2024
-	Alles in Markdown kopieren
-	Abgabe

