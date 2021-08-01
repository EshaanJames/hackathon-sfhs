import streamlit as st


def study(name):
    st.header(f"Welcome Student to SKY Learners Hub")
    if name:
        st.subheader("We are pleased to see you here.")
        subject = st.selectbox("Select the skill you want to study",
                               ['None', 'Language', 'Archeology', 'Science', 'Others'])
        if subject == 'Language':
            with st.beta_expander("Watch the following video to learn spoken english...", expanded=False):
                st.write("You can learn Spoken English here .")
                st.video("https://youtu.be/WfOS2tbkbbw")
        if subject == 'Archeology':
            with st.beta_expander("Watch the following video to know about Harappan Civilisation...",
                                  expanded=False):
                st.video("https://www.youtube.com/watch?v=XvrE38HL0HM")
            with st.beta_expander("Watch the following video to know about Mohan-jodaro Civilisation...",
                                  expanded=False):
                st.video("https://www.youtube.com/watch?v=VECJJIEYTXw")
            with st.beta_expander("Watch the following video to know about Indian physical features...",
                                  expanded=False):
                st.video("https://www.youtube.com/watch?v=gI9tibkul9A")

        if subject == 'Science':
            with st.beta_expander("Watch the following video to know about general physics...",
                                  expanded=False):
                st.video("https://www.youtube.com/watch?v=Hu-JL2J6ncE")
            with st.beta_expander("Watch the following video to know about general chemistry...",
                                  expanded=False):
                st.video("https://www.youtube.com/watch?v=L2Q2q20KaEk")
            with st.beta_expander("Watch the following video to know about general biology...",
                                  expanded=False):
                st.video("https://www.youtube.com/watch?v=xtbQH5PMWVE")

        if subject == 'Others':
            with st.beta_expander("Watch the following video to know about python programming language...",
                                  expanded=False):
                st.video("https://www.youtube.com/watch?v=_uQrJ0TkZlc")
            with st.beta_expander("Watch the following video to know about basic tricks in maths...",
                                  expanded=False):
                st.video("https://www.youtube.com/watch?v=yrMLtHTXHI0")
            with st.beta_expander("Watch the following video to learn doodling...",
                                  expanded=False):
                st.video("https://www.youtube.com/watch?v=2-OrSA6kaLM")
        st.header("Need Study material look here")
        with st.beta_expander("Heed Study Material Look here", expanded=False):
            st.write("check out this [National E-library by NCERT ](https://ndl.iitkgp.ac.in/)")
