# Challenge GD4H - Caliviz

*For an english translated version of this file, follow this [link](/README.en.md)*

Le <a href="https://gd4h.ecologie.gouv.fr/" target="_blank" rel="noreferrer">Green Data for Health</a> (GD4H) est une offre de service incubée au sein de l’ECOLAB, laboratoire d’innovation pour la transition écologique du Commissariat Général au Développement Durable.

Elle organise un challenge permettant le développement d’outils ancrés dans la communauté de la donnée en santé-environnement afin d’adresser des problématiques partagées.

Liens : 
<a href="https://challenge.gd4h.ecologie.gouv.fr/" target="_blank" rel="noreferrer">Site</a> / 
<a href="https://forum.challenge.gd4h.ecologie.gouv.fr/" target="_blank" rel="noreferrer">Forum</a>
a

## Caliviz

Selon les résultats de la denière édition de l’étude de l’alimentation totale (EAT), le risque sanitaire ne peut être exclu dans certains groupes de la population pour 12 substances présentes dans notre alimentation courante. Aujourd’hui, la surveillance alimentaire est réalisée aléatoirement.

Une optimisation de la surveillance via l’identification et le ciblage des couples aliments/substances qui posent problème est donc d’utilité publique, visant in fine à protéger le consommateur.

<a href="https://challenge.gd4h.ecologie.gouv.fr/defi/?topic=14" target="_blank" rel="noreferrer">En savoir plus sur le défi</a>

## **Documentation**

### Méthodologie - Traitement des données
La première étape du projet Caliviz a consisté à traiter les données inférieures aux limites de détection ou de quantification, dites données censurées, pour tenir compte des limites analytiques et des spécificités des différentes familles de substances. En fonction des substances et des groupes d’aliments pour lesquels les limites analytiques sont connues ou non, les données censurées étaient renseignées dans les fichiers sous différents formats. Par conséquent, plusieurs prétraitements spécifiques pour les différentes familles de substances ont été ainsi réalisés afin d'harmoniser l’ensemble des données qui seront ensuite intégrées à l’outil de visualisation.

Accès à notre GitLab : https://gitlab.com/data-challenge-gd4h/caliviz

#### Formatage de type 1 : Contaminants inorganiques et minéraux - Acrylamide

Dans ce cas, les données censurées sont uniquement sous la forme “ND/NQ” et les limites analytiques sont connues. La contamination de chaque aliment par chaque substance est estimée en fonction des hypothèses de censure comme suit:

- Hypothèse moyenne (MB) : ND = LOD/2 et NQ = LOQ/2
- Hypothèse basse (LB) : ND = 0 et NQ = LOD
- Hypothèse haute (UB) : ND = LOD et NQ = LOQ

#### Formatage de type 2 : HAP - Dioxynes, PC8 - Perfluorés - Bromés

Dans ce cas, les données censurées sont renseignées la forme “<valeur” et que les limites de détection et/ou de quantification ne sont pas connues. La contamination de chaque aliment par chaque substance est estimée en fonction des hypothèses de censure comme suit:

- Hypothèse moyenne (MB) : <valeur = valeur/2
- Hypothèse basse (LB) : <valeur = 0
- Hypothèse haute (UB) : <valeur = valeur

#### Formatage de type 3 : Additifs - Pesticides

Dans ce cas les données censurées sont sous la forme ND(valeur)/NQ(valeur) et que les limites analytiques ne sont pas fournies. La contamination de chaque aliment par chaque substance est estimée en fonction des hypothèses de censure comme suit:

- Hypothèse moyenne (MB) : ND(valeur) = valeur/2 et NQ(valeur) = valeur/2
- Hypothèse basse (LB) : ND(valeur) = 0 et NQ(valeur) = 0
- Hypothèse haute (UB) : ND(valeur) = valeur et NQ(valeur) = valeur

### **Utilisation**

Utilisation directement sur la plateforme : https://caliviz.streamlit.app/

### **Contributions**

Si vous souhaitez contribuer à ce projet, merci de suivre les [recommendations](/CONTRIBUTING.md).

### **Licence**

Le code est publié sous licence [MIT](/licence.MIT).

Les données référencés dans ce README et dans le guide d'installation sont publiés sous [Etalab Licence Ouverte 2.0](/licence.etalab-2.0).
