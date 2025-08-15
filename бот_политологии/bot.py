import telebot
token = '8127417884:AAGxq-Iss4tYopF7C5Zz0PmarTRdhbzqhcM'
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, row_width=3)
    btn1 = telebot.types.KeyboardButton('Да')
    btn2 = telebot.types.KeyboardButton('Нет')
    keyboard.add(btn1, btn2)
    bot.send_message(message.chat.id, 'Привет, я бот Анлайт, предлагаю тебе поиграть в игру по Эпохе Просвещения. Если хочешь начать игру, нажми "Да", иначе - "Нет"', reply_markup=keyboard)


def starting_the_game(message):
    bot.send_message(message.chat.id, "Вы — молодой писатель в эпоху Просвещения в Европе, охваченной политическими и социальными изменениями. Ваши решения и действия могут повлиять на ход истории и на ваше собственное будущее. Вы встретитесь с великими умыми того времени: Вольтером и Дени Дидро")
    bot.send_message(message.chat.id, 'Кафе "Procope", Париж, XVII год. Весь мир охвачен ожиданием войны (Семилетняя война). Во Франции начинались дискуссии о правлении, свободе и правах человека в виду цветущего абсолютизма')
    bot.send_photo(message.chat.id, open('valter.png', 'rb'))
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, row_width=3)
    btn1 = telebot.types.KeyboardButton('Поддержать Вольтера')
    btn2 = telebot.types.KeyboardButton('Засомневаться в его идеях')
    keyboard.add(btn1, btn2)
    bot.send_message(message.chat.id, "Вы оказались в кафе, где обсуждаются идеи свободы слова и критики власти. Вольтер привлекает ваше внимание своими высказываниями о Боге, церкви, власти и частной собственности. Сделайте выбор", reply_markup=keyboard)

def work_valter(message):
    bot.send_message(message.chat.id, 'Вольтер вдохновился вашим энтузиазмом и предложил вам написать общее произведение "Танту".')
    bot.send_photo(message.chat.id, open('valter_w.png', 'rb'))
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, row_width=3)
    btn1 = telebot.types.KeyboardButton('Добавить в произведение яркой критики')
    btn2 = telebot.types.KeyboardButton('Написать самому статью об образовании')
    keyboard.add(btn1, btn2)
    bot.send_message(message.chat.id, 'Вы и Вольтер пишете произведение на тему религиозной нетерпимости и предрассудков, которые поддерживаются властью и традициями. Вольтер критикует невежество и жестокость, встречающиеся среди тех, кто использует религию как инструмент подавления свободомыслия. Сделайте выбор',reply_markup=keyboard)

def conclus(message):
    bot.send_photo(message.chat.id, open('paris.png', 'rb'))
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, row_width=3)
    btn1 = telebot.types.KeyboardButton('Продолжать анонимно')
    btn2 = telebot.types.KeyboardButton('Вести открытую борьбу')
    keyboard.add(btn1, btn2)
    bot.send_message(message.chat.id, "Впоследствии ваши сатирические, а порой и жесткие высказывания, привели к тому, что вы стали объектом преследования властей. Однако ваши идеи продолжают активно обсуждаться в кругах прогрессивных мыслителей. Сделайте выбор",reply_markup=keyboard)

def article(message):
    bot.send_message(message.chat.id, 'Изучая вопросы воспитания и образования, вы решете написать об этом статью. Вы мечтаете искоренить социальную несправедливость путем такого образования и воспитания, которые позволили бы каждому человеку найти свое место в обществе, сочетая личное счастье со вкладом в справедливое переустройство общества.')
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, row_width=3)
    btn1 = telebot.types.KeyboardButton('Параллельно с публикацией начать писать книгу')
    btn2 = telebot.types.KeyboardButton('Участвовать в публичных диспутах')
    keyboard.add(btn1, btn2)
    bot.send_photo(message.chat.id, open('enc.png', 'rb'))
    bot.send_message(message.chat.id, 'Вы публикуете статью в Энциклопедии и она находит отклик у читателей. Сделайте выбор', reply_markup=keyboard)

def somn(message):
    bot.send_photo(message.chat.id, open('m1.jpg', 'rb'))
    bot.send_message(message.chat.id, 'Ваши вопросы и сомнения раздражают Вольтера. Он считает, что вы не понимаете основ Просвещения и уходит, оставив вас в недоумении. Вы решаете углубиться в познаниях философских идей. ')
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, row_width=3)
    btn1 = telebot.types.KeyboardButton('Написать Вольтеру')
    btn2 = telebot.types.KeyboardButton('Обратиться к Дидро')
    keyboard.add(btn1, btn2)
    bot.send_message(message.chat.id,'Что вам окажется ближе: желание абсолютного социального равенства, которое предлаает Дидро, или идеи частной собственности и естественных прав от Вольтера? Сделайте выбор', reply_markup=keyboard)

def didro(message):
    bot.send_photo(message.chat.id, open('didro.png', 'rb'))
    bot.send_message(message.chat.id,'Вы прочитали произведения Вольтера, с некоторыми из его идей вы всё же не согласны: особенно в темах, связанных с частной собственностью. Вы стремитесь победить неравенство в обществе. Помимо этого, вас заинтересовали работы Дидро, с которым у вас оказалось много схожих идей, касаемо социальной справедливости и образования. Вы решаете написать ему письмо и пригласить на встречу')
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, row_width=3)
    btn1 = telebot.types.KeyboardButton('Согласиться работать у Дидро')
    btn2 = telebot.types.KeyboardButton('Написать самому статью об образовании')
    keyboard.add(btn1, btn2)
    bot.send_message(message.chat.id,'Дидро восхищается вашей оригинальностью, вы сошлись во взглядах, он вдохновил вас на собственную литературную деятельность, но при этом предложил работать в его издании "Энциклопедия". Сделайте выбор', reply_markup=keyboard)

def book(message):
    bot.send_photo(message.chat.id, open('m.jpg', 'rb'))
    bot.send_message(message.chat.id, 'Вы решаете написать книгу о воспитании, вложив в книгу все свои идеи. Вы предлагаете новаторские идеи в области образования, акцентируя внимание на развитии естественных способностей и интересов ребенка. Вы отстаиваете в книге важность личного опыта, самообучения и развития нравственных качеств, а также независимого мышления. ')
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, row_width=3)
    btn1 = telebot.types.KeyboardButton('Добавить главу о религии')
    btn2 = telebot.types.KeyboardButton('Не добавлять главу')
    keyboard.add(btn1, btn2)
    bot.send_message(message.chat.id, 'Книга почти готова. Последнее, что вам хочется добавить: главу «Исповедание веры савойского викария». Это проповедь «естественной религии», отрицающая официальную церковную догматику. Сделайте выбор',reply_markup=keyboard)

def restart():
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, row_width=3)
    btn1 = telebot.types.KeyboardButton('Начать игру заново')
    keyboard.add(btn1)
    return keyboard
@bot.message_handler(content_types=['text'])
def q(message):
    if message.text == 'Да':
        bot.send_message(message.chat.id, 'Начинаем!')
        starting_the_game(message)
    elif message.text == 'Нет':
        bot.send_message(message.chat.id, 'До скорого!')
    elif message.text == 'Поддержать Вольтера':
        work_valter(message)
    elif message.text == 'Засомневаться в его идеях':
        somn(message)
    elif message.text == 'Добавить в произведение яркой критики':
        bot.send_message(message.chat.id, 'Вы добавили примечание к произведению, где, не стесняясь выражений, критиковали власть. ')
        conclus(message)
    elif message.text == 'Вести открытую борьбу':
        bot.send_photo(message.chat.id, open('bast.png', 'rb'))
        bot.send_message(message.chat.id, 'КОНЕЦ ИГРЫ: Ваше смелое решение приводит к тому, что вы оказыватесь в Бастилии, подобно Вольтеру, что вызывает общественный резонанс. Вам помогают вызволиться из тюрьмы и вы становитесь популярным публицистом эпохи Просвещения, правда уже не в Париже:).', reply_markup=restart())
    elif message.text == 'Продолжать анонимно':
        bot.send_photo(message.chat.id, open('result (4).jpg', 'rb'))
        bot.send_message(message.chat.id, 'КОНЕЦ ИГРЫ: Вы будете на пике популярности за счет своей анонимной смелости. Однако ввиду только анонимной деятельности вас скоро вытеснут открытые противники. Популярность спадет, вы каните в забвение', reply_markup=restart())
    elif message.text == 'Написать самому статью об образовании':
        article(message)
    elif message.text == 'Параллельно с публикацией начать писать книгу':
        book(message)
    elif message.text == 'Участвовать в публичных диспутах':
        bot.send_message(message.chat.id, 'Вы становитесь известным оратором на тему естественных прав человека и общественного договора. Это приводит к новым возможностям, и ваши идеи начинают распространяться.')
        conclus(message)
    elif message.text == 'Написать Вольтеру':
        bot.send_message(message.chat.id, 'Вы пишете Вольтеру, извиняетесь перед ним и описываете свои идеи, касающиеся прав человека на свободу мысли, слова и печати, а также выражаете свое несогласие с догмами религии')
        work_valter(message)
    elif message.text == 'Обратиться к Дидро':
        didro(message)
    elif message.text == 'Согласиться работать у Дидро':
        bot.send_message(message.chat.id, 'Вы становитесь главным помощником Дидро. Вы вошли в круг энциклопедистов, писали статьи для издания. Однако мелочная ссора погубила ваши отношения с Дидро, вы ушли из Энциклопедии и решаетесь написать книгу.')
        book(message)
    elif message.text == 'Добавить главу о религии':
        bot.send_photo(message.chat.id, open('j.jpg', 'rb'))
        bot.send_message(message.chat.id, 'КОНЕЦ ИГРЫ: Вы решились добавить главу, однако это привело к тому, что весь тираж книги был конфискован и сожжен. Вам пришлось в срочном порядке покинуть Францию. Вы продолжили свою работу в других странах: жили в Швейцарии и Англии.', reply_markup=restart())
    elif message.text == 'Не добавлять главу':
        bot.send_photo(message.chat.id, open('result.jpg', 'rb'))
        bot.send_message(message.chat.id, 'КОНЕЦ ИГРЫ: Вы решили не добавлять эту главу. Книга была напечатана, но встретила много критики со стороны других общественных деятелей. Вы не нашли поддержки во Франции и уехали. Но ваша книга через много лет станет вдохновением для людей, совершающих Великую Французскую революцию', reply_markup=restart())
    elif message.text == 'Начать игру заново':
        starting_the_game(message)
    else:
        bot.reply_to(message, 'Я вас не понимаю')

bot.polling() 

# все что связано с книгой - как эмиль у руссо. или все ок вы лектор, или вы популярный издатель у которого сожгли книгу! конец. 

# дописать к комментам к боту то как поссорились дидро и руссо
# добавить картинки