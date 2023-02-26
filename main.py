# Это - первая версия бота-переводчика (онлайн-словаря)
# для языков КМНС Сибири. Делал в 2021г t.me/@rokuntew
# Данный бот позволяет выдавать парные переводы из установленного
# словаря, работает на бибилиотеке py-telebot

# Установка бибилиотек на Debian:
# sudo apt-get install python python-pip
# pip install pytelegrambotapi

import time
import datetime
import os
import telebot
from telebot import types

try:
    try:
        print('###')
        bot = telebot.TeleBot('') # токен бота

        test_st = False # Перекючение источника словарей

        if test_st == True:
            a_s_ru = "//wlsel.txt"
            a_k_ru = "//wlkam.txt"
            a_h_ru = "//wlhant.txt"
            a_m_ru = "//wlmans.txt"
            a_kb_ru = '//wlkoj.txt'
            a_mt_ru = '//wlmat.txt'
            a_tz_ru = '//wltaz.txt'
            a_kt_ru = "//wlket.txt"
            a_im_ru = "//wlitm.txt"
            a_lg1_ru = ""
            a_s_en = '/wlselen.txt'
            a_k_en = '/wlkamen.txt'
            a_h_en = ''
            a_m_en = ''
            a_kb_en = ''
            a_mt_en = ''
            a_kt_en = ''
            a_im_en = ''
            a_lg1_en = ''
            a_s_fi = '/wlselfi.txt'
            a_k_fi = ''
            a_h_fi = ''
            a_m_fi = ''
            a_kb_fi = ''
            a_mt_fi = ''
            a_kt_fi = ''
            a_im_fi = ''
            a_lg1_fi = ''


        else:
            a_s_ru = "/wlsel.txt"
            a_k_ru = "/wlkam.txt"
            a_h_ru = "/wlhant.txt"
            a_m_ru = "/wlmans.txt"
            a_kb_ru = '/wlkoj.txt'
            a_mt_ru = '/wlmat.txt'
            a_tz_ru = '/wltaz.txt'
            a_kt_ru = "/wlket.txt"
            a_im_ru =  "/wlitm.txt"
            a_lg1_ru = ''
            a_s_en = '/wlselen.txt'
            a_k_en = '/wlkamen.txt'
            a_h_en = ''
            a_m_en = ''
            a_kb_en = ''
            a_mt_en = ''
            a_kt_en = ''
            a_im_en = ''
            a_lg1_en = ''
            a_s_fi = '/wlselfi.txt'
            a_k_fi = ''
            a_h_fi = ''
            a_m_fi = ''
            a_kb_fi = ''
            a_mt_fi = ''
            a_kt_fi = ''
            a_im_fi = ''
            a_lg1_fi = ''



        te = os.path.exists(a_s_ru) # проверка истинности путей
        print("! sel ru text enable = " + str(te))
        te = os.path.exists(a_s_en)
        print("! sel en text enable = " + str(te))
        te = os.path.exists(a_s_fi)
        print("! sel fi text enable = " + str(te))

        te = os.path.exists(a_k_ru)
        print("! kam ru text enable = " + str(te))
        te = os.path.exists(a_k_en)
        print("! kam en text enable = " + str(te))
        te = os.path.exists(a_k_fi)
        print("! kam fi text enable = " + str(te))

        te = os.path.exists(a_h_ru)
        print("! hant ru text enable = " + str(te))
        te = os.path.exists(a_h_en)
        print("! hant en text enable = " + str(te))
        te = os.path.exists(a_h_fi)
        print("! hant fi text enable = " + str(te))

        te = os.path.exists(a_m_ru)
        print("! mans ru text enable = " + str(te))
        te = os.path.exists(a_m_en)
        print("! mans en text enable = " + str(te))
        te = os.path.exists(a_m_fi)
        print("! mans fi text enable = " + str(te))

        print('! MODE = ' + str(test_st))

                 # счет строк!!!

    ### old mode version

        a_mod = True # true = selkup mode

        if a_mod == True: # блокировка значения lang на sel
            a = a_s_ru
            a_stat = 'not defined'
            a_lang = 'rus'
            print('### defaulf mode = sel   a_mod = ' + str(a_mod))
            resultcnt = 5
            actcnt = 0
        else:
            a = a_k_ru

        addwrd_key = True

        usermess = '' # сообщение юзеру
    ###

        averagesearchtime = []

        ###############################

        def xj(x):
            print('% ' + str(x))

        def workdictmaking(): # создание словаря в кэше

        # здесь можно загрузить перем. 'a' при смене раскладки

            global workdict, a, a_lang

            strcount = 0 # считаем строки
            workdict = []
            with open(str(a), "r") as a:
                for line in a:
                    line = ' ' + str(line)
                    workdict.append(str(line))
                    strcount + 1
            print("! strings = " + str(strcount))
            print('! str count = ' + str(len(workdict)))
            a.close()


        def langreverseturn(a_skhm):  ### переключение основного языка
            global a, a_lang, actcnt
            global a_s_ru, a_s_en, a_s_fi
            global a_k_ru, a_k_en, a_k_fi
            global a_h_ru, a_h_en, a_h_fi
            global a_m_ru, a_m_en, a_m_fi
            global a_kb_ru, a_kb_en, a_kb_fi
            global a_mt_ru, a_mt_en, a_mt_fi
            global a_tz_ru, a_tz_en, a_tz_fi
            global a_kt_ru, a_kt_en, a_kt_fi
            global a_im_ru, a_im_en, a_im_fi
            global a_lg1_ru, a_lg1_en, a_lg1_fi



            if a_skhm == 'sel':
                if a_lang == 'eng':
                    a = a_s_en
                elif a_lang == 'rus':
                    a = a_s_ru
                elif a_lang == 'fin':
                    a = a_s_fi
                else:
                    print('### a_lang ERROR')

            elif a_skhm == 'kam':
                if a_lang == 'eng':
                    a = a_k_en
                elif a_lang == 'rus':
                    a = a_k_ru
                elif a_lang == 'fin':
                    a = a_k_fi
                else:
                    print('### a_lang ERROR')

            elif a_skhm == 'hant':
                if a_lang == 'eng':
                    a = a_h_en
                elif a_lang == 'rus':
                    a = a_h_ru
                elif a_lang == 'fin':
                    a = a_h_fi
                else:
                    print('### a_lang ERROR')

            elif a_skhm == 'mans':
                if a_lang == 'eng':
                    a = a_m_en
                elif a_lang == 'rus':
                    a = a_m_ru
                elif a_lang == 'fin':
                    a = a_m_fi
                else:
                    print('### a_lang ERROR')

            elif a_skhm == 'koj':
                if a_lang == 'eng':
                    a = a_kb_en
                elif a_lang == 'rus':
                    a = a_kb_ru
                elif a_lang == 'fin':
                    a = a_kb_fi
                else:
                    print('### a_lang ERROR')

            elif a_skhm == 'mat':
                if a_lang == 'eng':
                    a = a_mt_en
                elif a_lang == 'rus':
                    a = a_mt_ru
                elif a_lang == 'fin':
                    a = a_mt_fi
                else:
                    print('### a_lang ERROR')

            elif a_skhm == 'taz':
                if a_lang == 'eng':
                    a = a_tz_en
                elif a_lang == 'rus':
                    a = a_tz_ru
                elif a_lang == 'fin':
                    a = a_tz_fi
                else:
                    print('### a_lang ERROR')

            elif a_skhm == 'ket':
                if a_lang == 'eng':
                    a = a_kt_en
                elif a_lang == 'rus':
                    a = a_kt_ru
                elif a_lang == 'fin':
                    a = a_kt_fi
                else:
                    print('### a_lang ERROR')

            elif a_skhm == 'itm':
                if a_lang == 'eng':
                    a = a_im_en
                elif a_lang == 'rus':
                    a = a_im_ru
                elif a_lang == 'fin':
                    a = a_im_fi
                else:
                    print('### a_lang ERROR')

            elif a_skhm == 'lg1':
                if a_lang == 'eng':
                    a = a_lg1_en
                elif a_lang == 'rus':
                    a = a_lg1_ru
                elif a_lang == 'fin':
                    a = a_lg1_fi
                else:
                    print('### a_lang ERROR')


        # команда на смену языка
        @bot.message_handler(commands=['lang'])
        def start_message(message):
        # все доступные словари для перевода
            markup = telebot.types.InlineKeyboardMarkup()
            markup.add(telebot.types.InlineKeyboardButton(text='s.selkup \n южноселькупский', callback_data='sel'))
            markup.add(telebot.types.InlineKeyboardButton(text='n.selkup \n северноселькупский', callback_data='taz'))
            markup.add(telebot.types.InlineKeyboardButton(text='kamassian \n камасинский', callback_data='kam'))
            markup.add(telebot.types.InlineKeyboardButton(text='hanty \n хантыйский (surgut.)', callback_data='hant'))
            markup.add(telebot.types.InlineKeyboardButton(text='hanty \n хантыйский (kazym.)', callback_data='koj'))
            markup.add(telebot.types.InlineKeyboardButton(text='mansi \n мансийский', callback_data='mans'))
            markup.add(telebot.types.InlineKeyboardButton(text='altay \n алтайский', callback_data='mat'))
            markup.add(telebot.types.InlineKeyboardButton(text='кетский \n ket', callback_data='ket'))
            markup.add(telebot.types.InlineKeyboardButton(text='ительменский \n itelmen', callback_data='itm'))
            markup.add(telebot.types.InlineKeyboardButton(text='...', callback_data='lg1'))


            bot.send_message(message.chat.id, text=
                "Select a language to translate\nВыберите язык для перевода", reply_markup=markup)

            bot.send_message(message.chat.id, text=
                "Чтобы бот перевёл слово, просто отправьте его в сообщении!")

        @bot.message_handler(commands=['rcnt'])
        def start_message(message):
            markup = telebot.types.InlineKeyboardMarkup()
            markup.add(telebot.types.InlineKeyboardButton(text='2', callback_data='rcnt2'))
            markup.add(telebot.types.InlineKeyboardButton(text='4', callback_data='rcnt4'))
            markup.add(telebot.types.InlineKeyboardButton(text='6', callback_data='rcnt6'))
            markup.add(telebot.types.InlineKeyboardButton(text='8', callback_data='rcnt8'))
            bot.send_message(message.chat.id, text=
                "Select a count of result / Выберите ширину поиска:", reply_markup=markup)
            print('### rcnt requested')


        @bot.message_handler(commands=['set']) # особые функции
        def start_message(message):
            global a, a_s, a_k, a_h, a_m, a_lang

            markup = telebot.types.InlineKeyboardMarkup()
            markup.add(telebot.types.InlineKeyboardButton(text='unlock AW key', callback_data='addword'))
            bot.send_message(message.chat.id,
                'Setting commands / Команды настройки\n\n'
                '# /rcnt - выбрать ширину поиска (кол-во ответов на запрос)'
                '\n# /printdict - печать словаря (не работает)'
                '\n# +addword - добавить слово в словарь (проверьте ключ)', reply_markup=markup)
            print('### settings')


               ### ответ на смену языка
        @bot.callback_query_handler(func=lambda call: True)
        def query_handler(call):
            global a, a_s, a_k, a_h, a_m, a_lang, a_skhm
            global addwrd_key, a_mod, a_stat, resultcnt, actcnt

            bot.answer_callback_query(callback_query_id=call.id, text='Success! \n\n Успешно!')
            answer = ''
            if call.data == "sel": #Собственно переключение языка
                a_mod = False
                print('### a_mod = ' + str(a_mod))
                a_skhm = 'sel'
                langreverseturn(a_skhm)

                workdictmaking()
                a_stat = 'selkup'
                x = '### keyboard changed > sel\n'
                xj(x)
                print(x)

            elif call.data == 'kam':
                a_mod = False
                print('### a_mod = ' + str(a_mod))
                a_skhm = 'kam'
                langreverseturn(a_skhm)

                workdictmaking()
                a_stat = 'kamassian'
                x = '### keyboard changed > kam\n'
                xj(x)
                print(x)


            elif call.data == "hant":
                a_mod = False
                print('### a_mod = ' + str(a_mod))
                a_skhm = 'hant'
                langreverseturn(a_skhm)

                workdictmaking()
                a_stat = 'surgut hanty'
                x = '### keyboard changed > hant\n'
                xj(x)
                print(x)


            elif call.data == "mans":
                a_mod = False
                print('### a_mod = ' + str(a_mod))
                a_skhm = 'mans'
                langreverseturn(a_skhm)

                workdictmaking()
                a_stat = 'mansi'
                x = '### keyboard changed > mans\n'
                xj(x)
                print(x)

            elif call.data == "koj":
                a_mod = False
                print('### a_mod = ' + str(a_mod))
                a_skhm = 'koj'
                langreverseturn(a_skhm)

                workdictmaking()
                a_stat = 'hanty kazym'
                x = '### keyboard changed > hanty kazym\n'
                xj(x)
                print(x)

            elif call.data == "mat":
                a_mod = False
                print('### a_mod = ' + str(a_mod))
                a_skhm = 'mat'
                langreverseturn(a_skhm)

                workdictmaking()
                a_stat = 'altay'
                x = '### keyboard changed > altay\n'
                xj(x)
                print(x)

            elif call.data == "taz":
                a_mod = False
                print('### a_mod = ' + str(a_mod))
                a_skhm = 'taz'
                langreverseturn(a_skhm)

                workdictmaking()
                a_stat = 'north selkup'
                x = '### keyboard changed > taz\n'
                xj(x)
                print(x)

            elif call.data == "ket":
                a_mod = False
                print('### a_mod = ' + str(a_mod))
                a_skhm = 'ket'
                langreverseturn(a_skhm)

                workdictmaking()
                a_stat = 'ket'
                x = '### keyboard changed > ket\n'
                xj(x)
                print(x)

            elif call.data == "itm":
                a_mod = False
                print('### a_mod = ' + str(a_mod))
                a_skhm = 'itm'
                langreverseturn(a_skhm)

                workdictmaking()
                a_stat = 'itelmen'
                x = '### keyboard changed > itelmen\n'
                xj(x)
                print(x)

            elif call.data == "lg1":
                a_mod = False
                print('### a_mod = ' + str(a_mod))
                a_skhm = 'sel'
                langreverseturn(a_skhm)

                workdictmaking()
                a_stat = '???'
                x = '### keyboard changed > ???\n'
                xj(x)
                print(x)


            elif call.data == "addword":
                print('### addword process')
                addwrd_key = False
                #bot.send_message(message.from_user.id, 'Type "+addstr new stings" to add them to choosed dictionary')


            elif call.data == "rcnt2":
                resultcnt = 2
                print('### rcnt: result count = ' + str(resultcnt))
                #bot.send_message(message.from_user.id, 'Success!\nResult count = ' + str(resultcnt) +
                #    '\n\nType /test for more info')

            elif call.data == "rcnt4":
                resultcnt = 4
                print('### rcnt: result count = ' + str(resultcnt))

            elif call.data == "rcnt6":
                resultcnt = 6
                print('### rcnt: result count = ' + str(resultcnt))


            elif call.data == "rcnt8":
                resultcnt = 8
                print('### rcnt: result count = ' + str(resultcnt))


            elif call.data == "cl_eng":
                a_lang = 'rus'
                x = '### lang changed to eng'
                #bot.send_message(message.from_user.id, 'Language choosed > ' + str(a_lang) + ', language of translation = ' + str(a_stat) + '\nSo pls say Hello!')
                print(x)
                xj(x)

            elif call.data == "cl_rus":
                a_lang = 'rus'
                x = '### lang changed to rus'
                #bot.send_message(message.from_user.id, 'Язык изменён > ' + str(a_lang) + ', язык перевода = ' + str(a_stat) + '\nТеперь скажи боту Привет!')
                print(x)
                xj(x)

            elif call.data == "cl_fin":
                a_lang = 'rus'
                x = '### lang changed to fin'
                #bot.send_message(message.from_user.id, 'Sun kieli on muuttunut > ' + str(a_lang) + ', käännöskieli = ' + str(a_stat) + '\nNy sanoa Hei botille!')
                print(x)
                xj(x)



        @bot.message_handler(commands=['test'])
        def start_message(message):
            global a, a_s, a_k, a_h, a_m, a_lang, a_skhm, averagesearchtime
            global a_stat, resultcnt, actcnt, test_st

            try:
                x = '### keyboard test requested'
                xj(x)
                print(x)

                a_test = str(a_lang) + ' <---> ' + str(a_skhm)

                #averagesearchtime_av = mean(averagesearchtime)
                #averagesearchtime_av = round(averagesearchtime_av,3)
                try:
                    bot.send_message(message.from_user.id, 'Keyboard = ' + str(a_test) + '\n\nKey = ' + str(a_mod) + '\nAddword key = ' + str(addwrd_key) + '\nLang = ' + str(a_lang) +
                        '\nResult count = ' + str(resultcnt) + '\nTesting mode = ' + str(test_st)  + '\nTranslates = ' + str(actcnt)  + '\nСреднее время поиска = ?')
                except Exception as ff:
                    print(ff)
                    bot.send_message(message.from_user.id,
                        'Key = ' + str(a_mod) + '\nAddword key = ' + str(addwrd_key) + '\nLang = ' + str(a_lang) + '\nTranslates = ' + str(actcnt))
            except Exception as rr:
                print('Error 4')
                print(rr)
                bot.send_message(message.from_user.id, '### Error 4')

        @bot.message_handler(commands=['start'])
        def start_message(message):
            global a, a_lang

            keyboard = telebot.types.ReplyKeyboardMarkup(True)
            keyboard.row('/lang', '/test', '/set')
            bot.send_message(message.chat.id, 'Please choose your language:', reply_markup=keyboard)
            x = "### welcome message"
            xj(x)
            print(x)

            markup = telebot.types.InlineKeyboardMarkup()
            markup.add(telebot.types.InlineKeyboardButton(text='Русский', callback_data='cl_rus'))
            markup.add(telebot.types.InlineKeyboardButton(text='English', callback_data='cl_eng'))
            markup.add(telebot.types.InlineKeyboardButton(text='Suomi', callback_data='cl_fin'))
            bot.send_message(message.chat.id, text=
                "Выберите ваш основной язык:", reply_markup=markup)

            bot.send_message(message.chat.id, 'Командой /lang вы можете выбрать язык перевода, /set - настройки бота и /test - состояние бота')




        @bot.message_handler(content_types=['text'])
        def get_text_messages(message):
            global a, a_lang, a_stat, resultcnt, actcnt, repltxt

            if message.text == "/help":
                bot.send_message(message.from_user.id, 'If the bot is not working > @lattar_bot')
                x = "### help message"
                xj(x)
                print(x)


            elif '+addword' in message.text:
            # добавляем слова в словарь

                if addwrd_key == False:
                    mtext = str(message.text)
                    mtext = mtext.replace('+addword', '')

                    strcount2 = 0 # считаем строки x2

                    with open(str(a), "w") as a_dict:
                        for line in mtext:
                            linetxt = str(line)
                            a_dict.write(linetxt + '\n')
                            print('! word added = ' + linetxt)
                            bot.send_message(message.from_user.id, 'Word added = ' + linetxt + '\n')
                            strcount2 + 1
                            a_dict.close()

                            bot.send_message(message.from_user.id, 'Success!\nStrings = ' + str(strcount2) + '\nSymbols = ' + str(len(mtext)))
                        a_dict.close()

                else:
                    bot.send_message(message.from_user.id, 'Requested permission')

            elif '/// ' in message.text:
            # позволяет конвертировать наборные символы в символы расширенной кириллицы
            # если у пользователя нет клавитатуры для нарымского диалекта
                try:
                    if addwrd_key == False:
                        mtext = str(message.text)
                        mtext = mtext.replace('/// ', '') # замена символов как функция

                    mtext = mtext.replace(':а', 'ӓ')
                    mtext = mtext.replace('г,,', 'ӷ')
                    mtext = mtext.replace('о=', 'ө')
                    mtext = mtext.replace('н,,', 'ӈ')
                    mtext = mtext.replace(':о', 'ӧ')
                    mtext = mtext.replace(':у', 'ӱ')
                    mtext = mtext.replace('з,,', 'ҙ')
                    mtext = mtext.replace('к,,', 'ӄ')
                    mtext = mtext.replace('ж,,', 'җ')
                    mtext = mtext.replace('х,,', 'ҳ')
                    mtext = mtext.replace('ч,,', 'ҷ')
                    mtext = mtext.replace(':э', 'ӭ')

                    mtext = mtext.replace(':А', 'Ӓ')
                    mtext = mtext.replace(':О', 'Ӧ')
                    mtext = mtext.replace(':У', 'Ӱ')
                    mtext = mtext.replace(':Э', 'Ӭ')
                    mtext = mtext.replace('З,,', 'Ҙ')
                    mtext = mtext.replace('Г,,', 'Ӷ')
                    mtext = mtext.replace('К,,', 'Ӄ')
                    mtext = mtext.replace('Н,,', 'Ӈ')
                    mtext = mtext.replace('Ж,,', 'Җ')
                    mtext = mtext.replace('Х,,', 'Ҳ')
                    mtext = mtext.replace('Ч,,', 'Ҷ')

                    mtext = mtext.replace('/-', ' ̄ ')
                    mtext = mtext.replace('^', '́ ')
                    mtext = mtext.replace('/.', '̇')

                    repltxt = str(mtext)
                    bot.send_message(message.from_user.id, 'Текст обработан! Нажмите /result и бот выведет конвертированный текст')

                except:
                    print(Exception.text)
                    bot.send_message(message.from_user.id, 'Текст не конвертирован. Почему - непонятно...')

            elif message.text == '/result':
                    bot.send_message(message.from_user.id, 'Результат:\n\n' + repltxt)
                    repltxt = 'Ничего!'
                    print('### text fully converted')

            elif message.text == '/convert':
                bot.send_message(message.from_user.id, 'Эта функция позволяет конвертировать текст на кириллице на селькупскую орфографию.'
                    'Бот превращает сочетания символов в символы для селькупского языка.'
                    'Для гласных - :а > ӓ, для согласных - к,, > ӄ. Полная таблица символов для конвертации > https://clck.ru/YycaP'
                    'Для конвертации текста на селькупские символы припишите вначале "///"')



            elif message.text == '/***printdict': # запрос на вывод
                x = '### printdict request'
                xj(x)
                strcount3 = 0
                with open(str(a), "r") as a_dict2:
                    for line in a_dict2:
                        strcount3 + 1
                        print('### strcount3 + 1')
                        if strcount3 > 20:
                            print('### printdict: strcount3 = 20')
                            bot.send_message(message.from_user.id, 'Strings: ' + str(strcount3) + '\nlenght: ' + str(len(a_dict2)) + '\n\n' + str(a_dict2))
                            break
                    bot.send_message(message.from_user.id, 'Strings = ' + str(strcount3) + '\n\n' + str(printdict))
                    print('### printdict: success, strings = ' + str(strcount3))
                    a_dict2.close()
            elif message.text != '/test':
                wdwordcount = 0
                try:
                    req = ' ' + str(message.text)
                    req.lower()

                    if len(req) > 2:


    ### поиск ###
    #############
                        start_time= time.time()
                        bot.send_message(message.from_user.id, "Найдено: \n")

                        try:
                            try:
                                bot.send_message(message.from_user.id, "[язык - " + str(a_stat) + ']')
                            except Exception as rrr:
                                print('Err 4 - ' + str(rrr))
                            for item in workdict:
                                if req in str(item):
                                    x = "### translated "
                                    xj(x)
                                    print(x)
                                    wdwordcount = wdwordcount + 1
                                    bot.send_message(message.from_user.id, item)
                                    actcnt = int(actcnt) + 1
                                    time.sleep(1/2)
                                    print(str(wdwordcount))


                                    if wdwordcount == int(resultcnt):
                                        print(str(wdwordcount))
                                        break

                            if wdwordcount == 0:
                                bot.send_message(message.from_user.id, 'ничего ¯|_(ツ)_/¯')
                                actcnt = int(actcnt) + 1
                                x = '### nothing is translated'
                                xj(x)
                                print(x)
                                print(str(wdwordcount))

                            end_time = time.time()
                            timetaken = end_time - start_time
                            print('! timer = ' + str(timetaken))
                            averagesearchtime.append(str(timetaken))

                        except:
                            print('### Error 3')


                    else:
                        bot.send_message(message.from_user.id, "Я не могу обработать запрос меньше 3х знаков :(")
                        x = "### not translated "
                        xj(x)
                        print(x)

                except Exception as u:
                    if a_stat == 'not defined':
                        bot.send_message(message.from_user.id,'Язык перевода не выбран! Type /lang')
                    else:
                        bot.send_message(message.from_user.id, '### Проблемы!\nError: [2] ' + str(u))
                    xj(u)
                    print(Exception)

            else:
                bot.send_message(message.from_user.id, "Не понимаю...")
                x = "### failed request"
                print(x)
                xj(x)


        bot.polling(none_stop=True, interval=0)


    except Exception as e:
       print ("### Error [1] : ",e.args[0])
       #xj(e)
       print(e)
except:
    print('Error 0')
