Páros projekt – Hotel Booking
Ebben a projektben ketten fogtok egy közös Python alkalmazáson dolgozni.

A cél egy egyszerű Hotel Booking Management App, amelyben:

hotelszobákat tároltok JSON fájlban;
elérhető szobákat tudtok megjeleníteni;
szobát tudtok keresni ID alapján;
foglalást tudtok létrehozni;
a foglalásokat JSON fájlba mentitek;
a lefoglalt szoba státuszát módosítjátok.
A projekt során a Python mellett a Git/GitHub csapatmunkát is gyakoroljátok.

A teljes folyamat:

GitHub repository
        ↓
clone
        ↓
külön branchek
        ↓
külön Python modulok
        ↓
commit + push
        ↓
Pull Request
        ↓
merge
        ↓
közös integration
        ↓
működő alkalmazás
A projekt során gyakoroljátok:

uv projekt létrehozását;
Git és GitHub használatát;
collaborator hozzáadását;
repository klónozását;
feature brancheket;
commitot és push-t;
Pull Requestet;
merge-et;
Python modulok importálását;
paraméterezett függvényeket;
return értékeket;
JSON fájl olvasását;
JSON fájl írását;
több modul összekapcsolását;
azt, amikor egyik függvény visszatérési értékét egy másik függvény argumentumként kapja meg.
Fontos szabály
Ne dolgozzatok közvetlenül a main branchen!
Új feladat előtt:

git switch main
git pull
Majd:

git switch -c feature/branch-name
Munka után:

git add .
git commit -m "Describe the change"
git push -u origin feature/branch-name
GitHubon:

Pull Request
→ review
→ merge
1. Projekt létrehozása
A pár egyik tagja legyen Student A.

Student A:

mkdir hotel-booking
cd hotel-booking
uv init
Ellenőrzés:

ls -la
A projektben legyen:

README.md
pyproject.toml
main.py
.gitignore
A .gitignore például:

__pycache__/
*.pyc
.venv/
.vscode/
2. Git repository létrehozása
Student A:

git init -b main
git add .
git commit -m "Create starter project"
GitHub repository:

gh repo create hotel-booking \
  --public \
  --source=. \
  --remote=origin \
  --push
3. Collaborator hozzáadása
Student A GitHubon:

Repository
→ Settings
→ Collaborators
→ Add people
Adja hozzá Student B-t.

Student B fogadja el a meghívást.

4. Student B klónozza a projektet
Student B:

cd ~/codecool
git clone REPOSITORY_URL
cd hotel-booking
Ellenőrzés:

git status
git branch --show-current
Az aktuális branch:

main
Mindketten futtassátok:

uv run main.py
5. A projekt végső struktúrája
hotel-booking/
│
├── main.py
├── README.md
├── pyproject.toml
├── .gitignore
│
├── data/
│   ├── rooms.json
│   └── bookings.json
│
└── hotel/
    ├── __init__.py
    ├── rooms.py
    └── bookings.py
6. Student A feladata – Rooms
Student A a szobák kezeléséért felel.

Branch
git switch main
git pull
git switch -c feature/rooms
Hozd létre
hotel/rooms.py
data/rooms.json
Ha szükséges:

hotel/__init__.py
7. rooms.json
Legyen legalább 5 szoba.

Például:

{
  "id": 101,
  "type": "double",
  "price": 35000,
  "available": true
}
Lehetséges szobatípusok:

single
double
family
suite
Minden szoba ID-ja legyen különböző.

8. Student A függvényei
Készítsd el:

def load_rooms(file_path):
    pass


def save_rooms(file_path, rooms):
    pass


def show_rooms(rooms):
    pass


def get_available_rooms(rooms):
    pass


def find_room_by_id(rooms, room_id):
    pass


def update_room_status(rooms, booking):
    pass
load_rooms(file_path)
Olvassa be a megadott JSON fájlt.

Térjen vissza a szobák listájával.

save_rooms(file_path, rooms)
Mentse el a szobák aktuális állapotát JSON fájlba.

show_rooms(rooms)
Írja ki a szobák fontos adatait.

get_available_rooms(rooms)
Csak azokat adja vissza, amelyeknél:

available == True
find_room_by_id(rooms, room_id)
Keresse meg a szobát ID alapján.

Ha megtalálta:

return room
Ha nincs ilyen szoba:

return None
update_room_status(rooms, booking)
A kapott foglalási adat alapján keresse meg a megfelelő szobát, és állítsa:

"available": False
értékre.

9. Student A – commit és push
git status
git add .
git commit -m "Add room management"
git push -u origin feature/rooms
GitHubon:

Pull Request
→ Student B review
→ merge
10. Student B feladata – Bookings
Student B a foglalások kezeléséért felel.

Branch
git switch main
git pull
git switch -c feature/bookings
Hozd létre
hotel/bookings.py
data/bookings.json
A bookings.json indulhat:

[]
11. Student B függvényei
Készítsd el:

def load_bookings(file_path):
    pass


def save_bookings(file_path, bookings):
    pass


def create_booking(room, guest_name):
    pass


def add_booking(bookings, booking):
    pass


def show_bookings(bookings):
    pass
load_bookings(file_path)
Olvassa be a foglalásokat a JSON fájlból.

save_bookings(file_path, bookings)
Mentse el a foglalásokat JSON fájlba.

create_booking(room, guest_name)
Ez a függvény nem keres szobát.

Egy már kiválasztott:

room
dictionaryt kap argumentumként.

Készítsen például ilyen adatot:

{
  "room_id": 101,
  "room_type": "double",
  "guest": "Peter"
}
Majd térjen vissza vele.

add_booking(bookings, booking)
Adja hozzá az új foglalást a foglalások listájához.

show_bookings(bookings)
Írja ki az eddigi foglalásokat.

12. Student B – commit és push
git add .
git commit -m "Add booking management"
git push -u origin feature/bookings
GitHubon:

Pull Request
→ Student A review
→ merge
13. Közös integráció
Mindketten:

git switch main
git pull
Ellenőrizzétek, hogy már megvan:

rooms.py
bookings.py
rooms.json
bookings.json
14. Kötelező adatfolyam
A programban történjen meg:

find_room_by_id()
      ↓
     room
      ↓
create_booking()
      ↓
   booking
      ↓
update_room_status()
Vagyis:

room = find_room_by_id(...)
eredménye menjen tovább:

booking = create_booking(room, guest_name)
Majd:

update_room_status(rooms, booking)
Ez kötelező része a feladatnak.

15. Közös integration branch
Student A:

git switch main
git pull
git switch -c feature/integration
Készítse el például:

importokat;
JSON adatok betöltését;
menü alapját.
Majd:

git add .
git commit -m "Start application integration"
git push -u origin feature/integration
16. Student B csatlakozik az integration branchhez
Student B:

git fetch origin
git switch --track origin/feature/integration
Ha már létezik lokálisan:

git switch feature/integration
Student B folytassa:

input kezelés;
szoba keresése;
booking létrehozása;
státusz módosítása;
JSON mentések;
eredmény kiírása.
Majd:

git add .
git commit -m "Complete application integration"
git push
17. A main.py feladata
A végső program legalább ezt tudja:

1. Show available rooms
2. Book room
3. Show bookings
4. Exit
Importáljátok a szükséges függvényeket:

from hotel.rooms import ...
from hotel.bookings import ...
Ne másoljátok át a már elkészült függvényeket a main.py-ba.

18. JSON mentés
Foglalás után mindkét adatot frissíteni kell:

rooms.json
+
bookings.json
Ha bezárjátok és újraindítjátok a programot, a foglalás maradjon meg.

19. Paraméteres függvények
Kerüljétek a felesleges hard-coded megoldásokat.

Ne:

def load_rooms():
    ...
hanem:

def load_rooms(file_path):
A szükséges adatokat lehetőség szerint paraméterként adjátok át.

20. Code Review
Minden Pull Requestet a másik csapattag nézzen át.

Ellenőrizzétek:

megfelelő branchet merge-eltek-e;
csak a szükséges fájlokat módosítottátok-e;
érthetőek-e a function nevek;
megfelelő paramétereket használtok-e;
van-e megfelelő return;
működik-e a JSON read;
működik-e a JSON write;
nincs-e duplikált logika;
fut-e a program.
21. Végső Pull Request
Ha elkészült az integration branch:

git status
git push
GitHubon:

feature/integration
        ↓
       main
Pull Request.

Nézzétek át:

Files changed
Ha megfelelő:

Merge pull request
→ Confirm merge
22. Merge után
Mindketten:

git switch main
git pull
git status
Ideális:

On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
Végső ellenőrző lista
A projekt akkor kész, ha:

[ ] uv projekt létrejött;
[ ] van Git repository;
[ ] van GitHub repository;
[ ] Student B collaborator;
[ ] Student B klónozta a repositoryt;
[ ] külön feature brancheken dolgoztatok;
[ ] van rooms.py;
[ ] van bookings.py;
[ ] van rooms.json;
[ ] van bookings.json;
[ ] JSON fájlból olvastok;
[ ] JSON fájlba írtok;
[ ] paraméterezett függvényeket használtok;
[ ] használtok return értékeket;
[ ] saját modulokból importáltok;
[ ] find_room_by_id() eredménye továbbmegy a create_booking() függvénynek;
[ ] create_booking() eredménye továbbmegy az update_room_status() függvénynek;
[ ] mindketten készítettetek commitot;
[ ] mindketten pusholtatok;
[ ] készítettetek Pull Requestet;
[ ] átnéztétek egymás kódját;
[ ] merge-eltétek a változtatásokat;
[ ] elkészült a közös main.py;
[ ] újraindítás után is megmaradnak az adatok.
Extra feladatok
1. Add room
Lehessen új szobát hozzáadni.

Az új szoba kerüljön:

rooms.json
fájlba.

2. Delete room
Lehessen szobát törölni ID alapján.

3. Search by type
Például:

single
double
family
suite
4. Statistics
Írjátok ki:

Available rooms: ...
Booked rooms: ...
5. Number of nights
A foglalás tartalmazzon:

nights
adatot.

Például:

{
  "room_id": 101,
  "room_type": "double",
  "guest": "Peter",
  "nights": 3
}
6. Total price
Számítsátok ki:

room price × number of nights
Például:

Room price: 35000 Ft
Nights: 3
Total: 105000 Ft
7. Cancel booking
Lehessen foglalást törölni.

A hozzá tartozó szoba legyen újra:

"available": True
8. Guest search
Lehessen megkeresni, hogy egy adott vendégnek van-e foglalása.

A projekt legfontosabb része
Nem két külön programot írtok.

A cél:

Student A kódja
       ↓
Student B kódja
       ↓
közös alkalmazás
A két modulnak adatot kell átadnia egymásnak.

A végén egyetlen közös programotok legyen, amelyhez mindkettőtök munkájára szükség van.