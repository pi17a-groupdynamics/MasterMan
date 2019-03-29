# MasterMan
by **Semen Asaevich, Alina Pavliy**

**MasterMan**  - веб-сайт, разработанный для оказания различного рода бытовых услуг. Продукт позволяет клиенту быстро найти мастера,
который может оказать какую-либо бытовую услугу.

**HTTPS (Hypertext Transport Protocol Secure)** 
> это протокол, который обеспечивает конфиденциальность обмена данными между сайтом и
пользовательским устройством. Безопасность информации обеспечивается за счет использования криптографических протоколов SSL/TLS, имеющих 3
уровня защиты.

**PostgreSQL**
> свободная объектно-реляционная система управления базами данных (СУБД). PostgreSQL базируется на языке SQL и поддерживает
многие из возможностей стандарта SQL:2011.

**API** 
> описание способов (набор классов, процедур, функций, структур или констант), которыми одна компьютерная программа может
взаимодействовать с другой программой. 

## Software Requirements Specification

### 1. Introduction
#### 1.1 Purpose 
Данный документ описывает спецификацию программного продукта MasterMan 1.0. Спецификация распространяется на весь программный продукт.

#### 1.2 Document Conventions
Далее по тексту _**полужирным курсивом**_ будут выделены термины, определение, которых дано в Глоссарии (Appendix A). 

#### 1.3 Project Scope
Продукт разрабатывается с целью предоставления различных бытовых услуг. Продукт позволяет клиенту быстро найти мастера, который может
оказать какую-либо бытовую услугу.

#### 1.4 References
[PostgreSQL](https://ru.wikipedia.org/wiki/PostgreSQL)  
[Sass](https://ru.wikipedia.org/wiki/Sass)  
[Django](https://ru.wikipedia.org/wiki/Django)  

### 2. Overall Description
#### 2.1 Product Perspective
Программный продукт MasterMan является полностью самостоятельной разработкой компании. Ранее продукт не разрабатывался. Представляет
собой независимый, самодостаточный  программный продукт.  

#### 2.2 Product Features
Продукт будет предоставлять бытовые услуги от компании. На сайте будет присутствовать информация о компании, список предоставляемых
услуг, отсортированный по категориям, а также форма для заполнения заявки на услугу.

#### 2.3 User Classes and Characteristics
Данное приложение может использоваться как администратором системы, так и обычным пользователем.
Клиент: выбирает необходимый тип услуги и оставляет заявку по телефону/онлайн.
Оператор-админ: принимает заявки клиентов, заносит их в базу данных и обрабатывает.

#### 2.4 Operating Environment
Продукт должен запускаться на любых устройствах и в любых браузерах.	

#### 2.5 Design and Implementation Constraints
Работа приложения не должна блокировать работу других приложений и своего собственного интерфейса. Продукт должен использовать протокол
HTTPS для передачи данных. Для хранении информации должна использоваться БД PostgreSQL.

#### 2.6 User Documentation 
Not applicable.

#### 2.7 Dependencies
Все библиотеки и API, необходимые для нормального функционирования сайта, будут располагаться на сервере, что сделает продукт независимым от софта установленного на устройстве клиента.

### 3. System Features (FR)
#### 3.1 System Feature «Interface»

3.1.1 Description and Priority  
Продукт должен иметь интуитивно понятный и удобный пользовательский интерфейс. Приоритет высокий.

3.1.2 Functional Requirements
* REQ-1:	Дизайн должен быть выполнен в правильно подобранной цветовой гамме с минимальным количеством цветов.
* REQ-2:	Качественный подбор изображений должен улучшить внешний вид сайта.
* REQ-3:	Шрифты должны быть лаконичными и сочетаемыми.

#### 3.2	System Feature «Services systematization»

3.2.1	Description and Priority  
Продукт должен систематизировать данные. Приоритет средний.

3.2.2	Functional Requirements
* REQ-1:	Услуги должны быть систематизированы по категориям.

#### 3.3	System Feature «Application form»

3.3.1	Description and Priority  
Сайт должен предоставлять удобную форму для подачи заявки. Приоритет средний.

3.3.2	Functional Requirements
* REQ-1:	Количество обязательных данных для подачи заявки должно быть минимизировано.
* REQ-2:	Заявка должна отправляться в БД для дальнейшей обработки.

#### 3.4	System Feature «Database»

3.4.1	Description and Priority  
Продукт должен обеспечивать хранения информации о заявках в БД. Приоритет высокий.

3.4.2	Functional Requirements
* REQ-1:	БД располагается на сервере.
* REQ-2:	Используется СУБД PostgreSQL.
* REQ-3:	Внутренняя структура БД – таблица заявки и таблицы справочники для хранения информации о заявке.

#### 3.5	System Feature «Adaptability»

3.5.1	Description and Priority  
Сайт должен иметь адаптивный интерфейс. Приоритет высокий.

3.5.2	Functional Requirements
* REQ-1:	Сайт должен иметь версию для всех устройств.
* REQ-2:	Сайт должен одинаково запускаться на любых платформах и в любых браузерах.

#### 3.6	System Feature «Security»

3.6.1	Description and Priority  
Сайт должен обеспечивать безопасноть трафика. Приоритет высокий.

3.6.2	Functional Requirements
* REQ-1:	Необходима поддержка протокола HTTPS.

#### 3.7	System Feature «Admin account»

3.7.1	Description and Priority  
На сайте необходима авторизация администратора-оператора. Приоритет высокий.

3.7.2	Functional Requirements
* REQ-1:	Аутентифицированные операторы имеют доступ к БД и могут обрабатывать заявки.

### 4.	External Interface Requirements (NFR)

#### 4.1	User Interfaces

##### Main
![Main](https://github.com/pi17a-groupdynamics/MasterMan/tree/Resources/main.png)

##### Category
![Category](https://github.com/pi17a-groupdynamics/MasterMan/tree/Resources/category.png)

##### Advantages
![Advantages](https://github.com/pi17a-groupdynamics/MasterMan/tree/Resources/advantages.png)

##### Form
![Form](https://github.com/pi17a-groupdynamics/MasterMan/tree/Resources/form.png)

##### Review
![Review](https://github.com/pi17a-groupdynamics/MasterMan/tree/Resources/review.png)

##### Footer
![Footer](https://github.com/pi17a-groupdynamics/MasterMan/tree/Resources/footer.png)

#### 4.2	Hardware Interfaces
Not applicable.

#### 4.3	Software Interfaces
Продукт должен использовать API взаимодействия с БД PostgreSQL.

### 5.	Other Nonfunctional Requirements (NFR)

#### 5.1	Performance Requirements
Not applicable.

#### 5.2	Security Requirements
Сайт должен быть защищен протоколом HTTPS.
 
### Appendix A: Glossary
**HTTPS (Hypertext Transport Protocol Secure)**
> это протокол, который обеспечивает конфиденциальность обмена данными между сайтом и
пользовательским устройством. Безопасность информации обеспечивается за счет использования криптографических протоколов SSL/TLS, имеющих
3 уровня защиты.

**PostgreSQL** 
> свободная объектно-реляционная система управления базами данных (СУБД). PostgreSQL базируется на языке SQL и поддерживает
многие из возможностей стандарта SQL:2011.

**API**
> описание способов (набор классов, процедур, функций, структур или констант), которыми одна компьютерная программа может
взаимодействовать с другой программой. 
