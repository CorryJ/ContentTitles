from openai import OpenAI
import streamlit as st
import time


# Setting page title and header
st.set_page_config(page_title="The SEO Works Content Titles Generator", 
                   page_icon="https://www.seoworks.co.uk/wp-content/themes/seoworks/assets/images/fav.png", 
                   layout="wide",initial_sidebar_state="collapsed")

#Defines custom css file
with open( "resources/style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)
file_name="resources/style.css"

# custom styling to remove red bar at top
st.markdown("""
<style>
	[data-testid="stDecoration"] {
		display: none;
	}
</style>                
            """, unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
   st.header("")
   
with col2:
   st.header("")
   st.image("resources/SeoWorksLogo-Dark.png")

with col3:
   st.header("")


st.markdown('<div style="text-align: center; font-size:36px;"><strong>Content Titles Generator by The SEO Works<strong></div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: center; font-size:22px;"></div>', unsafe_allow_html=True)

# Spacers for layout purposes
st.write("#")
# st.header("PersonaPlotter by The SEO Works")
# st.markdown("***PersonaPlotter reveals audience personas with targeted keywords and their most pressing questions.***")

st.markdown(
        """
        <style>
        .stMarkdownContainer p {
            font-size: 20px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


with st.expander("How it works"):
    st.write("Introducing The SEO Works Blog Title Generator. Select your parameters below and click go!")


col1, col2 = st.columns(2)

with col1:
   topic = st.text_input("Enter your topic", placeholder="Add your topic and press enter")
  

with col2:
   no_of_titles_to_generate = st.text_input("Add number of titles to generate", placeholder="Add number of titles to generate")


col1, col2 = st.columns(2)

with col1:
   style  = st.selectbox(
    'Writing style',
    (['Default', 'Academic', 'Analytical', 'Argumentative', 'Conversational', 'Creative', 'Critical', 'Descriptive', 'Epigrammatic', 'Epistolary', 
                 'Expository', 'Informative', 'Instructive', 'Journalistic', 'Metaphorical', 'Narrative', 'Persuasive', 'Poetic', 'Satirical', 'Technical']))
   

with col2:
   tone  = st.selectbox(
    'Writing tone',
    (['Default', 'Authoritative', 'Caring', 'Casual', 'Cheerful', 'Coarse', 'Conservative', 'Conversational', 'Creative', 'Dry', 'Edgy', 
'Enthusiastic', 'Expository', 'Formal', 'Frank', 'Friendly', 'Fun', 'Funny', 'Humorous', 'Informative', 'Irreverent', 'Journalistic', 'Matter of fact', 
'Nostalgic', 'Objective', 'Passionate', 'Poetic', 'Playful', 'Professional', 'Provocative', 'Quirky', 'Respectful', 'Romantic', 'Sarcastic', 'Serious', 
'Smart', 'Snarky', 'Subjective', 'Sympathetic', 'Trendy', 'Trustworthy', 'Unapologetic', 'Upbeat', 'Witty']))


client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"]) 

#  client = OpenAI(api_key=api_key) 

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []
        
#if topic := topic:
prompt = "Please ignore all previous instructions. You are an \
expert copywriter who writes catchy titles for articles. You have a " + tone +  " tone of voice. You have a " + style + " writing style. \
Write " + no_of_titles_to_generate +" catchy article titles with a hook for the topic " + "'" + topic + "'" +". The titles should be in the english language with UK grammar. Do not self reference. \
Do not explain what you are doing."
    
with st.form("Response_form", border=False, clear_on_submit=True):
    st.session_state.messages.append({"role": "user", "content": prompt})
    #with st.chat_message("user"):
    #    st.markdown("Here are the title ideas for your content")

    submitted = st.form_submit_button("Get your content titles!")
    if submitted:
            st.session_state.messages.append({"role": "user", "content": prompt})

            with st.chat_message("assistant", avatar="https://www.seoworks.co.uk/wp-content/themes/seoworks/assets/images/fav.png"):
                    st.markdown("***Here are the title ideas for your content...***")
                    stream = client.chat.completions.create(
                        model=st.session_state["openai_model"],
                        messages=[
                            {"role": m["role"], "content": m["content"]}
                            for m in st.session_state.messages
                        ],
                        stream=True,
                    )
        

            response = st.write_stream(stream)

            st.session_state.messages.append({"role": "assistant", "content": response})

st.divider()
# Spacers for layout purposes
st.write("#")

st.markdown('<div style="text-align: center; font-size:30px;"><strong>About The SEO Works<strong></div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: center; font-size:22px;">We are the Digital Growth Experts. As an award-winning provider of digital \
            marketing and websites to leading brands, we have worked for more than a decade with one key goal in mind - to get businesses more \
            customers online. Find out more <a href ="https://www.seoworks.co.uk/" target="_blank" > about us</a>.</div>', unsafe_allow_html=True)

st.write("#")

st.markdown('<div style="text-align: center; font-size:14px;">Check out our other <a href = "https://www.seoworks.co.uk/resources/downloads/">resources</a>.</div>', unsafe_allow_html=True)

