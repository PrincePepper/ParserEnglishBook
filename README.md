# ParserEnglishBook

## *Предисловие*

Нужно надо было найти учебник на просторах интернета, нашел на сайте [biblio-online](https://www.biblio-online.ru/viewer/angliyskiy-yazyk-dlya-estestvennonauchnyh-napravleniy-450653#page/1)

Пришлось заплатить 240 рублей за онлайн версию, следующая проблема возникла со скачиванием, т.к. если бы это был обычный png/jpg, то проблем не возникло сначала.
## *Реализация*
Реализовано на основе библиотеки Selenium и BeautifulSoup.

Используется Webdriver-[Chrome](https://chromedriver.storage.googleapis.com/index.html?path=86.0.4240.22/)  
Для работы нужно сначала авторизоваться, чтобы система дала нам полную версию учебника  
Данные авторизации используйсте свои если хотите потестить:)  
Все что делает наша прога - прогружает *div`ы* где хранится наш адрес на фотку, затем мы просто вызываем **get** для скачивания файлов  

Скачивается все в папку «Загрузки»
## *Результат*
После работы приложение в онлайн конвертере из [SVG в PDF](https://tools.pdf24.org/ru/svg-to-pdf)  
Затем обьяденил файлы в один файл и вуаля, все готово

### **P.S**
Как мне казалось, это должно все занимать немного времени, но я потратил на 40 строчек кода, 3 мать его часа...

***The project was released for my University course***

##### My contacts:
1. [Telegram](https://tgmsg.ru/princepepper)
2. [Вконтакте](https://vk.com/princepepper)
3. [Instargam](https://www.instagram.com/prince_pepper_official)
4. <sereda.wk@gmail.com>
