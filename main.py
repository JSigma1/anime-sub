import streamlit as st

# --- App Configuration ---
st.set_page_config(
    page_title="How to Watch Anime with Japanese Subtitles",
    layout="wide",
)

# --- Title and Introduction ---
st.title("How to Watch Anime with Japanese Subtitles")
st.markdown("""
This guide provides the essential steps to set up your environment for watching anime with Japanese subtitles.
""")

# --- Step 1: Get asbplayer ---
st.header("1. Get asbplayer Extension")
st.write("You'll need **asbplayer**, a browser extension for syncing subtitles. It's available for Chromium-based browsers (Chrome, Edge, Brave) and Firefox.")
st.link_button("Download asbplayer Here", "https://github.com/killergerbah/asbplayer/releases")
st.info("Download the correct version for your browser (e.g., .crx for Chromium, .xpi for Firefox) and install it.")
st.markdown("---")

# --- Step 2: Find Subtitles ---
st.header("2. Find Your Japanese Anime Subtitles")
st.write("You'll need Japanese subtitle files (.ass or .srt).")
st.markdown("A widely used resource for Japanese subtitles is [Kitsunekko](https://kitsunekko.net/dirlist.php?dir=subtitles%2Fjapanese%2F).")
st.write("On Kitsunekko, use **Ctrl + F** (or **Cmd + F** on Mac) to search for your anime by name and download the subtitle file.")
st.markdown("---")

# --- Step 3: Choose Streaming Site ---
st.header("3. Choose Your Anime Streaming Site")
st.write("You'll need a platform to stream your anime.")
st.link_button("Recommended: Hianime (Free Streaming)", "https://hianime.to/")
st.write("asbplayer is compatible with most web-based streaming sites.")
st.markdown("---")

# --- Step 4: Start Watching! ---
st.header("4. Set Up asbplayer and Start Watching!")
st.write("Follow these steps to integrate asbplayer with your streaming:")

st.markdown("""
1.  **Open asbplayer Interface:**
    Go to [https://killergerbah.github.io/asbplayer/](https://killergerbah.github.io/asbplayer/) in a new tab.

2.  **Upload Subtitle File:**
    On the asbplayer page, upload your downloaded Japanese subtitle file (.ass or .srt).

3.  **Start Anime Playback:**
    Go to your chosen streaming site (e.g., Hianime) and begin playing your anime.

4.  **Connect asbplayer:**
    While the anime plays, press **Ctrl + Shift + F** (Windows/Linux) or **Cmd + Shift + F** (Mac).
    *(Ensure the asbplayer extension is active).*

5.  **Select Subtitle Track:**
    When the asbplayer pop-up appears, select 'Subtitle Track 1' to load your subtitles.
""")

st.success("You should now have Japanese subtitles synced with your anime. Enjoy!")
st.write("For troubleshooting, refer to the asbplayer GitHub page.")