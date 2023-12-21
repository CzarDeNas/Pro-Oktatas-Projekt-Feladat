# pip list - ha nem tudom valamelyik lib-nek a verziojat

'''
Package-eknek altalaban van verzioja.
Nem mindegy, hogy melyik verziot hasznalom.


2 megkozelitese van a pachage hasznalatanak:

    Mindig a latest verziot hasznalom, ha nincs odairva semmi
        - Pro:
                - Mindig a legfrissebb verzio all rendelkezesemre -> Altalaban a legjobb verzio az uj
        
        - Con:
                - Production-be minden package valtozasnal veszelyezteted az utemezett mukodest azzal,
                hogy elofordulhat, hogy a fejlesztes mas verzion tortent, mint az elesites.
                Nem mindig okoz problemat, de okozhat nagyon nagy bajt

    
    Fix verziokkal dolgozom:
        - Pro:
                - Tudsz tervezni a releasekkel -> Ha valamelyik modult le kell cserelned ujra,
                akkor meg tudod tervezni ezt a munkafolyamatot.
        
        - Con:
                - Foglalkoznod kell a package menedzselessel.

Virtualis kornyezet letrehozasa requirements.txt-vel:
pipi install -r requirements.txt

Ha a teljes venv-ben levo package-et akarom feltelpiteni, hogy minden ugyan az legyen:

pip freeze > test.txt       letre fog hozni egy test.txt-t.
'''