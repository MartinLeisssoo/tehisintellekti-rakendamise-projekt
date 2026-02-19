# 🤖 Tehisintellekti rakendamise projektiplaani mall (CRISP-DM)

<br>
<br>


## 🔴 1. Äritegevuse mõistmine
*Fookus: mis on probleem ja milline on hea tulemus?*


### 🔴 1.1 Kasutaja kirjeldus ja eesmärgid
Kellel on probleem ja miks see lahendamist vajab? Mis on lahenduse oodatud kasu? Milline on hetkel eksisteeriv lahendus?

> Tartu Ulikooli ois-is on tuhandeid oppeaineid ning sobivate ainete leidmine on aeganoudev. Olemasolev otsing on vahepaindlik ning nouab tihti vaga konkreetseid otsingusonu; vabas vormis huvikirjeldus ei klapi aine nimedega ja varasemate semestrite aineid on raske leida. Eesmargiks on pakkuda vabatekstilist, semantilist otsingut, mis aitab tudengitel leida endale sobivad vaba- ja valikained ning tuua kokku erinevate valdkondade huvid. Kasu on paremad vasted ainete ja tudengite vahel ning nauditavam ainevaliku protsess.

### 🔴 1.2 Edukuse mõõdikud
Kuidas mõõdame rakenduse edukust? Mida peab rakendus teha suutma?

> Rakendus on edukas, kui ta leiab vabatekstilistele paringutele semantilisi vasteid ka siis, kui paringu sisu sona-sonalt ei esine aine kirjeldustes. Rakendus peab rakendama rangete filtrite tingimusi (semester, instituut/valdkond, asukoht, oppekeel) ning tagastama asjakohased tulemused sobivuse jargi. Tulemused peavad kasutama uusimat ainekirjelduste versiooni, mitte pakkuma ebasobivaid/mitteainega seotud vastuseid, ning toimima moistliku kiirusega. Edukust saab hinnata teststsenaariumitega ning kasutajate tagasisidega (nt vaba- ja valikainete valiku lihtsus).

### 🔴 1.3 Ressursid ja piirangud
Millised on ressursipiirangud (nt aeg, eelarve, tööjõud, arvutusvõimsus)? Millised on tehnilised ja juriidilised piirangud (GDPR, turvanõuded, platvorm)? Millised on piirangud tasuliste tehisintellekti mudelite kasutamisele?

> Projekti aeg on umbes 1 kuu ja eelarve piiratud (u ~50 EUR 20 inimese peale tasuliste mudelite kasutamiseks). Arendus toimub peamiselt lokaalselt; rakendus voiks olla veebipohine, kuid kursuse raames jooksutada lokaalselt. Eelistame vabavaralisi mudeleid ja tasuta API sid. Turvanouded: prompt injectioni risk, ressursi kuritarvitamine, ning kasutajasisendites voib esineda personaalset infot, mis ei tohi lekkida API pakkujale. Andmestik sisaldab oppejoudude isikuandmeid, seega avaliku rakenduse puhul tuleks kaaluda eetikakomitee luba voi isikuandmete eemaldamist. Rakendus ei tohi anda aineotsinguga mitteseotud vastuseid.

<br>
<br>


## 🟠 2. Andmete mõistmine
*Fookus: millised on meie andmed?*

### 🟠 2.1 Andmevajadus ja andmeallikad
Milliseid andmeid (ning kui palju) on lahenduse toimimiseks vaja? Kust andmed pärinevad ja kas on tagatud andmetele ligipääs?

> Vajame infot koigi UT oppeainete kohta (vaartuslikult vahemalt terve aasta, eelistatult viimased 2 aastat). Vajalikud on aine kirjeldused, koodid, nimetused, mahud, asukohad, oppekeel, semester, instituut/valdkond, ning veebis/kohapeal toimumise info. Andmed saavad tulla OIS2 APIst (vajadusel mitmest endpointist) ja on avalikult kattesadavad.

### 🟠 2.2 Andmete kasutuspiirangud
Kas andmete kasutamine (sh ärilisel eesmärgil) on lubatud? Kas andmestik sisaldab tundlikku informatsiooni?

> Andmed on avalikult kattesadavad; kasutuslubasid tuleb kontrollida API dokumentatsioonist. Andmestik sisaldab oppejoudude isikuandmeid, mis voiab avaliku rakenduse puhul nouda eetikakomitee luba voi andmete anonumiseerimist.

### 🟠 2.3 Andmete kvaliteet ja maht
Millises formaadis andmeid hoiustatakse? Mis on andmete maht ja andmestiku suurus? Kas andmete kvaliteet on piisav (struktureeritus, puhtus, andmete kogus) või on vaja märkimisväärset eeltööd)?

> Andmed on CSV formaadis (u 45.3 MB, 3031 rida, 223 veergu). Osad veerud on eri keeltes voi duplikaatides (kursuse vs versiooni kirjeldus), osa on tekstilised, osa numbrilised ning osa JSON kujul. Kvaliteet on uldiselt piisav, kuid vajab filtreerimist, veergude valikut ja JSON valjade puhastamist. Puuduvate vaartuste osakaal on osades veergudes suur.

### 🟠 2.4 Andmete kirjeldamise vajadus
Milliseid samme on vaja teha, et kirjeldada olemasolevaid andmeid ja nende kvaliteeti.

> Vaja on analuusida koigi 223 veeru tahendused, valida olulised veerud ning hinnata puuduvate vaartuste hulka. Tuleb puhastada JSON valjad, kombineerida kirjeldavad tunnused uheks vabatekstiks ning kontrollida, et valitud veerud sobivad semantilise otsingu/RAG jaoks. EDA on osaliselt tehtud, kuid vaja on formeerida loplik tunnuste valik.

<br>
<br>


## 🟡 3. Andmete ettevalmistamine
Fookus: Toordokumentide viimine tehisintellekti jaoks sobivasse formaati.

### 🟡 3.1 Puhastamise strateegia
Milliseid samme on vaja teha andmete puhastamiseks ja standardiseerimiseks? Kui suur on ettevalmistusele kuluv aja- või rahaline ressurss?

> 1) Probleemide identifitseerimine (puuduvad vaartused, duplikaadid, eri keelte variandid). 2) JSON valjade parsamine ning standardiseerimine. 3) Vajadusel puuduvate vaartuste imputimine voi tuletamine teistest OIS2 endpointidest. 4) Andmetuupide uhtlustamine. Ajaliselt hinnanguliselt ~1 nadal; raha ei plaani kulutada, piirdume tasuta/avatud mudelitega.

### 🟡 3.2 Tehisintellektispetsiifiline ettevalmistus
Kuidas andmed tehisintellekti mudelile sobivaks tehakse (nt tükeldamine, vektoriseerimine, metaandmete lisamine)?

> Valitakse ainet kirjeldavad veerud ning koostatakse iga aine jaoks uks kirjeldav tekst (ET/EN). See tekst vektoriseeritakse sobiva embedding-mudeliga ja salvestatakse koos metaandmetega (kood, semester, asukoht, oppekeel) andmebaasi. Vektorotsing + filtrid moodustavad RAG-pohise semantilise otsingu.

<br>
<br>

## 🟢 4. Tehisintellekti rakendamine
Fookus: Tehisintellekti rakendamise süsteemi komponentide ja disaini kirjeldamine.

### 🟢 4.1 Komponentide valik ja koostöö
Millist tüüpi tehisintellekti komponente on vaja rakenduses kasutada? Kas on vaja ka komponente, mis ei sisalda tehisintellekti? Kas komponendid on eraldiseisvad või sõltuvad üksteisest (keerulisem agentsem disan)?

> ...

### 🟢 4.2 Tehisintellekti lahenduste valik
Milliseid mudeleid on plaanis kasutada? Kas kasutada valmis teenust (API) või arendada/majutada mudelid ise?

> ...

### 🟢 4.3 Kuidas hinnata rakenduse headust?
Kuidas rakenduse arenduse käigus hinnata rakenduse headust?

> ...

### 🟢 4.4 Rakenduse arendus
Milliste sammude abil on plaanis/on võimalik rakendust järk-järgult parandada (viibadisain, erinevte mudelite testimine jne)?

> ...


### 🟢 4.5 Riskijuhtimine
Kuidas maandatakse tehisintellektispetsiifilisi riske (hallutsinatsioonid, kallutatus, turvalisus)?

> ...

<br>
<br>

## 🔵 5. Tulemuste hindamine
Fookus: kuidas hinnata loodud lahenduse rakendatavust ettevõttes/probleemilahendusel?

### 🔵 5.1 Vastavus eesmärkidele
Kuidas hinnata, kas rakendus vastab seatud eesmärkidele?

> ...

<br>
<br>

## 🟣 6. Juurutamine
Fookus: kuidas hinnata loodud lahenduse rakendatavust ettevõttes/probleemilahendusel?

### 🟣 6.1 Integratsioon
Kuidas ja millise liidese kaudu lõppkasutaja rakendust kasutab? Kuidas rakendus olemasolevasse töövoogu integreeritakse (juhul kui see on vajalik)?

> ...

### 🟣 6.2 Rakenduse elutsükkel ja hooldus
Kes vastutab süsteemi tööshoidmise ja jooksvate kulude eest? Kuidas toimub rakenduse uuendamine tulevikus?

> ...
