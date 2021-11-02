from kivy.app import App   
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.button import ButtonBehavior, Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.animation import Animation
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from kivy.uix.gridlayout import GridLayout
from kivy.app import runTouchApp
from email import encoders






class MyLayout_W(Widget):
    pass
class FirstScrren(Screen):
    
    pass
class BarGraph(Screen):
	pass
class Pulse(Screen):
    i = str('15')
    pass
class Breese(Screen):
    pass
class Resalt(Screen):
    pass
class SecondScreen(Screen):
	pass

class ImageButton(ButtonBehavior, Image):

	pass

class ThirdScreen(Screen):
	pass
class Information(Screen):
    pass

class Information_veiw(Screen):
    pass
class Drags(Screen):
    pass
class DragsChoise(Screen):
    pass



GUI = Builder.load_file("main.kv")


class MainApp(App):
    i = f"resalt"
    h="SoME STRING IS HERE "

    def build(self):
        
        def start_load(self):
            try:
                global block_list
                read_lines = open("data.txt", "r",encoding = 'utf-8')
                data= read_lines.readlines()
                counter= 0

                name_data = data[1].split("\n")
                if name_data[0] != '':
                    first_line=name_data[0]
                    counter += 1
                    block_list[1] = first_line

                name_data = data[2].split("\n")
                if name_data[0] != '':
                    second_line=name_data[0]
                    block_list[2] = second_line
                    counter += 1

                name_data = data[3].split("\n")
                if name_data[0] != '':
                    second_line1=name_data[0]
                    block_list[3] = second_line1

                name_data = data[4].split("\n")    
                if name_data[0] != '':
                    second_line2=name_data[0]
                    block_list[4] = second_line2
                name_data = data[5].split("\n")    
                if name_data[0] != '':
                    second_line2=name_data[0]
                    block_list[5] = second_line2
                name_data = data[6].split("\n")    
                if name_data[0] != '':
                    second_line2=name_data[0]
                    block_list[6] = second_line2
                name_data = data[7].split("\n")    
                if name_data[0] != '':
                    second_line2=name_data[0]
                    block_list[7] = second_line2
                name_data = data[8].split("\n")  
                if name_data[0] != '':
                    second_line2=name_data[0]
                    block_list[8] = second_line2

                


            except:
                print ("Not sefed")


            try:
                read_lines = open("data.txt", "r",encoding = 'utf-8')
                data= read_lines.readlines()
                counter= 0

                data1 = data[1].split("\n")
                if data1[0] != '':
                    first_line=data1[0]
                    counter += 1

                data1 = data[2].split("\n")
                if data1[0] != '':
                    second_line=data1[0]
                    counter += 1
                data1 = data[3].split("\n")
                if data1[0] != '':
                    third_line=data1[0]

                    counter += 1
                if counter == 3: # 1 screen label 1 - 4
                    text_label3 = self.root.ids.screen1.ids.text_label3
                    
                    text_label3.text = f"{first_line} / {second_line}"
                    text_label3.font_size = '60dp'
                    text_label4 = self.root.ids.screen1.ids.text_label4
                    text_label4.text = f"пульс {third_line} уд. / мин"
                    text_label4.font_size = '20dp'




            except:  
                print("nothing read")
            pass

    
        return GUI and  start_load(self)


    def change_screen(self, screen_name):
        screen_manager = self.root.ids['screen_manager']
        screen_manager.current = screen_name
        





    def change_screen1(self, screen_name1):
        # Get the screen

        screen_manager = self.root.ids.pulse.ids['screen_manager1']
        screen_manager.current =screen_name1
        text_button1 = self.root.ids.screen1.ids.text_button1
        text_button1.text = f'{block_list[1]}/{block_list[2]}'

    def animation_button(self, widget, *args):
            anim = Animation(background_color=(243/255,132/255,132/255,1), duration= .3)
            anim.start(widget)
    def animation_button_back(self, widget, *args):
            anim = Animation(background_color=(243/255,52/255,52/255,1), duration= .3)
            anim.start(widget)
    def animation_button_gray(self, widget, *args):
            anim = Animation(background_color=(131/255 , 131/255, 131/255, 1), duration= .3)
            anim.start(widget)
    def animation_button_back_gray(self, widget, *args):
            anim = Animation(background_color=(225/255,200/255,200/255,1), duration= .3)
            anim.start(widget)
    def base_breese(self, widget, *args):
        pass
    def color_pi(self, color):
        return '"F3CACA"'




    def first_screen1(self):
        print ("1231")
        try:
            read_lines = open("data.txt", "r",encoding = 'utf-8')
            data= read_lines.readlines()
            counter= 0

            data1 = data[1].split("\n")
            if data1[0] != '':
                first_line=data1[0]
                counter += 1

            data1 = data[2].split("\n")
            if data1[0] != '':
                second_line=data1[0]
                counter += 1
            data1 = data[3].split("\n")
            if data1[0] != '':
                third_line=data1[0]

                counter += 1
            if counter == 3: # 1 screen label 1 - 4
                text_label3 = self.root.ids.screen1.ids.text_label3
                
                text_label3.text = f"{first_line} / {second_line}"
                text_label3.font_size = '60dp'
                text_label4 = self.root.ids.screen1.ids.text_label4
                text_label4.text = f"пульс {third_line} уд. / мин"
                text_label4.font_size = '20dp'




        except:  
            print(block_list)
        pass


#---------------------------------------------------------------------------------

    def self_data_read(self):

        try:
            read_lines = open("data_mail.txt", "r",encoding = 'utf-8')
            data_mail= read_lines.readlines()
            first_name = self.root.ids.screen3.ids.first_name
            birthday = self.root.ids.screen3.ids.birthday
            sex = self.root.ids.screen3.ids.sex
            growth = self.root.ids.screen3.ids.growth
            number_self = self.root.ids.screen3.ids.number_self
            number_doc = self.root.ids.screen3.ids.number_doc
            number_doc2 = self.root.ids.screen3.ids.number_doc2
            mail_to = self.root.ids.screen3.ids.mail_to

            global data_list
            
            
            

            name = data_mail[1].split("\n")
            if name[0] != '':
                first_name.text=name[0]
                data_list[1] = name[0]

            name = data_mail[2].split("\n")
            if name[0] != '':
                birthday.text=name[0]
                data_list[2] = name[0]

            name = data_mail[3].split("\n")
            if name[0] != '':
                sex.text=name[0]
                data_list[3] = name[0]

            name = data_mail[4].split("\n")
            if name[0] != '':
                growth.text=name[0]
                data_list[4] = name[0]

            name = data_mail[5].split("\n")
            if name[0] != '':
                number_self.text=name[0]
                data_list[5] = name[0]

            name = data_mail[6].split("\n")
            if name[0] != '':
                number_doc.text=name[0]
                data_list[6] = name[0]

            name = data_mail[7].split("\n")
            if name[0] != '':
                number_doc2.text=name[0]
                data_list[7] = name[0]

            name = data_mail[8].split("\n")
            if name[0] != '':
                mail_to.text=name[0]
                data_list[8] = name[0]

        except:
            print ("error")
        pass

    def self_data_seve(self, line, data):
        my_file1 = open("data_mail.txt", 'a',encoding = 'utf-8')
        if line == 1:
            if data == "":
                name = my_file1.write(f'\n')
            else:
                name = my_file1.write(f'{data}\n')
        if line == 2:
            if data == "":
                name = my_file1.write(f'\n')
            else:
                name = my_file1.write(f'{data}\n')
        if line == 3:
            if data == "":
                name = my_file1.write(f'\n')
            else:
                name = my_file1.write(f'{data}\n')
        if line == 4:
            if data == "":
                name = my_file1.write(f'\n')
            else:
                name = my_file1.write(f'{data}\n')
        if line == 5:
            if data == "":
                name = my_file1.write(f'\n')
            else:
                name = my_file1.write(f'{data}\n')
        if line == 6:
            if data == "":
                name = my_file1.write(f'\n')
            else:
                name = my_file1.write(f'{data}\n')
        if line == 7:
            if data == "":
                name = my_file1.write(f'\n')
            else:
                name = my_file1.write(f'{data}\n')
        if line == 8:
            if data == "":
                name = my_file1.write(f'\n')
            else:
                name = my_file1.write(f'{data}\n')
        my_file1.close()  
        pass
    def starter(self):
        my_file = open("data_mail.txt", 'w',encoding = 'utf-8')
        my_file.write(f'data_mail\n')
        my_file.close()
    def starter2(self):
        my_file = open("data.txt", 'w',encoding = 'utf-8')
        my_file.write(f'data\n')
        my_file.close()
        pass
    def data_base(self, line, data):
        global block_list
        block_list[line]= data

    def base_data(self):
        my_file1 = open("data.txt", 'a',encoding = 'utf-8')
        global block_list
        for i in range(1, 10):
            if block_list[i] == "":

                name = my_file1.write(f'\n')
                
            else:
                name = my_file1.write(f'{block_list[i]}\n')
        my_file1.close()
        pass    


    def bar_state_secondscreen(self):
        global block_list
        bar_size_1 = block_list[1]
        bar_size_2 = block_list[2]
        try:     
            bar_size_1 = f".{int(bar_size_1) // 3}"
            bar_size_2 = f".{int(bar_size_2) // 3}"
            bar1 = self.root.ids.screen2.ids.bargraph.ids.bar1
            bar2 = self.root.ids.screen2.ids.bargraph.ids.bar2
            bar1.size_hint = (.3 , bar_size_1)
            bar2.size_hint = (.3 , bar_size_2)
            bar1.pos_hint = {"center_x": .35 , "bottom": 1}
            bar2.pos_hint = {"center_x": .75 , "bottom": 1}
            mass1 = self.root.ids.screen2.ids.mass1
            if block_list[8] != '':
                mass1.text=block_list[8]


        except:
            print("bar_state_secondscreen")
        pass


    def result_screen(self, num):
        global block_list
        bar_size_1 = block_list[1]
        bar_size_2 = block_list[2]
        bar_size_3 = block_list[3]
        if num == 2:
            
            try:     
                bar_size_1 = f".{int(bar_size_1) // 3}"
                bar_size_2 = f".{int(bar_size_2) // 3}"

                bar1 = self.root.ids.resalt.ids.bargraph.ids.bar1
                bar2 = self.root.ids.resalt.ids.bargraph.ids.bar2
                bar1.size_hint = (.4 , bar_size_1)
                bar2.size_hint = (.4 , bar_size_2)
                bar1.pos_hint = {"center_x": .35 , "bottom": 1}
                bar2.pos_hint = {"center_x": .75 , "bottom": 1}
            except:
                print("result_screen")

        if num == 1:
            try:     
                bar_size_1 = f".{int(bar_size_1) // 2}"
                bar_size_2 = f".{int(bar_size_2) // 3}"
                bar_size_3 = f".{int(bar_size_3) // 2}"
                
                bar1 = self.root.ids.resalt.ids.bargraph.ids.bar1
                bar2 = self.root.ids.resalt.ids.bargraph.ids.bar2
                bar1.size_hint = (.5 , bar_size_3)
                print(1)
                bar1.pos_hint = {"center_x": .5 , "bottom": 1}
                print(2)
                bar2.size_hint = (0 , 0)
            except:
                print("result_screen2")
        if num == 3:
            try:     
                bar_size_1 = f".{int(bar_size_1) // 5}"
                bar_size_2 = f".{int(bar_size_2) // 5}"

                
                bar1 = self.root.ids.resalt.ids.bargraph.ids.bar1
                bar2 = self.root.ids.resalt.ids.bargraph.ids.bar2
                bar2.size_hint = (.5 , bar_size_2)

                bar2.pos_hint = {"center_x": .5 , "bottom": 1}

                bar1.size_hint = (0 , 0)
            except:
                print("result_screen2")
            pass

    def bar_state_pulse(self, bar12, bar22):
        global block_list
        try:
            bar_size_1 = int(block_list[1]) // 2
            bar_size_2 = int(block_list[2]) // 2
            if bar_size_1 <=98:
                bar_size_1= f".{bar_size_1}"
            else:
                bar_size_1 = ".98"
            if bar_size_2 <= 98:
                bar_size_2= f".{bar_size_2}"
            else:
                bar_size_2 = ".98"
            print (bar_size_1,bar_size_2)
        except:
            print(111111)

        try:
            
            bar_size_1 = bar_size_1
            bar1 = self.root.ids.pulse.ids.bargraph.ids.bar1
            bar1.size_hint = (.4 , bar_size_1)
            bar_size_2 = bar_size_2
            bar2 = self.root.ids.pulse.ids.bargraph.ids.bar2
            bar2.size_hint = (.4 , bar_size_2)
        except:
            print("bar_state_pulse")

        try:
            pulse_up = self.root.ids.pulse.ids.pulse_up
            pulse_down = self.root.ids.pulse.ids.pulse_down
            pulse_self = self.root.ids.pulse.ids.pulse_self
            mass = self.root.ids.pulse.ids.mass   

            if block_list[1] != '':
                pulse_up.text=block_list[1]


            if block_list[2] != '':
                pulse_down.text=block_list[2]


            if block_list[3] != '':
                pulse_self.text=block_list[3]


            if block_list[4] != '':
                mass.text=block_list[4]

        except:
            print("bar_state_pulse2")
        try:

            bar1 = self.root.ids.breese.ids.bargraph.ids.bar1
            bar1.size_hint = (.4 , bar_size_1)
            bar2 = self.root.ids.breese.ids.bargraph.ids.bar2
            bar2.size_hint = (.4 , bar_size_2)
        except:
            print("bar_state_pulse3")

        pass


  
    def update_case(self):

        try:
            print(block_list)
        except:
            print("error")


    def mail_senter(self):
        try:
            my_file = open("DOC.docx", 'w',encoding = 'utf-8')
            my_file.write(f'data_mail\n')
            my_file.write(f'{data_list}\n')
            my_file.write(f'{block_list}\n')
            my_file.close()

            label_mail = self.root.ids.screen3.ids.label_mail
            label_mail.text = "ЧТО-ТО НЕ ТАК"

            mail_content = '''Hello,
            This is a test mail.
            In this mail we are sending some attachments.
            The mail is sent using Python SMTP library.
            Thank You
            '''
            sender_address = 'ascemme@mail.ru'
            sender = 'dpd.pdg123'
            receiver_address = f'{data_list[8]}'
            message = MIMEMultipart()
            message['From'] = sender_address
            message['To'] = receiver_address
            message['Subject'] = 'A test mail sent by Python. It has an attachment.'
            message.attach(MIMEText(mail_content, 'plain'))
            attach_file_name = 'DOC.docx'
            attach_file = open(attach_file_name, 'rb') # Open the file as binary mode
            payload = MIMEBase('application', 'octate-stream')
            payload.set_payload((attach_file).read())
            encoders.encode_base64(payload)
            payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
            message.attach(payload)
            session = smtplib.SMTP_SSL('smtp.mail.ru', 465) 
            session.login(sender_address, sender)
            text = message.as_string()
            session.sendmail(sender_address, receiver_address, text)
            session.quit()
            label_mail.text = "МАЙЛ ОТПРАВЛЕН"
            print('Mail Sent')
        except:
            print("mail error")

    def spinner_clicked(self):
        sp= self.root.ids['drags'].ids.spinner_id 
        sp2= self.root.ids['drags'].ids.spinner_id2 
        sp3= self.root.ids['drags'].ids.spinner_id3 
        pipi= ["Выбрать", ""]

        for i in range(1,176):
            pipi.append(f"{Text_info1[i]}")
        
            
        
        sp.values = map(str, pipi)
        sp2.values = map(str, Dizar)
        sp3.values = map(str, Days)

    def printer(self, war):
        print (war)

     




    def drags_add(self):
        global drags_list
        global drags_doz
        global drags_rate
        global counter_drags
        counter_1 = 1
        counter_2 = 1
        for pir in range (1,9):
            label = self.root.ids.dragschoise.ids[f"label_{pir}"] 
            but_r = self.root.ids.dragschoise.ids[f"btn_{pir}"]
            label.text = "" 
            but_r.pos_hint = {"top": counter_1, "center_x": 0}
            counter_1= counter_1 - 0.1
        counter_1 = 1
        for i in drags_list.values():
            label = self.root.ids.dragschoise.ids[f"label_{counter_2}"]    
            but_r = self.root.ids.dragschoise.ids[f"btn_{counter_2}"]
            but_r.pos_hint = {"top": counter_1, "center_x": .5}
            label.text = i
            counter_1 -=0.1
            counter_2 += 1
         

    def drags_remover(self, name, num):
        global drags_list
        global drags_doz
        global drags_rate
        but_r = self.root.ids.dragschoise.ids[f"label_{num}"]
        but_r = self.root.ids.dragschoise.ids[f"btn_{num}"]
        name_value = name.text
        
        desired_value = name_value
        for key, value in drags_list.items():
          if value == desired_value:
            del drags_list[key]
            del drags_doz[key]
            del drags_rate[key]
            break



        print (drags_list, drags_doz,drags_rate)
        
    def drag_save(self, name, doz, rate):
        global drags_list
        global drags_doz
        global drags_rate
        global counter_drags

        counter_drags += 1

        drags_list[f"{counter_drags}"] = f"{name}"
        drags_doz[f"{counter_drags}"] = f"{doz}"
        drags_rate[f"{counter_drags}"] = f"{rate}"


    def information(self, inform):  
        Label_1 = self.root.ids.information_veiw.ids.text_info 
        Label_1.text = Text_info[int(inform)]



    def drag_save1(self):
        print (drags_list,drags_doz,drags_rate)
        
        










counter_drags = 0

Text_info = {
    "0":"0",
    1: "Дневник пациента с сердечной недостаточностью(СН) разработан с целью помочь Вам принимать активное участие в лечении вашего заболевания вместе с лечащим врачом. "
    ' Вы сами сможете контролировать ключевые показатели состояния здоровья и в случае необходимости сообщить об изменениях лечащему врачу. '
    ' Кроме того, дневник поиожет Вам разобраться в сущности заболевания и лечебных методах, а также понять важность изменения образа жизни.\n'
    ' Ежедневные записи Ваших измерений будут очень полезны для обсуждения с врачом при последующих посещениях лечебного учереждения.\n '
    ' Вы можете узнать про сердечную недостаточность на официальном образовательном веб-сайте Белорусской ассоциации сердечной недостаточности:'
    'www.heartfailure.by',
    2: "Сердечная недостаточность - это нарушение функции сердца, при котором оно не может перекачивать кровь в достаточном объеме, в органах и тканях."
    ' В результате клетки тела получают недостаточное количество питательных веществ, испытывают кислородное голодание.\n'
    ' СН сопровождается комплексом симптомов: \n'
    ' - одышка;\n'
    ' - усталость;\n'
    ' - отеки(задержка жидкости).\n'
    ' На начальных стадиях симптомы хронической сердечной недостаточности (ХСН) возникают только во время физических нагрузок. '
    ' Со временем эти симптомы усиливаются, начинают беспокоить не только во время физической работы, но и в состоянии покоя. ',
    3: "- Медикаментозное лечение;\n"
    '- Хирургическое (по показаниям);\n'
    '- Электрофизиологические методы терапии (имплантация электрокардиостимуляторов, ресинхронизируещих устройств, дефибриляторов; денервация почечных артерий);\n'
    '- Эндоваскулярная имплантация мезенхимальных стволовых клеток;\n'
    '- Психологическая реабилитация;\n'
    '- Организация школ пациентов с сердечной недостаточностью (формирование мотивации к здоровому образу жизни);\n'
    '- Проведение ежегодных дней знаний о сердечной недостаточности. ',
    4: " Узнать, если у Вас проблемы с весом можно с помощью индекса массы тела (ИМТ), который рассчитывается по формуле:\n"
    '                ИМТ = масса тела (кг)/(рост,м)*(рост,м)\n '
    ' Наличие ожирения или избыточного веса ухудшает прогноз пациента с ХСН, поэтому при ИМТ более 25кг/м.кв. требуется принятие специальных мер и ограничения калорийности питания.\n'
    '                 ИМТ, кг/м.кв.\n' 
    ' Норма 18,5-24,9\n'
    ' Избыточный вес 25,0-29,0\n'
    ' Ожирение >= 30,0\n'
    ' Если у Вас увеличился вес более 2 кг в течении 1-3 дней при соблюдении вашего обычного рациона питания, то необходимо проконсультироваться с врачом, так как это может быть в следствие задержки жидкости в организме! ',
    5: "- Ограничьте употребление поваренной соли: суточное количество соли не должно превышать 3-5 г. "
    'Пищу лучше не подсаливать, достаточно той соли, которая имеется в продуктах.\n'
    '- Исключите газированные напитки.\n'
    '- Избегайте "фаст-фуда".\n'
    '- Ешьте рыбу 1-2 раза в неделю, в том числе рыбу жирных сортов.\n'
    '- Включите в ежедневный рацион по 200 г. фруктов и овощей.\n'
    '- Желательно употребление 30-45 г. в сутки пищевых волокон, особенно из цельнозерновых продуктов. ', 
    6: "Допускается прием до 7 бокалов вина в неделю (1 бокал в сутки).\n"
    ' Большее потребление алкоголя может индуцировать развитие кардиомиопатии токсического генеза.'
    ' В таком случае, прием алкоголя категорически противопоказан.',
    7: "  Курение оказывает неблагоприятное влияние на здоровье и ухудшает прогноз при сердечно-сосудистой патологии.\n"
    ' Курение усиливает эффект таких факторов риска, как возраст, мужской сахарный диабет.\n'
    ' Прекращение курения - одна из самых эффективных мер профилактики сердечно-сосудистых заболеваний.\n'
    ' Избегайте пассивного курения ',
    8: "Малоподвижный образ жизни и низкая физическая активность увеличивает риск раннего развития и прогрессирования ХСН\n"
    '  Не менее 30 минут в день посвящайте упражнениям легкой (пешая прогулка) и умеренной интенсивности (быстрая ходьба). Одним из вариантов физической нагрузки является скандинавская ходьба. '
    ' Выбор режима физической нагрузки зависит от Вашего состояния, оцененного вашим лечащим врачом.',
    9: " Поддерживайте уровень АД меньше 140/90 мм рт.ст.\n"
    ' Как правильно измерить АД в домашних условиях:\n'
    ' - перед измерением необходимо отдохнуть 3-5 минут;\n'
    ' - измеряйте АД в положении сидя, с опорой для спины и рук, поставьте ноги на пол, расположив руку на уровне сердца. Во время измерения не следует разговаривать, в т.ч. и по телефону;\n'
    ' - в идеале нужно производить 2 измерения с интервалом 1-2 мин., 1 раз утром и 1 раз вечером\n'
    ' Как измерить ЧСС в домашних условиях:\n'
    ' Оптимальное ЧСС 55-60 уд/мин.\n'
    ' - посидите спокойно не менее 5 минут;\n'
    ' - пульс удобно прощупывать на запястье руки у основания большого пальца. Удобнее это делать 4 пальцами, при этом 5 палец должен использоваться как опора.\n'
    ' - подсчитайте пульс в течение 60 секунд',    
    10: "  Уровень глюкозы крови у пациентов с ХСН не должен превышать 5 ммоль/л, уровень гликированного гемоглобина 5,6%.",
    11: "  Наличие отеков можно определить простым нажатием пальца в течении нескольких секунд на кожу в области лодыжек.  "
    ' Если нет отека, то после отнятия пальца ткани моментально расправляются. '
    ' Если есть отек, то остается ямка на 1-2 минуты, затем исчезает.',
    12: "Необходимым условием эффективной профилактики СН и ее прогрессирования являются хорошее взаимопонимание между врачом и пациентом.\n"
    ' Эффективность лекарственного средства зависит от его правильного и регулярного применения.'
    ' Не секрет, что пациенты часо не придерживаются предписанной схемы лечения по разным причинам, вследствие чего наступает обострение(декомпенсация) сердечной недостаточности.\n '
    ' Строгое соблюдение всех рекомендацией врача по проводимой терапии и принципов здорового образа жизни - залог уменьшения симптомов сердечной недостаточности, улучшения качества жизни пациента и предотвращения прогрессирования заболеваний!',
    13: "Незамедлительно проинформируйте своего лечащего врача, если Вы испытываете:\n "
    ' - усиление одышки;\n'
    ' - уменьшение переносимости физических нагрузок;\n '
    ' - частые пробуждения ночью из-за одышки и потребности в большем количестве подушек для обеспечения комфорта;\n'
    ' - стойкое учащенное сердцебиение;\n'
    ' - нарушение ритма сердечных сокращений;\n '
    ' - быстрое увеличение массы тела;\n'
    ' Следует вызвать скорую помощь в случае:\n'
    ' - постоянной боли в груди, от которой не избавляет прием нитроглицерина;\n'
    ' - тяжелой и стойкой одышки;\n'
    ' - слабости или обморока;',
}

Text_info1 = {
    "0":"0",    
    1:"АСК",
    2:'Аккузид',
    3:'Аккупро',
    4:'Амиодарон',
    5:'Амиокордин',
    6:'Амлесса',
    7:'Амлодин',
    8:'Амлодипин',
    9:'Амлотензин',
    10:'Амприлан',
    11:'Арифон ретард',
    12:'Асомекс',
    13:'Аспикард',
    14:'Аторвастатин',
    15:'Аторис',
    16:'Аудитор',
    17:'Ацетилсалициловая кислота',
    18:'Берлиприл',
    19:'Берлиприл Плюс',
    20:'Беталок',
    21:"Бикард",
    22:'Бисопролол',
    23:'Бравадин',
    24:'Валз',
    25:'Валз Н',
    26:'Валзан',
    27:'Валзан Н',
    28:'Валсартан',
    29:'Вальсакор',
    30:'Вальсакор Н',
    31:'Вальсакор Нд',
    32:'Варфарекс',
    33:'Варфарин',
    34:'Васкопин',
    35:'Верапамил',
    36:'Верошпирон',
    37:'Гидрохлортиазид',
    38:'Гипотиазид',
    39:'Даприл',
    40:'Дигоксин',
    41:"Диласидом",
    42:'Дилатренд',
    43:'Дилтиазем',
    44:'Дилтиазем ретард',
    45:'Диован',
    46:'Диротон',
    47:'Диувер',
    48:'Ивабрадин',
    49:'Изо-мик лонг',
    50:'Индалонг',
    51:'Индап',
    52:'Индапамид',
    53:'Индапафон',
    54:'Индапен',
    55:'Индапен ретард',
    56:'Индопрес',
    57:'Инспра',
    58:'Калчек',
    59:'Кандесартан',
    60:'Карведил',
    61:"Карведилол",
    62:'Карвелэнд',
    63:'Кардивас',
    64:'Кардикет',
    65:'Кардилопин',
    66:'Кардиомагнум',
    67:'Квинаприл',
    68:'Ко-Диован',
    69:'Ко-амлесса',
    70:'Ко-валсартан',
    71:'Ко-ренитек',
    72:'Конкор',
    73:'Конкор кор',
    74:'Кораксан',
    75:'Кордарон',
    76:'Кордафлекс',
    77:'Кордипин XL',
    78:'Кордипин ретард',
    79:'Коронал',
    80:'Крестор',
    81:"Ксарелто",
    82:'Леркамен',
    83:'Леркадипин',
    84:'Лизиноприл',
    85:'Лизиноприл плюс',
    86:'Лизитар',
    87:'Лизоретик',
    88:'Лизорил',
    89:'Липразид',
    90:'Липримар',
    91:'Ловастатин',
    92:'Лозартан',
    93:'Лориста',
    94:'Магнекард',
    95:'Мертенил',
    96:'Метокард',
    97:'Метопролол',
    98:'Молсидомин',
    99:'Небиволол',
    100:'Небивомед',
    101:"Небилет",
    102:'Небилет плюс',
    103:'Нитроглицерин',
    104:'Нитрокор',
    105:'Нитроминт',
    106:'Нитросорбид',
    107:'Нитроспрей',
    108:'Нифедипин',
    109:'Нифекард XL',
    110:'Норваск',
    111:'Нормодипин',
    112:'Омега 3',
    113:'Памид',
    114:'Паралель',
    115:'Периндоприл',
    116:'Периндоприл плюс',
    117:'Периндоприл+амлодипин',
    118:'Периндоприл+амлодипин+индапамид',
    119:'Полприл',
    120:'Парадакса',
    121:"Предуктал",
    122:'Принесса',
    123:'Престариум',
    124:'Рамилонг',
    125:'Рамиприл',
    126:'Рамприл',
    127:'Равел СР',
    128:'Ревелол XL',
    129:'Ренитек',
    130:'Розувастатин',
    131:'Розукард',
    132:'Розулип',
    133:'Розутатин',
    134:'Ромазик',
    135:'Сентор',
    136:'Сиднофарм',
    137:'Синатор',
    138:'Спироналктон',
    139:'Стамло',
    140:'Сустонит',
    141:"Тиотриазолин",
    142:'Торасемид',
    143:'Три-зидин М',
    144:'Трикард',
    145:'Триметазидин',
    146:'Трипликсам',
    147:'Тритаце',
    148:'Трован',
    149:'Тромбо асс',
    150:'Тулип',
    151:'Фозикард',
    152:'Фозикард Н',
    153:'Фозиноприл',
    154:'Фуросемид',
    155:'Хартил',
    156:'Хинаприл',
    157:'Эгилок',
    158:'Эгилок СР',
    159:'Экваприл',
    160:'Экватор',
    161:"Эналаприл",
    162:'Эналаприл HL',
    163:'Эналаприл Н',
    164:'Энам',
    165:'Энамед Н',
    166:'Энап',
    167:'Энап HL',
    168:'Энап Н',
    169:'Энаприл',
    170:'Энаприл-НТ',
    171:'Энаренал',
    172:'Энтресто (сакубитрил/валсартан)',
    173:'Эплеренон',
    174:'липромак',
    175:'нитрогранулонг',

}



block_list= {
    "0":"0",
    1:"",
    2:"",
    3:"",
    4:"",
    5:"",
    6:"",
    7:"",
    8:"",
    9:"9",
    "10":"10",
    "11":"11",

    }

data_list= {
    "0":"0",
    1:"",
    2:"",
    3:"",
    4:"",
    5:"",
    6:"",
    7:"",
    8:"",
    9:"9",
    "10":"10",
    "11":"11",

    }
drags_list= {}
drags_doz= {}
drags_rate= {}





           
Dizar= ["Другое", "0,2 мг", '0,25мг','0,4мг','1,25мг','1,5мг','10мг','100мг','10мг/2,5/10мг','10мг/2,5мг/5мг','150мг','15мг','160мг','2мг','2,5мг','20мг','200мг','30мг','35мг','4мг','4/10/1,25мг','4/10мг','4/5мг','4/5/1,25мг','40мг','5','50','5мг/1,25мг/10мг','50мг','5мг/1,25мг/10мг','5мг/1,25мг/5мг','6мг','6,25мг','60мг','7,5мг','8мг','8/10/2,5мг','8/2,5мг','8/10мг','8/5/2,5мг','8/5мг','90мг','97/103мг',       


        ]
Days= ["Другое", "1 раз в день",'2 раза в день','3 раза в день','4 раза в день','5 раз в день',
        


        ]







        
MainApp().run()