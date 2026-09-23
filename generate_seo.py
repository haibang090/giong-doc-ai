import os
from google import genai

# Lấy khóa API bảo mật từ GitHub Secrets
api_key = os.environ.get("GEMINI_API_KEY")

# Khởi tạo client theo chuẩn thư viện google-genai mới nhất
client = genai.Client(api_key=api_key)

# Chủ đề hoặc yêu cầu tạo SEO cho video của bạn
prompt = "Hãy đóng vai trò chuyên gia YouTube SEO, hãy tạo cho tôi: 1. Tiêu đề hấp dẫn chuẩn SEO, 2. Phần mô tả chi tiết có chứa từ khóa, 3. Các thẻ tags phù hợp cho video chủ đề hướng dẫn."

# Gọi mô hình Gemini xử lý
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt,
)

# In kết quả trực tiếp ra phần nhật ký (logs) của GitHub Actions
print("--- KẾT QUẢ SEO YOUTUBE ---")
print(response.text)
