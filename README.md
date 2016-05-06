# Questway

INSTALL MYSQLdb ON MAC

 (1)Öppna terminalen och installera Xcode. Detta gör du genom att skriva in kommandot:

    $ xcode-select --install

 (2)Gå in på följande länk: http://brew.sh/

     * Följ instruktionerna högst upp på sidan, eller:
        - klistra in: /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
          i terminalen
        - Du kommer bli informerad och få Godkänna (med retur-tangenten/skriva in ditt lösenord) varje steg i processen
     * Se till att gå igenom hela installationsprocessen.


 (3)När homebrew är installerat skriv in följande i terminalen, i tur och ordning. Följande kommandon kommer installera wget, MySQL och MySQL-python:

    $ brew install wget
    $ brew install MySQL
    $ sudo pip install MySQL-python
        - Här ska MySQL för Python nu installeras
        - If "command not found" skriver du in följande:
    $ sudo easy_install pip
    $ sudo pip install MySQL-python
   
