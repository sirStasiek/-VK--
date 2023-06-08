импорт  vk_api
из  vk_api . Импорт длинного опроса  VkLongPoll , VkEventType 
из  vk_api . утилиты  импорта  get_random_id
импорт  конфигурации
из  моделей . ВкБот  импортировать  ВкБот


токен = конфиг . ТОКЕН  
авторизация = vk_api . VkApi ( токен = токен )  
longpoll = VkLongPoll ( авторизация )  
# def write_msg(user_id, сообщение):
# authorize.method('messages.send', {'user_id': user_id, 'message': сообщение,
# 'random_id': get_random_id()} )

# # авторизуемся
# авторизация = vk_api.VkApi(токен=config.GROUP_TOKEN)
# user_access = vk_api.VkApi(токен=config.CLIENT_TOKEN)

def  write_msg ( user_id , сообщение ):
    разрешить . метод ( 'messages.send' , { 'user_id' : user_id , 'сообщение' : сообщение ,
                                       'random_id' : get_random_id (),})

# Прослушивание сервера по событию
для  события  в  longpoll . слушай ():
    если  событие . тип  ==  VkEventType . MESSAGE_NEW  и  событие . to_me :
        запрос  =  событие . текст
        отправитель  =  событие . user_id   # айдишник отправителя
# # доступ к событиям
# longpoll = VkLongPoll(авторизация)
# vk = авторизовать.get_api()
# # user_vk = user_access.get_api()

        если  запрос  ==  "привет" :
            write_msg ( event.user_id , f "Хай , { отправитель } " )
        Элиф  запрос  ==  "пока" :
            write_msg ( событие .user_id , "Пока(( " )
        еще :
            write_msg ( event . user_id , "Не понял вашего ответа..." )
если  __name__  ==  '__main__' :
    vk_bot  =  ВкБот ()
    # Прослушивание сервера по событию
    печать ( 'ckeiftv' )
    для  события  в  vk_bot . длинный опрос . слушай ():
        если  событие . тип  ==  VkEventType . MESSAGE_NEW :
            если  событие . to_me :
                сообщение  =  событие . текст . ниже ()
                отправитель  =  событие . ID пользователя
                vk_bot . write_msg ( user_id = отправитель , сообщение = сообщение )
