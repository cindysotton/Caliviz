import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import matplotlib.colors as colors


####### MISE EN FORME DU STREAMLIT
# paramétrage page d'accueil
st.set_page_config(page_title='Caliviz',
                   page_icon='🌽', 
                   layout="wide",
                   initial_sidebar_state="expanded",
    )

# logo ANSES
image_logo = Image.open('Logo_Anses.svg')
width = 80
st.image(image_logo, width=width)

# paramétrage du menu
selected = option_menu(None, ['Présentation du projet','Les substances','Contamination','Contribution','Données - Méthodologie'],
    icons=['house',"eyedropper",'basket','funnel','clipboard-data','envelope-fill'],
    menu_icon="cast", 
    default_index=0, 
    orientation="horizontal",
    styles={
                "icon": {"color": "#blank", "font-size": "13px"},
                "nav-link": {
                    "font-size": "13px",
                    "text-align": "center",
                    "margin": "0px",
                    "--hover-color": "#FF9940",
                },
                "nav-link-selected": {"background-color": "#FF9940"},        
            },)

# couleur des onglets du menu
flierprops = dict(marker="X", markerfacecolor='orange', markersize=12,
                  linestyle='none')


#######

####### DATAFRAME à modifier en concervant le nom attribué
# Famille des Contaminents Inorg et Mineraux
#df_ino = pd.read_csv('Reformatage_Conta_Inorg_Mineraux_aliment.csv')
df_ino = pd.read_csv('Contaminants inorg et mineraux.csv')

# Renommer les colonnes
df_ino = df_ino.rename(columns={'Libellé' : 'Aliment',"Groupe de la nomenclature INCA 2":"Groupe"})
#Suppression des lignes avec la Valeur NR
df_ino = df_ino.drop(df_ino[df_ino["Contamination rapportée"] == "NR"].index)
#Changer le type des colonnes LB UB MB en valeur décimale
df_ino['UB'] = df_ino['UB'].astype('float')
df_ino['LB'] = df_ino['LB'].astype('float')
df_ino['MB'] = df_ino['MB'].astype('float')
#Suppression des colonnes qui sont inutiles dans le cadre de la représentation graphique : Date, Région, Vague
df_ino = df_ino.drop(["Date", "Région", "Vague","Unité"], axis=1)
#Fusionner les lignes (moyenne) pour avoir un détail régional et national par aliment
df_ino = df_ino.groupby(["Groupe","Aliment","Type","Famille de substances","Substance"], as_index=False).mean()
# Créer un dictionnaire à partir des colonnes "Substance" et "nom substance"
dictionnaire = {'Ag': 'Argent', 'Al': 'Aluminium', 'As': 'Arsenic', 'Ba': 'Baryum', 'Ca': 'Calcium', 'Cd': 'Cadmium', 'Co': 'Cobalt', 'Cr': 'Chromium', 'Cu': 'Cuivre', 'Fe': 'Fer', 'Ga': 'Gallium', 'Ge': 'Germanium', 'Hg': 'Mercure', 'K': 'Potassium', 'Li': 'Lithium', 'Mg': 'Magnésium', 'Mn': 'Manganese', 'Mo': 'Molybdène', 'Na': 'Sodium', 'Ni': 'Nickel', 'Pb': 'Plomb', 'Sb': 'Antimoine', 'Se': 'Selenium', 'Sn': 'Etain', 'Sr': 'Strontium', 'Te': 'Tellure', 'V': 'Vanadium', 'Zn': 'Zinc', 'AN': 'Anthracene', 'BaA': 'Benzo(a)Anthracène', 'BaP': 'Benzo[a]Pyrène', 'BbF': 'Benzo(b)fluoranthène', 'BcFL': 'Benzo[c]fluorene', 'BghiP': 'Benzo[ghi]perylene', 'BjF': 'Benzo(j)fluoranthène', 'BkF': 'Benzo(k)fluoranthène', 'CHR': 'Chrysène', 'CPP': 'Cyclopenta[cd]pyrene', 'DbaeP': 'Dibenzo[a,e]pyrene', 'DBahA': 'Dibenz[a,h]anthracene', 'DbahP': 'DiBenzo[a,h]Pyrène', 'DbaiP': 'Dibenzo[a,i]pyrene', 'DbalP': 'Dibenzo[a,l]pyrene', 'FA': 'Fluoranthene', 'IP': 'Idenopyrene', 'MCH': '5-methylchrysene', 'PHE': 'Phenanthrene', 'PY': 'Pyrene', '15-Ac-DON': '15-acétyldéoxynivalénol', '3-Ac-DON': '3-acétyldéoxynivalénol', 'AFB1': 'Aflatoxines B1', 'AFB2': 'Aflatoxines B2', 'AFG1': 'Aflatoxines G1', 'AFG2': 'Aflatoxines G2', 'AFM1': 'Aflatoxines M1', 'alpha-ZAL': 'Alpha zéaralanol', 'alpha-ZOL': 'Alpha zéaralénol', 'beta-ZAL': 'Bêta zéaralanol', 'beta-ZOL': 'Bêta zéaralénol', 'DAS': 'diacétoxyscirpénol', 'DOM1': 'dérivé déépoxyde du DON', 'DON': 'déoxynivalénol', 'FB1': 'Fumonisine B1', 'FB2': 'Fumonisine B2', 'HT2': 'Toxine HT2', 'MAS': 'monoacétoxyscirpénol', 'NIV': 'Nivalenol', 'OTA': 'Ochratoxine A', 'OTB': 'Ochratoxine B', 'Pat': 'Patuline', 'T2': 'Toxine T2', 'Ver': 'Verrucarol', 'ZEA': 'zéaralénone', 'PFBA': 'Acide perfluorobutanoïque', 'PFBS': 'Perfluorobutane sulfonate', 'PFDA': 'Acide perfluorodecanoïque', 'PFDoA': 'Acide perfluorododecanoïque', 'PFDS': 'Perfluorodecane sulfonate', 'PFHpA': 'Acide perfluoroheptanoïque', 'PFHpS': 'Perfluorohptane sulfonate', 'PFHxA': 'Acide perfluorohexanoïque', 'PFHxS': 'Perfluorohexane sulfonate', 'PFNA': 'Acide perfluorononanoïque', 'PFOA': 'Acide perfluoroocanoïque', 'PFOS': 'Perfluorooctane sulfonate', 'PFPA': 'Acide perfluoropentanoïque', 'PFTeDA': 'Acide perfluorotetradecanoïque', 'PFTrDA': 'Acide perfluorotridecanoïque', 'PFUnA': 'Acide perfluoroundecanoïque'}
#Remplacer les abréviations des Substances par leurs noms complet
df_ino['Substance'] = df_ino['Substance'].replace(dictionnaire)

# Garder juste une ligne entre R et N
# Filtrer les lignes avec le 'Type' R
rows_to_remove = df_ino[df_ino['Type'] == 'R']
# Sélectionner les colonnes pour l'identification des doublons
cols_to_check = ['Groupe', 'Aliment', 'Famille de substances', 'Substance']
# Identifier les lignes à supprimer avec le même 'Groupe', 'Aliment','Famille de substances' et 'Substance' pour les deux 'Types' R et N
duplicated_rows = df_ino[df_ino.duplicated(subset=cols_to_check, keep=False)]
# Filtrer les lignes à supprimer avec le 'Type' R
duplicated_rows_to_remove = duplicated_rows[duplicated_rows['Type'] == 'R']
# Supprimer les lignes avec le 'Type' R
df_ino = df_ino.drop(duplicated_rows_to_remove.index)


# Contribution LB et UB
df_contrib_LB_UB = pd.read_csv('Contribution_EAT2_LB_UB.csv')
# Contribution MB
df_contrib_MB = pd.read_csv('Contribution_EAT2_MB.csv')
# LB = hypithèse basse
LB_pivot_ino = pd.read_csv('LB_Pivot_Inorg_Mineraux.csv')
# MB = hypithèse moyenne
MB_pivot_ino = pd.read_csv('MB_Pivot_Inorg_Mineraux.csv')
# UB = hypithèse haute
UB_pivot_ino = pd.read_csv('UB_Pivot_Inorg_Mineraux.csv')
#######


######## Présentation du projet
if selected == "Présentation du projet":
    st.title("Caliviz")
    st.header("Outil interactif permettant la visualisation des substances chimiques auxquelles est exposée la population française via son alimentation")
    image = Image.open('alimentation-banderole.jpg')
    st.image(image, use_column_width=True)
    st.subheader("Enjeux")
    st.markdown("Selon les résultats de la dernière édition de l’étude de l’alimentation totale (EAT), le risque sanitaire ne peut être exclu dans certains groupes de la population pour 12 substances présentes dans notre alimentation courante. Aujourd’hui, la surveillance alimentaire est réalisée aléatoirement. Une optimisation de la surveillance via l’identification et le ciblage des couples aliments/substances qui posent problème est donc d’utilité publique, visant in fine à protéger le consommateur.")
    st.markdown("**Comment optimiser la sécurité sanitaire des aliments et la surveillance des couples aliments/substances qui posent véritablement problème ?**")

    st.subheader("Qu'est ce que l'Etude de l'Alimentation Totale ? (EAT)")
    st.markdown("L’Anses a pour mission de contribuer à assurer la sécurité sanitaire dans les domaines de l’alimentation, de l’environnement et du travail. Dans ce cadre, elle a lancé en 2006 sa deuxième étude de l’alimentation totale (EAT 2), ayant pour objectifs d’une part de décrire les expositions alimentaires de la population française à des substances d’intérêt en termes de santé publique, d’autre part de caractériser les risques sanitaires liés à l’alimentation et associés à ces substances [...]")
    url = "https://www.anses.fr/fr/content/%C3%A9tude-de-l%E2%80%99alimentation-totale-eat-2-l%E2%80%99anses-met-%C3%A0-disposition-les-donn%C3%A9es-de-son-analyse"
    st.markdown("[Lire la suite de l'article](%s)" % url)

    st.subheader("Quelques chiffres")
    col1, col2, col3, col4, col5 = st.columns(5)
    # chiffres en orange
    st.markdown("""
    <style>
    .big-font {
        font-size:40px !important;
        color : orange;
        text-align : center;
        padding-bottom: 0rem;
 
    }
    </style>
    """, unsafe_allow_html=True)

    # texte
    st.markdown("""
    <style>
    .texte {
        font-size:20px !important;
        text-align : center;

    }
    </style>
    """, unsafe_allow_html=True)

    with col1:
        st.markdown('<p class="big-font">212</p><p class="texte">aliments</p>', unsafe_allow_html=True)
    with col2:
        st.markdown('<p class="big-font">1319</p><p class="texte">échantillons</p>', unsafe_allow_html=True)
    with col3:
        st.markdown('<p class="big-font">445</p><p class="texte">substances</p>', unsafe_allow_html=True)
    with col4:
        st.markdown('<p class="big-font"> 250 000</p><p class="texte">résultalts analytiques</p>', unsafe_allow_html=True)
    with col5:
        st.markdown('<p class="big-font">8</p><p class="texte">régions</p>', unsafe_allow_html=True)



#######


######## Les substances (et leurs risques)
if selected == "Les substances":
    st.header("Substances chimiques et risques sanitaires")

    col1, col2, col3= st.columns(3)

    with col3:
        substances = st.selectbox(
        "Choix de la famille de substances",
        ('Contaminants inorganiques et minéraux',))#'Acrylamide', 'HAP', 'Dioxines, PCB','Perfluorés','Bromés','Phytoestrogènes','Mycotoxines','Additifs','Pesticides'))

    #if substances == "Acrylamide":


   #if substances == "HAP":

    
    #if substances == "Dioxines, PCB":


    #if substances == "Perfluorés":

    
    #if substances == "Bromés":


    if substances == "Contaminants inorganiques et minéraux":
        st.markdown("***L’arsenic (As)*** est un élément présent dans la croûte terrestre. Il provient également des activités industrielles, de la combustion de produits fossiles, d'anciennes utilisations agricoles, etc. Il existe sous différentes formes chimiques, organiques ou inorganiques. Par ingestion, l’arsenic peut entraîner des lésions cutanées, des cancers, une toxicité sur le développement, une neurotoxicité, des maladies cardiovasculaires, une perturbation du métabolisme du glucose et du diabète.")
        st.markdown("***Le plomb (Pb)*** est un métal naturellement présent dans la croûte terrestre. Son utilisation intensive par l’homme (activités minières et industrielles : fonderies, accumulateurs, pigments, alliages, munitions, etc.) est à l’origine d’une forte dispersion dans l’environnement. L’homme y est exposé principalement par les aliments et l’eau qu’il consomme, mais aussi via l’air, le sol et les poussières. Du fait de son interdiction depuis la fin des années 90 dans l’essence automobile, les peintures utilisées à l’intérieur des habitations et les canalisations d’eau, le niveau d’exposition a fortement diminué ces dix dernières années. Chez l’homme, le principal organe cible est le système nerveux central, en particulier au cours du développement chez le foetus et le jeune enfant. Chez l’adulte, le plomb a des effets sur les reins et sur le système cardiovasculaire.")
        st.markdown("***Le cadmium (Cd)*** est un métal lourd qui se retrouve dans les différents compartiments de l’environnement (sols, eau, air) du fait de sa présence à l’état naturel dans la croûte terrestre et des activités industrielles et agricoles.  La source principale d’exposition au cadmium varie selon le type de population : l’alimentation pour la population générale, la fumée de cigarette et l’air ambiant pour les travailleurs exposés en milieu industriel.Chez l’homme, une exposition prolongée au cadmium par voie orale induit une atteinte rénale. Une fragilité osseuse, des troubles de la reproduction ont également été répertoriés, ainsi qu’un risque accru de cancer ayant donné lieu à un classement comme « cancérogène pour l’homme » (groupe 1) par le Centre International de Recherche sur le Cancer (CIRC) en 1993.")
        st.markdown("***L’aluminium (Al)*** est l’élément métallique le plus abondant de la croûte terrestre. Du fait de ses propriétés physico-chimiques (basse densité, malléabilité, résistance à la corrosion, etc.), il est utilisé dans de nombreux domaines industriels (agro-alimentaire, pharmaceutique, bâtiment, etc.) et pour le traitement des eaux d’alimentation. Il est présent dans les aliments et l’eau sous différentes formes chimiques qui déterminent sa toxicité. Les effets toxiques de l’aluminium portent essentiellement sur le système nerveux central (encéphalopathies, troubles psychomoteurs) et sur le tissu osseux. Chez l’homme, ces effets sont observés chez des sujets exposés par d’autres voies que l’alimentation, conduisant à l’accumulation de fortes quantités d’aluminium : patients insuffisants rénaux dialysés, alimentation parentérale, personnes professionnellement exposées. ")
        st.markdown("***L’antimoine (Sb)*** est un métalloïde très peu abondant dans la croûte terrestre. Il est utilisé dans les alliages métalliques pour en accroître la dureté, dans la fabrication de semi-conducteurs, dans les plastiques et les feux d’artifices. Le trioxyde d’antimoine est employé comme ignifugeant pour les textiles et les matières plastiques, comme opacifiant pour les verres, les céramiques et les émaux, comme pigment pour les peintures et comme catalyseur chimique. Le trioxyde d’antimoine a été classé considéré comme « peut-être cancérogène pour l’homme » (groupe 2B) par le Centre International de Recherche sur le Cancer (CIRC) en 1989. Les sels solubles d’antimoine provoquent, après ingestion, des effets irritants au niveau gastro-intestinal se traduisant par des vomissements, des crampes abdominales et des diarrhées. Une toxicité cardiaque ou oculaire est aussi rapportée à fortes doses. ")
        st.markdown("***Le baryum (Ba)*** est un métal présent dans de nombreux minerais. Son utilisation concerne de nombreux domaines (pesticides, textiles, pigments, traitement d’eaux, médical, etc.).Les sels solubles de baryum sont bien absorbés et se déposent essentiellement au niveau du tissu osseux. Il n’a pas été démontré d’effet cancérogène ni mutagène (altération de la structure de l'ADN). Les travailleurs exposés régulièrement par inhalation au baryum peuvent présenter des manifestations pulmonaires bénignes sans troubles fonctionnels associés. ")
        st.markdown("***Le gallium (Ga)*** est un métal provenant essentiellement de l’extraction de l’aluminium et du zinc. Essentiellement sous forme de sels, il est utilisé en petite quantité pour la fabrication de semi-conducteurs, dans l’industrie électrique et électronique ; c’est un substitut du mercure pour les lampes à arc et les thermomètres pour hautes températures. Plusieurs utilisations médicales sont décrites : traceur radioactif, alliage dentaires, traitement des hypercalcémies tumorales. Dans le contexte de l’exposition professionnelle, le gallium et ses composés pénètrent par voie respiratoire, et très peu par voie digestive. La rétention de gallium au niveau pulmonaire est certaine chez l’animal. L’absorption à partir du tube digestif semble faible. Il est transporté par le sang, et se distribue dans le foie, la rate, les tissus osseux et la moelle osseuse. La toxicité est basée essentiellement sur des études animales et varie selon les espèces et les composés du gallium. Les organes cibles sont le poumon, le système hématopoïétique (ormation des globules sanguins), le système immunitaire, le rein et l’appareil reproducteur male.  L’arséniure de gallium est classé par le Centre International de Recherche sur le Cancer parmi les « cancérogènes pour l’homme » (groupe 1) en s’appuyant surtout sur des données expérimentales animales et sans en avoir démontré le mécanisme d’action.")
        st.markdown("***Le germanium (Ge)*** est un métalloïde présent naturellement dans la croûte terrestre. Il peut exister sous forme organique ou inorganique. Généralement obtenu à partir du raffinage du cuivre, du zinc et du plomb, il est utilisé principalement dans le secteur de l’électronique (diodes, transistors, etc.) et du verre (élément optique) du fait de ses propriétés proches de celles du silicium. Dans certains pays, il est également commercialisé sous forme organique en tant que complément alimentaire. L’absorption du germanium au niveau intestinal est rapide et complète. Son élimination est principalement urinaire. Il n’est ni mutagène (altération de la structure de l'ADN), ni cancérigène sous ses formes ioniques ou dioxyde de germanium. Plusieurs cas rapportés de patients exposés de manière répétée à de fortes doses de germanium (complément alimentaire) indiquent notamment des perturbations au niveau rénal.")
        st.markdown("***Le tellure (Te)*** est un metalloïde issu principalement des résidus d’affinage du cuivre. Il est utilisé principalement en métallurgie (alliage), dans l’industrie chimique (caoutchouc, plastique) et dans l’électronique. Le tellure est absorbé par ingestion et éliminé en partie dans les urines. Il n’est ni mutagène (altération de la structure de l'ADN), ni cancérogène. Des effets tératogènes (susceptible de provoquer des malformations congénitales chez les enfants exposés in utero) ont été observés chez des rats exposés oralement à des doses élevées de tellure dans la nourriture. En milieu professionnel, l’exposition par inhalation au tellure peut engendrer des symptômes sans gravité particulière, caractérisés essentiellement par une haleine alliacée.")
        st.markdown("***Le vanadium (V)*** est un métal que l’on retrouve à l’état naturel. Il est principalement utilisé en métallurgie pour augmenter la résistance des aciers, et dans d’autres industries pour ses propriétés catalytiques, colorantes ou anticorrosives. Le rôle fonctionnel du vanadium n’a pas été clairement caractérisé chez l’animal ou chez l’homme. Selon la dose, le vanadium pourrait avoir des effets sur les métabolismes lipidique et glucidique et dans la fonction thyroïdienne. Le vanadium est peu absorbé par voie orale (<1%). Chez l’animal, les études expérimentales indiquent que les effets les plus sensibles observés suite à l’ingestion de sels de vanadium sont des perturbations au niveau sanguin (pression artérielle et taux de globules rouges), des systèmes nerveux et rénal et du développement. Des études expérimentales sur un composé de vanadium (le pentoxyde de vanadium) révèlent d’autres effets toxiques (atteinte de la rate, des reins, des poumons et cancers) mais la présence de cette forme dans les aliments n’a jamais été démontrée. ")
        st.markdown("***Le nickel (Ni)*** est un métal naturellement présent dans la croûte terrestre dont les propriétés de malléabilité, de magnétisme, de conduction de la chaleur et de l’électricité conduisent à le retrouver dans de très nombreuses applications industrielles principalement sous forme d’alliages (aciers inoxydables) et de catalyseurs pour les constructions automobile, navale et aéronautique, et les industries électriques. Le nickel se retrouve sous une grande variété de formes chimiques inorganiques (métal, oxydes, sels) ou organiques. L’homme y est exposé par inhalation (exposition professionnelle), par la consommation d’eau et d’aliments et par contact cutané. Dans ce dernier cas, il est allergisant et peut provoquer une dermatite de contact. Les effets cancérogènes des composés du nickel observés après une exposition par inhalation ont conduit à une classification par le Centre International de Recherche sur le Cancer (CIRC) parmi les « cancérogènes pour l’homme » (groupe 1). Toutefois, aucune étude par voie orale n’a montré d’effet cancérogène. Aucun composé du nickel n’est actuellement classé comme mutagène (altération dela structure de l'ADN).")
        st.markdown("***Le cobalt (Co)*** est un métal naturellement présent dans la croûte terrestre. Le cobalt et ses composés minéraux ont de nombreuses applications dans l’industrie chimique et pétrolière comme catalyseur, pour la fabrication d’alliages, comme pigment pour le verre et les céramiques, comme agent séchant des peintures, etc. Il est également utilisé en tant qu’additif dans les aliments pour animaux pour les espèces capables de synthétiser la vitamine B12. On trouve le cobalt dans les produits animaux (sous forme de cobalamine) et dans les végétaux (sous forme inorganique). Chez l'homme, le cobalt absorbé est majoritairement retrouvé dans le foie et les reins. Chez l’animal, les effets toxiques rapportés avec des sels de cobalt comprennent une polycythémie (augmentation de la masse érythrocytaire totale), des modifications cardiaques, des altérations fonctionnelles et morphologiques de la thyroïde, une dégénérescence et une atrophie testiculaires, une réduction de la croissance et de la survie de la descendance. Chez l’homme, des cardiomyopathies ont été rapportées dans les années 60 chez des forts buveurs de bière, auxquelles avait été ajouté du cobalt en tant qu’agent stabilisateur de mousse. Les composés du cobalt (II) ont été classés par le Centre International de Recherche surle Cancer (CIRC) comme « peut-être cancérogènes pour l’homme » (groupe 2B). Des études ont montré que les sels de cobalt sont capables d’induire des altérations génotoxiques tels que des dommages à l’ADN, des mutations géniques, la formation de micronoyaux, des aberrations chromosomiques chez l’animal par voie orale ou parentérale.")
        st.markdown("***Le chrome (Cr)*** est un métal abondant dans la croûte terrestre, est utilisé dans des alliages métalliques tels que l’acier inoxydable, en pigments, pour le tannage des peaux, etc. L’homme y est exposé par inhalation et par la consommation d’eau et d’aliments. Chez l’homme, la déficience en chrome a été observée chez des patients recevant une nutrition parentérale totale sur le long terme. Les symptômes sont une altération de l’utilisation et de la tolérance au glucose, une altération du métabolisme lipidique, une altération du métabolisme de l’azote, une perte de poids. En cas de carences profondes, des effets neurologiques peuvent être observés. Chez l’enfant, aucune carence en chrome n’a été décrite en dehors d’une malnutrition protéino-énergétique sévère. Le chrome présente une toxicité nettement différente en fonction de sa valence. Différents composés du chrome sont génotoxiques et sont classés par le Centre International de Recherche sur le Cancer comme « cancérogènes pour l’homme » (groupe 1), du fait d’un excès de risque de cancer du poumon chez les professionnels exposés par inhalation. Par voie orale, certaines données suggèrent une augmentation de l’incidence de cancer de l’estomac chez l’Homme exposé par l’eau de boisson. ")

    
    #if substances == "Phytoestrogènes":

    
    #if substances == "Mycotoxines":

    
    #if substances == "Additifs":


    #if substances == "Pesticides":

    

       

#######


######## Contamination
if selected == "Contamination":
    st.subheader("Quantification des substances : limites analytiques et hypothèses")
    st.markdown("La quantification d’une substance chimique dans un aliment peut parfois rencontrer des difficultés en raison des limites analytiques. Il s’agit notamment des limites de détection de la substance (LD) dans l’aliment par l’appareil de mesure et/ou de quantification (LQ).")
    st.markdown("""Une substance est dite « détectée » dès lors que l’analyse a mis en évidence sa présence dans un aliment. Dans le cas contraire, la substance sera inférieure à la limite de détection (<LD).

Une substance est dite « quantifiée » lorsqu’elle a été détectée et que sa teneur est suffisamment importante pour être quantifiée. Si la teneur est très basse et que l’appareil analytique n’est pas en mesure de la quantifier, elle est seulement dite « détectée » mais inférieure à la limite de quantification (<LQ).

Pour pouvoir exploiter ces données non chiffrées, différentes hypothèses peuvent être utilisées pour avoir une estimation du niveau de contamination de ces substances en tenant compte de ces limites analytiques. Deux cas de figure ont été retenus conformément aux lignes directrices (GEMS-Food Euro, 1995) : 

***1.    le pourcentage de résultats <LD et <LQ est inférieur à 60%, les données sont remplacées par une hypothèse moyenne dite « middle bound (MB) » :***
* Toutes les valeurs non détectées (<LD) sont fixées à ½ LD.
* Toutes les valeurs non quantifiées (<LQ) sont fixées à ½ LQ.

***2.    le pourcentage de résultats <LD et <LQ est supérieur à 60%, les données sont remplacées par deux hypothèses :***
* Hypothèse basse dite « lower bound (LB) » où toutes les valeurs non détectées (<LD) sont fixées à zéro et toutes les valeurs non quantifiées (<LQ) sont fixées à la LD ou à 0 si la LD n’est pas renseignée.
* Hypothèse haute dite « upper bound (UB) » où toutes les valeurs non détectées (<LD) sont fixées à la LD et toutes les valeurs non quantifiées (<LQ) sont fixées à la LQ.\n
\n""")

    col1, col2, col3, col4, col5, col6 = st.columns(6)
    
    with col2:
        image_hypothese = Image.open('Hypotheses_Analyses.png')
        width = 700
        st.image(image_hypothese, width=width)
    
    
    col1, col2, col3 = st.columns(3)
    
    with col3:
        substances = st.selectbox(
        "Choix de la famille de substances",
        ('Contaminants inorganiques','Acrylamide', 'HAP', 'Dioxines, PCB','Perfluorés','Bromés','Phytoestrogènes','Mycotoxines','Additifs','Pesticides'))

    if substances == "Acrylamide":
        st.markdown("")

    if substances == "HAP":
        st.markdown("")
    
    if substances == "Dioxines, PCB":
        st.markdown("")

    if substances == "Perfluorés":
        st.markdown("")
    
    if substances == "Bromés":
        st.markdown("")

    if substances == "Contaminants inorganiques":
        modalites = ['Arsenic', 'Plomb', 'Cadmium', 'Aluminium', 'Mercure', 'Antimoine', 'Argent', 'Baryum',
             'Etain', 'Gallium', 'Germanium', 'Strontium', 'Tellure', 'Vanadium', 'Nickel', 'Cobalt', 'Chrome']

        # Création du nouveau dataframe avec les modalités spécifiées
        df_ino = df_ino[df_ino['Substance'].isin(modalites)]

        tab1, tab2, tab3 = st.tabs(["Hypothèse Basse", "Hypothèse Moyenne","Hypothèse Haute"])
        df_ino_ali = df_ino.groupby(['Aliment','Substance' ]).agg({'LB': 'mean', 'UB': 'mean', 'MB': 'mean', "Groupe":lambda x: x.mode().iat[0]}).reset_index()
        df_ino_groupe = df_ino.groupby(['Groupe', 'Substance']).agg({'LB': 'mean', 'UB': 'mean', 'MB': 'mean'}).reset_index()

        choix_substances = df_ino['Substance'].unique()
        choix_groupe = df_ino['Groupe'].unique()

        with tab1:
            st.markdown("")
            image = Image.open('Heatmap_ino_LB.png')
            st.image(image, use_column_width=True)

            col1, col2, col3 = st.columns(3)
    
            with col3:
                substances_LB = st.selectbox("Sélectionner la substance que vous souhaitez analyser :", choix_substances, key="substances_LB")
                df_filtered_substance = df_ino_groupe[df_ino_groupe['Substance'] == substances_LB]

            fig = px.bar(df_filtered_substance, x='LB', y='Groupe')
            fig.update_xaxes(title="Concentration dans l'aliment en µg/g")
            fig.update_yaxes(title=None)  # Supprime le titre de l'axe y
            fig.update_layout(
                      yaxis={'categoryorder': 'total ascending'},
                      legend_title_text='Substances',
                      #ascending=True
                  )
            st.plotly_chart(fig, use_container_width=True, sharing='streamlit')

            col1, col2, col3 = st.columns(3)
            with col3:
                #Groupe
                choix_groupe = df_ino_ali['Groupe'].unique().astype(str).tolist()
                # Définir la valeur par défaut
                valeur_par_defaut = "Crustacés et mollusques"
                # Trouver l'index correspondant à la valeur par défaut
                index_valeur_par_defaut = choix_groupe.index(valeur_par_defaut)
                groupe_LB= st.selectbox("Choix du groupe d'aliments", choix_groupe, index=index_valeur_par_defaut, key="groupe_LB")
                df_filtered_groupe = df_ino_ali.loc[(df_ino_ali['Groupe'] == groupe_LB) & (df_ino_ali['Substance'] == substances_LB)]
    
            fig = px.bar(df_filtered_groupe, x='LB', y='Aliment')
            fig.update_xaxes(title="Concentration dans l'aliment en µg/g")
            fig.update_yaxes(title=None)  # Supprime le titre de l'axe y
            fig.update_layout(
                    yaxis={'categoryorder': 'total ascending'},
                    legend_title_text='Substances',
                    #ascending=True
                )
            st.plotly_chart(fig, use_container_width=True, sharing='streamlit')

        with tab2:
            st.markdown("")
            image = Image.open('Heatmap_ino_MB.png')
            st.image(image, use_column_width=True)

            col1, col2, col3 = st.columns(3)
    
            with col3:
                substances_MB = st.selectbox("Sélectionner la substance que vous souhaitez analyser :", choix_substances, key="substances_MB")
                df_filtered_substance = df_ino_groupe[df_ino_groupe['Substance'] == substances_MB]

            fig = px.bar(df_filtered_substance, x='MB', y='Groupe')
            fig.update_xaxes(title="Concentration dans l'aliment en µg/g")
            fig.update_yaxes(title=None)  # Supprime le titre de l'axe y
            fig.update_layout(
                      yaxis={'categoryorder': 'total ascending'},
                      legend_title_text='Substances',
                      #ascending=True
                  )
            st.plotly_chart(fig, use_container_width=True, sharing='streamlit')

            col1, col2, col3 = st.columns(3)
    
            with col3:
                #Groupe
                choix_groupe = df_ino_ali['Groupe'].unique().astype(str).tolist()
                # Définir la valeur par défaut
                valeur_par_defaut = "Crustacés et mollusques"
                # Trouver l'index correspondant à la valeur par défaut
                index_valeur_par_defaut = choix_groupe.index(valeur_par_defaut)
                groupe_MB= st.selectbox("Choix du groupe d'aliments", choix_groupe,index=index_valeur_par_defaut, key="groupe_MB")
                df_filtered_groupe = df_ino_ali.loc[(df_ino_ali['Groupe'] == groupe_MB) & (df_ino_ali['Substance'] == substances_MB)]
    

            fig = px.bar(df_filtered_groupe, x='MB', y='Aliment')
            fig.update_xaxes(title="Concentration dans l'aliment en µg/g")
            fig.update_yaxes(title=None)  # Supprime le titre de l'axe y
            fig.update_layout(
                    yaxis={'categoryorder': 'total ascending'},
                    legend_title_text='Substances',
                    #ascending=True
                )
            st.plotly_chart(fig, use_container_width=True, sharing='streamlit')


    
        with tab3:
            st.markdown("")
            image = Image.open('Heatmap_ino_UB.png')
            st.image(image, use_column_width=True)


            col1, col2, col3 = st.columns(3)
    
            with col3:
                substances_UB = st.selectbox("Sélectionner la substance que vous souhaitez analyser :", choix_substances, key="substances_UB")
                df_filtered_substance = df_ino_groupe[df_ino_groupe['Substance'] == substances_UB]

            fig = px.bar(df_filtered_substance, x='UB', y='Groupe')
            fig.update_xaxes(title="Concentration dans l'aliment en µg/g")
            fig.update_yaxes(title=None)  # Supprime le titre de l'axe y
            fig.update_layout(
                      yaxis={'categoryorder': 'total ascending'},
                      legend_title_text='Substances',
                      #ascending=True

                  )
            st.plotly_chart(fig, use_container_width=True, sharing='streamlit')

            col1, col2, col3 = st.columns(3)
    
            with col3:
                groupe_UB= st.selectbox("Choix du groupe d'aliments", choix_groupe, key="groupe_UB")
                df_filtered_groupe = df_ino_ali.loc[(df_ino_ali['Groupe'] == groupe_UB) & (df_ino_ali['Substance'] == substances_UB)]
    

            fig = px.bar(df_filtered_groupe, x='UB', y='Aliment')
            fig.update_xaxes(title="Concentration dans l'aliment en µg/g")
            fig.update_yaxes(title=None)  # Supprime le titre de l'axe y
            fig.update_layout(
                    yaxis={'categoryorder': 'total ascending'},
                    legend_title_text='Substances',
                    #ascending=True
                )
            st.plotly_chart(fig, use_container_width=True, sharing='streamlit')


     
    
    if substances == "Phytoestrogènes":
        st.markdown("")
    
    if substances == "Mycotoxines":
        st.markdown("")
    
    if substances == "Additifs":
        st.markdown("")

    if substances == "Pesticides":
        st.markdown("")
        

if selected == "Contribution":
    st.subheader("Exposition alimentaire de la population aux substances chimiques")
    st.markdown("""L’exposition est la quantité d’une substance ingérée par le consommateur. Elle se calcule pour une personne via son alimentation en prenant en compte à la fois le niveau de contamination de tous les différents aliments / groupe d’aliments par cette substance, sa consommation individuelle de ces aliments ainsi que son poids corporel. 
\nL’exposition est calculée pour tous les individus et une exposition moyenne de la population est ainsi calculée. Elle représente la quantité moyenne d’une substance ingérée par la population via son régime alimentaire total.
\nSi l’on souhaite connaître la part apportée par chaque groupe d’aliments dans cette quantité de substance ingérée par la population, on parlera de contribution à l’exposition totale. Celle-ci, exprimée en pourcentage, représente la quantité de substance apportée par un groupe d’aliments par rapport à tout le régime alimentaire. La somme des contributions est égale à 100%.
""")
    st.markdown("""Une substance est dite « détectée » dès lors que l’analyse a mis en évidence sa présence dans un aliment. Dans le cas contraire, la substance sera inférieure à la limite de détection (<LD).

Une substance est dite « quantifiée » lorsqu’elle a été détectée et que sa teneur est suffisamment importante pour être quantifiée. Si la teneur est très basse et que l’appareil analytique n’est pas en mesure de la quantifier, elle est seulement dite « détectée » mais inférieure à la limite de quantification (<LQ).

Pour pouvoir exploiter ces données non chiffrées, deux cas de figure ont été retenus conformément aux lignes directrices (GEMS-Food Euro, 1995) : 
***1.    le pourcentage de résultats <LD et <LQ est inférieur à 60%, les données sont remplacées par une hypothèse moyenne dite « middle bound (MB) » :***
* Toutes les valeurs non détectées (<LD) sont fixées à ½ LD.
* Toutes les valeurs non quantifiées (<LQ) sont fixées à ½ LQ.

***2.    le pourcentage de résultats <LD et <LQ est supérieur à 60%, les données sont remplacées par deux hypothèses :***
* Hypothèse basse dite « lower bound (LB) » où toutes les valeurs non détectées (<LD) sont fixées à zéro et toutes les valeurs non quantifiées (<LQ) sont fixées à la LD ou à 0 si la LD n’est pas renseignée.
* Hypothèse haute dite « upper bound (UB) » où toutes les valeurs non détectées (<LD) sont fixées à la LD et toutes les valeurs non quantifiées (<LQ) sont fixées à la LQ.\n
\n""")

    col1, col2, col3, col4, col5, col6 = st.columns(6)
    
    with col2:
        image_hypothese = Image.open('Hypotheses_Analyses.png')
        width = 700
        st.image(image_hypothese, width=width)

    col1, col2, col3= st.columns(3)

    with col3:
        substances = st.selectbox(
        "Choix de la famille de substances",
        ('Contaminants inorganiques et minéraux','Acrylamide', 'HAP', 'Dioxines, PCB','Perfluorés','Bromés','Phytoestrogènes','Mycotoxines','Additifs','Pesticides'))

    if substances == "Acrylamide":
        st.markdown("")

    if substances == "HAP":
        st.markdown("")
    
    if substances == "Dioxines, PCB":
        st.markdown("")

    if substances == "Perfluorés":
        st.markdown("")
    
    if substances == "Bromés":
        st.markdown("")

    if substances == "Contaminants inorganiques et minéraux":

        tab1, tab2, tab3 = st.tabs(["Hypothèse Basse", "Hypothèse Moyenne","Hypothèse Haute"])

        with tab1:
            
            col1, col2, col3= st.columns(3)

            with col3:
              #SelectBox
              contrib_option_substances_ino_ub = st.selectbox('Sélectionner la substance que vous souhaitez analyser :',
                                                  df_contrib_LB_UB['Substance'].unique(),
                                                  key='substances_ub')

              # Convertir la valeur unique en liste
              selected_substances = [contrib_option_substances_ino_ub]
              # Filtrer les données en fonction des options sélectionnées
              df_filtered_contrib = df_contrib_LB_UB[df_contrib_LB_UB['Substance'].isin(selected_substances)]


              # Filtrer les données en fonction des options sélectionnées
              df_filtered_contrib = df_contrib_LB_UB[df_contrib_LB_UB['Substance'].isin([contrib_option_substances_ino_ub])]

            # Vérifier si des substances et familles d'aliments ont été sélectionnées
            fig = px.bar(df_filtered_contrib, x='Contribution_UB', y="Groupe d'aliments",color_discrete_sequence=['#00AC8C']) 
            fig.update_xaxes(title="% de la contribution à l’exposition totale")
            fig.update_yaxes(title=None)  # Supprime le titre de l'axe y
            fig.update_layout(
                    yaxis={'categoryorder': 'total ascending'},
                )
            st.plotly_chart(fig, use_container_width=True, sharing='streamlit')


            # Texte dynamique en fonction du choix de l'utilisateur
            if contrib_option_substances_ino_ub == 'Arsenic inorganique':
                st.caption("L’arsenic (As) est un élément présent dans la croûte terrestre. Il provient également des activités industrielles, de la combustion de produits fossiles, d'anciennes utilisations agricoles, etc. Il existe sous différentes formes chimiques, organiques ou inorganiques. Par ingestion, l’arsenic peut entraîner des lésions cutanées, des cancers, une toxicité sur le développement, une neurotoxicité, des maladies cardiovasculaires, une perturbation du métabolisme du glucose et du diabète.")
            elif contrib_option_substances_ino_ub == 'Plomb':
                st.caption("Le plomb (Pb) est un métal naturellement présent dans la croûte terrestre. Son utilisation intensive par l’homme (activités minières et industrielles : fonderies, accumulateurs, pigments, alliages, munitions, etc.) est à l’origine d’une forte dispersion dans l’environnement. L’homme y est exposé principalement par les aliments et l’eau qu’il consomme, mais aussi via l’air, le sol et les poussières. Du fait de son interdiction depuis la fin des années 90 dans l’essence automobile, les peintures utilisées à l’intérieur des habitations et les canalisations d’eau, le niveau d’exposition a fortement diminué ces dix dernières années. Chez l’homme, le principal organe cible est le système nerveux central, en particulier au cours du développement chez le foetus et le jeune enfant. Chez l’adulte, le plomb a des effets sur les reins et sur le système cardiovasculaire.")
            elif contrib_option_substances_ino_ub == 'Cadmium':
                st.caption("Le cadmium (Cd) est un métal lourd qui se retrouve dans les différents compartiments de l’environnement (sols, eau, air) du fait de sa présence à l’état naturel dans la croûte terrestre et des activités industrielles et agricoles.  La source principale d’exposition au cadmium varie selon le type de population : l’alimentation pour la population générale, la fumée de cigarette et l’air ambiant pour les travailleurs exposés en milieu industriel.Chez l’homme, une exposition prolongée au cadmium par voie orale induit une atteinte rénale. Une fragilité osseuse, des troubles de la reproduction ont également été répertoriés, ainsi qu’un risque accru de cancer ayant donné lieu à un classement comme « cancérogène pour l’homme » (groupe 1) par le Centre International de Recherche sur le Cancer (CIRC) en 1993.")
            elif contrib_option_substances_ino_ub == 'Aluminium':
                st.caption("L’aluminium (Al) est l’élément métallique le plus abondant de la croûte terrestre. Du fait de ses propriétés physico-chimiques (basse densité, malléabilité, résistance à la corrosion, etc.), il est utilisé dans de nombreux domaines industriels (agro-alimentaire, pharmaceutique, bâtiment, etc.) et pour le traitement des eaux d’alimentation. Il est présent dans les aliments et l’eau sous différentes formes chimiques qui déterminent sa toxicité. Les effets toxiques de l’aluminium portent essentiellement sur le système nerveux central (encéphalopathies, troubles psychomoteurs) et sur le tissu osseux. Chez l’homme, ces effets sont observés chez des sujets exposés par d’autres voies que l’alimentation, conduisant à l’accumulation de fortes quantités d’aluminium : patients insuffisants rénaux dialysés, alimentation parentérale, personnes professionnellement exposées. ")
            elif contrib_option_substances_ino_ub == 'Antimoine':
                st.caption("L’antimoine (Sb) est un métalloïde très peu abondant dans la croûte terrestre. Il est utilisé dans les alliages métalliques pour en accroître la dureté, dans la fabrication de semi-conducteurs, dans les plastiques et les feux d’artifices. Le trioxyde d’antimoine est employé comme ignifugeant pour les textiles et les matières plastiques, comme opacifiant pour les verres, les céramiques et les émaux, comme pigment pour les peintures et comme catalyseur chimique. Le trioxyde d’antimoine a été classé considéré comme « peut-être cancérogène pour l’homme » (groupe 2B) par le Centre International de Recherche sur le Cancer (CIRC) en 1989. Les sels solubles d’antimoine provoquent, après ingestion, des effets irritants au niveau gastro-intestinal se traduisant par des vomissements, des crampes abdominales et des diarrhées. Une toxicité cardiaque ou oculaire est aussi rapportée à fortes doses. ")
            elif contrib_option_substances_ino_ub == 'Baryum':
                st.caption("Le baryum (Ba) est un métal présent dans de nombreux minerais. Son utilisation concerne de nombreux domaines (pesticides, textiles, pigments, traitement d’eaux, médical, etc.).Les sels solubles de baryum sont bien absorbés et se déposent essentiellement au niveau du tissu osseux. Il n’a pas été démontré d’effet cancérogène ni mutagène (altération de la structure de l'ADN). Les travailleurs exposés régulièrement par inhalation au baryum peuvent présenter des manifestations pulmonaires bénignes sans troubles fonctionnels associés. ")
            elif contrib_option_substances_ino_ub == 'Gallium':
                st.caption("Le gallium (Ga) est un métal provenant essentiellement de l’extraction de l’aluminium et du zinc. Essentiellement sous forme de sels, il est utilisé en petite quantité pour la fabrication de semi-conducteurs, dans l’industrie électrique et électronique ; c’est un substitut du mercure pour les lampes à arc et les thermomètres pour hautes températures. Plusieurs utilisations médicales sont décrites : traceur radioactif, alliage dentaires, traitement des hypercalcémies tumorales. Dans le contexte de l’exposition professionnelle, le gallium et ses composés pénètrent par voie respiratoire, et très peu par voie digestive. La rétention de gallium au niveau pulmonaire est certaine chez l’animal. L’absorption à partir du tube digestif semble faible. Il est transporté par le sang, et se distribue dans le foie, la rate, les tissus osseux et la moelle osseuse. La toxicité est basée essentiellement sur des études animales et varie selon les espèces et les composés du gallium. Les organes cibles sont le poumon, le système hématopoïétique (ormation des globules sanguins), le système immunitaire, le rein et l’appareil reproducteur male.  L’arséniure de gallium est classé par le Centre International de Recherche sur le Cancer parmi les « cancérogènes pour l’homme » (groupe 1) en s’appuyant surtout sur des données expérimentales animales et sans en avoir démontré le mécanisme d’action.")
            elif contrib_option_substances_ino_ub == 'Germanium':
                st.caption("Le germanium (Ge) est un métalloïde présent naturellement dans la croûte terrestre. Il peut exister sous forme organique ou inorganique. Généralement obtenu à partir du raffinage du cuivre, du zinc et du plomb, il est utilisé principalement dans le secteur de l’électronique (diodes, transistors, etc.) et du verre (élément optique) du fait de ses propriétés proches de celles du silicium. Dans certains pays, il est également commercialisé sous forme organique en tant que complément alimentaire. L’absorption du germanium au niveau intestinal est rapide et complète. Son élimination est principalement urinaire. Il n’est ni mutagène (altération de la structure de l'ADN), ni cancérigène sous ses formes ioniques ou dioxyde de germanium. Plusieurs cas rapportés de patients exposés de manière répétée à de fortes doses de germanium (complément alimentaire) indiquent notamment des perturbations au niveau rénal.")
            elif contrib_option_substances_ino_ub == 'Tellure':
                st.caption("Le tellure (Te) est un metalloïde issu principalement des résidus d’affinage du cuivre. Il est utilisé principalement en métallurgie (alliage), dans l’industrie chimique (caoutchouc, plastique) et dans l’électronique. Le tellure est absorbé par ingestion et éliminé en partie dans les urines. Il n’est ni mutagène (altération de la structure de l'ADN), ni cancérogène. Des effets tératogènes (susceptible de provoquer des malformations congénitales chez les enfants exposés in utero) ont été observés chez des rats exposés oralement à des doses élevées de tellure dans la nourriture. En milieu professionnel, l’exposition par inhalation au tellure peut engendrer des symptômes sans gravité particulière, caractérisés essentiellement par une haleine alliacée.")
            elif contrib_option_substances_ino_ub == 'Vanadium':
                st.caption("Le vanadium (V) est un métal que l’on retrouve à l’état naturel. Il est principalement utilisé en métallurgie pour augmenter la résistance des aciers, et dans d’autres industries pour ses propriétés catalytiques, colorantes ou anticorrosives. Le rôle fonctionnel du vanadium n’a pas été clairement caractérisé chez l’animal ou chez l’homme. Selon la dose, le vanadium pourrait avoir des effets sur les métabolismes lipidique et glucidique et dans la fonction thyroïdienne. Le vanadium est peu absorbé par voie orale (<1%). Chez l’animal, les études expérimentales indiquent que les effets les plus sensibles observés suite à l’ingestion de sels de vanadium sont des perturbations au niveau sanguin (pression artérielle et taux de globules rouges), des systèmes nerveux et rénal et du développement. Des études expérimentales sur un composé de vanadium (le pentoxyde de vanadium) révèlent d’autres effets toxiques (atteinte de la rate, des reins, des poumons et cancers) mais la présence de cette forme dans les aliments n’a jamais été démontrée. ")
            elif contrib_option_substances_ino_ub == 'Nickel':
                st.caption("Le nickel (Ni) est un métal naturellement présent dans la croûte terrestre dont les propriétés de malléabilité, de magnétisme, de conduction de la chaleur et de l’électricité conduisent à le retrouver dans de très nombreuses applications industrielles principalement sous forme d’alliages (aciers inoxydables) et de catalyseurs pour les constructions automobile, navale et aéronautique, et les industries électriques. Le nickel se retrouve sous une grande variété de formes chimiques inorganiques (métal, oxydes, sels) ou organiques. L’homme y est exposé par inhalation (exposition professionnelle), par la consommation d’eau et d’aliments et par contact cutané. Dans ce dernier cas, il est allergisant et peut provoquer une dermatite de contact. Les effets cancérogènes des composés du nickel observés après une exposition par inhalation ont conduit à une classification par le Centre International de Recherche sur le Cancer (CIRC) parmi les « cancérogènes pour l’homme » (groupe 1). Toutefois, aucune étude par voie orale n’a montré d’effet cancérogène. Aucun composé du nickel n’est actuellement classé comme mutagène (altération dela structure de l'ADN).")
            elif contrib_option_substances_ino_ub == 'Cobalt':
                st.caption("Le cobalt (Co) est un métal naturellement présent dans la croûte terrestre. Le cobalt et ses composés minéraux ont de nombreuses applications dans l’industrie chimique et pétrolière comme catalyseur, pour la fabrication d’alliages, comme pigment pour le verre et les céramiques, comme agent séchant des peintures, etc. Il est également utilisé en tant qu’additif dans les aliments pour animaux pour les espèces capables de synthétiser la vitamine B12. On trouve le cobalt dans les produits animaux (sous forme de cobalamine) et dans les végétaux (sous forme inorganique). Chez l'homme, le cobalt absorbé est majoritairement retrouvé dans le foie et les reins. Chez l’animal, les effets toxiques rapportés avec des sels de cobalt comprennent une polycythémie (augmentation de la masse érythrocytaire totale), des modifications cardiaques, des altérations fonctionnelles et morphologiques de la thyroïde, une dégénérescence et une atrophie testiculaires, une réduction de la croissance et de la survie de la descendance. Chez l’homme, des cardiomyopathies ont été rapportées dans les années 60 chez des forts buveurs de bière, auxquelles avait été ajouté du cobalt en tant qu’agent stabilisateur de mousse. Les composés du cobalt (II) ont été classés par le Centre International de Recherche surle Cancer (CIRC) comme « peut-être cancérogènes pour l’homme » (groupe 2B). Des études ont montré que les sels de cobalt sont capables d’induire des altérations génotoxiques tels que des dommages à l’ADN, des mutations géniques, la formation de micronoyaux, des aberrations chromosomiques chez l’animal par voie orale ou parentérale.")
            elif contrib_option_substances_ino_ub == 'Chrome':
                st.caption("Le chrome (Cr), un métal abondant dans la croûte terrestre, est utilisé dans des alliages métalliques tels que l’acier inoxydable, en pigments, pour le tannage des peaux, etc. L’homme y est exposé par inhalation et par la consommation d’eau et d’aliments. Chez l’homme, la déficience en chrome a été observée chez des patients recevant une nutrition parentérale totale sur le long terme. Les symptômes sont une altération de l’utilisation et de la tolérance au glucose, une altération du métabolisme lipidique, une altération du métabolisme de l’azote, une perte de poids. En cas de carences profondes, des effets neurologiques peuvent être observés. Chez l’enfant, aucune carence en chrome n’a été décrite en dehors d’une malnutrition protéino-énergétique sévère. Le chrome présente une toxicité nettement différente en fonction de sa valence. Différents composés du chrome sont génotoxiques et sont classés par le Centre International de Recherche sur le Cancer comme « cancérogènes pour l’homme » (groupe 1), du fait d’un excès de risque de cancer du poumon chez les professionnels exposés par inhalation. Par voie orale, certaines données suggèrent une augmentation de l’incidence de cancer de l’estomac chez l’Homme exposé par l’eau de boisson. ")


            


        with tab2:

            col1, col2, col3= st.columns(3)

            with col3:
           
                #SelectBox
                contrib_option_substances_ino_mb = st.selectbox('Sélectionner la substance que vous souhaitez analyser :',
                                                            df_contrib_MB['Substance'].unique())
                # Convertir la valeur unique en liste
                selected_substances = [contrib_option_substances_ino_mb]
                # Filtrer les données en fonction des options sélectionnées
                df_filtered_contrib = df_contrib_MB[df_contrib_MB['Substance'].isin(selected_substances)]

                # Filtrer les données en fonction des options sélectionnées
                df_filtered_contrib = df_contrib_MB[df_contrib_MB['Substance'].isin([contrib_option_substances_ino_mb])]

            # Vérifier si des substances et familles d'aliments ont été sélectionnées
            fig = px.bar(df_filtered_contrib, x='Contribution_MB', y="Groupe d'aliments",color_discrete_sequence=['#00AC8C']) 
            fig.update_xaxes(title="% de la contribution à l’exposition totale")
            fig.update_yaxes(title=None)  # Supprime le titre de l'axe y
            fig.update_layout(
                    yaxis={'categoryorder': 'total ascending'},
                )
            st.plotly_chart(fig, use_container_width=True, sharing='streamlit')
            
            # Texte dynamique en fonction du choix de l'utilisateur
            if contrib_option_substances_ino_mb == 'Arsenic inorganique':
                st.caption("L’arsenic (As) est un élément présent dans la croûte terrestre. Il provient également des activités industrielles, de la combustion de produits fossiles, d'anciennes utilisations agricoles, etc. Il existe sous différentes formes chimiques, organiques ou inorganiques. Par ingestion, l’arsenic peut entraîner des lésions cutanées, des cancers, une toxicité sur le développement, une neurotoxicité, des maladies cardiovasculaires, une perturbation du métabolisme du glucose et du diabète.")
            elif contrib_option_substances_ino_mb == 'Plomb':
                st.caption("Le plomb (Pb) est un métal naturellement présent dans la croûte terrestre. Son utilisation intensive par l’homme (activités minières et industrielles : fonderies, accumulateurs, pigments, alliages, munitions, etc.) est à l’origine d’une forte dispersion dans l’environnement. L’homme y est exposé principalement par les aliments et l’eau qu’il consomme, mais aussi via l’air, le sol et les poussières. Du fait de son interdiction depuis la fin des années 90 dans l’essence automobile, les peintures utilisées à l’intérieur des habitations et les canalisations d’eau, le niveau d’exposition a fortement diminué ces dix dernières années. Chez l’homme, le principal organe cible est le système nerveux central, en particulier au cours du développement chez le foetus et le jeune enfant. Chez l’adulte, le plomb a des effets sur les reins et sur le système cardiovasculaire.")
            elif contrib_option_substances_ino_mb == 'Cadmium':
                st.caption("Le cadmium (Cd) est un métal lourd qui se retrouve dans les différents compartiments de l’environnement (sols, eau, air) du fait de sa présence à l’état naturel dans la croûte terrestre et des activités industrielles et agricoles.  La source principale d’exposition au cadmium varie selon le type de population : l’alimentation pour la population générale, la fumée de cigarette et l’air ambiant pour les travailleurs exposés en milieu industriel.Chez l’homme, une exposition prolongée au cadmium par voie orale induit une atteinte rénale. Une fragilité osseuse, des troubles de la reproduction ont également été répertoriés, ainsi qu’un risque accru de cancer ayant donné lieu à un classement comme « cancérogène pour l’homme » (groupe 1) par le Centre International de Recherche sur le Cancer (CIRC) en 1993.")
            elif contrib_option_substances_ino_mb == 'Aluminium':
                st.caption("L’aluminium (Al) est l’élément métallique le plus abondant de la croûte terrestre. Du fait de ses propriétés physico-chimiques (basse densité, malléabilité, résistance à la corrosion, etc.), il est utilisé dans de nombreux domaines industriels (agro-alimentaire, pharmaceutique, bâtiment, etc.) et pour le traitement des eaux d’alimentation. Il est présent dans les aliments et l’eau sous différentes formes chimiques qui déterminent sa toxicité. Les effets toxiques de l’aluminium portent essentiellement sur le système nerveux central (encéphalopathies, troubles psychomoteurs) et sur le tissu osseux. Chez l’homme, ces effets sont observés chez des sujets exposés par d’autres voies que l’alimentation, conduisant à l’accumulation de fortes quantités d’aluminium : patients insuffisants rénaux dialysés, alimentation parentérale, personnes professionnellement exposées. ")
            elif contrib_option_substances_ino_mb == 'Antimoine':
                st.caption("L’antimoine (Sb) est un métalloïde très peu abondant dans la croûte terrestre. Il est utilisé dans les alliages métalliques pour en accroître la dureté, dans la fabrication de semi-conducteurs, dans les plastiques et les feux d’artifices. Le trioxyde d’antimoine est employé comme ignifugeant pour les textiles et les matières plastiques, comme opacifiant pour les verres, les céramiques et les émaux, comme pigment pour les peintures et comme catalyseur chimique. Le trioxyde d’antimoine a été classé considéré comme « peut-être cancérogène pour l’homme » (groupe 2B) par le Centre International de Recherche sur le Cancer (CIRC) en 1989. Les sels solubles d’antimoine provoquent, après ingestion, des effets irritants au niveau gastro-intestinal se traduisant par des vomissements, des crampes abdominales et des diarrhées. Une toxicité cardiaque ou oculaire est aussi rapportée à fortes doses. ")
            elif contrib_option_substances_ino_mb == 'Baryum':
                st.caption("Le baryum (Ba) est un métal présent dans de nombreux minerais. Son utilisation concerne de nombreux domaines (pesticides, textiles, pigments, traitement d’eaux, médical, etc.).Les sels solubles de baryum sont bien absorbés et se déposent essentiellement au niveau du tissu osseux. Il n’a pas été démontré d’effet cancérogène ni mutagène (altération de la structure de l'ADN). Les travailleurs exposés régulièrement par inhalation au baryum peuvent présenter des manifestations pulmonaires bénignes sans troubles fonctionnels associés. ")
            elif contrib_option_substances_ino_mb == 'Gallium':
                st.caption("Le gallium (Ga) est un métal provenant essentiellement de l’extraction de l’aluminium et du zinc. Essentiellement sous forme de sels, il est utilisé en petite quantité pour la fabrication de semi-conducteurs, dans l’industrie électrique et électronique ; c’est un substitut du mercure pour les lampes à arc et les thermomètres pour hautes températures. Plusieurs utilisations médicales sont décrites : traceur radioactif, alliage dentaires, traitement des hypercalcémies tumorales. Dans le contexte de l’exposition professionnelle, le gallium et ses composés pénètrent par voie respiratoire, et très peu par voie digestive. La rétention de gallium au niveau pulmonaire est certaine chez l’animal. L’absorption à partir du tube digestif semble faible. Il est transporté par le sang, et se distribue dans le foie, la rate, les tissus osseux et la moelle osseuse. La toxicité est basée essentiellement sur des études animales et varie selon les espèces et les composés du gallium. Les organes cibles sont le poumon, le système hématopoïétique (ormation des globules sanguins), le système immunitaire, le rein et l’appareil reproducteur male.  L’arséniure de gallium est classé par le Centre International de Recherche sur le Cancer parmi les « cancérogènes pour l’homme » (groupe 1) en s’appuyant surtout sur des données expérimentales animales et sans en avoir démontré le mécanisme d’action.")
            elif contrib_option_substances_ino_mb == 'Germanium':
                st.caption("Le germanium (Ge) est un métalloïde présent naturellement dans la croûte terrestre. Il peut exister sous forme organique ou inorganique. Généralement obtenu à partir du raffinage du cuivre, du zinc et du plomb, il est utilisé principalement dans le secteur de l’électronique (diodes, transistors, etc.) et du verre (élément optique) du fait de ses propriétés proches de celles du silicium. Dans certains pays, il est également commercialisé sous forme organique en tant que complément alimentaire. L’absorption du germanium au niveau intestinal est rapide et complète. Son élimination est principalement urinaire. Il n’est ni mutagène (altération de la structure de l'ADN), ni cancérigène sous ses formes ioniques ou dioxyde de germanium. Plusieurs cas rapportés de patients exposés de manière répétée à de fortes doses de germanium (complément alimentaire) indiquent notamment des perturbations au niveau rénal.")
            elif contrib_option_substances_ino_mb == 'Tellure':
                st.caption("Le tellure (Te) est un metalloïde issu principalement des résidus d’affinage du cuivre. Il est utilisé principalement en métallurgie (alliage), dans l’industrie chimique (caoutchouc, plastique) et dans l’électronique. Le tellure est absorbé par ingestion et éliminé en partie dans les urines. Il n’est ni mutagène (altération de la structure de l'ADN), ni cancérogène. Des effets tératogènes (susceptible de provoquer des malformations congénitales chez les enfants exposés in utero) ont été observés chez des rats exposés oralement à des doses élevées de tellure dans la nourriture. En milieu professionnel, l’exposition par inhalation au tellure peut engendrer des symptômes sans gravité particulière, caractérisés essentiellement par une haleine alliacée.")
            elif contrib_option_substances_ino_mb == 'Vanadium':
                st.caption("Le vanadium (V) est un métal que l’on retrouve à l’état naturel. Il est principalement utilisé en métallurgie pour augmenter la résistance des aciers, et dans d’autres industries pour ses propriétés catalytiques, colorantes ou anticorrosives. Le rôle fonctionnel du vanadium n’a pas été clairement caractérisé chez l’animal ou chez l’homme. Selon la dose, le vanadium pourrait avoir des effets sur les métabolismes lipidique et glucidique et dans la fonction thyroïdienne. Le vanadium est peu absorbé par voie orale (<1%). Chez l’animal, les études expérimentales indiquent que les effets les plus sensibles observés suite à l’ingestion de sels de vanadium sont des perturbations au niveau sanguin (pression artérielle et taux de globules rouges), des systèmes nerveux et rénal et du développement. Des études expérimentales sur un composé de vanadium (le pentoxyde de vanadium) révèlent d’autres effets toxiques (atteinte de la rate, des reins, des poumons et cancers) mais la présence de cette forme dans les aliments n’a jamais été démontrée. ")
            elif contrib_option_substances_ino_mb == 'Nickel':
                st.caption("Le nickel (Ni) est un métal naturellement présent dans la croûte terrestre dont les propriétés de malléabilité, de magnétisme, de conduction de la chaleur et de l’électricité conduisent à le retrouver dans de très nombreuses applications industrielles principalement sous forme d’alliages (aciers inoxydables) et de catalyseurs pour les constructions automobile, navale et aéronautique, et les industries électriques. Le nickel se retrouve sous une grande variété de formes chimiques inorganiques (métal, oxydes, sels) ou organiques. L’homme y est exposé par inhalation (exposition professionnelle), par la consommation d’eau et d’aliments et par contact cutané. Dans ce dernier cas, il est allergisant et peut provoquer une dermatite de contact. Les effets cancérogènes des composés du nickel observés après une exposition par inhalation ont conduit à une classification par le Centre International de Recherche sur le Cancer (CIRC) parmi les « cancérogènes pour l’homme » (groupe 1). Toutefois, aucune étude par voie orale n’a montré d’effet cancérogène. Aucun composé du nickel n’est actuellement classé comme mutagène (altération dela structure de l'ADN).")
            elif contrib_option_substances_ino_mb == 'Cobalt':
                st.caption("Le cobalt (Co) est un métal naturellement présent dans la croûte terrestre. Le cobalt et ses composés minéraux ont de nombreuses applications dans l’industrie chimique et pétrolière comme catalyseur, pour la fabrication d’alliages, comme pigment pour le verre et les céramiques, comme agent séchant des peintures, etc. Il est également utilisé en tant qu’additif dans les aliments pour animaux pour les espèces capables de synthétiser la vitamine B12. On trouve le cobalt dans les produits animaux (sous forme de cobalamine) et dans les végétaux (sous forme inorganique). Chez l'homme, le cobalt absorbé est majoritairement retrouvé dans le foie et les reins. Chez l’animal, les effets toxiques rapportés avec des sels de cobalt comprennent une polycythémie (augmentation de la masse érythrocytaire totale), des modifications cardiaques, des altérations fonctionnelles et morphologiques de la thyroïde, une dégénérescence et une atrophie testiculaires, une réduction de la croissance et de la survie de la descendance. Chez l’homme, des cardiomyopathies ont été rapportées dans les années 60 chez des forts buveurs de bière, auxquelles avait été ajouté du cobalt en tant qu’agent stabilisateur de mousse. Les composés du cobalt (II) ont été classés par le Centre International de Recherche surle Cancer (CIRC) comme « peut-être cancérogènes pour l’homme » (groupe 2B). Des études ont montré que les sels de cobalt sont capables d’induire des altérations génotoxiques tels que des dommages à l’ADN, des mutations géniques, la formation de micronoyaux, des aberrations chromosomiques chez l’animal par voie orale ou parentérale.")
            elif contrib_option_substances_ino_mb == 'Chrome':
                st.caption("Le chrome (Cr), un métal abondant dans la croûte terrestre, est utilisé dans des alliages métalliques tels que l’acier inoxydable, en pigments, pour le tannage des peaux, etc. L’homme y est exposé par inhalation et par la consommation d’eau et d’aliments. Chez l’homme, la déficience en chrome a été observée chez des patients recevant une nutrition parentérale totale sur le long terme. Les symptômes sont une altération de l’utilisation et de la tolérance au glucose, une altération du métabolisme lipidique, une altération du métabolisme de l’azote, une perte de poids. En cas de carences profondes, des effets neurologiques peuvent être observés. Chez l’enfant, aucune carence en chrome n’a été décrite en dehors d’une malnutrition protéino-énergétique sévère. Le chrome présente une toxicité nettement différente en fonction de sa valence. Différents composés du chrome sont génotoxiques et sont classés par le Centre International de Recherche sur le Cancer comme « cancérogènes pour l’homme » (groupe 1), du fait d’un excès de risque de cancer du poumon chez les professionnels exposés par inhalation. Par voie orale, certaines données suggèrent une augmentation de l’incidence de cancer de l’estomac chez l’Homme exposé par l’eau de boisson. ")



        with tab3:
            
            col1, col2, col3= st.columns(3)

            with col3:
            
                #SelectBox
                contrib_option_substances_ino_lb = st.selectbox('Sélectionner la substance que vous souhaitez analyser :',
                                                            df_contrib_LB_UB['Substance'].unique())
                # Convertir la valeur unique en liste
                selected_substances = [contrib_option_substances_ino_lb]
                # Filtrer les données en fonction des options sélectionnées
                df_filtered_contrib = df_contrib_LB_UB[df_contrib_LB_UB['Substance'].isin(selected_substances)]

                # Filtrer les données en fonction des options sélectionnées
                df_filtered_contrib = df_contrib_LB_UB[df_contrib_LB_UB['Substance'].isin([contrib_option_substances_ino_lb])]

            # Vérifier si des substances et familles d'aliments ont été sélectionnées
            fig = px.bar(df_filtered_contrib, x='Contribution_LB', y="Groupe d'aliments",color_discrete_sequence=['#00AC8C']) 
            fig.update_xaxes(title="% de la contribution à l’exposition totale")
            fig.update_yaxes(title=None)  # Supprime le titre de l'axe y
            fig.update_layout(
                    yaxis={'categoryorder': 'total ascending'},
                )
            st.plotly_chart(fig, use_container_width=True, sharing='streamlit')

            # Texte dynamique en fonction du choix de l'utilisateur
            if contrib_option_substances_ino_lb == 'Arsenic inorganique':
                st.caption("L’arsenic (As) est un élément présent dans la croûte terrestre. Il provient également des activités industrielles, de la combustion de produits fossiles, d'anciennes utilisations agricoles, etc. Il existe sous différentes formes chimiques, organiques ou inorganiques. Par ingestion, l’arsenic peut entraîner des lésions cutanées, des cancers, une toxicité sur le développement, une neurotoxicité, des maladies cardiovasculaires, une perturbation du métabolisme du glucose et du diabète.")
            elif contrib_option_substances_ino_lb == 'Plomb':
                st.caption("Le plomb (Pb) est un métal naturellement présent dans la croûte terrestre. Son utilisation intensive par l’homme (activités minières et industrielles : fonderies, accumulateurs, pigments, alliages, munitions, etc.) est à l’origine d’une forte dispersion dans l’environnement. L’homme y est exposé principalement par les aliments et l’eau qu’il consomme, mais aussi via l’air, le sol et les poussières. Du fait de son interdiction depuis la fin des années 90 dans l’essence automobile, les peintures utilisées à l’intérieur des habitations et les canalisations d’eau, le niveau d’exposition a fortement diminué ces dix dernières années. Chez l’homme, le principal organe cible est le système nerveux central, en particulier au cours du développement chez le foetus et le jeune enfant. Chez l’adulte, le plomb a des effets sur les reins et sur le système cardiovasculaire.")
            elif contrib_option_substances_ino_lb == 'Cadmium':
                st.caption("Le cadmium (Cd) est un métal lourd qui se retrouve dans les différents compartiments de l’environnement (sols, eau, air) du fait de sa présence à l’état naturel dans la croûte terrestre et des activités industrielles et agricoles.  La source principale d’exposition au cadmium varie selon le type de population : l’alimentation pour la population générale, la fumée de cigarette et l’air ambiant pour les travailleurs exposés en milieu industriel.Chez l’homme, une exposition prolongée au cadmium par voie orale induit une atteinte rénale. Une fragilité osseuse, des troubles de la reproduction ont également été répertoriés, ainsi qu’un risque accru de cancer ayant donné lieu à un classement comme « cancérogène pour l’homme » (groupe 1) par le Centre International de Recherche sur le Cancer (CIRC) en 1993.")
            elif contrib_option_substances_ino_lb == 'Aluminium':
                st.caption("L’aluminium (Al) est l’élément métallique le plus abondant de la croûte terrestre. Du fait de ses propriétés physico-chimiques (basse densité, malléabilité, résistance à la corrosion, etc.), il est utilisé dans de nombreux domaines industriels (agro-alimentaire, pharmaceutique, bâtiment, etc.) et pour le traitement des eaux d’alimentation. Il est présent dans les aliments et l’eau sous différentes formes chimiques qui déterminent sa toxicité. Les effets toxiques de l’aluminium portent essentiellement sur le système nerveux central (encéphalopathies, troubles psychomoteurs) et sur le tissu osseux. Chez l’homme, ces effets sont observés chez des sujets exposés par d’autres voies que l’alimentation, conduisant à l’accumulation de fortes quantités d’aluminium : patients insuffisants rénaux dialysés, alimentation parentérale, personnes professionnellement exposées. ")
            elif contrib_option_substances_ino_lb == 'Antimoine':
                st.caption("L’antimoine (Sb) est un métalloïde très peu abondant dans la croûte terrestre. Il est utilisé dans les alliages métalliques pour en accroître la dureté, dans la fabrication de semi-conducteurs, dans les plastiques et les feux d’artifices. Le trioxyde d’antimoine est employé comme ignifugeant pour les textiles et les matières plastiques, comme opacifiant pour les verres, les céramiques et les émaux, comme pigment pour les peintures et comme catalyseur chimique. Le trioxyde d’antimoine a été classé considéré comme « peut-être cancérogène pour l’homme » (groupe 2B) par le Centre International de Recherche sur le Cancer (CIRC) en 1989. Les sels solubles d’antimoine provoquent, après ingestion, des effets irritants au niveau gastro-intestinal se traduisant par des vomissements, des crampes abdominales et des diarrhées. Une toxicité cardiaque ou oculaire est aussi rapportée à fortes doses. ")
            elif contrib_option_substances_ino_lb == 'Baryum':
                st.caption("Le baryum (Ba) est un métal présent dans de nombreux minerais. Son utilisation concerne de nombreux domaines (pesticides, textiles, pigments, traitement d’eaux, médical, etc.).Les sels solubles de baryum sont bien absorbés et se déposent essentiellement au niveau du tissu osseux. Il n’a pas été démontré d’effet cancérogène ni mutagène (altération de la structure de l'ADN). Les travailleurs exposés régulièrement par inhalation au baryum peuvent présenter des manifestations pulmonaires bénignes sans troubles fonctionnels associés. ")
            elif contrib_option_substances_ino_lb == 'Gallium':
                st.caption("Le gallium (Ga) est un métal provenant essentiellement de l’extraction de l’aluminium et du zinc. Essentiellement sous forme de sels, il est utilisé en petite quantité pour la fabrication de semi-conducteurs, dans l’industrie électrique et électronique ; c’est un substitut du mercure pour les lampes à arc et les thermomètres pour hautes températures. Plusieurs utilisations médicales sont décrites : traceur radioactif, alliage dentaires, traitement des hypercalcémies tumorales. Dans le contexte de l’exposition professionnelle, le gallium et ses composés pénètrent par voie respiratoire, et très peu par voie digestive. La rétention de gallium au niveau pulmonaire est certaine chez l’animal. L’absorption à partir du tube digestif semble faible. Il est transporté par le sang, et se distribue dans le foie, la rate, les tissus osseux et la moelle osseuse. La toxicité est basée essentiellement sur des études animales et varie selon les espèces et les composés du gallium. Les organes cibles sont le poumon, le système hématopoïétique (ormation des globules sanguins), le système immunitaire, le rein et l’appareil reproducteur male.  L’arséniure de gallium est classé par le Centre International de Recherche sur le Cancer parmi les « cancérogènes pour l’homme » (groupe 1) en s’appuyant surtout sur des données expérimentales animales et sans en avoir démontré le mécanisme d’action.")
            elif contrib_option_substances_ino_lb == 'Germanium':
                st.caption("Le germanium (Ge) est un métalloïde présent naturellement dans la croûte terrestre. Il peut exister sous forme organique ou inorganique. Généralement obtenu à partir du raffinage du cuivre, du zinc et du plomb, il est utilisé principalement dans le secteur de l’électronique (diodes, transistors, etc.) et du verre (élément optique) du fait de ses propriétés proches de celles du silicium. Dans certains pays, il est également commercialisé sous forme organique en tant que complément alimentaire. L’absorption du germanium au niveau intestinal est rapide et complète. Son élimination est principalement urinaire. Il n’est ni mutagène (altération de la structure de l'ADN), ni cancérigène sous ses formes ioniques ou dioxyde de germanium. Plusieurs cas rapportés de patients exposés de manière répétée à de fortes doses de germanium (complément alimentaire) indiquent notamment des perturbations au niveau rénal.")
            elif contrib_option_substances_ino_lb == 'Tellure':
                st.caption("Le tellure (Te) est un metalloïde issu principalement des résidus d’affinage du cuivre. Il est utilisé principalement en métallurgie (alliage), dans l’industrie chimique (caoutchouc, plastique) et dans l’électronique. Le tellure est absorbé par ingestion et éliminé en partie dans les urines. Il n’est ni mutagène (altération de la structure de l'ADN), ni cancérogène. Des effets tératogènes (susceptible de provoquer des malformations congénitales chez les enfants exposés in utero) ont été observés chez des rats exposés oralement à des doses élevées de tellure dans la nourriture. En milieu professionnel, l’exposition par inhalation au tellure peut engendrer des symptômes sans gravité particulière, caractérisés essentiellement par une haleine alliacée.")
            elif contrib_option_substances_ino_lb == 'Vanadium':
                st.caption("Le vanadium (V) est un métal que l’on retrouve à l’état naturel. Il est principalement utilisé en métallurgie pour augmenter la résistance des aciers, et dans d’autres industries pour ses propriétés catalytiques, colorantes ou anticorrosives. Le rôle fonctionnel du vanadium n’a pas été clairement caractérisé chez l’animal ou chez l’homme. Selon la dose, le vanadium pourrait avoir des effets sur les métabolismes lipidique et glucidique et dans la fonction thyroïdienne. Le vanadium est peu absorbé par voie orale (<1%). Chez l’animal, les études expérimentales indiquent que les effets les plus sensibles observés suite à l’ingestion de sels de vanadium sont des perturbations au niveau sanguin (pression artérielle et taux de globules rouges), des systèmes nerveux et rénal et du développement. Des études expérimentales sur un composé de vanadium (le pentoxyde de vanadium) révèlent d’autres effets toxiques (atteinte de la rate, des reins, des poumons et cancers) mais la présence de cette forme dans les aliments n’a jamais été démontrée. ")
            elif contrib_option_substances_ino_lb == 'Nickel':
                st.caption("Le nickel (Ni) est un métal naturellement présent dans la croûte terrestre dont les propriétés de malléabilité, de magnétisme, de conduction de la chaleur et de l’électricité conduisent à le retrouver dans de très nombreuses applications industrielles principalement sous forme d’alliages (aciers inoxydables) et de catalyseurs pour les constructions automobile, navale et aéronautique, et les industries électriques. Le nickel se retrouve sous une grande variété de formes chimiques inorganiques (métal, oxydes, sels) ou organiques. L’homme y est exposé par inhalation (exposition professionnelle), par la consommation d’eau et d’aliments et par contact cutané. Dans ce dernier cas, il est allergisant et peut provoquer une dermatite de contact. Les effets cancérogènes des composés du nickel observés après une exposition par inhalation ont conduit à une classification par le Centre International de Recherche sur le Cancer (CIRC) parmi les « cancérogènes pour l’homme » (groupe 1). Toutefois, aucune étude par voie orale n’a montré d’effet cancérogène. Aucun composé du nickel n’est actuellement classé comme mutagène (altération dela structure de l'ADN).")
            elif contrib_option_substances_ino_lb == 'Cobalt':
                st.caption("Le cobalt (Co) est un métal naturellement présent dans la croûte terrestre. Le cobalt et ses composés minéraux ont de nombreuses applications dans l’industrie chimique et pétrolière comme catalyseur, pour la fabrication d’alliages, comme pigment pour le verre et les céramiques, comme agent séchant des peintures, etc. Il est également utilisé en tant qu’additif dans les aliments pour animaux pour les espèces capables de synthétiser la vitamine B12. On trouve le cobalt dans les produits animaux (sous forme de cobalamine) et dans les végétaux (sous forme inorganique). Chez l'homme, le cobalt absorbé est majoritairement retrouvé dans le foie et les reins. Chez l’animal, les effets toxiques rapportés avec des sels de cobalt comprennent une polycythémie (augmentation de la masse érythrocytaire totale), des modifications cardiaques, des altérations fonctionnelles et morphologiques de la thyroïde, une dégénérescence et une atrophie testiculaires, une réduction de la croissance et de la survie de la descendance. Chez l’homme, des cardiomyopathies ont été rapportées dans les années 60 chez des forts buveurs de bière, auxquelles avait été ajouté du cobalt en tant qu’agent stabilisateur de mousse. Les composés du cobalt (II) ont été classés par le Centre International de Recherche surle Cancer (CIRC) comme « peut-être cancérogènes pour l’homme » (groupe 2B). Des études ont montré que les sels de cobalt sont capables d’induire des altérations génotoxiques tels que des dommages à l’ADN, des mutations géniques, la formation de micronoyaux, des aberrations chromosomiques chez l’animal par voie orale ou parentérale.")
            elif contrib_option_substances_ino_lb == 'Chrome':
                st.caption("Le chrome (Cr), un métal abondant dans la croûte terrestre, est utilisé dans des alliages métalliques tels que l’acier inoxydable, en pigments, pour le tannage des peaux, etc. L’homme y est exposé par inhalation et par la consommation d’eau et d’aliments. Chez l’homme, la déficience en chrome a été observée chez des patients recevant une nutrition parentérale totale sur le long terme. Les symptômes sont une altération de l’utilisation et de la tolérance au glucose, une altération du métabolisme lipidique, une altération du métabolisme de l’azote, une perte de poids. En cas de carences profondes, des effets neurologiques peuvent être observés. Chez l’enfant, aucune carence en chrome n’a été décrite en dehors d’une malnutrition protéino-énergétique sévère. Le chrome présente une toxicité nettement différente en fonction de sa valence. Différents composés du chrome sont génotoxiques et sont classés par le Centre International de Recherche sur le Cancer comme « cancérogènes pour l’homme » (groupe 1), du fait d’un excès de risque de cancer du poumon chez les professionnels exposés par inhalation. Par voie orale, certaines données suggèrent une augmentation de l’incidence de cancer de l’estomac chez l’Homme exposé par l’eau de boisson. ")


    
    if substances == "Phytoestrogènes":
        st.markdown("")
    
    if substances == "Mycotoxines":
        st.markdown("")
    
    if substances == "Additifs":
        st.markdown("")

    if substances == "Pesticides":
        st.markdown("")
    


    


# Données - Méthodologie
if selected == 'Données - Méthodologie':
    st.header("Données")
    st.markdown("Les données intégrées dans cet outil de visualisation sont issues de l’étude de l’alimentation totale (EAT2) menée par l’Anses et publiée en 2014. Ces données sont accessibles sur data.gouv:")
    
    url = "https://www.data.gouv.fr/fr/datasets/donnees-regionales-eat2-etude-de-l-alimentation-totale/"
    st.markdown("[Données issues de l’étude EAT2 (Anses, 2014)](%s)" % url)
    url = "https://www.data.gouv.fr/fr/datasets/bisphenol-a/"
    st.markdown("[Données aux niveaux de concentration en BPA des différents aliments issus de l’EAT2 (Anses, 2013) ](%s)" % url)
    
    st.header("Méthodologie - Traitement des données")

    st.markdown("""La première étape du projet Caliviz a consisté à traiter les données inférieures aux limites de détection ou de quantification, dites données censurées, pour tenir compte des limites analytiques et des spécificités des différentes familles de substances. En fonction des substances et des groupes d’aliments pour lesquels les limites analytiques sont connues ou non, les données censurées étaient renseignées dans les fichiers sous différents formats. Par conséquent, plusieurs prétraitements spécifiques pour les différentes familles de substances ont été ainsi réalisés afin d'harmoniser l’ensemble des données qui seront ensuite intégrées à l’outil de visualisation.

***Formatage de type 1 : Contaminants inorganiques et minéraux - Acrylamide***\n
Dans ce cas, les données censurées sont uniquement sous la forme “ND/NQ” et les limites analytiques sont connues. La contamination de chaque aliment par chaque substance est estimée en fonction des hypothèses de censure comme suit:
* Hypothèse moyenne (MB) : ND = LOD/2 et NQ = LOQ/2
* Hypothèse basse (LB) : ND = 0 et NQ = LOD
* Hypothèse haute (UB) : ND = LOD et NQ = LOQ

***Formatage de type 2 : HAP - Dioxynes, PC8 - Perfluorés - Bromés***\n
Dans ce cas, les données censurées sont renseignées la forme “<valeur” et que les limites de détection et/ou de quantification ne sont pas connues. La contamination de chaque aliment par chaque substance est estimée en fonction des hypothèses de censure comme suit: 
* Hypothèse moyenne (MB) : <valeur = valeur/2
* Hypothèse basse (LB) : <valeur = 0
* Hypothèse haute (UB) : <valeur = valeur\n

***Formatage de type 3 : Additifs - Pesticides***\n
Dans ce cas les données censurées sont sous la forme ND(valeur)/NQ(valeur) et que les limites analytiques ne sont pas fournies. La contamination de chaque aliment par chaque substance est estimée en fonction des hypothèses de censure comme suit:
* Hypothèse moyenne (MB) : ND(valeur) = valeur/2 et NQ(valeur) = valeur/2
* Hypothèse basse (LB) : ND(valeur) = 0 et NQ(valeur) = 0
* Hypothèse haute (UB) : ND(valeur) = valeur et NQ(valeur) = valeur
""")

    st.subheader("Toutes les données prétraitées sont accessibles ici")
    def main():
        style = f"background-color: #5770BE; border-radius: 5px; padding: 10px; text-align: center; font-size: 16px; color: white;"
        button_html = f'<a href="https://gitlab.com/data-challenge-gd4h/caliviz" target="_blank" style="{style}">GitLab de nos données</a>'
        st.markdown(button_html, unsafe_allow_html=True)

    if __name__ == "__main__":
        main()
