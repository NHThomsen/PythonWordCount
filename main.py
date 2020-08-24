import wordCounter

lyric = """
Mine tarme skriger
I munden på folk der snakker ondt om rakkerpak som mig
Imens de smider og strøer med de gyldne gryn om sig
Som ku' ha' gjort gavn for mig, til min hungrende vom
Men jeg har ikke et særligt stort navn så, den er hungrende tom
Jeg dufter dolmerkål, stegte bornholmer ål, alverdens mad
Serveret på sølvfad, men min lomme er flad
Jeg fryser min fod for jeg har slidt min skosål
Mit andet ben og min sko har jeg solgt for en slik til et godt formål
Jeg føler mig yderst fjern
Men skal blot bryde min hjern' med at fryse en halv krop
Jeg spiller op med den ene hånd, i den anden holder jeg en tom kop
De kalder mig betler, eller bare den flade gademusikant
En ækel klam stodder, der æder skodder imod en usselt pant
Fordømt rådden røv det' blevet en luder at være rapper
Der er ingen scene jeg er helt alene i det 21' århundrede på de kolde trapper
Så hist hvor vejen slår en bugt, ser du en såkaldt gammel nar
Der drømte om at blive ægte familiefar, spise rådden frugt
En viadukt må være stedet at søge ly for en lilla sky
Der giver tegn på syreregn, snart vil hærge den indre by
For det er oven uden udmattende
At slentre rundt med huller i hud og hår
Jeg prøver at regne ud hvornår
Mine kødsår bliver til aske, jeg ser en taske
Daske i hånden på en gammel dam' jeg burde fam'
Men nej de er blevet for smarte
Nu til dags kan de baske en i karate
Så jeg må nøjes med de ligegyldige små basører
Jeg føler blikket sløre
Og hører fløjten til det sidste tog der snart kører
Så jeg gør klar, tar' mine ting begynder at vandre
Ser tilbage til de dage af mit liv og det jeg godt ville forandre
Men opgir' opsir' min tilstedeværelse på denne planet
Gjort er gjort og sket er fortid
En alt for hård tid for en falleret gammel gadestryger
Smyger mig ned af strøgen forsvinder i røgen fra min sidste ryger
Som fordamper ligesom mig og bliver ét med de triste skyer
Langt væk fra den her klode for det på mode at vær' psyko
Så jeg er klar parat til start og så væk i en fart

Jeg tjalder rundt og ser smart ud
Og andre synes at det ser rart ud
At se så 24 karat ud
Men jeg er skæv og fuld og fuld af ligeså meget lort som alle andre
Og der står no future malet på min port
Det er for sort når jeg ser sort og skærmen flimrer øjnene
Løber i vand, min sved er kold og hjernen simrer
For jeg er fanget i en fremmed verden det er en krig man
Jeg kaldes Geo, men jeg har det som en Brian
I dekadente Disneyland så det er mig du gør nar af
Når du råber efter folk der ligner dommedag
Min verden bryder sammen som en lego planet
Og geologeisme bliver en egomentalitet
Jeg drømmer om et stille rum med lys og bad og seng i
Og ik' at trisse rundt på må og få og være afhængig
Af tjald og tobak og elefanter og af kroner
For at glemme alt om sultne børn og voldtægt og kanoner
Har set så mange nøgne kvinder at jeg går
Og prøver på ikke at brække mig hver gang jeg ser et bart lår
Jeg har kun kulde, vil gerne bytte det til varme
Så jeg synker en klump imens det flår i mine tarme
Mine arme går i bund som et lod af bly
Ja det vel nok en ringe trøst at i morgen er en ny dag
Jeg mumler tak til Chirac, Yeltsin og Billie-boy
Med foldede hænder tak for guldøl og billig røg
Plastic og piller, nervegas og mobiler
Tiden iler når mit kød er væk så ved jeg kraniet smiler hånligt

Jeg må stimuleres for ingenting fungerer som det burde
Der skal mere end urtete til at kvæle mine sjæle kvaler
Jeg daler, falder
Maler blå verbaler
For det hænder for selv den bedste at bøtten den vender til det værste
Noget af det sværeste man kan undvære må være nærvær fra de næreste
Jeg ta'r endnu en tår, imens et år bliver til årtier
Tier blir' til årtusinder, jeg hører susen for mit indre øre
Mit sind det kører non-stop som skod pop på fucked up diskoteker
Sct. Hans eller Skt. Peter venter spændte på at se mig til te
Men de må sande at jeg blir' oven vande
For det er for let at bare forbande det hele langt væk
I trit med man ligger sig i sprit, spiller sig selv og går fallit
Jeg vågner stum op i et tomrum og køber ord på kredit
Mit tankespind det holder mig bundet på hænder og fødder
Så jeg er fortabt, hvis ondskabens træ slår rødder i mit sind abstrakt sagt

Så jeg synger den blues
Og bliver hængende i min rus
Så jeg synger den blues
Og bliver hængende i min rus"""
counter = wordCounter.wordCounter()
counter.wordsToRemove({"og"})
counted = sorted(counter.wordCount(lyric).items(), key=lambda x: x[1], reverse=True)

for i in counted:
    print(i[0], i[1])