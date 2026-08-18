🚀 Capstone Project: Library Management System (Console-Based)

Concept

Ek chhoti library ka system jisme books add ho sakein, members register ho sakein, books issue/return ho sakein, aur search/reports nikaal sakein — sab kuch ek menu-driven console program se.

---

Requirements & Features

1\. Book Management

* Naya book add karo — har book ek dictionary ho: title, author, genre, total\_copies, available\_copies.  
* Saari books dikhao (loop se, neat format mein).  
* Book ko title se search karo.

2\. Member Management

* Naya member register karo — har member bhi ek dictionary: name, member\_id, borrowed\_books (list, jisme abhi jo books unke paas hain unke titles honge).  
* Saare members dikhao.

3\. Issue/Return System

* Ek book issue karo kisi member ko — check karo available\_copies \> 0 hai ya nahi (agar 0 hai, "Not Available" bolo, issue mat karo).  
* Book issue hote hi: available\_copies ek se kam ho, member ki borrowed\_books list mein book add ho.  
* Book return karo — available\_copies wapas badhe, member ki list se book hate.

4\. Search & Reports

* Genre ke hisab se books search karo (jaise "sab Fiction books dikhao").  
* Ek member ka poora current-borrowed-books dikhao.  
* Total unique genres kitne hain library mein — ye set use karke nikaalna hai.

5\. Menu System  
 Loop-driven menu jab tak "Exit" na choose kare:

1\. Add New Book  
2\. Add New Member  
3\. Issue a Book  
4\. Return a Book  
5\. View All Books  
6\. View All Members  
7\. Search Book by Title/Genre  
8\. View Library Stats (total books, unique genres, etc.)  
9\. Exit  
---

Konsa part kaunsa topic test karta hai:

| Feature | Topics Practice Ho Rahe |
| ----- | ----- |
| Book/Member dictionaries, list of dictionaries | 1.5 — Dictionaries, Nested Data Structures |
| Menu loop, input validation | 1.3 — while loop, if/elif/else |
| available\_copies \> 0 check | 1.2 — Comparison operators |
| Har function alag kaam kare | 1.4 — Functions, parameters, return |
| Search by title/genre — loop se scan karna | 1.3 — for loops, 1.5 — list/dict iteration |
| Unique genres nikaalna | 1.5 — Sets |
| String cleaning (title/author names) | 1.1 — String methods |
| Formatted output (reports, stats) | 1.1 — f-strings, print formatting |

---

Inputs

* Book details (title, author, genre, copies count) — user input se.  
* Member details (name) — member\_id khud generate kar sakte ho (ek counter variable jo har naye member pe badhe).  
* Menu choices, search queries, issue/return requests — sab user input se.

Outputs

* Formatted book list, member list.  
* Success/failure messages ("Book Issued Successfully", "No Copies Available", "Member Not Found", etc.).  
* Stats report (total books, total members, unique genres count).

Constraints

* Kam se kam 5-6 alag functions honi chahiye — koi bhi ek function sab kuch na kare.  
* Books aur Members dono global lists of dictionaries honi chahiye — is baar dhyan rakhna Student Manager wale bugs (shared list, break placement) na dohraye jaayein.  
* Har function apne kaam ke hisab se return ya print kare — decide khud karo.  
* Koi exception handling abhi mat karo — sirf if checks se invalid cases handle karo.

Folder Structure

library\_management\_system/  
  main.py  
  README.md

Optional Improvements (stretch, sirf agar time/interest ho)

* Har book ke liye times\_issued track karo → "Most Popular Book" report.  
* Genre-wise book count dikhao.

---

Suggestion: Ise bhi phases mein todo, jaise humne pehle discuss kiya tha:

1. Book add \+ View all books  
2. Member add \+ View all members  
3. Issue/Return logic  
4. Search \+ Stats (sets wala part)

Jis phase se shuru karna chahte ho, waha se start karo — jab bhi code bhejoge, main check karke hints dunga, jaisa ab tak karte aaye hain.

