import streamlit as st
import base64

# Load logo image and return a base64 string because it didn't work out to load an image as png or jpg
def load_logo_image(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    return encoded_string

# Handling bot response
get_response = lambda user_input: (
    """Welcome to TuwaiqBot! \n
    Please select from the list below what you would like to know?""" 
    if user_input.lower() == "hi" 
    else "I'm sorry, I only respond to specific words'."
)

# Initialize session state variables
if 'selected_option' not in st.session_state:
    st.session_state['selected_option'] = None

if 'selected_bootcamp' not in st.session_state:
    st.session_state['selected_bootcamp'] = None

if 'selected_program' not in st.session_state:
    st.session_state['selected_program'] = None

if 'conversation' not in st.session_state:
    st.session_state['conversation'] = []

if 'logo_image' not in st.session_state:
    st.session_state['logo_image'] = load_logo_image("logo.jpg")

if 'current_state' not in st.session_state:
    st.session_state['current_state'] = 'initial'

# Title
st.title("👾TuwaiqBot")
st.markdown("""**Tuwaiq Academy** is the first academy in the Kingdom of Saudi Arabia to offer 
educational programs in advanced technologies, with a wide range of courses for different age groups 
and technical fields. It was founded in August 2019. """)
st.markdown("---")

# Conversation history
for message in st.session_state['conversation']:
    if message["role"] == "user":
        st.markdown(f"""
        <div style='display: flex; align-items: center; justify-content: flex-end; margin-bottom: 10px;'>
            <div style='margin-right: 10px; padding: 10px; background-color: #f2f2f2; border-radius: 10px;'>
                {message['content']}
            </div>
            <div style='width: 40px; height: 40px; border-radius: 50%; background-color: #DBC6F8 ; display: flex; align-items: center; justify-content: center;'>
                👩🏻‍💻
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div style='display: flex; align-items: center; margin-bottom: 10px;'>
            <div style='width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center;'>
                <img src="data:image/jpg;base64,{st.session_state['logo_image']}" width="30" height="30">
            </div>
            <div style='margin-left: 10px; padding: 10px; background-color: #EFECF4; border-radius: 10px;'>
                {message['content']}
            </div>
        </div>
        """, unsafe_allow_html=True)

# Predefined responses
if st.session_state["current_state"] == "initial":
    if st.button("Hi👋"):
        user_input = "hi"
        st.session_state['conversation'].append({
            "role": "user",
            "content": user_input
        })
        response = get_response(user_input)
        st.session_state['conversation'].append({"role": "bot", "content": response})
        st.session_state["current_state"] = "greeted"
        st.experimental_rerun()

if st.session_state["current_state"] == "greeted" and st.session_state['selected_option'] is None:

    if st.button("📋Bootcamps"):
        st.session_state['conversation'].append({
            "role": "user",
            "content": "Bootcamps📋"
        })
        st.session_state['selected_option'] = "📋Bootcamps"
        st.experimental_rerun()

    if st.button("⚙️Programs"):
        st.session_state['conversation'].append({
            "role": "user",
            "content": "Programs⚙️"
        })
        st.session_state['selected_option'] = "⚙️Programs"
        st.experimental_rerun()

    if st.button("🤝🏼Events"):
        st.session_state['conversation'].append({
            "role": "user",
            "content": "Events🤝🏼"
        })
        st.session_state['selected_option'] = "🤝🏼Events"
        st.experimental_rerun()

    if st.button("🧐Ask us!"):
        st.session_state['conversation'].append({
            "role": "user",
            "content": "Ask us!🧐"
        })
        st.session_state['selected_option'] = "🧐Ask us!"
        st.experimental_rerun()

    if st.button("✌️Join us as a Trainee!"):
        st.session_state['conversation'].append({
            "role": "user",
            "content": "Join us as a Trainee!✌️"
        })
        st.session_state['selected_option'] = "✌️Join us as a Trainee!"
        st.experimental_rerun()

    if st.button("🦾Team"):
        st.session_state['conversation'].append({
            "role": "user",
            "content": "Team🦾"
        })
        st.session_state['selected_option'] = "🦾Team"
        st.experimental_rerun()

if st.session_state['selected_option']:
    selected_option = st.session_state['selected_option']
    st.markdown(f"### {selected_option}")

    # Display bootcamp details
    if selected_option == "📋Bootcamps":
        bootcamps = [
            {'name': 'Game development using Unreal Engine', 'location': 'Online', 'duration': "8 Weeks", 'start_at': '11-08-2024', 'end_at': '03-10-2024', 'time': '5:30 P.M - 9:30 P.M'},
            {'name': 'Developing Web Solutions on AWS', 'location': 'Onsite', 'duration': "4 Weeks", 'start_at': '18-08-2024', 'end_at': '12-09-2024', 'time': '4 P.M - 10 P.M'},
            {'name': 'Building Websites and Applications Using JavaScript', 'location': 'Onsite', 'duration': "10 Weeks", 'start_at': '25-08-2024', 'end_at': '31-10-2024', 'time': '10 A.M - 3 P.M'},
            {'name': 'Building and developing AI models', 'location': 'Onsite', 'duration': "8 Weeks", 'start_at': '01-09-2024', 'end_at': '24-10-2024', 'time': '4 P.M - 9 P.M'},
            {'name': 'Advanced AWS Cloud Solutions Engineering', 'location': 'Onsite', 'duration': "4 Weeks", 'start_at': '06-10-2024', 'end_at': '31-10-2024', 'time': '4 P.M - 10 P.M'},
            {'name': 'AWS Cloud Computing Operations Management', 'location': 'Onsite', 'duration': "4 Weeks", 'start_at': '03-11-2024', 'end_at': '28-11-2024', 'time': '4 P.M - 10 P.M'},
            {'name': 'Web development using Java', 'location': 'Onsite', 'duration': "12 Weeks", 'start_at': '13-10-2024', 'end_at': '02-01-2025', 'time': '10 A.M - 3 P.M'}
        ]

        def display_bootcamp_details(bootcamp):
            st.write(f"**Bootcamp Name:** {bootcamp['name']}")
            st.write(f"**Location:** {bootcamp['location']}")
            st.write(f"**Duration:** {bootcamp['duration']}")
            st.write(f"**Start at:** {bootcamp['start_at']}")
            st.write(f"**End at:** {bootcamp['end_at']}")
            st.write(f"**Time:** {bootcamp['time']}")

        for bootcamp in bootcamps:
            with st.expander(bootcamp['name']):
                display_bootcamp_details(bootcamp)

    # Display program details
    if selected_option == "⚙️Programs":
        programs = [
            {'name': 'Cloud+الأنظمة السحابية', 'location': 'Riyadh', 'duration': '2 weeks', 'start_at': '04-08-2024', 'end_at': '15-08-2024', 'time': '06:30 P.M to 10:30 P.M', 'more_info': 'https://tuwaiq.edu.sa/bootcamp/wYd8Ddq4/view'},
            {'name': 'ITIL ممارسات إدارة الخدمات التقنية', 'location': 'Riyadh', 'duration': 'One week', 'start_at': '11-08-2024', 'end_at': '15-08-2024', 'time': '06:00 P.M to 09:00 P.M', 'more_info': 'https://tuwaiq.edu.sa/bootcamp/LBmBp6V4/view'},
            {'name': 'أساسيات الدوائر الإلكترونية', 'location': 'Riyadh', 'duration': 'One week', 'start_at': '18-08-2024', 'end_at': '22-08-2024', 'time': '05:00 P.M to 08:00 P.M', 'more_info': 'https://tuwaiq.edu.sa/bootcamp/J3MNmGkw/view'},
            {'name': 'مايكروسوفت SQL Server', 'location': 'Riyadh', 'duration': '2 weeks', 'start_at': '18-08-2024', 'end_at': '29-08-2024', 'time': '05:30 P.M to 09:30 P.M', 'more_info': 'https://tuwaiq.edu.sa/bootcamp/JYLkMAw9/view'},
            {'name': 'مهارات تقنية المعلومات', 'location': 'Riyadh', 'duration': 'One week', 'start_at': '18-08-2024', 'end_at': '22-08-2024', 'time': '06:00 P.M to 09:00 P.M', 'more_info': 'https://tuwaiq.edu.sa/bootcamp/QJWXYV7q/view'},
            {'name': 'إتقان حوكمة ومخاطر والتزام الأمن السيبراني', 'location': 'Riyadh', 'duration': '2 weeks', 'start_at': '18-08-2024', 'end_at': '29-08-2024', 'time': '07:00 P.M to 10:00 P.M', 'more_info': 'https://tuwaiq.edu.sa/bootcamp/7pY4Vdb9/view'}
        ]

        def display_program_details(program):
            st.write(f"**Program Name:** {program['name']}")
            st.write(f"**Location:** {program['location']}")
            st.write(f"**Duration:** {program['duration']}")
            st.write(f"**Start at:** {program['start_at']}")
            st.write(f"**End at:** {program['end_at']}")
            st.write(f"**Time:** {program['time']}")
            st.markdown(f"[More Info]({program['more_info']})")

        for program in programs:
            with st.expander(program['name']):
                display_program_details(program)

    # Display events details
    elif selected_option == "🤝🏼Events":
        def meetings():

            return {
            "Site Reliability Engineering (SRE) Roles and Responsibilities": 
                ["2024-08-01", "07:30 PM", "Riyadh", "https://tuwaiq.edu.sa/bootcamp/yBQvgAMv/view"],
            "How to start a successful career journey?": 
                ["2024-08-06", "07:30 PM", "Riyadh", "https://tuwaiq.edu.sa/bootcamp/J4Q4j6rq/view"],
            "Twelve-factor App Project Management": 
                ["2024-08-03", "07:30 PM", "Riyadh", "https://tuwaiq.edu.sa/bootcamp/a9Qp66rZ/view"],
            "The role of business analysis in decision support systems": 
                ["2024-08-04", "07:30 PM", "Riyadh", "https://tuwaiq.edu.sa/bootcamp/GnALMer8/view"],
            "Performance digital marketing concept": 
                ["2024-08-05", "07:30 PM", "Riyadh", "https://tuwaiq.edu.sa/bootcamp/3Rr1OKQ8/view"],
            "The importance of infrastructure to enhance cybersecurity": 
                ["2024-08-06", "07:30 PM",  "Riyadh", "https://tuwaiq.edu.sa/bootcamp/892YPZr3/view"],
        }

        meetings = meetings()

        meeting_names = list(meetings.keys())
        selected_meeting = st.selectbox("Select an event:", meeting_names)

        if selected_meeting:
            meeting_info = meetings[selected_meeting]
            st.write(f"**Date:** {meeting_info[0]}")
            st.write(f"**Time:** {meeting_info[1]}")
            st.write(f"**Location:** {meeting_info[2]}")
            enroll_link = meeting_info[3]
            st.markdown(f'<a href="{enroll_link}" target="_blank"><button style="background-color: #8564B3; color: white; padding: 8px 18px; border: none; border-radius: 5px; cursor: pointer;">Enroll</button></a>', unsafe_allow_html=True)
   
    # Display ask us details
    elif selected_option == "🧐Ask us!":
        st.write("----")

        contact_form = """
        <p>Let's get in touch🤝🏻</p>
       <form action="https://formsubmit.co/your@email.com" method="POST" style="background-color: #f2f2f2; padding: 20px; border-radius: 10px; max-width: 500px; margin: auto;">
        <input type="hidden" name="_captcha" value="false"> 
        <input type="text" name="name" placeholder="Your name" required style="width: 100%; padding: 10px; margin: 10px 0; border: 1px solid #ccc; border-radius: 5px;"> <br>
        <input type="email" name="email" placeholder="Your email" required style="width: 100%; padding: 10px; margin: 10px 0; border: 1px solid #ccc; border-radius: 5px;"> <br>
        <textarea name="message" placeholder="Your message here" required style="width: 100%; padding: 10px; margin: 10px 0; border: 1px solid #ccc; border-radius: 5px;"></textarea> <br>
        <button type="submit" style="background-color: #8564B3; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer; margin-left: 120px;">Send</button> <br>
        </form> <br>

        """

        left_c, right_c = st.columns(2)
        with left_c:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_c:
            st.empty()
    
    # Display join us details
    elif selected_option == "✌️Join us as a Trainee!":
        st.markdown("Kindly fill out the [form](https://forms.gle/6YJv5YnTmRqWqJn37) and become a part of our incredible trainees!")
    
    # Display team details
    elif selected_option == "🦾Team":
        raghad_number = 966569566905
        hatoon_number = 966550275960
        musaab_number = 966500283891
        hamad_number = 966550894355
        st.markdown(f"- [Raghad Almalki](https://www.linkedin.com/in/raghad-almalki-aa0aa71b2/) - {raghad_number}")
        st.markdown(f"- [Musab Alsobhi](https://www.linkedin.com/in/musabalsobhi/) - {musaab_number} ")
        st.markdown(f"- [Hatoon Aloqaily-](https://www.linkedin.com/in/hatoon-al-oqaily-73b808253/) - {hatoon_number}")
        st.markdown(f"- [Hamad Altamimi-]() - {hamad_number}")

    if st.button("🔙"):
        st.session_state['selected_option'] = None
        st.experimental_rerun()
