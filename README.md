# ⚙️ TOASTER.COMMAND-HANDLING-SERVICE

![main_img](https://github.com/STALCRAFT-FUNCKA/toaster.command-handling-service/assets/76991612/bbb5fee4-803e-4613-8f19-9acb5daf4e1e)


Вся документирующая информация продублированна внутри кода на английском языке.<br>
All documenting information is duplicated within the code in English.<br>


## 📄 Информация ##

**TOASTER.COMMAND-HANDLING-SERVICE** - сервис обработки событий, классифицированных как вызов команды. Событие приходит от сервиса фетчинга, после чего обрабатывается. Праллельно производятся необходимые действия внутреннего\внешнего логирования.

### Входные данные:

**CommandEvent (command_call):**

    content type: application\json

    {
        "ts": 1709107923,
        "datetime": "2024-02-28 11:12:03",
        "event_type": "command_call", 
        "event_id": "8dd52b4d7c822b78db23db85bf351c7114e46b36", 
        "user_id": 206295116, 
        "user_name": "Руслан Башинский", 
        "user_nick": "oidaho", 
        "peer_id": 2000000002, 
        "peer_name": "FUNCKA | DEV | CHAT", 
        "chat_id": 2, 
        "cmid": 2708, 
        "text": "Hi!", 
        "reply": null, 
        "forward": [], 
        "attachments": []
    }

Пример события, которое приходит от toaster.event-routing-service сервера на toaster.command-handling-service.

Далее, сервис определяет, какая команда была вызвана, а уже после - исполняет все действия, которые за этой командой сокрыты.


### Дополнительно

    docker network
        name: TOASTER
        ip_gateway: 172.18.0.1
        subnet: 172.18.0.0/16
        driver: bridge
    

    docker image
        name: toaster.command-handling-service
        args:
            TOKEN: "..."
            GROUPID: "..."
            SQL_HOST: "..."
            SQL_PORT: "..."
            SQL_USER: "..."
            SQL_PSWD: "..."
    

    docker container
        name: toaster.command-handling-service
        network_ip: 172.1.08.6

    docker volumes:
        /var/log/TOASTER/toaster.command-handling-service:/service/logs
        

*Дополнительная информация, которая может пригодиться для поднятия сервиса внутри инфраструктуры.
