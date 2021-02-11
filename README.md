##Oppgåve 1:
(sjå kode)
Ved bruk av TkInter vil dette python-skriptet lage ei enkel (les: stygg) framvising av diverse data frå felles datakatalog.

TkInter og Python er vald då det var enklast for å få gjennomført utfordringane. Dersom ein ser i koden vil ein sjå at mykje er hardkoda og kunne blitt gjort finare. Spesielt rendring av resultat. 

Oppgåve 1.a) er ein tekstboks på toppen av vinduet som blir laga dersom ein kjøre skriptet, medan 1.b) er informasjonen under.

##Oppgåve 2
###1.a):
Eit alternativ for android-einingar er å "publisere" ein privat app som er test-versjonen av appen. Dokumentasjon/vidare lesing kan ein finne her: https://developers.google.com/android/work/play/custom-app-api/publish 
Dette er kanskje mykje arbeid om ein sett det opp mot å la testerar installere direkte frå ei .apk-fil. Men direkte installering har derimot såpass mange ulemper at arbeidet med å styre tilgang til ein app via google play er verdt det. 
For iOS bør ein bruke TestFlight som beskreve på denne lenka: https://help.apple.com/xcode/mac/current/#/dev2539d985f

###2): 
Tilnærminga til dette var rett og slett Google-Fu. Eg satte meg først inn i kva Cordova faktisk er, for så å vurdere om React Native hadde vore eit godt alternativ dersom de allereie nyttar React som JS i appane. Eg skjønte fort nok at det hadde vore unødvendig, då det kun handlar om sjølve deployeringa av appane som er problemet. Då var det bare å finna google play og app store sine innebygde verktøy for privat deployering som eg antok måtte eksistera. Med tanke på at dykk allereie publiserer på begge plattformar, burde prosessane i lenkane eg gav vera enkle å følge. 