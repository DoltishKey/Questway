# Questway

INSTALL MYSQLdb ON MAC

Öppna terminalen och installera Xcode. Detta gör du genom att skriva in kommandot:
$ xcode-select --install

Gå in på följande länk: http://brew.sh/

     * Följ instruktionerna högst upp på sidan
        - klistra in: /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
          i terminalen
        - Du kommer bli informerad och få Godkänna (med retur-tangenten/skriva in ditt lösenord) varje steg i processen
     * Se till att gå igenom hela installationsprocessen.

När homebrew är installerat skriv in följande i terminalen, i tur och ordning. Följande kommandon kommer installera wget, MySQL och MySQL-python:
$ brew install wget
$ brew install MySQL
$ sudo pip install MySQL-python
