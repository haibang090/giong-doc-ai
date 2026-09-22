import streamlit as st
import edge_tts
import asyncio
import os

st.title("🎙️ Trình Tạo Giọng Đọc AI Tiếng Việt")

script = st.text_area("Nhập hoặc dán kịch bản của bạn vào đây:", height=150)
voice_style = st.selectbox(
    "Chọn chất giọng:",
    [
        "Nam Trung Niên (Trầm ấm, chững chạc)",
        "Nam Trẻ (Năng động, giọng sáng)",
        "Nữ Trung Niên (Điềm đạm, ấm áp)",
        "Nữ Trẻ (Tươi trẻ, truyền cảm)"
    ]
)

VOICE_CONFIGS = {
    "Nam Trung Niên (Trầm ấm, chững chạc)": {"voice": "vi-VN-NamMinhNeural", "pitch": "-1st", "rate": "+0%"},
    "Nam Trẻ (Năng động, giọng sáng)": {"voice": "vi-VN-NamMinhNeural", "pitch": "+3st", "rate": "+5%"},
    "Nữ Trung Niên (Điềm đạm, ấm áp)": {"voice": "vi-VN-HoaiMyNeural", "pitch": "+0st", "rate": "+0%"},
    "Nữ Trẻ (Tươi trẻ, truyền cảm)": {"voice": "vi-VN-HoaiMyNeural", "pitch": "+4st", "rate": "+5%"}
}

if st.button("Tạo Giọng Đọc & Tải Về", type="primary"):
    if not script.strip():
        st.warning("Vui lòng nhập nội dung kịch bản!")
    else:
        with st.spinner("Đang xử lý phân tách kịch bản và tạo file MP3..."):
            config = VOICE_CONFIGS[voice_style]
            voice = config["voice"]
            pitch = config["pitch"]
            rate = config["rate"]

            processed = (script.replace(".", ". <break time='400ms'/>")
                               .replace(",", ", <break time='250ms'/>")
                               .replace(";", "; <break time='300ms'/>")
                               .replace("?", "? <break time='500ms'/>")
                               .replace("!", "! <break time='500ms'/>"))

            ssml = f"""
            <speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="vi-VN">
                <voice name="{voice}">
                    <prosody rate="{rate}" pitch="{pitch}">
                        {processed}
                    </prosody>
                </voice>
            </speak>
            """
            
            output_path = "giong_doc_ai.mp3"
            asyncio.run(edge_tts.Communicate(ssml, voice).save(output_path))
            
            st.success("Tạo giọng đọc thành công!")
            st.audio(output_path, format="audio/mp3")
            
            with open(output_path, "rb") as f:
                st.download_button("Tải file MP3 về máy", f, file_name="giong_doc_ai.mp3", mime="audio/mpeg")
