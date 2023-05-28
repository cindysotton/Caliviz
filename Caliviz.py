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
                   layout="centered", initial_sidebar_state="expanded",
    )


# paramétrage des fichiers

# Famille des Contaminents Inorg et Mineraux
df_ino = pd.read_csv('Reformatage_Conta_Inorg_Mineraux_aliment.csv')
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
selected = option_menu(None, ['Présentation du projet','Risques des substances','Notre alimentation','Exposition','Données - Méthodologie','Contact'],
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
    st.header("Outil interactif permettant le traitement et la visualisation des substances chimiques auxquelles est exposée la population française via son alimentation")
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
        st.markdown('<p class="big-font">295</p><p class="texte">aliments</p>', unsafe_allow_html=True)
    with col2:
        st.markdown('<p class="big-font">9324</p><p class="texte">échantillons</p>', unsafe_allow_html=True)
    with col3:
        st.markdown('<p class="big-font">479</p><p class="texte">substances</p>', unsafe_allow_html=True)
    with col4:
        st.markdown('<p class="big-font">> 273 000</p><p class="texte">analyses</p>', unsafe_allow_html=True)
    with col5:
        st.markdown('<p class="big-font">9</p><p class="texte">régions</p>', unsafe_allow_html=True)








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
if selected == "Notre alimentation":
    
    st.subheader("Définition de la notion de concentration")
    col1, col2, col3, col4 = st.columns(4)
    
    with col4:
        substances = st.selectbox(
        "Choix du groupe de substances",
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
        st.markdown("Explications des différents types d'hypothèses : ")
        st.markdown("texte + préciser les échelles")

        tab1, tab2, tab3 = st.tabs(["Hypothèse Basse", "Hypothèse Moyenne","Hypothèse Haute"])

        with tab1:
            st.markdown("")
            image = Image.open('Heatmap_ino_LB.png')
            st.image(image, use_column_width=True)

            # Filtrer les substances
            option_substances_ino_lb = st.multiselect(
                '**Sélectionner les substances que vous souhaitez analyser :**',
                options=df_ino['Nom Substance'].unique(),
                default=df_ino['Nom Substance'].unique(),
                key='substances_options_ino_lb'
            )

            # Selected substances
            if len(option_substances_ino_lb) == 0:
                st.warning('Merci de sélectionner au moins une substance')

            # Filtrer les familles d'aliments
            option_ali_ino_lb = st.multiselect(
                "**Sélectionner les familles d'aliments que vous souhaitez analyser :**",
                options=df_ino['Groupe'].unique(),
                default=df_ino['Groupe'].unique(),
                key='ali_options_ino_lb'
            )

            # Selected aliment
            if len(option_ali_ino_lb) == 0:
                st.warning("Merci de sélectionner au moins une substance et une famille d'aliments")


            # Filtrer les données en fonction des options sélectionnées
            df_filtered = df_ino[(df_ino['Nom Substance'].isin(option_substances_ino_lb)) & (df_ino['Groupe'].isin(option_ali_ino_lb))]

            # Vérifier si des substances et familles d'aliments ont été sélectionnées
            if len(option_substances_ino_lb) == 0 or len(option_ali_ino_lb) == 0:
                st.warning("Merci de sélectionner au moins une substance et une famille d'aliments")
            else:
                fig = px.bar(df_filtered, x='LB', y='Groupe', color='Nom Substance', hover_data=['Aliment'])
                fig.update_xaxes(title="Volume de la substance en µg/g")
                fig.update_yaxes(title=None)  # Supprime le titre de l'axe y
                fig.update_layout(
                    xaxis={'categoryorder': 'total descending'},
                    legend_title_text='Substances',
                    height=700,
                    width=1200,  # Augmente la largeur du graphique (ajustez la valeur selon vos besoins)
                    margin=dict(l=50, r=50, t=50, b=50, pad=4)  # Définit les marges pour centrer le graphique
                )
                st.plotly_chart(fig)

        with tab2:
            st.markdown("")
            image = Image.open('Heatmap_ino_MB.png')
            st.image(image, use_column_width=True)

                        # Filtrer les substances
            option_substances_ino_mb = st.multiselect(
                '**Sélectionner les substances que vous souhaitez analyser :**',
                options=df_ino['Nom Substance'].unique(),
                default=df_ino['Nom Substance'].unique(),
                key='substances_options_ino_mb'
            )

            # Selected substances
            if len(option_substances_ino_mb) == 0:
                st.warning('Merci de sélectionner au moins une substance')

            # Filtrer les familles d'aliments
            option_ali_ino_mb = st.multiselect(
                "**Sélectionner les familles d'aliments que vous souhaitez analyser :**",
                options=df_ino['Groupe'].unique(),
                default=df_ino['Groupe'].unique(),
                key='ali_options_ino_mb'
            )

            # Selected aliment
            if len(option_ali_ino_mb) == 0:
                st.warning("Merci de sélectionner au moins une substance et une famille d'aliments")


            # Filtrer les données en fonction des options sélectionnées
            df_filtered = df_ino[(df_ino['Nom Substance'].isin(option_substances_ino_mb)) & (df_ino['Groupe'].isin(option_ali_ino_mb))]

            # Vérifier si des substances et familles d'aliments ont été sélectionnées
            if len(option_substances_ino_mb) == 0 or len(option_ali_ino_mb) == 0:
                st.warning("Merci de sélectionner au moins une substance et une famille d'aliments")
            else:
                fig = px.bar(df_filtered, x='MB', y='Groupe', color='Nom Substance', hover_data=['Aliment'])
                fig.update_xaxes(title="Volume de la substance en µg/g")
                fig.update_yaxes(title=None)  # Supprime le titre de l'axe y
                fig.update_layout(
                    xaxis={'categoryorder': 'total descending'},
                    legend_title_text='Substances',
                    height=700,
                    width=1200,  # Augmente la largeur du graphique (ajustez la valeur selon vos besoins)
                    margin=dict(l=50, r=50, t=50, b=50, pad=4)  # Définit les marges pour centrer le graphique
                )
                st.plotly_chart(fig)
    
        with tab3:
            st.markdown("")
            image = Image.open('Heatmap_ino_UB.png')
            st.image(image, use_column_width=True)

            # Filtrer les substances
            option_substances_ino_ub = st.multiselect(
                '**Sélectionner les substances que vous souhaitez analyser :**',
                options=df_ino['Nom Substance'].unique(),
                default=df_ino['Nom Substance'].unique(),
                key='substances_options_ino_ub'
            )

            # Selected substances
            if len(option_substances_ino_ub) == 0:
                st.warning('Merci de sélectionner au moins une substance')

            # Filtrer les familles d'aliments
            option_ali_ino_ub = st.multiselect(
                "**Sélectionner les familles d'aliments que vous souhaitez analyser :**",
                options=df_ino['Groupe'].unique(),
                default=df_ino['Groupe'].unique(),
                key='ali_options_ino_ub'
            )

            # Selected aliment
            if len(option_ali_ino_ub) == 0:
                st.warning("Merci de sélectionner au moins une substance et une famille d'aliments")


            # Filtrer les données en fonction des options sélectionnées
            df_filtered = df_ino[(df_ino['Nom Substance'].isin(option_substances_ino_ub)) & (df_ino['Groupe'].isin(option_ali_ino_ub))]

            # Vérifier si des substances et familles d'aliments ont été sélectionnées
            if len(option_substances_ino_ub) == 0 or len(option_ali_ino_ub) == 0:
                st.warning("Merci de sélectionner au moins une substance et une famille d'aliments")
            else:
                fig = px.bar(df_filtered, x='UB', y='Groupe', color='Nom Substance', hover_data=['Aliment'])
                fig.update_xaxes(title="Volume de la substance en µg/g")
                fig.update_yaxes(title=None)  # Supprime le titre de l'axe y
                fig.update_layout(
                    xaxis={'categoryorder': 'total descending'},
                    legend_title_text='Substances',
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
if selected == "Exposition":
    st.markdown("Définition de l'exposition")

    


# Données - Méthodologie
if selected == 'Données - Méthodologie':
    st.header("Liens de nos données")
    st.subheader("Données fournies par le gouvernement")
    url = "https://www.data.gouv.fr/fr/datasets/bisphenol-a/"
    st.markdown("[Bisphenol A](%s)" % url)
    url = "https://www.data.gouv.fr/fr/datasets/donnees-regionales-eat2-etude-de-l-alimentation-totale/"
    st.markdown("[Etudes EAT2 ](%s)" % url)

    st.subheader("Notre méthodologie")

    st.subheader("Retraitement des données par nos équipes")
    
    st.markdown("Aperçu de nos données par groupe d'aliments")

    st.markdown("Aperçu de nos données globales")

     

# Condlusion
if selected == "Contact":
    st.markdown("")
    st.markdown("")

