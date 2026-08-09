import speech_recognition as sr

reconhecedor = sr.Recognizer()

with sr.Microphone() as microfone:
    print("BILLY está ouvindo...")
    audio = reconhecedor.listen(microfone)

try:
    texto = reconhecedor.recognize_google(audio, language="pt-BR")
    print("Você disse:", texto)

except sr.UnknownValueError:
    print("BILLY não conseguiu entender.")

except sr.RequestError:
    print("Erro ao acessar o serviço de reconhecimento de voz.")