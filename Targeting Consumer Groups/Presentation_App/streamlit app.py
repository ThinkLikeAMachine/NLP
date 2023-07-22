import streamlit as st
from PIL import Image

def app():
    st.title('Market Positioning of Protein Beverage Products')
    st.subheader('**_- New products launched between 2020-2023_**')
    st.divider()
    st.markdown('**Author: Hanyu Yangcheng**')
    st.divider()
    option = st.selectbox(
            'Select region:',
            ('Global', 'North America', 'Europe'))
    bar_images = dict(zip(['Global', 'North America', 'Europe'], ['global_plot.png', 'NA_plot.png', 'EU_plot.png']))
    word_images = dict(zip(['Global', 'North America', 'Europe'], ['global_words.png', 'NA_words.png', 'EU_words.png']))
    
    col1, col2 = st.columns([0.65,0.35])
    
    with col1:
        bar_image = Image.open(bar_images[option])
        st.image(bar_image, use_column_width='always')
        
    with col2:
        st.markdown('**Consumer groups explained**')
        if option == 'Global' or option == 'Europe':
            st.caption('**Nutrition**: Consumers who care most about the nutrition claims, such as high protein, high quality (complete) amino acids, contributing to muscle building')
            st.caption('**Certifications**: Consumers who care most about product certifications, such as plant-based, organic, non-GMO, naturally sourced,  recycable packaging')
            st.caption('**Muscle building & Workout**: The product can help recovery, provide energy, and increase performance during excercise, contributing to muscle building')
        else:
            st.caption('**Certifications**: Consumers who care most about product certifications, such as organic, gluten/dairy/soy-free, non-GMO, natural,  kosher')
            st.caption('**Muscle building & Nutrition**: The product can provide energy, help body recovery, and increase performance during excercise, contributing to muscle building')
            
    st.divider()
    
    with st.container():
        word_image = Image.open(word_images[option])
        st.write("Word Frequencies by Targeted Consumer Groups")
        st.image(word_image,use_column_width='always')
        
    st.divider()
    
    st.header('Most Commonly Used Ingredients for Targeted Consumer Groups - Global')
    Col1, Col2 = st.columns([0.2,0.8])
    with Col1:
        selection = st.radio(
        "**Select a targeted consumer group**",
        ('Nutrition', 'Certifications', 'Muscle building & Workout'))

    with Col2:
        if selection == 'Nutrition':
            st.markdown('xanthan gum, valine, leucine, isoleucine, methionine, tryptophan, threonine, phenylalanine, histidine, lysine, arginine, proline, glycine, serine, tyrosine, sunflower lecithin, soy lecithin, cysteine, pea protein, glutamine, alanine, inulin, cocoa powder, maltodextrin, whey protein concentrate (milk)')
        if selection == 'Certifications':
            st.markdown('gellan gum, sunflower oil, sunflower lecithin, calcium carbonate, tricalcium phosphate, vitamin d, pea protein, rapeseed oil, guar gum, locust bean gum, maltodextrin, xanthan gum, dipotassium phosphate, calcium phosphate, calcium, vitamin e, vitamin a palmitate, gellan, vitamin a, carrageenan, cocoa powder, almonds, inulin, zinc gluconate, potassium citrate')
        if selection == 'Muscle building & Workout':
            st.markdown('taurine, tyrosine, isoleucine, valine, citrulline, leucine, maltodextrin, silicon dioxide, beta-alanine, glutamine, theanine, sodium citrate, citrulline malate, creatine monohydrate, potassium citrate, caffeine, caffeine anhydrous, arginine, cluster dextrin (maltodextrin), anti-caking agent (silicon dioxide), sunflower lecithin, palatinose (isomaltulose), potassium chloride, magnesium citrate, calcium silicate, phenylalanine, tryptophan, dextrose, xanthan gum, threonine')
            
if __name__ == '__main__':
    app()
