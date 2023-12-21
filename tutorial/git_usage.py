'''
Git kezeles:

    

Git 2 flowja van:

    Amikor meg nem git kezelt a kod:
    1. Git init parancs kiadasa a megfelelo maggaban -> letrejon a .git mappa, minden file-t, mappat, stb.
    2. El kell donteni, hogy mely file-okat, mappakat NEM akarod feltolteni a git repository-ba.

        - Sensitive adatok: jelszavak, user nevek, stb

        - Olyan adatok, amelyeknek nincs relevanciaja a fejlesztes soran:
            - temporalis mappak,
            - virtualis kornyezetek,
            - IDE beallitasok, stb.


    3. Initial commit - EZ A MENTETT ALLAPOT
        - A valtozasokatSTAGE-elni kell -> ez utan mar COMMIT-alni tudsz. 
        - COMMIT-olom a valtozast: Adok egy COMMIT uzenetet, lerogzitem az allapotot. Gyakorlatilag elmented/fixalod az allapotot.
        - Adok egy COMMIT UZENETET. Egyszeru, rovid es arrol ami a valtozas volt.
            - terminal: git log -> mutatja mit COMMIT-altunk
    
    4. Letre hozok egy Remote Branch-et, pl. a Github-pn es felPUSHolom a meglevo kodot.

Amikor mar git kezelt
Git flow:

    1. Letrehozol valamilyen valtozast a kodbazison: uj sor, karakter, file, mappa, etc.
    2. Ezeket a valtozasokat figyelni akarod: STAGE-eled a valtozast
        Azt az allapotot, amit figyelek ahhoz merten fogom tudni a visszallitasst alkalmazni
        Vagy a flow tovabbi lepcsojere lepni:
    3. COMMIT message es COMMIT
    4. PUSH-olod a lokal valtozasokat a remote repository-ba

git config --global user.email "an.carde888@gmail.com"
git config --global user.name "CzarDeNas"

'''