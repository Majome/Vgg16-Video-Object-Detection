import streamlit as st

def app():
    
    st.title('Object Detection using VGG16 Model...')

    c1, c2, c3 = st.beta_columns([4,2,4])
    with c2:
        st.write('Done by:')

    b1,m1,l1 = st.beta_columns([3,1,3])
    with b1:
        st.write('Blessed Mutengwa - R182565F')
        st.write('blessedmutengwa@gmail.com')
    with m1:
        st.write("|")
    with l1:
        st.write('Linval Chisoko - R182565F')
        st.write('linvaltchisoko@gmail.com')