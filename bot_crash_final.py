import time
import schedule
import random
import telegram
from datetime import datetime

# === Configurações do Telegram ===
TOKEN = 'SEU_TOKEN_AQUI'
CHAT_ID = 'SEU_CHAT_ID_AQUI'
bot = telegram.Bot(token=TOKEN)

# === Variáveis de histórico ===
sinais_enviados = []
historico_resultados = []

# === Estratégia simplificada (simulação) ===
def detectar_padrao():
    chance = random.random()
    if chance > 0.8 and chance <= 0.95:
        bot.send_message(chat_id=CHAT_ID, text="🚨 ALFA_BOT PREMIUM: Um padrão está prestes a se formar! Fique atento na próxima rodada.")
    elif chance > 0.95:
        alvo = random.choice([2, 3, 4])
        sucesso = random.choice([True, False])
        sinais_enviados.append((datetime.now().strftime("%H:%M"), alvo, sucesso))
        historico_resultados.append(sucesso)
        resultado_texto = "✅ Sucesso" if sucesso else "❌ Erro"
        msg = f"🔥 ALFA_BOT PREMIUM: Entrada sugerida ➤ Crash acima de {}x\n🎯 Resultado: {}".format(alvo, resultado_texto)
        bot.send_message(chat_id=CHAT_ID, text=msg)

# === Envio de histórico a cada 1 hora ===
def enviar_historico():
    acertos = historico_resultados.count(True)
    erros = historico_resultados.count(False)
    resumo = f"📊 Histórico da última hora (ALFA_BOT PREMIUM):\n✅ Acertos: {acertos}\n❌ Erros: {erros}\n⏱️ Total de sinais: {len(historico_resultados)}"
    bot.send_message(chat_id=CHAT_ID, text=resumo)
    historico_resultados.clear()

# Agendamentos
schedule.every(5).minutes.do(detectar_padrao)
schedule.every().hour.at(":00").do(enviar_historico)

# Loop principal
while True:
    schedule.run_pending()
    time.sleep(1)
