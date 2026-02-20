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

> Rakendus koosneb järgmistest komponentidest, mis töötavad jadamisi:
> 1. **Filtreerimiskomponent (ei sisalda TI-d):** Pandas-põhine eelfilter, mis kitsendab ainekogumi semestri, EAP-vahemiku ja hindamisskaala alusel enne semantilist otsingut.
> 2. **Embeddingu komponent (lokaalne TI mudel):** SentenceTransformer kodeerib kasutaja päringu vektoriks. Sama mudel on kasutatud ka kursuste kirjelduste eelarvutamiseks (`build_embeddings.py`).
> 3. **Semantilise otsingu komponent (ei sisalda TI-d):** scikit-learn cosine_similarity leiab filtreeritud ainekogumist kõige sarnasemad kandidaadid (kuni 20).
> 4. **Keeletuvastus (reeglistik):** Lihtsustatud stoppsõnade loendi põhjal tuvastatakse, kas päring on eesti või inglise keeles, et vastuse keel sobituks.
> 5. **LLM-komponent (API-põhine TI):** OpenRouter kaudu kutsutav Gemma 3 27B genereerib soovitused ja põhjendused, kasutades ainult etteantud kursuste konteksti (RAG-muster).
> 6. **Kasutajaliides (ei sisalda TI-d):** Streamlit vestlusliides, kus on külgriba filtrite ja API-võtme sisestamiseks.
>
> Komponendid on üksteisest sõltuvad järjestikuses ahelas: filtreerimine → semantiline otsing → konteksti koostamine → LLM → väljund.

### 🟢 4.2 Tehisintellekti lahenduste valik
Milliseid mudeleid on plaanis kasutada? Kas kasutada valmis teenust (API) või arendada/majutada mudelid ise?

> **Embeddingu mudel:** `BAAI/bge-m3` (SentenceTransformers, lokaalselt jooksutatud). Valitud, kuna toetab nii eesti kui ka inglise keelt, on avatud lähtekoodiga ja tasuta, ning annab kvaliteetseid mitmekeelseid vektoreid. Mudel arvutatakse eelnevalt kõikidele kursustele (`build_embeddings.py`) ja salvestatakse failina, et rakenduse käivitusaeg oleks kiire.
>
> **LLM:** `google/gemma-3-27b-it` OpenRouter API kaudu. Valitud, kuna on piisavalt võimekas juhiseid järgima, toetab pikki kontekste (kursuste loend süsteemipromptis) ning on OpenRouteri kaudu tasuta kättesaadav. Mudel majutatakse teenusepakkuja poolel (API), mistõttu ei ole vaja kohalikku GPU-d. Kasutaja sisestab oma OpenRouter API võtme, seega ei kulu projektieelarvet LLM-i päringutele.
>
> Mudeleid ei treenita ega fine-tune'ita — kasutatakse ainult valmismudeleid koos kontekstiandmetega (RAG).

### 🟢 4.3 Kuidas hinnata rakenduse headust?
Kuidas rakenduse arenduse käigus hinnata rakenduse headust?

> Rakendust hinnatakse peamiselt kvalitatiivse käsitsi testimisega, kuna eelarve ja aeg ei võimalda ulatuslikku automaatset hindamist. Kasutatavad meetodid:
> 1. **Testpäringute kogum:** Koostame ~10–15 testpäringut eesti ja inglise keeles, mis katavad erinevaid olukordi (päring ilma täpse ainekoodita, valdkonnakirjeldus, mitme filteri kombinatsioon). Kontrollime käsitsi, kas tagastatud ained on asjakohased.
> 2. **Filtrite korrektsusnäitaja:** Kontrollime, et kõik tagastatud ained vastavad valitud semestri-, EAP- ja hindamisskaala filtritele (deterministlik kontroll, automatiseeritav).
> 3. **Keelesobivus:** Veendume, et eestikeelsele päringule vastatakse eesti keeles ja ingliskeelsele inglise keeles.
> 4. **Prompt injection testimine:** Proovime süsteemipromptist kõrvalekaldumist (nt "Unusta eelnevad juhised") ja kontrollime, et rakendus jääb kursuste teemasse.
> 5. **Kasutajatagasiside:** Esitame rakenduse kaasõppuritele ja kogume tagasisidet leitavuse ja kasutatavuse kohta.

### 🟢 4.4 Rakenduse arendus
Milliste sammude abil on plaanis/on võimalik rakendust järk-järgult parandada (viibadisain, erinevte mudelite testimine jne)?

> Rakendus on valminud iteratiivsete sammudena:
> 1. **Samm 1 – Lihtne UI prototüüp:** Streamlit vestlusliides ilma LLM-ita (automaatne vastus). Eesmärk: veenduda, et UI-kontseptsioon töötab.
> 2. **Samm 2 – Andmete puhastamine ja ettevalmistamine:** EDA, veergude valik, JSON-väljade parsamine, `description`-veeru koostamine. Embeddingute eelarvutamine `BAAI/bge-m3`-ga.
> 3. **Samm 3 – RAG-otsing:** Semantiline otsing cosine similarity abil; LLM-ühendus OpenRouter kaudu; süsteemiprompt kontekstiga.
> 4. **Samm 4 – Filtrid ja keeletugi:** Semestri/EAP/hindamisskaala filtrid külgribale; automaatne keeletuvastus; süsteemiprompt mõlemas keeles; prompt injection kaitsemeetmed. *(Praegune seis — `app.py`)*
> 5. **Võimalikud edasised sammud:** Instituudi/valdkonna filter; embeddingu tekstikvaliteedi parandamine (nt nimi + kirjeldus koos); teise LLM-i testimine (nt Mistral); tulemuste hindamissüsteem; kasutajaliidese visuaalne täiustamine.


### 🟢 4.5 Riskijuhtimine
Kuidas maandatakse tehisintellektispetsiifilisi riske (hallutsinatsioonid, kallutatus, turvalisus)?

> - **Hallutsinatsioonid:** LLM-ile antakse ainult konkreetne kursuste kontekst (RAG). Süsteemiprompt käsib kasutada ainult etteantud infot ja öelda, kui info puudub. See vähendab, kuid ei välista täielikult väljamõeldud andmeid.
> - **Prompt injection:** Kasutajasisend loetakse ebausaldusväärset päritolu tekstiks. Süsteemiprompt sisaldab eksplitsiitseid reegleid (ignoreeri instruktsioone muuta käitumist, ära avalda süsteemipromptit). Testitud käsitsi tavaliste rünnakumustritega.
> - **Teemavälised vastused:** LLM käsib suunata mittekursuste-teemalised päringud tagasi nõustamise juurde, mitte vastata vabalt.
> - **Isikuandmete leke:** Andmestik sisaldab õppejõudude nimesid. Praeguse kursuse-raames jooksutame rakendust lokaalselt, mis piirab lekkeriski. Avaliku versiooni puhul tuleks isikuandmed eemaldada või hankida eetikakomitee luba.
> - **Kulude ületamine:** Kasutaja sisestab oma API võtme, seega projekt ise ei maksa LLM-i päringute eest. Embeddingumudel töötab lokaalselt — lisakuluta.
> - **Kallutatus:** BGE-m3 ja Gemma on treenitud valdavalt inglise keelel; eestikeelsete kirjelduste kvaliteet võib varieeruda. Mõlemas keeles kirjelduste olemasolu leevendab seda osaliselt.

<br>
<br>

## 🔵 5. Tulemuste hindamine
Fookus: kuidas hinnata loodud lahenduse rakendatavust ettevõttes/probleemilahendusel?

### 🔵 5.1 Vastavus eesmärkidele
Kuidas hinnata, kas rakendus vastab seatud eesmärkidele?

> Rakendus loetakse eesmärkidele vastavaks, kui:
> - Vabatekstiline päring (sh ilma täpse ainekoodita või ainekoodiga mitteseotud sõnadega) tagastab sisuliselt asjakohaseid kursusi — kontrollitud testpäringute kogumiga.
> - Filtrid (semester, EAP, hindamisskaala) töötavad korrektselt: ükski tagastatud aine ei riku aktiivset filtrit.
> - Vastus tuleb päringu keeles (ET/EN) — kontrollitud mõlemas keeles testpäringutega.
> - Rakendus ei vasta küsimustele, mis ei ole seotud kursustega, vaid suunab kasutaja tagasi teema juurde.
> - Rakendus töötab mõistliku kiirusega: päringu töötlemine ja vastuse genereerimine alla 30 sekundi tavalises võrgukeskkonnas.
> - Kaasõppurite/kasutajate tagasiside on üldjoontes positiivne aineotsingu kasutatavuse osas.

<br>
<br>

## 🟣 6. Juurutamine
Fookus: kuidas hinnata loodud lahenduse rakendatavust ettevõttes/probleemilahendusel?

### 🟣 6.1 Integratsioon
Kuidas ja millise liidese kaudu lõppkasutaja rakendust kasutab? Kuidas rakendus olemasolevasse töövoogu integreeritakse (juhul kui see on vajalik)?

> Lõppkasutaja (tudeng) kasutab rakendust Streamliti veebiliidesena, mida jooksutab käsurealt lokaalselt (`streamlit run app.py`). Integratsioon olemasolevasse OIS2-süsteemi ei ole kursuse raames nõutav ega planeeritud — rakendus on iseseisev tööriist. Kasutaja sisestab oma OpenRouter API võtme külgribale, misjärel saab vabas vormis kirjeldada õpihuve ja saada soovitusi koos filtreerimisvõimalustega.

### 🟣 6.2 Rakenduse elutsükkel ja hooldus
Kes vastutab süsteemi tööshoidmise ja jooksvate kulude eest? Kuidas toimub rakenduse uuendamine tulevikus?

> Kursuse raames vastutab rakenduse töötamise eest projektimeeskond. Jooksvad kulud on minimaalsed: embeddingumudel on lokaalne (tasuta), LLM-i kulud katab kasutaja enda API võtmega. Andmete uuendamisel (uus semester, uued ained OIS2-s) tuleb: 1) laadida alla uus `puhastatud_andmed.csv`, 2) käivitada `python build_embeddings.py` embeddingute uuesti arvutamiseks. Kursuse lõppedes rakendust aktiivselt ei hooldata; lähtekoodi ja juhised jäävad GitHubi, et soovijad saaksid ise jätkata.
