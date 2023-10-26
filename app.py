import streamlit as st

def main():
    # URL of the image
    image_url = "https://pbs.twimg.com/profile_images/1716188114652168192/pBfDyMkG_400x400.jpg"

    # Display the image centered using Markdown and HTML
    st.markdown(f'<div style="display: flex; justify-content: center;"><img src="{image_url}" alt="Image" style="width: 400px; height: 400px;"></div>', unsafe_allow_html=True)
    # Add CSS animation for changing font color
    st.markdown('''
    <style>
        @keyframes changeColor {
             0% { color: #0072b1; }
            20% { color: #1E90FF; } /* DodgerBlue */
            40% { color: #9932CC; } /* DarkOrchid */
            60% { color: #8A2BE2; } /* BlueViolet */
            80% { color: #4B0082; } /* Indigo */
            100% { color: #2E8B57; } /* SeaGreen */
        }
        .changing-color {
            animation: changeColor 30s linear infinite;
            font-size: 48px;
            font-family: Arial, sans-serif;
            text-align: center;
        }
        @import url('https://fonts.googleapis.com/css2?family=Cutive+Mono&display=swap');
        .changing-color {
            font-family: 'Cutive Mono', monospace;
            font-size: 16px;
            color: #0072b1;
            text-align: center;
        }
    </style>
    <div class="changing-color">research and quantitative solutions for defi on solana</div>
''', unsafe_allow_html=True)
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url("https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExNGwzdWloa2o0d2hiaTVlNm1laWVmcGN6NnBwcHJpcjd2YzIwNmE4cyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/hWKAL74roavpBb75t3/giphy.gif");
            # background-size: cover
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


if __name__ == '__main__':
    main()