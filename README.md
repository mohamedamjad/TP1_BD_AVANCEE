# TP1_BD_AVANCEE
Rendu du TP1 du cours bases de données avancées. Le sujet est proposé par Mr. Cyril Trambouze intervenant dans l'élément BD avancée et Big Data à l'École Nationale des Sciences Géographiques.

Ce rendu est sous licence GNU GPL 2.0. consultez le fichier LICENSE pour plus d'informations.

### Problématique:
Nous disposons de deux jeux de données (IR.csv et Zigbee.csv).
"Le premier fichier IR contient les résultats des capteurs infrarouges.
Il contient :
- un sender_id et un local_id, les identifiants des personnes portant les badges
- un date_time correspondant au moment où il y a eu contact entre les badges
infrarouges.
Le second fichier zigbee contient les résultats des capteurs bluetooth. On retrouve nos local_id et
sender_id,
un date_time, un RSSI, qui correspond à une distance entre les deux personnes." ([Cliquez ici](http://cours-express.fr/cherche-cours-exercices/lire-sujet-cours.php?id_sujet_a_lire=233) pour plus d'informations sur le sujet proposé par Mr. Cyril Trambouze).
Le but est de déterminer, à partir des positions relatives des personnes portant un badge, s'il y a eu discussion entre eux ou pas.

### Dépendances logicielles:
Ce programme est développé avec python. Il nécéssite, pour tourner, une multitude de paquets complémentaires:
- pymongo: gérer les interactions avec le serveurs MongoDB
- psycopg2: gérer les interactions avec le serveur PostgreSQL
- sys, os, pour l'interaction avec le système d'exploitation, en l'occurence Linux (testé sur la distribution Debian/Ubuntu).
- Le paquet postgresql-9.3-server-dev avec la configuration nécéssaire
- le paquet mongodb, mongodb-clients et mongodb-server

### Éxécution du programme:

 Pour faciliter à l'utilisateur la tâche de l'installation de ces dépendances. J'ai préparé un script Bash (config_db.sh). Il suffit de le lancer en ligne de commande:
```
/bin/bash src/config_db.sh
```
Ce script installe l'environnement nécéssaire à l'éxécution du programme CSV2DB.py et configure automatiquement une base de données par défaut pour effectuer le TP. Pour lancer le programme:

```
python3 src/CSV2DB.py
```
Ce programme effectue tous les tâches demandées pour le TP1:
- réaliser la connexion avec une BD postgreSQL
- Parser les 2 fichiers CSV
- Insérer leur contenus dans les tableaux appropriés dans la BD
- réaliser une première requête en utilisant l'EXPLAIN et sans indexation
- réaliser une deuxième requête en indexant la base de données et en utilisant EXPLAIN
- comparer les résultats obtenus
- configurer la BD mongoDB
- re-parser les fichiers csv et les insérer dans la BD
- effectuer une requête
- comparer les résultats obtenus

### À quoi ressemble les logs du programme:
Si les dépendances sont satisfaites et vous disposez de python3. vous aurez les logs du programme comme suit (si oui! BRAVOOO VOUS AVEZ RÉUSSIT)

```
Database Connection ... OK
CREATE TABLES ... SUCCESS
FILL THE TABLES ... SUCCESS
Analyze queries before indexation
Seq Scan on mit_zigbee  (cost=0.00..20504.64 rows=4851 width=20) (actual time=0.108..829.649 rows=85820 loops=1)
  Filter: ((rssi < 15) AND (rssi > 3))
  Rows Removed by Filter: 925887
Total runtime: 896.845 ms
Indexing RSSI column ... SUCCESS
Bitmap Heap Scan on mit_zigbee  (cost=100.28..6151.76 rows=5059 width=20) (actual time=53.774..150.223 rows=85820 loops=1)
  Recheck Cond: ((rssi < 15) AND (rssi > 3))
  ->  Bitmap Index Scan on rssi_index  (cost=0.00..99.02 rows=5059 width=0) (actual time=51.417..51.417 rows=85820 loops=1)
        Index Cond: ((rssi < 15) AND (rssi > 3))
Total runtime: 198.275 ms
connected to: 127.0.0.1
Sun Feb  1 23:02:37.324 check 9 34011
Sun Feb  1 23:02:42.555 imported 34010 objects
connected to: 127.0.0.1
Sun Feb  1 23:02:45.067 		Progress: 426012/30920097	1%
Sun Feb  1 23:02:45.075 			14000	4666/second
Sun Feb  1 23:02:48.356 		Progress: 1506903/30920097	4%
Sun Feb  1 23:02:48.356 			49300	8216/second
Sun Feb  1 23:02:51.939 		Progress: 2148690/30920097	6%
Sun Feb  1 23:02:51.940 			70300	7811/second
Sun Feb  1 23:02:55.319 		Progress: 2742011/30920097	8%
Sun Feb  1 23:02:55.319 			89600	6892/second
Sun Feb  1 23:02:59.001 		Progress: 3388640/30920097	10%
Sun Feb  1 23:02:59.002 			110700	6918/second
Sun Feb  1 23:03:01.018 		Progress: 3927249/30920097	12%
Sun Feb  1 23:03:01.050 			128200	6747/second
Sun Feb  1 23:03:04.007 		Progress: 4639556/30920097	15%
Sun Feb  1 23:03:04.008 			151500	6886/second
Sun Feb  1 23:03:07.978 		Progress: 5285322/30920097	17%
Sun Feb  1 23:03:07.979 			172600	6904/second
Sun Feb  1 23:03:10.685 		Progress: 5864825/30920097	18%
Sun Feb  1 23:03:10.685 			191400	6835/second
Sun Feb  1 23:03:13.263 		Progress: 6489627/30920097	20%
Sun Feb  1 23:03:13.263 			211800	6832/second
Sun Feb  1 23:03:16.007 		Progress: 7239466/30920097	23%
Sun Feb  1 23:03:16.007 			236100	6944/second
Sun Feb  1 23:03:19.755 		Progress: 8020676/30920097	25%
Sun Feb  1 23:03:19.755 			261500	7067/second
Sun Feb  1 23:03:22.528 		Progress: 8646902/30920097	27%
Sun Feb  1 23:03:22.528 			282000	7050/second
Sun Feb  1 23:03:25.455 		Progress: 9309068/30920097	30%
Sun Feb  1 23:03:25.455 			303600	7060/second
Sun Feb  1 23:03:28.718 		Progress: 9879477/30920097	31%
Sun Feb  1 23:03:28.718 			322300	7006/second
Sun Feb  1 23:03:31.233 		Progress: 10484720/30920097	33%
Sun Feb  1 23:03:31.234 			342800	6995/second
Sun Feb  1 23:03:35.009 		Progress: 11423815/30920097	36%
Sun Feb  1 23:03:35.010 			373200	7041/second
Sun Feb  1 23:03:38.760 		Progress: 12341756/30920097	39%
Sun Feb  1 23:03:38.761 			403000	7196/second
Sun Feb  1 23:03:41.250 		Progress: 12966582/30920097	41%
Sun Feb  1 23:03:41.251 			423500	7177/second
Sun Feb  1 23:03:44.008 		Progress: 13842051/30920097	44%
Sun Feb  1 23:03:44.008 			452200	7293/second
Sun Feb  1 23:03:47.852 		Progress: 14483756/30920097	46%
Sun Feb  1 23:03:47.853 			473200	7280/second
Sun Feb  1 23:03:50.806 		Progress: 15091146/30920097	48%
Sun Feb  1 23:03:50.806 			493000	7250/second
Sun Feb  1 23:03:53.459 		Progress: 15719055/30920097	50%
Sun Feb  1 23:03:53.460 			513500	7232/second
Sun Feb  1 23:03:56.136 		Progress: 16321161/30920097	52%
Sun Feb  1 23:03:56.140 			533400	7208/second
Sun Feb  1 23:03:59.008 		Progress: 17015044/30920097	55%
Sun Feb  1 23:03:59.009 			555900	7219/second
Sun Feb  1 23:04:02.019 		Progress: 17712161/30920097	57%
Sun Feb  1 23:04:02.023 			579000	7237/second
Sun Feb  1 23:04:05.138 		Progress: 18314374/30920097	59%
Sun Feb  1 23:04:05.139 			598900	7215/second
Sun Feb  1 23:04:08.008 		Progress: 19019580/30920097	61%
Sun Feb  1 23:04:08.009 			622100	7233/second
Sun Feb  1 23:04:11.017 		Progress: 19626414/30920097	63%
Sun Feb  1 23:04:11.017 			641900	7212/second
Sun Feb  1 23:04:14.831 		Progress: 20486293/30920097	66%
Sun Feb  1 23:04:14.832 			670200	7284/second
Sun Feb  1 23:04:17.710 		Progress: 21144160/30920097	68%
Sun Feb  1 23:04:17.710 			691800	7282/second
Sun Feb  1 23:04:20.180 		Progress: 21751151/30920097	70%
Sun Feb  1 23:04:20.180 			711700	7262/second
Sun Feb  1 23:04:23.008 		Progress: 22569654/30920097	72%
Sun Feb  1 23:04:23.009 			738400	7310/second
Sun Feb  1 23:04:26.804 		Progress: 23273999/30920097	75%
Sun Feb  1 23:04:26.805 			761400	7321/second
Sun Feb  1 23:04:29.127 		Progress: 23560420/30920097	76%
Sun Feb  1 23:04:29.128 			770800	7203/second
Sun Feb  1 23:04:32.006 		Progress: 24400527/30920097	78%
Sun Feb  1 23:04:32.007 			798500	7259/second
Sun Feb  1 23:04:35.108 		Progress: 24913058/30920097	80%
Sun Feb  1 23:04:35.109 			815800	7219/second
Sun Feb  1 23:04:38.190 		Progress: 25528546/30920097	82%
Sun Feb  1 23:04:38.190 			836200	7208/second
Sun Feb  1 23:04:41.631 		Progress: 26173123/30920097	84%
Sun Feb  1 23:04:41.631 			857300	7204/second
Sun Feb  1 23:04:44.059 		Progress: 26642570/30920097	86%
Sun Feb  1 23:04:44.060 			872500	7151/second
Sun Feb  1 23:04:47.022 		Progress: 27175969/30920097	87%
Sun Feb  1 23:04:47.034 			889900	7119/second
Sun Feb  1 23:04:50.051 		Progress: 27586696/30920097	89%
Sun Feb  1 23:04:50.051 			903300	7057/second
Sun Feb  1 23:04:53.403 		Progress: 28351928/30920097	91%
Sun Feb  1 23:04:53.404 			928000	7083/second
Sun Feb  1 23:04:56.028 		Progress: 28987189/30920097	93%
Sun Feb  1 23:04:56.031 			948800	7080/second
Sun Feb  1 23:04:59.059 		Progress: 29383588/30920097	95%
Sun Feb  1 23:04:59.070 			961700	7019/second
Sun Feb  1 23:05:02.038 		Progress: 29807342/30920097	96%
Sun Feb  1 23:05:02.044 			975700	6969/second
Sun Feb  1 23:05:05.135 		Progress: 30610163/30920097	98%
Sun Feb  1 23:05:05.136 			1001700	7004/second
Sun Feb  1 23:05:06.034 check 9 1011708
Sun Feb  1 23:05:10.549 imported 1011707 objects
Importing CSV files into MongoDB ... SUCCESS !
MongoDB Client initilization ... SUCCESS !
```
