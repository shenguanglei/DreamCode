import pyttsx3
import os
import time

def text_to_audio(text, output_file, language="zh"):
    try:
        # 初始化 TTS 引擎
        engine = pyttsx3.init()

        # 配置语音属性
        engine.setProperty('rate', 150)  # 设置语速
        engine.setProperty('volume', 0.9)  # 设置音量（0.0 到 1.0）

        # 获取可用的语音列表并选择对应语言的语音
        voices = engine.getProperty('voices')
        for voice in voices:
            if language == "zh" and 'zh' in voice.id:  # 选择中文语音
                engine.setProperty('voice', voice.id)
                break
            elif language == "en" and 'en' in voice.id:  # 选择英文语音
                engine.setProperty('voice', voice.id)
                break

        # 确保目录存在
        os.makedirs(os.path.dirname(output_file), exist_ok=True)

        # 保存音频到文件
        engine.save_to_file(text, output_file)
        engine.runAndWait()
        print(f"音频已成功保存为 {output_file}")
    except Exception as e:
        print(f"生成音频时出现错误: {e}")


if __name__ == "__main__":
    # 用户输入示例文本
    text = input("请输入要转换为语音的文本：").strip()
    if not text:
        print("输入文本为空，使用默认文本。")
        text = "你好，这是 pyttsx3 生成的语音！"

    # 使用时间戳生成随机文件名
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    output_file = rf"D:\MP3\output_audio_{timestamp}.mp3"  # 指定保存路径

    # 用户选择语言（中文或英文）
    language = input("请输入语言（zh 表示中文，en 表示英文）：").strip().lower()
    if language not in ["zh", "en"]:
        print("无效的语言选择，默认为中文。")
        language = "zh"

    # 调用函数生成 MP3 文件
    text_to_audio(text, output_file, language)