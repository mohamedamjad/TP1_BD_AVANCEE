# TP1_BD_AVANCEE
Rendu du TP1 du cours bases de données avancées.
### Problématique:
Nous disposons de deux jeux de données (IR.csv et Zigbee.csv).
"Le premier fichier IR contient les résultats des capteurs infrarouges.
Il contient :
- un sender_id et un local_id, les identifiants des personnes portant les badges
- un date_time correspondant au moment où il y a eu contact entre les badges
infrarouges.
Le second fichier zigbee contient les résultats des capteurs bluetooth. On retrouve nos local_id et
sender_id,
un date_time, un RSSI, qui correspond à une distance entre les deux personnes." ([Cliquez ici](http://cours-express.fr/cherche-cours-exercices/lire-sujet-cours.php?id_sujet_a_lire=233) pour plus d'informations sur le sujet proposé par Mr. Cyril Trambouz).
Le but est de déterminer, à partir des positions relatives des personnes portant un badge, s'il y a eu discussion entre eux ou pas.
