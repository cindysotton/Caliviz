import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import matplotlib.colors as colors

# paramétrage page d'accueil
st.set_page_config(page_title='Caliviz',
                    # icon à modifier
                   page_icon='🌽', 
                   layout="wide",
                   initial_sidebar_state="expanded",
    )


# paramétrage des fichiers

# Famille des Contaminents Inorg et Mineraux
df_ino = pd.read_csv('Reformatage_Conta_Inorg_Mineraux_aliment.csv')
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


# a modifier
flierprops = dict(marker="X", markerfacecolor='orange', markersize=12,
                  linestyle='none')

# logo ANSES
image_logo = Image.open('Logo Anses.jpg')
width = 80

st.image(image_logo, width=width)

# 2. horizontal menu
selected = option_menu(None, ['Présentation du projet','Risques des substances','Contamination','Contribution','Données - Méthodologie','Contact'],
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

# Présentation du projet
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








# Les substances et leurs risques
if selected == "Risques des substances":
    st.markdown("Comprendre les risques")

    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10 = st.tabs(["Risque 1", "Risque 2","Risque 3","Risque 4","Risque 5","Risque 6","Risque 7","Risque 8","Risque 9","Risque 10"])

    with tab1:
        st.markdown("")

    with tab2:
        st.markdown("")
   
    with tab3:
        st.markdown("")
    
    with tab4:
        st.markdown("")
    
    with tab5:
        st.markdown("")

    with tab6:
        st.markdown("")

    with tab7:
        st.markdown("")

    with tab8:
        st.markdown("")

    with tab9:
        st.markdown("")

    with tab10:
        st.markdown("")
    
    st.markdown("Détails des groupes d'aliments")
    st.markdown("Détails des familles de substances")
       
# Notre alimentation
if selected == "Contamination":
    st.subheader("Définition de la notion de la contamination")

    col1, col2 = st.columns(2)
    
    with col1:
        substances = st.selectbox("Choix du groupe de substances",
        ('Contaminants inorg et minéraux','Acrylamide', 'HAP', 'Dioxines, PCB','Perfluorés','Bromés','Phytoestrogènes','Mycotoxines','Additifs','Pesticides'))


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

    if substances == "Contaminants inorg et minéraux":

        st.subheader("Explications des 3 hypothèses :")
        st.markdown("""Une substance est dite « détectée » dès lors que l’analyse a mis en évidence sa présence dans un aliment. Dans le cas contraire, la substance sera inférieure à la limite de détection (<LD).

Une substance est dite « quantifiée » lorsqu’elle a été détectée et que sa teneur est suffisamment importante pour être quantifiée. Si la teneur est très basse et que l’appareil analytique n’est pas en mesure de la quantifier, elle est seulement dite « détectée » mais inférieure à la limite de quantification (<LQ).

Pour pouvoir exploiter ces données non chiffrées, deux cas de figure ont été retenus conformément aux lignes directrices (GEMS-Food Euro, 1995) : 
1.    le pourcentage de résultats <LD et <LQ est inférieur à 60%, les données sont remplacées par une hypothèse moyenne dite « middle bound (MB) » :
* Toutes les valeurs non détectées (<LD) sont fixées à ½ LD.
* Toutes les valeurs non quantifiées (<LQ) sont fixées à ½ LQ.
 
2.    le pourcentage de résultats <LD et <LQ est supérieur à 60%, les données sont remplacées par deux hypothèses :
* Hypothèse basse dite « lower bound (LB) » où toutes les valeurs non détectées (<LD) sont fixées à zéro et toutes les valeurs non quantifiées (<LQ) sont fixées à la LD ou à 0 si la LD n’est pas renseignée.
* Hypothèse haute dite « upper bound (UB) » où toutes les valeurs non détectées (<LD) sont fixées à la LD et toutes les valeurs non quantifiées (<LQ) sont fixées à la LQ.\n
\n""")

        tab1, tab2, tab3 = st.tabs(["Hypothèse Basse", "Hypothèse Moyenne","Hypothèse Haute"])

        with tab1:
            st.markdown("")
            image = Image.open('Heatmap_ino_LB.png')
            st.image(image, use_column_width=True)
            
 
        with tab2:
            st.markdown("")
            image = Image.open('Heatmap_ino_MB.png')
            st.image(image, use_column_width=True)

  
        with tab3:
            st.markdown("")
            image = Image.open('Heatmap_ino_UB.png')
            st.image(image, use_column_width=True)

    
    if substances == "Phytoestrogènes":
        st.markdown("")
    
    if substances == "Mycotoxines":
        st.markdown("")
    
    if substances == "Additifs":
        st.markdown("")

    if substances == "Pesticides":
        st.markdown("")
        

    #tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10 = st.tabs(["Famille 1", "Famille 2","Famille 3","Famille 4","Famille 5","Famille 6","Famille 7","Famille 8","Famille 9","Famille 10"])

    #with tab1:
        st.markdown("")

    #with tab2:
        st.markdown("")
   
    #with tab3:
        st.markdown("")
    
    #with tab4:
        st.markdown("")
    
    #with tab5:
        st.markdown("")

    #with tab6:
        st.markdown("")

    #with tab7:
        st.markdown("")

    #with tab8:
        st.markdown("")

    #with tab9:
        st.markdown("")

    #with tab10:
        st.markdown("")

# Exposition des substances
if selected == "Contribution":
    st.subheader("Définition de l'exposition")
    st.markdown("""L’exposition est la quantité d’une substance ingérée par le consommateur. Elle se calcule pour une personne via son alimentation en prenant en compte à la fois le niveau de contamination de tous les différents aliments / groupe d’aliments par cette substance, sa consommation individuelle de ces aliments ainsi que son poids corporel. 
L’exposition est calculée pour tous les individus et une exposition moyenne de la population est ainsi calculée. Elle représente la quantité moyenne d’une substance ingérée par la population via son régime alimentaire total.
Si l’on souhaite connaître la part apportée par chaque groupe d’aliments dans cette quantité de substance ingérée par la population, on parlera de contribution à l’exposition totale. Celle-ci, exprimée en pourcentage, représente la quantité de substance apportée par un groupe d’aliments par rapport à tout le régime alimentaire. La somme des contributions est égale à 100%.
""")
    col1, col2, col3= st.columns(3)

    with col3:
        substances = st.selectbox(
        "Choix du groupe de substances",
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
        st.subheader("Explications des 3 hypothèses :")
        st.markdown("""Une substance est dite « détectée » dès lors que l’analyse a mis en évidence sa présence dans un aliment. Dans le cas contraire, la substance sera inférieure à la limite de détection (<LD).

Une substance est dite « quantifiée » lorsqu’elle a été détectée et que sa teneur est suffisamment importante pour être quantifiée. Si la teneur est très basse et que l’appareil analytique n’est pas en mesure de la quantifier, elle est seulement dite « détectée » mais inférieure à la limite de quantification (<LQ).

Pour pouvoir exploiter ces données non chiffrées, deux cas de figure ont été retenus conformément aux lignes directrices (GEMS-Food Euro, 1995) : 
1.    le pourcentage de résultats <LD et <LQ est inférieur à 60%, les données sont remplacées par une hypothèse moyenne dite « middle bound (MB) » :
* Toutes les valeurs non détectées (<LD) sont fixées à ½ LD.
* Toutes les valeurs non quantifiées (<LQ) sont fixées à ½ LQ.
 
2.    le pourcentage de résultats <LD et <LQ est supérieur à 60%, les données sont remplacées par deux hypothèses :
* Hypothèse basse dite « lower bound (LB) » où toutes les valeurs non détectées (<LD) sont fixées à zéro et toutes les valeurs non quantifiées (<LQ) sont fixées à la LD ou à 0 si la LD n’est pas renseignée.
* Hypothèse haute dite « upper bound (UB) » où toutes les valeurs non détectées (<LD) sont fixées à la LD et toutes les valeurs non quantifiées (<LQ) sont fixées à la LQ.\n
\n""")
        tab1, tab2, tab3 = st.tabs(["Hypothèse Basse", "Hypothèse Moyenne","Hypothèse Haute"])

        with tab1:
            st.markdown("**texte explicatif substances manquantes**")
            
            col1, col2, col3= st.columns(3)

            with col3:
            #SelectBox
            contrib_option_substances_ino_ub = st.selectbox('Sélectionner les substances que vous souhaitez analyser :',
                                                df_contrib_LB_UB['Substance'].unique(),
                                                key='substances_ub')

            # Convertir la valeur unique en liste
            selected_substances = [contrib_option_substances_ino_ub]
            # Filtrer les données en fonction des options sélectionnées
            df_filtered_contrib = df_contrib_LB_UB[df_contrib_LB_UB['Substance'].isin(selected_substances)]

            # Selected substances
            if len(contrib_option_substances_ino_ub) == 0:
                st.warning('Merci de sélectionner au moins une substance')

            # Filtrer les données en fonction des options sélectionnées
            df_filtered_contrib = df_contrib_LB_UB[df_contrib_LB_UB['Substance'].isin([contrib_option_substances_ino_ub])]

            # Vérifier si des substances et familles d'aliments ont été sélectionnées
            fig = px.bar(df_filtered_contrib, x='Contribution_UB', y="Groupe d'aliments", color='Substance')
            fig.update_xaxes(title="% de la contribution à l’exposition totale")
            fig.update_yaxes(title=None)  # Supprime le titre de l'axe y
            fig.update_layout(
                    yaxis={'categoryorder': 'total ascending'},
                    legend_title_text='Substances',
                    #ascending=True
                    height=700,
                    width=1200,  # Augmente la largeur du graphique (ajustez la valeur selon vos besoins)
                    margin=dict(l=50, r=50, t=50, b=50, pad=4)  # Définit les marges pour centrer le graphique
                )
            st.plotly_chart(fig)


        with tab2:
            st.markdown("")
           
             #SelectBox
            contrib_option_substances_ino_mb = st.selectbox('Sélectionner les substances que vous souhaitez analyser :',
                                                           df_contrib_MB['Substance'].unique())
            # Convertir la valeur unique en liste
            selected_substances = [contrib_option_substances_ino_mb]
            # Filtrer les données en fonction des options sélectionnées
            df_filtered_contrib = df_contrib_MB[df_contrib_MB['Substance'].isin(selected_substances)]

            # Selected substances
            if len(contrib_option_substances_ino_mb) == 0:
                st.warning('Merci de sélectionner au moins une substance')

            # Filtrer les données en fonction des options sélectionnées
            df_filtered_contrib = df_contrib_MB[df_contrib_MB['Substance'].isin([contrib_option_substances_ino_mb])]

            # Vérifier si des substances et familles d'aliments ont été sélectionnées
            fig = px.bar(df_filtered_contrib, x='Contribution_MB', y="Groupe d'aliments", color='Substance')
            fig.update_xaxes(title="Contribution de la substance sur 100")
            fig.update_yaxes(title=None)  # Supprime le titre de l'axe y
            fig.update_layout(
                    yaxis={'categoryorder': 'total ascending'},
                    legend_title_text='Substances',
                    #ascending=True
                    height=700,
                    width=1200,  # Augmente la largeur du graphique (ajustez la valeur selon vos besoins)
                    margin=dict(l=50, r=50, t=50, b=50, pad=4)  # Définit les marges pour centrer le graphique
                )
            st.plotly_chart(fig)

        with tab3:
            st.markdown("**texte explicatif substances manquantes**")
            
            #SelectBox
            contrib_option_substances_ino_lb = st.selectbox('Sélectionner les substances que vous souhaitez analyser :',
                                                           df_contrib_LB_UB['Substance'].unique())
            # Convertir la valeur unique en liste
            selected_substances = [contrib_option_substances_ino_lb]
            # Filtrer les données en fonction des options sélectionnées
            df_filtered_contrib = df_contrib_LB_UB[df_contrib_LB_UB['Substance'].isin(selected_substances)]

            # Selected substances
            if len(contrib_option_substances_ino_lb) == 0:
                st.warning('Merci de sélectionner au moins une substance')

            # Filtrer les données en fonction des options sélectionnées
            df_filtered_contrib = df_contrib_LB_UB[df_contrib_LB_UB['Substance'].isin([contrib_option_substances_ino_lb])]

            # Vérifier si des substances et familles d'aliments ont été sélectionnées
            fig = px.bar(df_filtered_contrib, x='Contribution_LB', y="Groupe d'aliments", color='Substance')
            fig.update_xaxes(title="Contribution de la substance sur 100")
            fig.update_yaxes(title=None)  # Supprime le titre de l'axe y
            fig.update_layout(
                    yaxis={'categoryorder': 'total ascending'},
                    legend_title_text='Substances',
                    #ascending=True
                    height=700,
                    width=1200,  # Augmente la largeur du graphique (ajustez la valeur selon vos besoins)
                    margin=dict(l=50, r=50, t=50, b=50, pad=4)  # Définit les marges pour centrer le graphique
                )
            st.plotly_chart(fig)

    
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
    st.header("Liens de nos données")
    st.subheader("Données fournies par le gouvernement")
    url = "https://www.data.gouv.fr/fr/datasets/bisphenol-a/"
    st.markdown("[Bisphenol A](%s)" % url)
    url = "https://www.data.gouv.fr/fr/datasets/donnees-regionales-eat2-etude-de-l-alimentation-totale/"
    st.markdown("[Etudes EAT2 ](%s)" % url)
    
    st.header("Notre méthodologie")
    st.subheader("EAT2 - Méthodologie des valeurs manques")
    st.markdown("""Les différents types de valeurs présents dans les fichiers utilisés dans le cadre du projet Caliviz étaient les suivantes :
* ND : non détecté (analytique) (données censurées)
* NQ : non quantifié (analytique) (données censurées)
* NR : analyse non réalisée
* Valeur quantifiée

Les données censurées ont été traitées en utilisant les hypothèses de l’OMS (1995) pour le traitement de la censure et les valeurs de LOD (limite de détection) et LOQ (limite de quantification) correspondants aux substances chimiques étudiées. Plusieurs modèles de formatage ont été ainsi établis en fonction des informations à disposition.

Formatage de type 1 : Contaminants inorganiques et minéraux - Acrylamide\n
Dans ce cas, les données censurées sont uniquement sous la forme ND/NQ et nous avons accès aux limites analytiques.
* Hypothèse moyenne (MB) : ND = LOD/2 et NQ = LOQ/2
* Hypothèse basse (LB) : ND = 0 et NQ = LOD
* Hypothèse haute (UB) : ND = LOD et NQ = LOQ

Formatage de type 2 : HAP - Dioxynes, PC8 - Perfluorés - Bromés\n
Dans ce cas, les données censurées sont sous la forme “<valeur” et nous n’avons pas accès aux limites analytiques.
* Hypothèse moyenne (MB) : <valeur = valeur/2
* Hypothèse basse (LB) : <valeur = 0
* Hypothèse haute (UB) : <valeur = valeur\n

Formatage de type 3 : Additifs - Pesticides\n
Dans ce cas les données censurées sont sous la forme ND(valeur)/NQ(valeur) et nous n’avons pas accès aux limites analytiques.
* Hypothèse moyenne (MB) : ND(valeur) = valeur/2 et NQ(valeur) = valeur/2
* Hypothèse basse (LB) : ND(valeur) = 0 et NQ(valeur) = 0
* Hypothèse haute (UB) : ND(valeur) = valeur et NQ(valeur) = valeur
""")

    st.subheader("Retraitement des données par nos équipes")
    
    st.markdown("Aperçu de nos données par groupe d'aliments")

    st.markdown("Aperçu de nos données globales")



     

# Condlusion
if selected == "Contact":
    st.markdown("")
    st.markdown("")
