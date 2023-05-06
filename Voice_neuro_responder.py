import time
from googletrans import Translator
from Voice_Commands import stream, rec, speak, speak_tts
from colorama import init, Fore, Style
from loader import download_generator
from vocabulary import queries_generating_facts


from pygpt4all import GPT4All

model = GPT4All('./models/ggml-gpt4all-l13b-snoozy.bin')

"""
from pygpt4all import GPT4All_J

model = GPT4All_J('./models/ggml-gpt4all-j-v1.3-groovy.bin')
"""
model_name = "ggml-gpt4all-l13b-snoozy.bin"

LRE = Fore.LIGHTRED_EX
YEL = Fore.YELLOW
LYE = Fore.LIGHTYELLOW_EX
BLU = Fore.BLUE
LBL = Fore.LIGHTBLUE_EX
CYA = Fore.CYAN
LCY = Fore.LIGHTCYAN_EX
GRE = Fore.GREEN
LGR = Fore.LIGHTGREEN_EX
MAG = Fore.MAGENTA
LMA = Fore.LIGHTMAGENTA_EX
WHI = Fore.WHITE
SRA = Style.RESET_ALL
init(convert=True)


def generate_response(user_input_gener):
    response_gener = model.generate(user_input_gener)
    responses = ""
    for token in response_gener:
        print(f"{token}", end='', flush=True)
    for r in response_gener:
        responses += r
    return responses


if __name__ == '__main__':
    translatorrr = Translator()
    speak.Rate = 4
    while True:
        download_generator()
        full_sentence = ""
        while True:
            if rec.AcceptWaveform(stream.read(4000)):
                try:
                    prompt = rec.Result()[13:-2]
                    words = prompt[1:-1].split()
                    part_prompt = prompt[1:-1]
                    full_sentence += part_prompt + " "
                    # print(full_sentence)
                    if prompt in ('"поговорим"', '"переводчик"', '"закройся"', '"с свали"', '"свали"'):
                        exit()
                    elif prompt != '""':  # !
                        print(f' {LYE}{part_prompt}{SRA} ', end='')

                        if len(words) > 0 and \
                                any(word in prompt[1:-1]
                                    for word in ('ответ', 'ответь', 'отвечай', 'хватит', 'переведи', 'переводи',
                                                 'перевод', 'давай', 'вопрос', 'ладно', 'слышала', 'слышал', 'понял',
                                                 'поняла', 'дальше', 'стоп', 'запрос', 'продолжай', 'продолжи',
                                                 'согласен', 'согласись', 'запрос')):
                            # full_sentence = full_sentence.rsplit(words[-1], 1)[0]  # Удалите последнее слово
                            print(f'{LGR} >>>{WHI}')
                            # trans = translator.translate(vocabulary.random_response_aphorism(), dest="en")
                            trans = translatorrr.translate(str(full_sentence), dest="en")  # print(full_sentence)
                            print(" " + YEL + trans.text + GRE)
                            #  user_input = ': come up with funny aphorisms! '  # дополнительная фраза
                            #  print(" " + GRE + user_input + SRA)
                            response = generate_response(trans.text)  # (trans.text + user_input)
                            gpt = translatorrr.translate(str(response), dest="ru")
                            responegpt = gpt.text
                            print(LCY + model_name + " : \n " + LGR + responegpt)
                            speak_tts(gpt.text)
                            time.sleep(2.5)
                            speak_tts("согласен!")
                            time.sleep(.5)
                            break
                        if prompt in ('"факты"', '"факт"'):
                            random_fact = str(queries_generating_facts())
                            print(YEL + f" > {random_fact} > " + SRA)
                            response = generate_response(random_fact)
                            gpt = translatorrr.translate(str(response), dest="ru")
                            responegpt = gpt.text
                            print(LCY + model_name + " : \n " + LGR + responegpt)
                            speak_tts(gpt.text)
                            time.sleep(2.5)
                            speak_tts("согласен!")
                            time.sleep(.5)
                            break

                    if prompt in ('"заново"', '"снова"', '"сначала"', '"сброс"', '"сбросить"'):
                        print(f' {LRE}X{SRA}\n', end='')
                        break
                except Exception as e:
                    print(full_sentence)
                    print(f"{LRE} переводчик :{SRA}", e)
