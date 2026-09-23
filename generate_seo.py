import json
import os
import google.generativeai as genai

# Lấy API Key từ bảo mật GitHub Secrets
api_key = os.environ.get("GEMINI_API_KEY")
genai.configure(api_key=api_key)


def generate_seo_metadata(keyword):
  print(f"🔍 Đang yêu cầu AI tối ưu SEO cho từ khóa: '{keyword}'...")
  model = genai.GenerativeModel("gemini-1.5-flash")

  prompt = f"""
    Đóng vai trò chuyên gia YouTube SEO hàng đầu. 
    Dựa trên từ khóa cốt lõi: '{keyword}', hãy viết các thông tin sau để video dễ lên top tìm kiếm:
    
    [TITLE] (Tiêu đề hấp dẫn, dưới 60 ký tự, chứa từ khóa chính)
    [DESCRIPTION] (Mô tả chi tiết 3-4 dòng thu hút, chèn từ khóa tự nhiên và 3 hashtag ở cuối)
    [TAGS] (Liệt kê 8-10 thẻ tag liên quan, cách nhau bằng dấu phẩy)
    
    Chỉ trả về đúng định dạng trên, không giải thích gì thêm.
    """

  response = model.generate_content(prompt)
  text = response.text

  try:
    title = text.split("[TITLE]")[1].split("[DESCRIPTION]")[0].strip()
    description = text.split("[DESCRIPTION]")[1].split("[TAGS]")[0].strip()
    tags_raw = text.split("[TAGS]")[1].strip()
    tags = [t.strip() for t in tags_raw.split(",")]
  except Exception:
    title = f"Bí quyết về {keyword} hiệu quả nhất"
    description = f"Chia sẻ kiến thức chi tiết về {keyword}. #shorts"
    tags = [keyword, f"cách {keyword}", "hướng dẫn"]

  metadata = {"title": title, "description": description, "tags": tags}

  print("\n✅ ĐÃ TẠO XONG THÔNG TIN SEO:")
  print(f"📌 Tiêu đề: {title}")
  print(f"📝 Mô tả: {description}")
  print(f"🏷️ Thẻ Tag: {tags}")


if __name__ == "__main__":
  user_keyword = "cách làm video youtube automation"
  generate_seo_metadata(user_keyword)
