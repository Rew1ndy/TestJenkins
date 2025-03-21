﻿# У цьому файлі міститься сценарій гри.

# Визначення персонажів для гри.
# Аргумент color змінює колір ім’я персонажа.

define e = Character("Монолог героя")
define a = Character("Кіт")
define r = Character("Раян Гослінг")

define audio.mus1 = "cloth-flapping-in-wind-74205.mp3"
define audio.mus2 = "6d64cbf7b17425e.mp3"
# Гра починається тут.

label start:

   scene bg2

   play music mus1

   
   e "Запізно… Зазвичай у цей час у кампусі вже тихо. Тільки ліхтарі майже не працюють, створюючи якусь дивну атмосферу. Ніби університет готується до сну." 

   
   "Герой йде в бік бібліотеки. Вдалині чути звук миготливого ліхтаря, який час від часу потріскує і спалахує."
   
   
   e "Скоріше б знайти потрібну книгу і піти"

   menu optional_name:
      "Вибір"
      "Піти до бібліотеки":
         stop music fadeout 1.0
         jump library_scene
      "Повернутись додому":
         stop music fadeout 1.0
         jump end_scene

   return
   
label library_scene:

   scene bg4
   
  
   e "Завжди дивно бачити бібліотеку такою пустою. Зазвичай тут повно студентів, а тепер – лише тиша та слабкий запах старих книг"
   
   
   "У кутку помітний силует бібліотекаря, але він занадто занурений у свої справи, щоб звертати увагу відвідувачів."
   
   
   e "Добре, якщо ніхто не заважатиме, я швидко знайду книгу і піду"

   "Герой підходить до каталогу — старої масивної книги з переліком доступних видань."
   jump catalog_scene
   

   return

label catalog_scene:

   scene bg5
 
   
   e "Каталог старий, але добре збережений. Цікаво, де знайти потрібну книгу?"

  
   "Герой гортає сторінки, перевіряючи список книг..."

   
   e "Так… ось вона. Але…"

   show text "Ця книга видана іншому студенту." with fade

   
   e "Ну звісно. Варто було очікувати. Ладно, може, знайду щось схоже."


   "Герой іде в потрібний відділ бібліотеки – слабо освітлений кут зі стелажами."

   jump bookshelf_scene  #
   
   return

label bookshelf_scene:

   scene bg6  

  
   e "Тут має бути щось корисне... Можливо, навіть краще за ту книгу."


   "На нижній полиці привертає увагу стара книга з потертою обкладинкою."

   menu:
      "Взяти книгу":
            jump take_book

      "Ігнорувати":
            jump ignore_book

label take_book:

   
   "Герой простягає руку і бере книгу в руки."

   
   "Як тільки пальці торкаються обкладинки, по шкірі пробігає дивне тепло."
   
   
   e "Що за?.. Вона ніби жива."

   jump mysterious_event

label ignore_book:

   
   "Герой відвертається, але…"

  
   "Раптом роздається приглушений глухий звук – книга сама випадає з полиці і з хлопком падає на підлогу, відкриваючись на випадковій сторінці."

   
   e "Що за… Вона сама впала?!"

   jump mysterious_event

label mysterious_event:

   
   "Сторінки починають перегортатися самі по собі, текст на них повільно світиться, літери ніби складаються в нові форми."

  
   e "Це… неможливо…"

   
   "Герой не може відірвати погляд – книга сама привернула його увагу."

   jump transition_to_parallel_library

label transition_to_parallel_library:
   
   
   e "Що за чорт…?"

   scene black with fade

   pause 1.5  

   jump Parallel_library

label Parallel_library:

   scene bg4

   e "Де я?.. Це ж та сама бібліотека, але…"
   
   e "Це все ще бібліотека… але щось змінилося"

   "Герой оглядається, зауважує силует на столі."

   "Камера повільно наближається – це кіт незвичайний *скрин тг*. Він сидить нерухомо, його янтарні очі вивчають героя."

   e "…Тварина? Як вона тут виявилася?"

   "Герой підходить ближче, повільно нахиляється, дивиться на кота."

   e "Звичайний кіт. Напевно ..."

   "Кіт жмуриться, дивиться на героя і ліниво каже:"
   
   a "Чого вилупився? Котів не бачив?"

   "Герой застигає, обробляючи почуте."

   e "Воно... каже?"

   a "Добре, двоногий, не гальмуй. Тобі вихід потрібен? Почни з книги перед тобою."

   show text "Далі буде..." with fade

   return

label end_scene:

   scene bg3
   
   play music mus2

   "Ти повернувся додому. Це кінець. Ти нічого не дізнався."

   return

return
