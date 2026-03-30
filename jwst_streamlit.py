import streamlit as st
import pandas as pd


st.set_page_config(page_title="JWST Image Gallery", page_icon="🪐", layout="wide") #setting up the name and icon in browser tab, as well as layout

#dealing with html and reformatting for streamlit dataframe
dfs = pd.read_html('JWST_gallery.html') #read html file we downloaded from jupyternotebook
df = dfs[0] #it reads as multiple dataframes, so set to the first one that is read
images = ['m101.jpeg', 'wlm.jpeg', 'm64.jpeg', 'ngc6357.jpeg', 'ngc2566.jpeg', 'm16.jpeg', 'm1.jpeg', 'eso350.jpeg', 'm82.jpeg', 'ugca205.jpeg', 'm51.jpeg', 'ngc1300.jpeg', 'ngc4038.jpeg', 'ngc2207.jpeg', 'sgrb2.jpeg']
df['Images'] = images #input image file names back into columns, since html file displayed the images
df.rename(columns={"Images": "Image Filepath"}, inplace=True) #change column name to something more accurate
df.rename(columns={"Unnamed: 0": "Index"}, inplace=True) #set html index column as dataframe column. was set as unnamed after reading
df.set_index('Index', inplace=True) #set index as new index column

st.header("JWST Image Gallery")

#multiple tabs
gallery, select, compare = st.tabs(['Image Gallery', 'Select Object', 'Compare Objects']) #setting tab names and variables

with gallery:
    st.header("JWST Image Gallery")
    st.image(images, width=450)
    
col1, col2 = st.columns(2)

with select: #single selection tab
    st.header("Object Viewing")
    st.subheader("Select any object to view its image and information :star:") #section for selecting objects
    event1 = st.dataframe(df, width='stretch', on_select="rerun", selection_mode="single-row", column_config={'Image Filepath': None}) #setting as 'event' variable stores selection in order to be accessed later
    try: #must be a try/except block to avoid displaying error messages when no object is selected
        chosen = event1.selection.rows 
        chosendf = df.iloc[chosen]
        image = chosendf['Image Filepath'].iloc[0] #setting image variable to proper filepath of selected object
        st.dataframe(chosendf)
        st.image(image, width=500)
    except:
        st.write("No object selected :disappointed:")
        
with compare:
    st.header("Object Comparison")
    st.subheader("Select two or more objects to compare their information :stars:")
    event2 = st.dataframe(df, width="stretch", on_select="rerun", selection_mode="multi-row", column_config={'Image Filepath': None}) #setting as 'event' variable stores selection in order to be accessed later
    try:
        comp = event2.selection.rows 
        compdf = df.iloc[comp]
        st.dataframe(compdf)
    except:
        st.write("No objects to compare :slightly_frowning_face:")
